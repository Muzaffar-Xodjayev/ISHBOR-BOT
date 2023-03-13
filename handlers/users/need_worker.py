import uuid

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.subs import show_channels
from loader import db, dp, bot
from keyboards.inline.choose_format import *
from data.config import ADMINS
from states.need_worker import worker
from utils.misc.subs import check_sub_channels


@dp.callback_query_handler(text='hodim_kerak')
async def welcome(call: CallbackQuery):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.answer(
            f"Assalomu alaykum, hurmatli {call.from_user.full_name}. Sizga beriladigan savollarga rost va to'g'ri javob berishingizni so'raymiz 😇.")
        await call.message.answer(f"<b>1-savol</b>\n\nSizga qanday hodim kerak.\n<em>Masalan: ( Grafik Dizayner, Web Dasturchi )</em> ")
        await worker.hodim.set()
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)

@dp.message_handler(state=worker.hodim)
async def get_hodim(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"hodim":msg.text}
    )
    await msg.answer(f"<b>2-savol</b>\n\nE'lon haqida qisqacha ta'rif.\n<em>Masalan: ( O'z ishini yaxshi biladigan va halol hodim kerak. )</em> ")
    await worker.tarif.set()

@dp.message_handler(state=worker.tarif)
async def get_tarif(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"tarif":msg.text.capitalize()}
    )
    await msg.answer(f"<b>2-savol</b>\n\nKompaniya nomi:\n"
                        f"<em>Masalan: ( Unisoft )</em>")
    await worker.kompaniya.set()

@dp.message_handler(state=worker.kompaniya)
async def get_comp_name(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"kompaniya":msg.text.capitalize()}
    )
    await msg.answer(f"<b>3-savol</b>\n\nHududni yozing:\n"
                        f"<em>Masalan: ( Toshkent )</em>")
    await worker.hudud.set()

@dp.message_handler(state=worker.hudud)
async def get_comp_name(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"hudud":msg.text.capitalize()}
    )
    await msg.answer(f"<b>4-savol</b>\n\nTalablar:\n"
                        f"<em>Masalan: ( Tajribasi 6-oy dan kam bo'lmasligi va h.k )</em>")
    await worker.talablar.set()

@dp.message_handler(state=worker.talablar)
async def talablar(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"talab":msg.text.capitalize()}
    )
    await msg.answer(f"<b>5-savol</b>\n\nMaosh:\n"
                        f"<em>Masalan: ( 200$ yoki suhbat asosida )</em>")
    await worker.maosh.set()

@dp.message_handler(state=worker.maosh)
async def get_maosh(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"maosh":msg.text}
    )
    await msg.answer(f"<b>6-savol</b>\n\nTelegram akkaunt yozing:\n"
                     f"<em>Masalan ( @Manager_boshqaruvchi )</em>")
    await worker.telegram.set()

@dp.message_handler(state=worker.telegram)
async def get_telegram(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"telegram":msg.text}
    )
    await msg.answer(f"<b>7-savol</b>\n\nTelefon raqam yozing:\n"
                     f"<em>Masalan ( +998991234567 )</em>")
    await worker.aloqa.set()

@dp.message_handler(state=worker.aloqa)
async def get_aloqa(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"aloqa":msg.text}
    )
    await msg.answer(f"<b>8-savol</b>\n\nMurojat qilish vaqtini yozing:\n"
                     f"<em>Masalan ( 8:00-19:00 )</em>")
    await worker.murojat_vaqti.set()

@dp.message_handler(state=worker.murojat_vaqti)
async def m(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"m_vaqt":msg.text}
    )
    await msg.answer(f"<b>9-savol</b>\n\nMa'sul shahs ismini yozing:")
    await worker.masul.set()

@dp.message_handler(state=worker.masul)
async def masul_shahs(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"masul": msg.text.capitalize()}
    )
    data = await state.get_data("masul")
    hodim = data['hodim']
    tarif = data['tarif']
    kompaniya = data['kompaniya']
    hudud = data['hudud']
    talab = data['talab']
    maosh = data['maosh']
    telegram = data['telegram']
    aloqa = data['aloqa']
    m_vaqt = data['m_vaqt']
    masul = data['masul']
    post = f"Ma'lumotlar hammasi to'g'rimi ?\n\n"
    post += f"👨‍💼 Xodim: {hodim}\n"
    post += f"<em>  📌 {tarif}</em>\n"
    post += f"🏢 Idora: {kompaniya}\n"
    post += f"🗺  Hudud: {hudud}\n"
    post += f"‼️ Talab: {talab}\n"
    post += f"💰 Maosh: {maosh}\n"
    post += f"🔗 Telegram: {telegram}\n"
    post += f"☎️ Aloqa: {aloqa}\n"
    post += f"🕰 Murojaat qilish vaqti: {m_vaqt}\n"
    post += f"✍️ Mas'ul: {masul}"
    await msg.answer(text=post, reply_markup=check_post)
    await worker.check.set()

@dp.callback_query_handler(text='xa',state=worker.check)
async def checked_post(call: CallbackQuery,state:FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(
        f"Hurmatli {call.from_user.full_name}, e'loningiz uchun rahmat.\n Sizning e'loningiz 2-bosqichga o'tkazildi, agar muvaffaqiyatli o'tsa 2 - kun ichida <a href='https://t.me/vakansiya_ishbor_nam'>Ish Bor | Kerak</a> kanaliga joylanadi. Aks holda to'gri tushunasiz. 😊",
        reply_markup=main)
    data = await state.get_data("masul")
    hodim = data['hodim']
    tarif = data['tarif']
    kompaniya = data['kompaniya']
    hudud = data['hudud']
    talab = data['talab']
    maosh = data['maosh']
    telegram = data['telegram']
    aloqa = data['aloqa']
    m_vaqt = data['m_vaqt']
    masul = data['masul']
    myUnique2 = ""
    try:
        myUnique2 += str(uuid.uuid4())
        await db.add_work(myUnique2)
    except:
        pass
    one = await db.select_one_work(myUnique2)
    post = f"Xodim kerak: <b>№{one['id']}</b>\n\n"
    post += f"👨‍💼 Xodim: {hodim}\n"
    post += f"<em>  📌 {tarif}</em>\n"
    post += f"🏢 Idora: {kompaniya}\n"
    post += f"🗺  Hudud: {hudud}\n"
    post += f"‼️ Talab: {talab}\n"
    post += f"💰 Maosh: {maosh}\n"
    post += f"⚡️Ish holati: #aktiv \n"
    post += f"🔗 Telegram: {telegram}\n"
    post += f"☎️ Aloqa: {aloqa}\n"
    post += f"🕰 Murojaat qilish vaqti: {m_vaqt}\n"
    post += f"✍️ Mas'ul: {masul}\n\n"
    post += f"@vakansiya_ishbor_nam — Ish oluvchi va beruvchilarni uchrashtiruvchi  platforma\n\n"
    post += f"#xodim #{hudud.lower()}"
    for i in ADMINS:
        await bot.send_message(chat_id=i,text=post)
    text = f"Sizning navbatingiz – {one['id']}. Kanalni kuzatishda davom eting !\n\n"
    text += f"<b>Kanallar ro'yhati</b>: \n\n"
    text += f"@vakansiya_ishbor_nam – Ish izlaganlar uchun\n"
    text += f"@ishkerak_bor – Xodim izlaganlar uchun\n"
    text += f"@elonpeshtaxta – Muhokama uchun Chat."
    await call.message.answer(text=text, reply_markup=main)
    await state.finish()

@dp.callback_query_handler(text='yoq', state=worker.check)
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


