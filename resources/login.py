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
#from jose import jwt, JWTError
current_datetime = datetime.utcnow()
router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")

@router.get('/login')
def login(request:Request,):
      return templates.TemplateResponse('login.html', context={'request': request})
  

@router.post("/logcheck")
def logcheck(request:Request,db:Session=Depends(get_db),username:str=Form(...),password:str=Form(...)):
    find=db.query(models.User).filter(models.User.Username==username,models.User.Password==password).first()
    print(find)
    if find is not None:
        error="Valid Creditional"
        access_token_expires = timedelta(minutes=BaseConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"user_name": find.Username},expires_delta=access_token_expires)
        sessid = access_token
        request.session["user"] = sessid
        error= "Done"   
        return RedirectResponse("/home", status_code=303)
    else:
        error= "Invalid password or username"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)