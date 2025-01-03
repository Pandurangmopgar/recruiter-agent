import streamlit as st
import uuid
from agent.conversation_handler import ConversationHandler
import time
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO

def set_custom_css():
    st.markdown("""
        <style>
        /* Main container */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* Header */
        .header {
            background: linear-gradient(135deg, #1976d2, #1565c0);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Chat container */
        .chat-message {
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            line-height: 1.5;
            position: relative;
            animation: fadeIn 0.3s ease-in;
        }
        
        .user-message {
            background-color: #e3f2fd;
            margin-left: 20%;
            margin-right: 1rem;
            border: 1px solid #bbdefb;
        }
        
        .assistant-message {
            background-color: white;
            margin-right: 20%;
            margin-left: 1rem;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* Progress indicators */
        .stage-indicator {
            padding: 0.75rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .stage-active {
            background-color: #4caf50;
            color: white;
            box-shadow: 0 2px 4px rgba(76,175,80,0.3);
        }
        
        .stage-pending {
            background-color: #f5f5f5;
            color: #757575;
            border: 1px solid #e0e0e0;
        }
        
        /* Input area */
        .input-container {
            background-color: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        
        .stTextInput > div > div > input {
            border-radius: 25px !important;
            padding: 0.75rem 1.5rem !important;
            border: 2px solid #e0e0e0 !important;
            font-size: 1rem !important;
        }
        
        .stButton > button {
            border-radius: 25px !important;
            padding: 0.75rem 2rem !important;
            background: linear-gradient(135deg, #1976d2, #1565c0) !important;
            color: white !important;
            font-weight: 500 !important;
            border: none !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: #bbdefb !important;
        }
        
        .stProgress > div > div > div {
            background: linear-gradient(135deg, #1976d2, #1565c0) !important;
        }
        
        /* Form styling */
        .form-container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        /* Message formatting */
        .formatted-message {
            white-space: pre-line;
            line-height: 1.6;
        }
        
        /* Technical questions styling */
        .question-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border-left: 4px solid #1976d2;
        }
        
        /* AI Evaluation Styling */
        .ai-evaluation {
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .evaluation-section {
            margin: 15px 0;
        }
        
        .evaluation-section h4 {
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .evaluation-section ul {
            margin: 0;
            padding-left: 20px;
        }
        
        .evaluation-section li {
            margin: 5px 0;
            line-height: 1.5;
        }
        
        .evaluation-section p {
            margin: 5px 0;
            line-height: 1.5;
        }
        
        /* Loading animation */
        .loading-spinner {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        
        .loading-spinner::after {
            content: "";
            width: 40px;
            height: 40px;
            border: 5px solid #f3f3f3;
            border-top: 5px solid #1976d2;
            border-radius: 50%;
            animation: spinner 1s linear infinite;
        }
        
        @keyframes spinner {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Pulse animation for processing text */
        .processing-text {
            animation: pulse 1.5s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
        </style>
    """, unsafe_allow_html=True)

def format_message(message: str) -> str:
    """Format message text for better readability"""
    return message.replace('\\n', '\n').replace('\\t', '\t')

def handle_greeting():
    st.markdown("""
        <div class="chat-message assistant-message">
            <h3>Welcome to TalentScout AI!</h3>
            <p>I'll guide you through the technical interview process. Let's start with your information.</p>
        </div>
    """, unsafe_allow_html=True)
    return create_personal_info_form()

def handle_tech_stack(name: str):
    st.markdown(f"""
        <div class="chat-message assistant-message">
            <h3>Technical Skills Assessment</h3>
            <p>Hi {name}, let's understand your technical expertise better.</p>
        </div>
    """, unsafe_allow_html=True)
    return create_tech_stack_form()

