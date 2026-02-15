from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.grievance import Grievance
from app.models.user import User
from app.schemas.grievance import GrievanceCreate, GrievanceStatusUpdate
from app.api.deps import get_db, get_current_user, require_role

router = APIRouter()


@router.post("/")
def create_grievance(data: GrievanceCreate,
                     db: Session = Depends(get_db),
                     user: User = Depends(require_role("student"))):

    grievance = Grievance(
        title=data.title,
        description=data.description,
        is_anonymous=data.is_anonymous,
        created_by=None if data.is_anonymous else user.id
    )

    db.add(grievance)
    db.commit()
    db.refresh(grievance)

    return {"success": True, "data": {"id": grievance.id}}


@router.get("/")
def list_grievances(db: Session = Depends(get_db),
                    user: User = Depends(get_current_user)):

    if user.role in ["admin", "authority"]:
        items = db.query(Grievance).all()
    else:
        items = db.query(Grievance).filter(
            Grievance.created_by == user.id
        ).all()

    return {"success": True, "data": items}


@router.put("/{grievance_id}")
def update_status(grievance_id: int,
                  payload: GrievanceStatusUpdate,
                  db: Session = Depends(get_db),
                  user: User = Depends(require_role("authority"))):

    grievance = db.query(Grievance).filter(
        Grievance.id == grievance_id
    ).first()

    if not grievance:
        raise HTTPException(status_code=404, detail="Not found")

    grievance.status = payload.status
    db.commit()

    return {"success": True}
