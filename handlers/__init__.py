from aiogram import Router

router = Router()

from .start_command import router as start_rr
router.include_router(start_rr)