def handle_technical_interview(skills: list):
    """Handle the technical interview stage with proper question management"""
    
    # Initialize technical interview session if not already done
    if 'tech_questions_initialized' not in st.session_state:
        with st.spinner("🤖 AI is preparing your technical questions..."):
            st.markdown("""
                <div class="loading-spinner"></div>
                <p class="processing-text" style="text-align: center;">Analyzing your skills and generating relevant questions...</p>
            """, unsafe_allow_html=True)
            try:
                # Generate questions based on skills
                questions = st.session_state.conversation_handler.generate_technical_questions(skills)
                if not questions or len(questions) == 0:
                    st.error("Failed to generate technical questions. Please try again.")
                    return
                
                st.session_state.tech_questions = questions
                st.session_state.current_question = 0
                st.session_state.tech_questions_initialized = True
                st.session_state.responses = []
                
            except Exception as e:
                st.error(f"Error initializing technical interview: {str(e)}")
                return

    # Safety check for questions
    if not hasattr(st.session_state, 'tech_questions') or not st.session_state.tech_questions:
        st.error("No technical questions available. Please restart the interview.")
        if st.button("Restart Interview"):
            st.session_state.clear()
            st.rerun()
        return

    current_q = st.session_state.current_question
    total_q = len(st.session_state.tech_questions)

    # Display progress
    st.markdown(f"""
        <div style="margin-bottom: 2rem;">
            <h3>Technical Interview</h3>
            <p>Question {current_q + 1} of {total_q}</p>
        </div>
    """, unsafe_allow_html=True)

    # Display current question
    try:
        current_question = st.session_state.tech_questions[current_q]
        st.markdown(f"""
            <div class="question-card">
                <p style="font-size: 1.1rem; font-weight: 500;">{current_question}</p>
            </div>
        """, unsafe_allow_html=True)

        # Answer input
        answer = st.text_area(
            "Your Answer",
            height=150,
            help="Provide a detailed explanation of your solution"
        )

        # Navigation buttons in three columns
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            if st.button("Previous", disabled=current_q == 0):
                st.session_state.current_question -= 1
                st.rerun()
        
        with col2:
            if st.button("Next", disabled=current_q == total_q - 1):
                st.session_state.current_question += 1
                st.rerun()

        with col3:
            submit_button = st.button(
                "Submit & Continue",
                type="primary",
                use_container_width=True,
                disabled=not answer
            )

        if submit_button and answer:
            with st.spinner(""):  # Empty spinner to prevent double spinners
                st.markdown("""
                    <div class="loading-spinner"></div>
                    <p class="processing-text" style="text-align: center;">AI is analyzing your response...</p>
                """, unsafe_allow_html=True)
                try:
                    response = st.session_state.conversation_handler.evaluate_answer(
                        current_question,
                        answer
                    )
                    
                    # Store response
                    if 'responses' not in st.session_state:
                        st.session_state.responses = []
                    
                    st.session_state.responses.append({
                        'question': current_question,
                        'answer': answer,
                        'evaluation': response
                    })
                    
                    # Show evaluation feedback
                    st.markdown("""
                        <div style="margin-top: 1rem; padding: 1rem; background-color: #f8f9fa; border-radius: 10px;">
                            <h4 style="color: #1976d2;">Evaluation Feedback:</h4>
                    """, unsafe_allow_html=True)
                    st.write(response)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Progress to next question or complete
                    if current_q + 1 < total_q:
                        st.session_state.current_question += 1
                        time.sleep(1)  # Brief pause to show feedback
                        st.rerun()
                    else:
                        st.session_state.current_stage = 'completed'
                        st.rerun()
                        
                except Exception as e:
                    st.error(f"Error evaluating answer: {str(e)}")
                    return

    except IndexError:
        st.error("An error occurred accessing the current question. Resetting interview...")
        if st.button("Reset Interview"):
            st.session_state.clear()
            st.rerun()

