import re
import uuid
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

# local
from data.config import ADMINS
from keyboards.inline.subs import show_channels
from loader import dp,db, bot
from keyboards.inline.choose_format import *
from keyboards.default.contact import menu,otmen
from states.simple_job import simple
from utils.misc.subs import check_sub_channels


@dp.callback_query_handler(text='ish_kerak')
async def need_job(call: CallbackQuery):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.edit_text(f"Sizning mutaxasisligingiz qaysi turga kiradi.",reply_markup=choose_how)
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)


@dp.callback_query_handler(text='boshqa_ish')
async def simple_job(call: CallbackQuery, state:FSMContext):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.edit_text(
            f"Assalomu alaykum, hurmatli {call.from_user.full_name}. Sizga beriladigan savollarga rost va to'g'ri javob berishingizni so'raymiz 😇.")
        await call.message.answer(
            f"<b>1-savol</b>\n\nTo'liq Ism Familiyangizni kiriting.\n<em>Masalan: ( Abdullayev Muminjon )</em> ")
        await simple.fio.set()
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"

@dp.message_handler(state=simple.fio)
async def name(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"full_name":msg.text}
    )
    await msg.answer(f"<b>2-savol</b>\n\nYoshingizni kiriting\n<em>Masalan: ( 19 )</em> :")
    await simple.yosh.set()

@dp.message_handler(state=simple.yosh)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"age":msg.text}
    )
    await msg.answer(f"<b>3-savol</b>\n\nKasbingizni yozing:\n"
                     f"<em>Masalan (sartarosh)</em>:")
    await simple.kasbi.set()

@dp.message_handler(state=simple.kasbi)
async def get_job(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"job":msg.text.capitalize()}
    )
    await msg.answer(f"<b>4-savol</b>\n\n"
                     f"Tarjibangiz bo'lsa yozing aks holda <em>yo'q</em> deb yozing:\n"
                     f"<em>Masalan: ( 2-yil )</em>")
    await simple.tajriba.set()

@dp.message_handler(state=simple.tajriba)
async def get_exp(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"exp":msg.text}
    )
    await msg.answer(f"<b>5-savol</b>\n\n"
                     f"Telegram akkaunt yozing: \n<em>Masalan ( @Manager_boshqaruvchi )</em>")
    await simple.telegram.set()

@dp.message_handler(state=simple.telegram)
async def get_tlg(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"telegram":msg.text}
    )
    await msg.answer(f"<b>6-savol</b>\n\n"
                     f'Telefon raqam yuboring: \n<em>(Telefon raqam yuborish tugmasini</em> bosing)',reply_markup=menu)
    await simple.aloqa.set()

@dp.message_handler(state=simple.aloqa, content_types=types.ContentType.CONTACT)
async def get_phone(msg: types.Message, state:FSMContext):
    txt = msg.contact.phone_number
    try:
        if txt.find("+") == -1:
            m = f"+{txt}"
            x = re.search("^[\+][998]{3}", m)
            if x:
                await state.update_data(
                    {"phone": m}
                )
                await msg.answer(f"<b>7-savol</b>\n\n"
                                 f'Hududingizni yozing: \n<em>Masalan ( Toshkent )</em>\n',reply_markup=ReplyKeyboardRemove(True)
                                 )
                await simple.hudud.set()
            else:
                await msg.answer(f"Faqat O'zbekistan davlatiga tegishli raqamni yuboring", reply_markup=menu)
        else:
            x = re.search("^[\+][998]{3}", txt)
            if x:
                await state.update_data(
                    {"phone": txt}
                )
                await msg.answer(f"<b>7-savol</b>\n\n"
                                 f'Hududingizni yozing: \n<em>Masalan ( Toshkent )</em>\n',reply_markup=ReplyKeyboardRemove(True))
                await simple.hudud.set()
            else:
                await msg.answer(f"Faqat O'zbekistan davlatiga tegishli raqamni yuboring", reply_markup=menu)

    except:
        print("uzb nomer emas")


@dp.message_handler(state=simple.aloqa, content_types=['text'])
async def get_phone(msg: types.Message):
    await msg.answer(f"Iltimos <em>(Telefon raqam yuborish tugmasini</em> bosing)",reply_markup=menu)
    await simple.aloqa.set()

@dp.message_handler(state=simple.hudud)
async def get_area(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"hudud":msg.text.capitalize()}
    )
    await msg.answer(f"<b>8-savol</b>\n\n"
                     f"Murojaat qilish vaqtini yozing: \n"
                     f"<em>Masalan (8:00-18:00)</em>")
    await simple.murojat_vaqti.set()

