import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.choose_format import choose_job
from aiogram.types import CallbackQuery
from keyboards.inline.subs import show_channels
from utils.misc.subs import check_sub_channels
from data.config import ADMINS, CHANNELS
from loader import dp, db, bot

@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    name = message.from_user.full_name
    is_subs = await check_sub_channels(message)
    if is_subs:
        try:
            await db.add_user(
                telegram_id=message.from_user.id,
                full_name=name,
                username=message.from_user.username
            )
            await message.answer(
                f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
                reply_markup=choose_job)
            count = await db.select_all_user()
            msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
            for user in ADMINS:
                await bot.send_message(user, msg)

        except asyncpg.exceptions.UniqueViolationError:
            await message.answer(f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.",
                                      reply_markup=choose_job)
    else:
        btn = await show_channels()
        context = f"Xurmatli {message.from_user.full_name} botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
        await message.answer(text=context,reply_markup=btn)

@dp.message_handler()
async def just_text(message: types.Message):
    is_subs = await check_sub_channels(message)
    if is_subs:
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
    else:
        btn = await show_channels()
        context = f"Xurmatli {message.from_user.full_name} botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
        await message.answer(text=context, reply_markup=btn)

@dp.callback_query_handler(text='sub_channel_done')
async def check_kanal(call: CallbackQuery):
    async def is_subs(message):
        for channel in CHANNELS:
            check = await bot.get_chat_member(chat_id='-100' + str(channel[1]), user_id=message.id)
            if check.status == 'left':
                return False

        return True
    che_subs = await is_subs(call["from"])
    if che_subs:
        await call.message.delete()
        try:
            await db.add_user(
                telegram_id=call.from_user.id,
                full_name=call.from_user.full_name,
                username=call.from_user.username
            )
            await call.message.answer(
                f"Assalomu alaykum, {call.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b> Botiga xush kelibsiz!",reply_markup=choose_job)
            count = await db.select_all_user()
            msg = f"{call.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
            try:
                for user in ADMINS:
                    await bot.send_message(user, msg)
            except:
                pass
        except asyncpg.exceptions.UniqueViolationError:
            await call.message.answer(
                f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.",reply_markup=choose_job)
    else:
        await call.answer(text="Berilgan kanallarga obuna bo'ling !", show_alert=True)
