from fastapi import APIRouter, Depends, HTTPException, FastAPI, Request, Form
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from config.base_config import BaseConfig
from fastapi.staticfiles import StaticFiles
from datetime import  datetime,date, timedelta
from models import get_db,models
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from resources.utils import create_access_token
from starlette.middleware.sessions import SessionMiddleware
from jose import jwt, JWTError

current_datetime = datetime.utcnow()
router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")







@router.get("/leader")
def home(request:Request,db:Session=Depends(get_db)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")

        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            login_status=1
            
            return templates.TemplateResponse('leader.html', context={'request': request,"login_status":login_status,"username":username}) 
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401,detail="Unauthorized")

@router.get("/leaderboard_data")
def leaderboard_data(request: Request, db: Session = Depends(get_db)):
    try:
        # Check if user is logged in
        token = request.session.get("user")
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Decode JWT token to get username
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
        username = payload.get("user_name")
        if not username:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Fetch all users and their scores
        user_scores = db.query(models.Score.Username, models.Score.score, models.Score.submitted_at).all()

        # Calculate total points for each user
        user_points = {}
        for user, score, _ in user_scores:
            user_points[user] = user_points.get(user, 0) + score

        # Sort users based on submitted time and total points
        sorted_users = sorted(user_scores, key=lambda x: (x[2], -user_points[x[0]]))  # Sort by submitted time ascending, then total points descending

        # Generate leaderboard data
        leaderboard_data = []
        position = 1
        prev_points = None
        for user, score, submitted_at in sorted_users:
            # Check for tie and break it using total points
            if user_points[user] != prev_points:
                position += 1
            leaderboard_data.append({"position": position, "teamname": user, "points": user_points[user]})
            prev_points = user_points[user]

        return JSONResponse(content=leaderboard_data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")