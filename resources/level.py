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


problem = {
    "l1c1" : "XXl1c1flagGY9IWGM",
    "l1c2" : "XXl1c2flagZ7KKLEC",
    "l1c3" : "XXl1c3flagpetshop",
    "l1c4" : "XXl1c4flagNIPJTR7",
    "l1c5" : "XXl1c5flagIB3BWYJ",
    "l2c1" : "XXl2c1flagRGMCR4J",
    "l2c2" : "XXl2c2flagWR6CFRY"
}

problem_score = {
    "l1c1" : 5,
    "l1c2" : 8,
    "l1c3" : 10,
    "l1c4" : 12,
    "l1c5" : 15,
    "l2c1" : 20,
    "l2c2" : 30
}



@router.get("/level1")
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
        return templates.TemplateResponse('level1.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get('/final')
def login(request:Request,):
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
        return templates.TemplateResponse('final.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")



@router.get("/l1c1")
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
        return templates.TemplateResponse('level1/l1c1.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l1c2")
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
        return templates.TemplateResponse('level1/l1c2.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l1c3")
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
        return templates.TemplateResponse('level1/l1c3.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l1c4")
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
        return templates.TemplateResponse('level1/l1c4.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l1c5")
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
        return templates.TemplateResponse('level1/l1c5.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l2c1")
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
        return templates.TemplateResponse('final/l2c1.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/l2c2")
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
        return templates.TemplateResponse('final/l2c2.html', context={'request': request, "login_status": login_status, "username": username})
    except HTTPException as http_exception:
        return RedirectResponse(url="/")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/flag_verify")
def home(request:Request,db:Session=Depends(get_db), flag : str = Form(...), pblm_id : str = Form(...)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")

        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            status = False 
            if problem[pblm_id] == flag:
                score = db.query(models.Score).filter(models.Score.Username == username, models.Score.problem_id == pblm_id).first()
                if not score:
                    new = models.Score(
                        Username = username,
                        problem_id = pblm_id,
                        score = problem_score[pblm_id]
                    )
                    db.add(new)
                    db.commit()
                    status = True
                else:
                    status = "repeat"
            
            return JSONResponse({"status" : status}) 
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401,detail="Unauthorized")

@router.get("/get_flag")
def home(request:Request,db:Session=Depends(get_db)):
    return JSONResponse({"data" : "XXl2c1flagRGMCR4J"}) 


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