# BudgetSyncAPI

BudgetSync API is a secure and extensible REST API built with **FastAPI** for tracking personal finances — including income, expenses, and savings goals.

It features full JWT-based authentication, analytics-ready endpoints, and a local database for storing transaction history. Fully containerized with Docker and CI/CD-ready with Jenkins.

---

## Features
- User Registration & JWT Login. -> Create & Retrieve Financial Transactions  
- Classify transactions by type & category  
- Auto timestamping and summaries  
- Secure password storage using bcrypt  
- SQLite database for local persistence  
- Docker container support  
- Jenkinsfile for CI/CD automation  
- Fully tested with Pytest  

---

## 🛠️ Tech Stack

| Layer          | Technology          |
|----------------|---------------------|
| API Framework  | FastAPI              |
| Auth           | JWT + OAuth2         |
| Database       | SQLite + SQLAlchemy  |
| Security       | bcrypt, python-jose  |
| Testing        | Pytest               |
| Container      | Docker               |
| CI/CD          | Jenkins              |

---

## Installation

```bash
git clone https://github.com/yourusername/budgetsync-api.git
cd budgetsync-api
pip install -r requirements.txt
uvicorn app.main:app --reload
