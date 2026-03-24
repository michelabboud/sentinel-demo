"""Seed the database with demo data."""
from passlib.context import CryptContext
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.models.group import Group
from app.models.task import Task

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Task).delete()
db.query(Group).delete()
db.query(User).delete()
db.commit()

# Create users
admin = User(id="u-admin", email="admin@demo.com", name="Admin User", hashed_password=pwd_context.hash("Admin123!"), role="admin")
manager = User(id="u-manager", email="manager@demo.com", name="Manager User", hashed_password=pwd_context.hash("Manager123!"), role="manager")
user = User(id="u-user", email="user@demo.com", name="Regular User", hashed_password=pwd_context.hash("User123!"), role="user")

db.add_all([admin, manager, user])
db.commit()

# Create groups
engineering = Group(id="g-eng", name="Engineering", description="Engineering team")
marketing = Group(id="g-mkt", name="Marketing", description="Marketing team")

db.add_all([engineering, marketing])
db.commit()

# Add members
engineering.members.append(admin)
engineering.members.append(manager)
engineering.members.append(user)
marketing.members.append(manager)
db.commit()

# Create tasks
tasks = [
    Task(title="Set up CI/CD pipeline", status="done", priority="high", assignee_id="u-admin", group_id="g-eng"),
    Task(title="Write API documentation", status="in_progress", priority="medium", assignee_id="u-manager", group_id="g-eng"),
    Task(title="Fix login page styling", status="todo", priority="low", assignee_id="u-user", group_id="g-eng"),
    Task(title="Create marketing landing page", status="todo", priority="high", assignee_id="u-manager", group_id="g-mkt"),
    Task(title="Update brand guidelines", status="in_progress", priority="medium", group_id="g-mkt"),
]

db.add_all(tasks)
db.commit()

print("Seeded: 3 users, 2 groups, 5 tasks")
db.close()
