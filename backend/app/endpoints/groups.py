from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.group import Group
from app.models.user import User
from app.schemas.group import GroupCreate, GroupRead, GroupUpdate
from app.deps import get_current_user, require_manager_or_admin

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=list[GroupRead])
def list_groups(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Group).all()


@router.post("/", response_model=GroupRead)
def create_group(body: GroupCreate, db: Session = Depends(get_db), current_user: User = Depends(require_manager_or_admin)):
    group = Group(name=body.name, description=body.description)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


@router.get("/{group_id}", response_model=GroupRead)
def get_group(group_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.patch("/{group_id}", response_model=GroupRead)
def update_group(group_id: str, body: GroupUpdate, db: Session = Depends(get_db), current_user: User = Depends(require_manager_or_admin)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    if body.name is not None:
        group.name = body.name
    if body.description is not None:
        group.description = body.description
    db.commit()
    db.refresh(group)
    return group


@router.delete("/{group_id}")
def delete_group(group_id: str, db: Session = Depends(get_db), current_user: User = Depends(require_manager_or_admin)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(group)
    db.commit()
    return {"detail": "Group deleted"}


# BUG: This endpoint has NO auth — Sentinel should catch this RBAC violation
@router.get("/{group_id}/members")
def list_group_members(group_id: str, db: Session = Depends(get_db)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    # BUG: N+1 query — loading each member's tasks individually in a loop
    result = []
    for member in group.members:
        tasks = db.query(Task).filter(Task.assignee_id == member.id).all()
        result.append({"id": member.id, "name": member.name, "task_count": len(tasks)})
    return result


# Need this import for the N+1 bug above
from app.models.task import Task
