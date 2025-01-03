# TalentScout AI: Your Smart Hiring Assistant 

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-orange.svg)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Gemini--1.5--Flash-green.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Meet TalentScout AI - your intelligent companion for technical interviews, powered by Google's cutting-edge Gemini-1.5-Flash model! 

## What is TalentScout AI?

TalentScout AI revolutionizes the technical interview process by acting as your smart hiring assistant. It's designed to make technical interviews more efficient, consistent, and insightful. Whether you're screening candidates for Python, JavaScript, or any other tech stack, TalentScout AI has got you covered!

### What Can It Do?
- Conducts personalized technical interviews
- Generates smart questions based on candidate's tech stack
- Provides real-time evaluation of responses
- Creates detailed interview summaries
- Maintains natural, context-aware conversations

## Built With Love Using

- **Frontend:** Streamlit - for a clean, responsive UI
- **Brain:** Google's Gemini-1.5-Flash - our AI powerhouse
- **Backend:** Python 3.8+ - keeping things fast and reliable
- **Reports:** ReportLab - for professional PDF summaries
- **Experience:** Streamlit Session State - for smooth conversations

## Getting Started

### Prerequisites
- Python 3.8 or higher
- A Google API key for Gemini
- Your favorite code editor
- A passion for innovation! 

### Quick Setup

1. **Clone & Enter:**
```bash
git clone https://github.com/Pandurangmopgar/recruiter-agent.git
cd recruiter-agent
```

2. **Set Up Your Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure:**
```bash
cp .env.example .env
# Edit .env with your Google API key
```

4. **Launch:**
```bash
streamlit run src/app.py
```

## Features in Detail

### Smart Interview Flow
1. **Warm Welcome:** Greets candidates and explains the process
2. **Info Gathering:** Collects essential details naturally
3. **Tech Assessment:** Generates relevant technical questions
4. **Real-time Evaluation:** Provides instant, constructive feedback
5. **Summary Generation:** Creates comprehensive interview reports

### The Magic Behind the Scenes

#### Prompt Engineering
We've crafted our prompts to be:
- Conversational yet professional
- Technically precise
- Adaptable to different tech stacks
- Context-aware throughout the interview

#### Privacy First
- No permanent storage of candidate data
- Session-based information handling
- GDPR-compliant practices
- Secure API communication

## Project Structure
```
recruiter-agent/
├── src/
│   ├── app.py              # Main application
│   ├── agent/              # AI conversation logic
│   ├── components/         # UI components
│   ├── config/            # Configuration
│   └── utils/             # Helper functions
├── tests/                 # Test suite
└── requirements.txt       # Dependencies
```

## Challenges We Tackled

1. **Making AI More Human**
   - Challenge: Creating natural conversation flow
   - Solution: Fine-tuned prompts and context management

2. **Technical Depth vs. Accessibility**
   - Challenge: Balancing question difficulty
   - Solution: Dynamic difficulty adjustment based on responses

3. **Performance & Scalability**
   - Challenge: Quick response times
   - Solution: Optimized prompt engineering and caching

## See It in Action

Want to see TalentScout AI in action? Check out our [demo video](your-demo-link-here) or try it yourself!

## Join the Journey

Found a bug? Have an idea? Want to contribute? We'd love to hear from you!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingIdea`)
3. Commit your changes (`git commit -m 'Add AmazingIdea'`)
4. Push to the branch (`git push origin feature/AmazingIdea`)
5. Open a Pull Request

## Let's Connect

- Found an issue? [Report it here](https://github.com/Pandurangmopgar/recruiter-agent/issues)
- Questions? Email me at pandurangmopgar7410@gmail.com
- Want to contribute? Check our [contribution guidelines](CONTRIBUTING.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Built with by [Pandurang Mopgar](https://github.com/Pandurangmopgar)
