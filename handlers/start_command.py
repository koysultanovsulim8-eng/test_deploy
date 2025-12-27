from aiogram import Router, filters, types

router = Router()

@router.message(filters.Command('start'))
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать! '
                         'Напиши /movie для сайта кинофильмов !')