def handle_completion():
    """Handle the completion stage with results summary and PDF download"""
    st.markdown("""
        <div class="chat-message assistant-message">
            <h3>Technical Interview Completed! 🎉</h3>
            <p>Here's a comprehensive summary of your interview responses:</p>
        </div>
    """, unsafe_allow_html=True)

    if hasattr(st.session_state, 'responses') and st.session_state.responses:
        # Display responses
        for i, resp in enumerate(st.session_state.responses, 1):
            with st.expander(f"Question {i}", expanded=True):
                st.markdown(f"""
                    <div class="question-card">
                        <p><strong>Question:</strong></p>
                        <p>{resp['question']}</p>
                        <br>
                        <p><strong>Your Answer:</strong></p>
                        <p>{resp['answer']}</p>
                        <br>
                        <p><strong>Evaluation:</strong></p>
                        {format_ai_response_html(resp['evaluation'])}
                    </div>
                """, unsafe_allow_html=True)
        
        # Generate and offer PDF download
        col1, col2 = st.columns([1, 2])
        with col1:
            if st.button("Generate PDF Summary", type="primary"):
                with st.spinner(""):  # Empty spinner to prevent double spinners
                    st.markdown("""
                        <div class="loading-spinner"></div>
                        <p class="processing-text" style="text-align: center;">Generating your comprehensive interview summary...</p>
                    """, unsafe_allow_html=True)
                    pdf_buffer = generate_interview_summary(st.session_state)
                    if pdf_buffer:
                        st.session_state.pdf_buffer = pdf_buffer
                        st.session_state.pdf_generated = True
                        st.rerun()
        
        with col2:
            if hasattr(st.session_state, 'pdf_generated') and st.session_state.pdf_generated:
                st.download_button(
                    label="📥 Download Interview Summary",
                    data=st.session_state.pdf_buffer.getvalue(),
                    file_name="interview_summary.pdf",
                    mime="application/pdf",
                    key="download_pdf"
                )
    else:
        st.warning("No interview responses found. Please complete the interview first.")
        if st.button("Start New Interview"):
            st.session_state.clear()
            st.rerun()

def preprocess_ai_response(response: str) -> dict:
    """
    Preprocess AI response to extract and format different sections
    Returns a dictionary with structured response data
    """
    sections = {
        'strengths': [],
        'areas_for_improvement': [],
        'overall_assessment': ''
    }
    
    try:
        # Remove ** markers and split into lines
        lines = response.replace('**', '').split('\n')
        
        current_section = None
        current_points = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('Strengths:'):
                current_section = 'strengths'
                continue
            elif line.startswith('Areas for improvement:'):
                if current_points and current_section:
                    sections[current_section].extend(current_points)
                current_section = 'areas_for_improvement'
                current_points = []
                continue
            elif line.startswith('Overall assessment:'):
                if current_points and current_section:
                    sections[current_section].extend(current_points)
                current_section = 'overall_assessment'
                current_points = []
                continue
            
            # Process bullet points
            if line.startswith('* '):
                current_points.append(line[2:])
            else:
                if current_section == 'overall_assessment':
                    sections[current_section] = line
                else:
                    current_points.append(line)
        
        # Add any remaining points
        if current_points and current_section:
            if current_section == 'overall_assessment':
                sections[current_section] = ' '.join(current_points)
            else:
                sections[current_section].extend(current_points)
                
        return sections
        
    except Exception as e:
        st.error(f"Error processing AI response: {str(e)}")
        return {
            'strengths': [],
            'areas_for_improvement': [],
            'overall_assessment': response  # Return original response as overall assessment
        }

def format_ai_response_html(response: str) -> str:
    """Format AI response for HTML display"""
    sections = preprocess_ai_response(response)
    
    html = '<div class="ai-evaluation">'
    
    if sections['strengths']:
        html += '<div class="evaluation-section">'
        html += '<h4 style="color: #2e7d32;">Strengths:</h4>'
        html += '<ul>'
        for point in sections['strengths']:
            html += f'<li>{point}</li>'
        html += '</ul></div>'
    
    if sections['areas_for_improvement']:
        html += '<div class="evaluation-section">'
        html += '<h4 style="color: #c62828;">Areas for Improvement:</h4>'
        html += '<ul>'
        for point in sections['areas_for_improvement']:
            html += f'<li>{point}</li>'
        html += '</ul></div>'
    
    if sections['overall_assessment']:
        html += '<div class="evaluation-section">'
        html += '<h4 style="color: #1976d2;">Overall Assessment:</h4>'
        html += f'<p>{sections["overall_assessment"]}</p>'
        html += '</div>'
    
    html += '</div>'
    return html

