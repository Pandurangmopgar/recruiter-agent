from dotenv import load_dotenv
import os
import google.generativeai as genai
from typing import Dict, List, Optional

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GEMINI_MODEL = "gemini-1.5-flash"
TEMPERATURE = 0.7
TOP_P = 0.9
TOP_K = 40
MAX_OUTPUT_TOKENS = 2048

class GeminiAgent:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config={
                "temperature": TEMPERATURE,
                "top_p": TOP_P,
                "top_k": TOP_K,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
            }
        )
        self.chat = self.model.start_chat(history=[])
        
    def get_response(self, message: str, context: Optional[Dict] = None) -> str:
        try:
            if context:
                prompt = self._build_contextual_prompt(message, context)
            else:
                prompt = message
                
            response = self.chat.send_message(prompt)
            return response.text
            
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again."
    
    def generate_technical_questions(self, tech_stack: List[str]) -> List[str]:
        prompt = self._build_tech_question_prompt(tech_stack)
        try:
            response = self.chat.send_message(prompt)
            questions = self._parse_questions(response.text)
            return questions
        except Exception as e:
            return [f"Error generating questions: {str(e)}"]
    
    def _build_contextual_prompt(self, message: str, context: Dict) -> str:
        context_str = "\n".join([f"{k}: {v}" for k, v in context.items()])
        return f"""
        Previous Context:
        {context_str}
        
        Current Message:
        {message}
        
        Please provide a relevant response while maintaining the conversation context.
        """
    
    def _build_tech_question_prompt(self, tech_stack: List[str]) -> str:
        return f"""
        Generate 3-5 technical interview questions for the following technologies:
        {', '.join(tech_stack)}
        
        Requirements:
        1. Questions should be challenging but appropriate for an interview
        2. Mix of theoretical and practical questions
        3. Include at least one problem-solving question
        4. Format each question with difficulty level (Easy/Medium/Hard)
        """
    
    def _parse_questions(self, response: str) -> List[str]:
        questions = [q.strip() for q in response.split('\n') if q.strip()]
        return questions 