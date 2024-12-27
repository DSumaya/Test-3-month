from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import  database

dialog_router = Router()

class Complaint (StatesGroup):
    name = State()
    phone_or_instagram = State()
    complaint_comment = State()

@dialog_router.message(Command("complaint"))
async def complaint_name(message: types.Message, state: FSMContext):
    await message.answer('Как вас зовут?')
    await state.set_state(Complaint.name)


@dialog_router.message(Complaint.name)
async def phone_or_instagram(message: types.Message, state:FSMContext):
    await state.update_data(name =message.text)
    await message.answer('Введите номер телефона или акк инстаграмм:')
    await state.set_state(Complaint.phone_or_instagram)


@dialog_router.message(Complaint.phone_or_instagram)
async def complaint_comment(message: types.Message, state: FSMContext):
    await state.update_data(phone_or_instagram = message.text)
    await message.answer('Опишите вашу проблему или жалобу:')
    await state.set_state(Complaint.complaint_comment)

@dialog_router.message(Complaint.complaint_comment)
async def complaint_finish(message: types.Message, state:FSMContext):
    await state.update_data(complaint_comment = message.text)
    await message.answer('Мы свяжемся с вами в ближайшее время. Спасибо за обратную связь!')
    data = await state.get_data()
    print(data)
    database.save_dialog(data)

    await state.clear()


