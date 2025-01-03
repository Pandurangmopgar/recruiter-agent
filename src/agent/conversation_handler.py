from dotenv import load_dotenv
import os
import google.generativeai as genai
from typing import List, Tuple, Dict, Any

class ConversationHandler:
    def __init__(self):
        # Load environment variables and configure Gemini AI
        load_dotenv()
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def generate_technical_questions(self, skills: List[str]) -> List[str]:
        """Generate technical questions based on provided skills"""
        try:
            # Create a focused prompt for question generation
            prompt = f"""
            Generate 5 technical interview questions for a candidate with expertise in: {', '.join(skills)}
            
            Requirements:
            1. Each question should be specific to the candidate's skills
            2. Include a mix of:
               - Practical problem-solving
               - System design
               - Technical concepts
               - Best practices
            3. Questions should be challenging but answerable
            4. Format each question with difficulty level in square brackets
            
            Example format:
            [Difficulty: Medium] Question about skill...
            [Difficulty: Hard] Technical scenario question...
            
            Please generate questions now.
            """

            # Get response from AI
            response = self.chat.send_message(prompt)
            
            if not response.text:
                return self._get_fallback_questions(skills)

            # Process and clean the response
            questions = []
            for line in response.text.split('\n'):
                line = line.strip()
                if line and any(line.startswith(str(i)) for i in range(1, 6)):
                    # Remove numbering and clean up
                    question = line.split('.', 1)[1].strip()
                    # Remove any existing ** markers
                    question = question.replace('**', '')
                    # Check if difficulty is already in square brackets, if not add it
                    if not question.startswith('['):
                        question = '[Difficulty: Medium] ' + question
                    questions.append(question)

            # Ensure we have exactly 5 questions
            if len(questions) < 5:
                questions.extend(self._get_fallback_questions(skills)[:5 - len(questions)])
            
            return questions[:5]

        except Exception as e:
            print(f"Error generating questions: {str(e)}")
            return self._get_fallback_questions(skills)

    def _get_fallback_questions(self, skills: List[str]) -> List[str]:
        """Provide fallback questions if AI generation fails"""
        general_questions = [
            f"[Difficulty: Medium] Explain how you would implement a scalable system using {skills[0] if skills else 'your preferred technology'}.",
            "[Difficulty: Medium] Describe a challenging technical problem you've solved recently and your approach to solving it.",
            "[Difficulty: Hard] How do you ensure code quality and maintainability in your projects?",
            "[Difficulty: Medium] Explain your approach to debugging complex issues in a production environment.",
            "[Difficulty: Hard] How do you handle performance optimization in your applications?"
        ]
        return general_questions

    def evaluate_answer(self, question: str, answer: str) -> str:
        """Evaluate the candidate's answer"""
        try:
            prompt = f"""
            Evaluate the following technical interview response:

            Question: {question}
            
            Candidate's Answer: {answer}
            
            Please provide a constructive evaluation considering:
            1. Technical accuracy
            2. Completeness of the answer
            3. Problem-solving approach
            4. Communication clarity
            
            Format your evaluation with:
            - Strengths
            - Areas for improvement (if any)
            - Overall assessment
            
            Keep the tone professional and constructive.
            """

            response = self.chat.send_message(prompt)
            return response.text if response.text else "Unable to evaluate answer. Please try again."

        except Exception as e:
            return f"Evaluation error: Please provide more details in your answer. {str(e)}"

    def handle_message(self, session_id: str, message: str) -> Tuple[str, Dict[str, Any]]:
        """Handle general conversation messages"""
        try:
            # Process message based on context
            response = self.chat.send_message(message)
            return response.text, {"status": "success"}
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again.", {"status": "error"}