📚 Multi-Agent Research & Report Writer

A multi-agent AI application that researches a given topic and generates a structured research report in both **Markdown and PDF** format.

🚀 Features

- AI-powered research
- Multiple specialized CrewAI agents
- Tavily web search
- Research, analysis, writing, and editing workflow
- Markdown (`.md`) report generation
- PDF generation and download
- SQLite database for storing reports
- Streamlit frontend
- FastAPI backend

🏗️ Tech Stack

- Python
- Streamlit
- FastAPI
- CrewAI
- LiteLLM
- Gemini / Groq
- Tavily
- SQLAlchemy
- SQLite
- Pydantic
- ReportLab

🔄 Working Flow

```text
User enters topic
       ↓
Streamlit Frontend
       ↓
FastAPI Backend
       ↓
CrewAI
       ↓
Research Agent → Analyst Agent → Writer Agent → Editor Agent
       ↓
Final Report
       ↓
.md + .pdf
       ↓
Database
       ↓
PDF Download

📁 Project Structure

Research generator/
├── Backend/
│   ├── api/
│   ├── services/
│   ├── utils/
│   ├── agents.py
│   ├── tasks.py
│   ├── crew.py
│   ├── tools.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── Frontend/
│   └── app.py
│
├── reports/
├── README.md
└── .gitignore

Coding Working Flow
## 🔄 Complete Working Flow

```text
User enters a topic
        ↓
Frontend (app.py)
        ↓
FastAPI API (api/report.py)
        ↓
Report Service (services/report_service.py)
        ↓
CrewAI (crew.py)
        ↓
Agents (agents.py)
        ↓
Tasks (tasks.py)
        ↓
Research Agent → Tavily Search (tools.py)
        ↓
Analyst Agent
        ↓
Writer Agent
        ↓
Editor Agent
        ↓
Final Research Report
        ↓
report_service.py
   ┌────┴────┐
   ↓         ↓
  .md       .pdf
   │         │
   └────┬────┘
        ↓
SQLite Database
        ↓
Frontend
        ↓
Download PDF

📂 What Each Python File Does
           File	                            Purpose
Frontend/app.py	Streamlit UI. Takes the topic and displays the result.

Backend/main.py	Starts the FastAPI application and loads the API routes.

Backend/api/report.py	Handles report generate, view, download, and delete requests.

Backend/services/report_service.py	Main business logic. Runs CrewAI, saves .md, 
creates .pdf, and stores report information.

Backend/crew.py	Connects the agents and tasks and runs the CrewAI workflow.

Backend/agents.py	Defines the Research, Analyst, Writer, and Editor agents.

Backend/tasks.py	Defines what each agent has to do.

Backend/tools.py	Configures the Tavily search and extraction tools.

Backend/config.py	Loads API keys and model configuration from .env.

Backend/models.py	Defines the SQLite database table using SQLAlchemy.

Backend/schemas.py	Defines API request and response formats using Pydantic.

Backend/database.py	Creates and manages the database connection.

Backend/utils/pdf_generator.py	Converts the final Markdown report into a PDF.

⚙️ Setup

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd "Research generator"

Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\Activate.ps1

Install dependencies:

cd Backend
pip install -r requirements.txt

Create a .env file inside Backend/:

GEMINI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
MODEL=your_model
▶️ Run Backend

From the Backend folder:

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
▶️ Run Frontend

Open another terminal and activate the virtual environment:

cd "Research generator"
.\venv\Scripts\Activate.ps1
cd Frontend
streamlit run app.py

The application will open in your browser.

🌐 Deployment

The backend can be deployed using Render, and the frontend can be deployed using Streamlit Community Cloud.

API keys should be added as environment variables on the deployment platforms and should never be uploaded to GitHub.

👨‍💻 Author

Kauser Ahmed Anik
OSTAD Learning Project