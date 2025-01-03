# TalentScout AI 🤖

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-orange.svg)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Gemini--1.5--Flash-green.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An intelligent technical interview assistant powered by Google's Gemini-1.5-Flash model

## 🎯 Overview

TalentScout AI automates technical interviews by conducting adaptive assessments, providing real-time evaluations, and generating comprehensive reports.

## ✨ Features

- Dynamic question generation based on tech stack
- Real-time response evaluation using Gemini AI
- Comprehensive PDF report generation
- Multi-stage interview process
- Context-aware conversations
- Secure data handling

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python 3.8+
- **AI Model:** Google Gemini-1.5-Flash
- **PDF Generation:** ReportLab
- **State Management:** Streamlit Session State

## 📦 Installation 

1. Clone the repository:

```bash
git clone https://github.com/Pandurangmopgar/recruiter-agent.git
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment

```bash
source venv/bin/activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

# Configure environment

```bash
cp .env.example .env
```

## 📁 Project Structure

recruiter-agent/
├── src/
│ ├── app.py # Main application
│ ├── agent/
│ │ ├── conversation.py # Interview logic
│ │ └── evaluation.py # AI evaluation
│ └── utils/
│ └── pdf_generator.py # PDF generation
├── tests/ # Test suite
├── .env.example # Environment template

## ⚙️ Configuration

```bash
# Required environment variables (.env)
GOOGLE_API_KEY=your-api-key-here
MODEL_NAME=gemini-1.5-flash
MAX_TOKENS=2048
TEMPERATURE=0.7
```

## 🚀 Usage

```bash
streamlit run src/app.py
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

## 📞 Support

- Issues: [GitHub Issues](https://github.com/Pandurangmopgar/recruiter-agent/issues)
- Email:pandurangmopgar7410@gmail.com

---
Made with ❤️ by [Pandurang Mopgar](https://github.com/Pandurangmopgar)
