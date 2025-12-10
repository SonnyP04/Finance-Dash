# Finance Dashboard

A personal financial tracking application with spending analytics and predictions.

## Features (Planned)

### Phase 1: Core Database
- ✓ PostgreSQL database setup
- ✓ Users, Transactions, Budgets tables
- ✓ Relationships and constraints

### Phase 2: FastAPI Backend
- [ ] User registration and login
- [ ] CRUD operations for transactions
- [ ] Budget management

### Phase 3: Authentication
- [ ] JWT token-based auth
- [ ] Password hashing
- [ ] Protected endpoints

### Phase 4: Analytics
- [ ] Spending by category
- [ ] Monthly reports
- [ ] Budget vs actual

### Phase 5: Machine Learning
- [ ] Spending predictions
- [ ] Anomaly detection

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT + Bcrypt
- **ML**: scikit-learn
- **ORM**: SQLAlchemy

## Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- Git

### Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/finance-dashboard.git
cd finance-dashboard
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your PostgreSQL credentials
```

5. Create database
```bash
createdb finance_app
psql -d finance_app -f ../database/schema.sql
```

6. Run the application
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for API documentation

## Project Structure