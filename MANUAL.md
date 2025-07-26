# 📘 Quick Start Manual for Developers

This manual will help you start building your own project using the **DevSecOps Starter Kit**. It covers how to launch the environment, create backend APIs, design frontend pages, and integrate both.

---

## ✅ 1. Understanding the Project Structure
```
DevSecOps-Starter-Kit/
├── backend/           # FastAPI backend (APIs and DB logic)
│   ├── app/
│   │   ├── main.py    # Application entry point
│   │   ├── routes/    # API endpoints
│   │   ├── models/    # Database models
│   └── requirements.txt
│
├── frontend/          # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx    # Main React component
│   │   └── pages/     # UI pages
│   └── package.json
│
├── docker-compose.yml         # Development setup
├── docker-compose.prod.yml    # Production setup
├── .env                       # Environment variables
└── README.md
```

---

## ✅ 2. Start the Development Environment

### Using Docker:
```bash
docker-compose up -d
```
Access:
- Frontend (Dev): http://localhost:5173
- Backend API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs

---

## ✅ 3. Create Backend APIs (FastAPI)

### Example: Add a new route `/users`
1. Create a new file: `backend/app/routes/users.py`
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}
```

2. Register the route in `main.py`:
```python
from fastapi import FastAPI
from app.routes import users

app = FastAPI()
app.include_router(users.router)
```

3. Check in Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ 4. Create Frontend Pages (React + Vite)

### Example: Create a Home page
1. Create `frontend/src/pages/Home.jsx`:
```jsx
export default function Home() {
  return <h1>Welcome to My New Project 🚀</h1>;
}
```

2. Update `App.jsx`:
```jsx
import Home from "./pages/Home";

function App() {
  return (
    <div>
      <Home />
    </div>
  );
}

export default App;
```

3. Run:
```bash
cd frontend
npm run dev
```
Access: http://localhost:5173

---

## ✅ 5. Connect Frontend to Backend

Example: Fetch `/users` API from React:
```jsx
import axios from "axios";
import { useEffect, useState } from "react";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/users").then((res) => {
      setUsers(res.data.users);
    });
  }, []);

  return (
    <ul>
      {users.map((u, i) => (
        <li key={i}>{u}</li>
      ))}
    </ul>
  );
}
```

---

## ✅ 6. Add Database Support
- Define models in `backend/app/models/`
- Use SQLAlchemy for DB operations
- Migrate schema with Alembic (optional)

Example (model):
```python
from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
```

---

## ✅ 7. Deploy in Production

Build and run:
```bash
docker-compose -f docker-compose.prod.yml build --no-cache
docker-compose -f docker-compose.prod.yml up -d
```

Access:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

---

## ✅ Best Practices
- Use `.env` to manage secrets
- Run **Bandit** and **Trivy** before deploying:
```bash
bandit -r backend
trivy image devsecops-frontend
```

- Use GitHub Actions CI/CD pipeline for automation

---

🎯 **Next Steps:** Start adding your own API endpoints, build React pages, and deploy securely!
