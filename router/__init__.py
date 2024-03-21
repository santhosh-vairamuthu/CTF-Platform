from fastapi import APIRouter
from resources.login import router as userloginRouter
from resources.home import router as homeRouter
from resources.level import router as levelRouter
from resources.leader import router as leaderRouter


router = APIRouter()
router.include_router(userloginRouter, prefix='', tags=['Login'])
router.include_router(homeRouter, prefix='', tags=['Login'])
router.include_router(levelRouter, prefix='', tags=['Login'])
router.include_router(leaderRouter, prefix='', tags=['Login'])