def generate_interview_summary(session_state):
    """Generate a PDF summary of the interview with proper error handling"""
    try:
        # Initialize PDF buffer
        buffer = BytesIO()
        
        # Set up the document with margins
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Initialize story and styles
        story = []
        styles = getSampleStyleSheet()
        
        # Modify existing styles instead of adding new ones
        title_style = ParagraphStyle(
            'CustomTitle',  # Changed from 'Title' to avoid conflict
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1  # Center alignment
        )
        
        section_style = ParagraphStyle(
            'CustomSection',  # Changed from 'Section' to avoid conflict
            parent=styles['Heading2'],
            fontSize=16,
            spaceBefore=20,
            spaceAfter=12
        )
        
        # Add title
        story.append(Paragraph("Technical Interview Summary", title_style))
        
        # Add personal information section
        if hasattr(session_state, 'personal_info'):
            story.append(Paragraph("Personal Information", section_style))
            
            # Create table data
            info = session_state.personal_info
            data = [
                ["Full Name", info.get('full_name', 'N/A')],
                ["Email", info.get('email', 'N/A')],
                ["Phone", info.get('phone', 'N/A')],
                ["Experience", info.get('experience', 'N/A')],
                ["Position", info.get('desired_position', 'N/A')],
                ["Location", info.get('location', 'N/A')]
            ]
            
            # Create and style table
            table = Table(data, colWidths=[150, 300])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ]))
            story.append(table)
            story.append(Spacer(1, 20))
        
        # Add technical skills section
        if hasattr(session_state, 'tech_stack'):
            story.append(Paragraph("Technical Skills", section_style))
            skills_text = ", ".join(session_state.tech_stack)
            story.append(Paragraph(skills_text, styles['Normal']))
            story.append(Spacer(1, 20))
        
        # Add interview responses section
        if hasattr(session_state, 'responses'):
            story.append(Paragraph("Interview Questions and Evaluations", section_style))
            
            for i, resp in enumerate(session_state.responses, 1):
                # Question
                story.append(Paragraph(
                    f"Question {i}:",
                    styles['Heading3']
                ))
                story.append(Paragraph(resp['question'], styles['Normal']))
                story.append(Spacer(1, 10))
                
                # Answer
                story.append(Paragraph("Your Answer:", styles['Heading4']))
                story.append(Paragraph(resp['answer'], styles['Normal']))
                story.append(Spacer(1, 10))
                
                # Evaluation
                sections = preprocess_ai_response(resp['evaluation'])
                
                # Strengths
                if sections['strengths']:
                    story.append(Paragraph("Strengths:", styles['Heading4']))
                    for strength in sections['strengths']:
                        story.append(Paragraph(f"• {strength}", styles['Normal']))
                    story.append(Spacer(1, 10))
                
                # Areas for Improvement
                if sections['areas_for_improvement']:
                    story.append(Paragraph("Areas for Improvement:", styles['Heading4']))
                    for area in sections['areas_for_improvement']:
                        story.append(Paragraph(f"• {area}", styles['Normal']))
                    story.append(Spacer(1, 10))
                
                # Overall Assessment
                if sections['overall_assessment']:
                    story.append(Paragraph("Overall Assessment:", styles['Heading4']))
                    story.append(Paragraph(sections['overall_assessment'], styles['Normal']))
                
                story.append(Spacer(1, 20))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer

    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        return None

