from aiogram import Router

router = Router()

from .start_command import router as start_rr
router.include_router(start_rr)

from .movie_command import router as movie_r
router.include_router(movie_r)