@dp.message_handler(state=simple.murojat_vaqti)
async def vaqt(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"m_vaqt":msg.text.capitalize()}
    )
    await msg.answer(f"<b>9-savol</b>\n\n"
                     f"Maqsadingizni yozing: \n"
                     f"<em>Masalan (Yaxshi va halol ishda ishlash)</em>")
    await simple.maqsad.set()

@dp.message_handler(state=simple.maqsad)
async def maq(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"maqsad":msg.text}
    )
    try:
        data = await state.get_data("maqsad")
        full_name = data['full_name']
        age = data['age']
        job = data['job']
        exp = data['exp']
        telegram = data['telegram']
        phone = data['phone']
        hudud = data['hudud']
        m_vaqt = data['m_vaqt']
        maqsad = data['maqsad']
        post = f"Ma'lumotlaringizni hammasi to'g'rimi ?\n\n"
        post += f"👨‍💼 Ishchi: {full_name}\n"
        post += f"🕑 Yosh: {age}\n"
        post += f"📚 Kasb: {job}\n"
        post += f"💼 Tajriba: {exp}\n"
        post += f"📎 Telegram: {telegram}\n"
        post += f"📞 Aloqa: {phone}\n"
        post += f"🏘 Hudud: {hudud}\n"
        post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
        post += f"📈 Maqsad: {maqsad}"
        await state.update_data(
            {"post":post}
        )
        await msg.answer(text=post, reply_markup=check_post)
    except:
        await msg.answer(f"Nimadir Xato ketti !")
    await simple.check.set()

@dp.callback_query_handler(text='xa', state=simple.check)
async def checked(call: CallbackQuery, state:FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Hurmatli {call.from_user.full_name}, e'loningiz uchun rahmat.\n Sizning e'loningiz 2-bosqichga o'tkazildi. Agar muvaffaqiyatli o'tsa 2 - kun ichida <a href='https://t.me/vakansiya_ishbor_nam'>Ish Bor | Kerak</a> kanaliga joylanadi. Aks holda to'gri tushunasiz. 😊",reply_markup=ReplyKeyboardRemove(True))
    try:
        data = await state.get_data("maqsad")
        full_name = data['full_name']
        # print(get_post_id)
        age = data['age']
        job = data['job']
        exp = data['exp']
        telegram = data['telegram']
        phone = data['phone']
        hudud = data['hudud']
        m_vaqt = data['m_vaqt']
        maqsad = data['maqsad']
        myUnique = ""
        try:
            myUnique += str(uuid.uuid4())
            await db.add_post(myUnique)
        except:
            pass
        one = await db.select_one_post(myUnique)
        post = f"Ish joyi kerak: <b>№{one['id']}</b>\n\n"
        post += f"👨‍💼 Ishchi: {full_name}\n"
        post += f"🕑 Yosh: {age}\n"
        post += f"📚 Kasb: {job}\n"
        post += f"💼 Tajriba: {exp}\n"
        post += f"📎 Telegram: {telegram}\n"
        post += f"📞 Aloqa: {phone}\n"
        post += f"🏘 Hudud: {hudud}\n"
        post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
        post += f"📈 Maqsad: {maqsad}\n\n"
        post += f"@vakansiya_ishbor_nam — Ish oluvchi va beruvchilarni uchrashtiruvchi  platforma\n\n"
        post += f"#ish_joyi #{hudud.lower()}"
        for i in ADMINS:
            await bot.send_message(chat_id=i, text=post)
        text = f"Sizning navbatingiz – {one['id']}. Kanalni kuzatishda davom eting !\n\n"
        text += f"<b>Kanallar ro'yhati</b>: \n\n"
        text += f"@vakansiya_ishbor_nam – Ish izlaganlar uchun\n"
        text += f"@ishkerak_bor – Xodim izlaganlar uchun\n"
        text += f"@elonpeshtaxta – Muhokama uchun Chat."
        await call.message.answer(text=text, reply_markup=main)
    except:
        await call.message.answer(f"xato !")
    await state.finish()

@dp.callback_query_handler(text='yoq', state=simple.check)
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(f"Hurmatli {call.from_user.full_name}, e'loningiz bekor qilindi. Qaytadan e'lon bering. Buning uchun Bosh Sahifa tugmasini bosing.",reply_markup=main)
    await state.finish()

@dp.callback_query_handler(text='bosh_sahifa')
async def welcome(call: CallbackQuery):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(
            f"Assalomu alaykum, {call.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)