def create_personal_info_form():
    """Create and handle the personal information form"""
    with st.form("personal_info_form", clear_on_submit=True):
        st.markdown("""
            <div class="form-container">
                <h3 style='color: #1976d2; margin-bottom: 1.5rem;'>Personal Information</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name*", key="name")
            email = st.text_input("Email Address*", key="email")
            phone = st.text_input("Phone Number*", key="phone")
        
        with col2:
            experience = st.text_input("Years of Experience*", key="experience")
            position = st.text_input("Desired Position*", key="position")
            location = st.text_input("Current Location*", key="location")
        
        submit_button = st.form_submit_button(
            label="Submit Information",
            type="primary",
            use_container_width=True
        )
        
        if submit_button:
            if all([full_name, email, phone, experience, position, location]):
                return {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "desired_position": position,
                    "location": location
                }, True
            else:
                st.error("Please fill in all required fields.")
                return None, False
        return None, False

def create_tech_stack_form():
    """Create and handle the technical skills form"""
    with st.form("tech_stack_form", clear_on_submit=True):
        st.markdown("""
            <div class="form-container">
                <h3 style='color: #1976d2; margin-bottom: 1.5rem;'>Technical Skills</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Programming Languages
        languages = st.multiselect(
            "Programming Languages",
            [
                "Python", "JavaScript", "Java", "C++", "C#", "Ruby", "PHP",
                "Swift", "Kotlin", "Go", "Rust", "TypeScript"
            ]
        )
        
        # Frontend
        frontend = st.multiselect(
            "Frontend Technologies",
            [
                "React", "Angular", "Vue.js", "Svelte", "HTML5", "CSS3",
                "SASS/SCSS", "Webpack", "Bootstrap", "Tailwind CSS"
            ]
        )
        
        # Backend
        backend = st.multiselect(
            "Backend Technologies",
            [
                "Node.js", "Django", "Flask", "Spring Boot", "Laravel",
                "Express.js", "FastAPI", "Ruby on Rails", "ASP.NET"
            ]
        )
        
        # Databases
        databases = st.multiselect(
            "Databases",
            [
                "PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite",
                "Oracle", "Microsoft SQL Server", "Cassandra", "DynamoDB"
            ]
        )
        
        # Cloud & DevOps
        cloud_devops = st.multiselect(
            "Cloud & DevOps",
            [
                "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes",
                "Jenkins", "Git", "GitHub Actions", "CircleCI", "Terraform"
            ]
        )
        
        # Other Skills
        other_skills = st.text_area(
            "Other Skills (comma-separated)",
            placeholder="Enter any additional skills not listed above"
        )
        
        submit_button = st.form_submit_button(
            label="Submit Technical Skills",
            type="primary",
            use_container_width=True
        )
        
        if submit_button:
            with st.spinner(""):
                st.markdown("""
                    <div class="loading-spinner"></div>
                    <p class="processing-text" style="text-align: center;">Processing your technical skills...</p>
                """, unsafe_allow_html=True)
                all_skills = languages + frontend + backend + databases + cloud_devops
                if other_skills:
                    additional_skills = [skill.strip() for skill in other_skills.split(',') if skill.strip()]
                    all_skills.extend(additional_skills)
                
                if all_skills:
                    return list(set(all_skills)), True  # Remove duplicates
                else:
                    st.error("Please select at least one skill.")
                    return None, False
            return None, False

def main():
    st.set_page_config(
        page_title="TalentScout AI Assistant",
        page_icon="👨‍💼",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    set_custom_css()
    
    # Initialize session state
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.current_stage = 'greeting'
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.conversation_handler = ConversationHandler()
    
    # Header
    st.markdown("""
        <div class="header">
            <h1>TalentScout AI Assistant</h1>
            <p>Your AI-powered technical interviewer</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress tracking
    stages = ['greeting', 'tech_stack', 'tech_questions', 'completed']
    stage_names = ['Personal Info', 'Technical Skills', 'Interview', 'Completed']
    current_index = stages.index(st.session_state.current_stage)
    
    # Progress bar
    st.progress((current_index) / (len(stages) - 1))
    
    # Stage indicators
    cols = st.columns(len(stages))
    for i, (stage, name) in enumerate(zip(stages, stage_names)):
        with cols[i]:
            if i < current_index:
                st.markdown(f"✅ {name}")
            elif i == current_index:
                st.markdown(f"🔵 {name}")
            else:
                st.markdown(f"⚪ {name}")
    
    # Main content
    if st.session_state.current_stage == 'greeting':
        info, submitted = handle_greeting()
        if submitted and info:
            st.session_state.personal_info = info
            st.session_state.current_stage = 'tech_stack'
            st.rerun()
    
    elif st.session_state.current_stage == 'tech_stack':
        skills, submitted = handle_tech_stack(st.session_state.personal_info['full_name'])
        if submitted and skills:
            st.session_state.tech_stack = skills
            st.session_state.current_stage = 'tech_questions'
            st.rerun()
    
    elif st.session_state.current_stage == 'tech_questions':
        handle_technical_interview(st.session_state.tech_stack)
    
    elif st.session_state.current_stage == 'completed':
        handle_completion()

if __name__ == "__main__":
    main()