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
from jose.exceptions import JWTError

current_datetime = datetime.utcnow()
router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")

@router.get("/home")
def home(request: Request, db: Session = Depends(get_db)):
    try:
        token = request.session.get("user")
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized: User not logged in")

        try:
            payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM])
        except JWTError:
            # JWT decoding error, redirect to login page
            return RedirectResponse(url="/")

        username = payload.get("user_name")
        
        if not username:
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid user token")

        login_status = 1
        return templates.TemplateResponse('index.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")