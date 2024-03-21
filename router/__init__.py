from fastapi import APIRouter
from resources.login import router as userloginRouter
from resources.home import router as homeRouter


router = APIRouter()
router.include_router(userloginRouter, prefix='', tags=['Login'])
router.include_router(homeRouter, prefix='', tags=['Login'])
