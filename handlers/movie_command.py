from aiogram import Router, filters, types

router = Router()

@router.message(filters.Command('movie'))
async def movie_command(message: types.Message):
    await message.answer('https://www.kinopoisk.ru/'
                         'Сайт для фильмов')