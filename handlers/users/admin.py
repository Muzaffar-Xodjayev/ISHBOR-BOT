import time
import asyncio
from aiogram import types
from aiogram.types import CallbackQuery
from data.config import ADMINS, ADMINS_NAME
from loader import dp, db, bot
from keyboards.inline.choose_format import *
from keyboards.default.ads import menu
from aiogram.types import ReplyKeyboardRemove
from states.ads import Advers
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin import admin

try:
    @dp.message_handler(text="/admin", user_id=ADMINS)
    async def show_menu(msg: types.Message):
        await msg.answer(text=f'Xush kelibsiz {msg.from_user.full_name} - ADMIN', reply_markup=menu)


    @dp.message_handler(text="👤 Foydalanuvchilar", user_id=ADMINS)
    async def all_user(msg: types.Message):
        users = await db.select_all_user()
        text = f"Bazada <b>{len(users)}</b> ta foydalanuvchi bor\n\n"
        await bot.send_message(msg.from_user.id, text)

    @dp.message_handler(text='📊 Statistika', user_id = ADMINS)
    async def statistik(msg: types.Message):
        text = f"Qaysi bo'limning statistikasini olmoqchisiz?"
        await bot.send_message(chat_id=msg.from_user.id,text=text,reply_markup=admin)

    @dp.callback_query_handler(text='ish_statistika')
    async def show_need_job_st(call: CallbackQuery):
        await call.answer(cache_time=60)
        text = f'Botga <b>{await db.select_count_post()}</b> ta "Ish Kerak" bo\'limidan e\'lonlar yuborilgan.'
        await call.message.edit_text(text)

    @dp.callback_query_handler(text="xodim_statistika")
    async def show_need_job_st(call: CallbackQuery):
        await call.answer(cache_time=60)
        text = f'Botga <b>{await db.select_count_work()}</b> ta "Xodim Kerak" bo\'limidan e\'lonlar yuborilgan.'
        await call.message.edit_text(text)

    @dp.callback_query_handler(text='umumiy_statistika')
    async def total_report(call: CallbackQuery):
        await call.answer(cache_time=60)
        total = int(await db.select_count_work()) + int(await db.select_count_post())
        text= f"Botga Umumiy {total} - ta E'lon yuborilgan."
        await call.message.edit_text(text)

    @dp.message_handler(text="👮🏼‍♂️ Adminlar", user_id=ADMINS)
    async def show_admins(msg: types.Message):
        users = ADMINS
        text = f"Botda {len(users)} ta admin bor:\n\n"
        num = 0
        a = ''
        for i in range(0, len(users)):
            num += 1
            a += f"{num}. <a href='tg://user?id={ADMINS[i]}'>{ADMINS_NAME[i]} [{ADMINS[i]}]</a>\n"
        text += a
        await bot.send_message(msg.from_user.id, text)


    @dp.message_handler(text="📝 Xabar Yuborish", user_id=ADMINS)
    async def check_adver(msg: types.Message):
        await msg.answer("Xabarni yuboring:",reply_markup=cancel)
        await Advers.text.set()


    @dp.message_handler(state=Advers.text, content_types=['text', 'video', 'photo', 'audio', 'location'],
                        user_id=ADMINS)
    async def send_ads(msg: types.Message, state: FSMContext):
        users = await db.select_all_user()
        text_caption = msg.caption
        text_type = msg.content_type
        text = msg.html_text
        rep_btn = msg.reply_markup

        send_user = 0
        send_error = 0
        for user in users:
            user_id = user[3]
            try:
                if text_type == 'sticker':
                    return
                elif text_type == 'text':
                    await bot.send_message(chat_id=user_id,text=text,reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'video':
                    await bot.send_video(user_id, msg.video.file_id, caption=text_caption,reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'photo':
                    await bot.send_photo(user_id, msg.photo[-1].file_id, caption=text_caption,reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'audio':
                    await bot.send_audio(user_id, msg.audio,reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'location':
                    lat = msg.location['latitude']
                    lon = msg.location['longitude']
                    await bot.send_location(chat_id=user_id, latitude=lat, longitude=lon,reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                send_user += 1
            except Exception:
                send_error += 1
                continue
        if send_user == 0:
            await bot.send_message(msg.from_user.id, 'Xech kimga yuborilmadi')
        else:
            await bot.send_message(msg.from_user.id,
                                   f"Jonatildi: <b>{send_user + send_error}</b> ta foydalanuvchiga\n"
                                   f"Aktiv A'zolar: <b>{send_user}</b> ta \n"
                                   f"Ban bergan a'zolar: <b>{send_error}</b> ta\n")
        await state.finish()

    @dp.callback_query_handler(text='bekor_qilish',state=Advers.text)
    async def cancel_admin(call: CallbackQuery, state:FSMContext):
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"Xabar yuborish bekor qilindi.")
        await state.finish()

    @dp.message_handler(text="🔙 Chiqish", user_id=ADMINS)
    async def send_adver(msg: types.Message):
        await msg.answer("Siz ADMIN PANEL dan chiqdingiz", reply_markup=ReplyKeyboardRemove(True))
except:
    print('Bu foydalanuvchi admin emas')


@dp.message_handler(commands="admin")
async def check_admin(msg: types.Message):
    await msg.answer(f"{msg.from_user.full_name}. Siz ADMIN emassiz 😉.")
