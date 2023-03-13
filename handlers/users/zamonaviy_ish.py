import re
import uuid
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.inline.subs import show_channels
from states.modern_job import modern_job
from loader import dp, db, bot
from keyboards.inline.choose_format import *
from keyboards.default.contact import menu
from utils.misc.subs import check_sub_channels


@dp.callback_query_handler(text='ish_kerak')
async def need_job(call: CallbackQuery, state: FSMContext):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.edit_text(f"Sizning mutaxasisligingiz qaysi turga kiradi.",reply_markup=choose_how)
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)

@dp.callback_query_handler(text='zamonaviy_kasb')
async def zamonaviy_kasb(call: CallbackQuery, state: FSMContext):
    is_subs = await check_sub_channels(call)
    if is_subs:
        await call.answer(cache_time=60)
        await call.message.edit_text(f"Assalomu alaykum, hurmatli {call.from_user.full_name}. Sizga beriladigan savollarga rost va to'g'ri javob berishingizni so'raymiz 😇.")
        await call.message.answer(f"<b>1-savol</b>\n\nTo'liq Ism Familiyangizni kiriting.\n<em>Masalan: ( Abdullayev Muminjon )</em> ")
        await modern_job.fio.set()
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)
@dp.message_handler(state=modern_job.fio)
async def get_fullname(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"full_name":msg.text}
    )
    await msg.answer(f"<b>2-savol</b>\n\nYoshingizni kiriting:\n<em>Masalan: ( 19 )</em> :")
    await modern_job.yosh.set()
@dp.message_handler(state=modern_job.yosh, content_types=['text'])
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"age":msg.text}
    )
    await msg.answer(f"<b>3-savol</b>\n\n"
                     f"Mutaxasisligingiz: (siz bilgan dasturlash tili yoki boshqalarni yozing)\n"
                     f"<em>Masalan: ( JavaScript, Python )</em>")
    await modern_job.mutaxasisligi.set()

@dp.message_handler(state=modern_job.yosh, content_types=['photo','video','sticker','file','animation','document','emoji','audio'])
async def get_age(msg: types.Message, state: FSMContext):
    await msg.answer(f"Iltimos yoshingizni faqat raqamlarda kiriting")
    await modern_job.yosh.set()

@dp.message_handler(state=modern_job.mutaxasisligi)
async def get_prof(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"profession":msg.text.capitalize()}
    )
    await msg.answer(f"<b>4-savol</b>\n\n"
                     f"Resume ingiz bo'lsa pdf yoki document ko'rinishida junating aks holda <em>yo\'q</em> deb yozing.")
    await modern_job.resume.set()

@dp.message_handler(state=modern_job.resume, content_types=['document','file'])
async def file_resume(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"file_resume":msg.document.file_id}
    )
    await msg.answer(f"<b>5-savol</b>\n\n"
                     f"Tarjibangiz bo'lsa yozing aks holda <em>yo'q</em> deb yozing:\n"
                     f"<em>Masalan: ( 2-yil )</em>")
    await modern_job.tajriba.set()

@dp.message_handler(state=modern_job.resume, content_types=['text'])
async def text_resume(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"text_resume":msg.text.capitalize()}
    )
    await msg.answer(f"<b>5-savol</b>\n\n"
                     f"Tarjibangiz bo'lsa yozing aks holda <em>yo'q</em> deb yozing:\n"
                     f"<em>Masalan: ( 2-yil )</em>")
    await modern_job.tajriba.set()

@dp.message_handler(state=modern_job.tajriba)
async def tajriba(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"tajriba":msg.text}
    )

    await msg.answer(f"<b>6-savol</b>\n\n"
                     f"Telegram akkaunt yozing: \n<em>Masalan ( @Manager_boshqaruvchi )</em>")
    await modern_job.telegram.set()

@dp.message_handler(state=modern_job.telegram)
async def telegram_username(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"telegram":msg.text}
    )
    await msg.answer(f"<b>7-savol</b>\n\n"
                     f'Telefon raqam yuboring: \n<em>(Telefon raqam yuborish tugmasini</em> bosing)',reply_markup=menu)
    await modern_job.aloqa.set()

@dp.message_handler(state=modern_job.aloqa, content_types=types.ContentType.CONTACT)
async def get_phone(msg: types.Message, state:FSMContext):
    txt = msg.contact.phone_number
    try:
        if txt.find("+")==-1:
            m = f"+{txt}"
            x = re.search("^[\+][998]{3}", m)
            if x:
                await state.update_data(
                    {"phone": m}
                )
                await msg.answer(f"<b>8-savol</b>\n\n"
                                     f'Hududingizni yozing: \n<em>Masalan ( Toshkent )</em>\n',
                                     reply_markup=ReplyKeyboardRemove(True))

                await modern_job.hudud.set()
            else:
                await msg.answer(f"Faqat O'zbekistan davlatiga tegishli raqamni yuboring", reply_markup=menu)
        else:
            x = re.search("^[\+][998]{3}", txt)
            if x:
                await state.update_data(
                    {"phone": txt}
                )
                await msg.answer(f"<b>8-savol</b>\n\n"
                                 f'Hududingizni yozing: \n<em>Masalan ( Toshkent )</em>\n',
                                 reply_markup=ReplyKeyboardRemove(True))
                await modern_job.hudud.set()
            else:
                await msg.answer(f"Faqat O'zbekistan davlatiga tegishli raqamni yuboring", reply_markup=menu)

    except:
        print("uzb nomer emas")



@dp.message_handler(state=modern_job.aloqa, content_types=['text'])
async def get_phone(msg: types.Message, state:FSMContext):
    await msg.answer(f"Iltimos <em>(Telefon raqam yuborish tugmasini</em> bosing)",reply_markup=menu)
    await modern_job.aloqa.set()


@dp.message_handler(state=modern_job.hudud)
async def get_area(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"hudud":msg.text.capitalize()}
    )
    await msg.answer(f"<b>9-savol</b>\n\n"
                     f"Murojaat qilish vaqtini yozing: \n"
                     f"<em>Masalan (8:00-18:00)</em>")
    await modern_job.murojat_vaqti.set()

@dp.message_handler(state=modern_job.murojat_vaqti)
async def contact_us(msg:types.Message, state:FSMContext):
    await state.update_data(
        {"m_vaqt":msg.text}
    )
    await msg.answer(f"<b>10-savol</b>\n\n"
                     f"Maqsadingizni yozing: \n"
                     f"<em>Masalan (Yaxshi jamoa va yaxshi kompaniyada ishlab yaxshi mutaxasis bo'lish)</em>")
    await modern_job.maqsad.set()

@dp.message_handler(state=modern_job.maqsad)
async def maqsad(msg: types.Message, state:FSMContext):
    await state.update_data(
        {"maqsad":msg.text}
    )
    await msg.answer(f"<b>11-savol</b>\n\n"
                     f"Portfolio Link bo'lsa yuboring aks holda <em>yo'q</em> deb yozing:\n"
                     f"<em>Masalan (mahsulot.com)</em>")
    await modern_job.portfolio_link.set()

@dp.message_handler(state=modern_job.portfolio_link)
async def portfolio(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"link":msg.text}
    )
    data = await state.get_data('link')
    try:
        if data['file_resume']:
            full_name = data['full_name']
            age = data['age']
            profession = data['profession']
            resume_file = data['file_resume']
            tajriba = data['tajriba']
            telegram = data['telegram']
            phone = data['phone']
            hudud = data['hudud']
            m_vaqt = data['m_vaqt']
            maqsad = data['maqsad']
            link = data['link']
            post = f"Ma'lumotlaringizni hammasi to'g'rimi ?\n\n"
            post += f"👨‍💼 Hodim: {full_name}\n"
            post += f"🕑 Yosh: {age}\n"
            post += f"📚 Mutaxasisligi: {profession}\n"
            post += f"💼 Tajriba: {tajriba}\n"
            post += f"📧 Telegram: {telegram}\n"
            post += f"📱 Aloqa: {phone}\n"
            post += f"🗺 Hudud: {hudud}\n"
            post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
            post += f"📈 Maqsad: {maqsad}\n"
            post += f"🔗 Portfolio-link: {link}\n"
            await msg.answer_document(document=resume_file,
                                      caption=post,
                                      reply_markup=check_post)
    except:
        if data['text_resume']:
            full_name = data['full_name']
            age = data['age']
            profession = data['profession']
            resume_text = data['text_resume']
            tajriba = data['tajriba']
            telegram = data['telegram']
            phone = data['phone']
            hudud = data['hudud']
            m_vaqt = data['m_vaqt']
            maqsad = data['maqsad']
            link = data['link']
            post = f"Ma'lumotlaringizni hammasi to'g'rimi ?\n\n"
            post += f"👨‍💼 Hodim: {full_name}\n"
            post += f"🕑 Yosh: {age}\n"
            post += f"📚 Mutaxasisligi: {profession}\n"
            post += f"Resume: {resume_text}\n"
            post += f"💼 Tajriba: {tajriba}\n"
            post += f"📧 Telegram: {telegram}\n"
            post += f"📱 Aloqa: {phone}\n"
            post += f"🗺 Hudud: {hudud}\n"
            post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
            post += f"📈 Maqsad: {maqsad}\n"
            post += f"🔗 Portfolio-link: {link}\n"
            await msg.answer(text=post, reply_markup=check_post)
    await modern_job.check.set()


@dp.callback_query_handler(text='xa', state=modern_job.check)
async def checked(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(f"Hurmatli {call.from_user.full_name}, e'loningiz uchun rahmat.\n Sizning e'loningiz 2-bosqichga o'tkazildi, agar muvaffaqiyatli o'tsa 2 - kun ichida <a href='https://t.me/ishkerak_bor'>Ish Kerak | Bor</a> kanaliga joylanadi. Aks holda to'gri tushunasiz. 😊",reply_markup=main)
    data = await state.get_data("tajriba")
    try:
        if data['file_resume']:
            full_name = data['full_name']
            age = data['age']
            profession = data['profession']
            resume_file = data['file_resume']
            tajriba = data['tajriba']
            telegram = data['telegram']
            phone = data['phone']
            hudud = data['hudud']
            m_vaqt = data['m_vaqt']
            maqsad = data['maqsad']
            link = data['link']
            id = [-1001833367838]
            l = await bot.send_document(chat_id=id[0],document=resume_file,caption=full_name)
            resume_link = f"https://t.me/ishborkerakrresume/{l.message_id}"
            myUnique = ""
            try:
                myUnique += str(uuid.uuid4())
                await db.add_post(myUnique)
            except:
                pass
            one = await db.select_one_post(myUnique)
            post = f'Ish joyi kerak: <b>№{one["id"]}</b>\n\n'
            post += f"👨‍💼 Hodim: {full_name}\n"
            post += f"🕑 Yosh: {age}\n"
            post += f"📚 Mutaxasisligi: {profession}\n"
            post += f"🧾 Rezyume: <a href='{resume_link}'>Link</a>\n"
            post += f"💼 Tajriba: {tajriba}\n"
            post += f"📧 Telegram: {telegram}\n"
            post += f"📱 Aloqa: {phone}\n"
            post += f"🗺 Hudud: {hudud}\n"
            post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
            post += f"📈 Maqsad: {maqsad}\n"
            post += f"🔗 Portfolio-link: {link}\n\n"
            post += f"@vakansiya_ishbor_nam — Ish oluvchi va beruvchilarni uchrashtiruvchi  platforma\n\n"
            post += f"#ish_joyi #{hudud.lower()}"
            for i in ADMINS:
                await bot.send_message(chat_id=i,text=post,disable_web_page_preview=True)
            text = f"Sizning navbatingiz – {one['id']}. Kanalni kuzatishda davom eting !\n\n"
            text += f"<b>Kanallar ro'yhati</b>: \n\n"
            text += f"@vakansiya_ishbor_nam – Ish izlaganlar uchun\n"
            text += f"@ishkerak_bor – Xodim izlaganlar uchun\n"
            text += f"@elonpeshtaxta – Muhokama uchun Chat."
            await call.message.answer(text=text,reply_markup=main)
    except:
        if data['text_resume']:
            full_name = data['full_name']
            age = data['age']
            profession = data['profession']
            resume_text = data['text_resume']
            tajriba = data['tajriba']
            telegram = data['telegram']
            phone = data['phone']
            hudud = data['hudud']
            m_vaqt = data['m_vaqt']
            maqsad = data['maqsad']
            link = data['link']
            myUnique1 = ""
            try:
                myUnique1 += str(uuid.uuid4())
                await db.add_post(myUnique1)
            except:
                pass
            one = await db.select_one_post(myUnique1)
            post = f'Ish joyi kerak: <b>№{one["id"]}</b>\n\n'
            post += f"👨‍💼 Hodim: {full_name}\n"
            post += f"🕑 Yosh: {age}\n"
            post += f"📚 Mutaxasisligi: {profession}\n"
            post += f"🧾 Resume: {resume_text}\n"
            post += f"💼 Tajriba: {tajriba}\n"
            post += f"📧 Telegram: {telegram}\n"
            post += f"📱 Aloqa: {phone}\n"
            post += f"🗺 Hudud: {hudud}\n"
            post += f"⏱ Murojaat qilish vaqti: {m_vaqt}\n"
            post += f"📈 Maqsad: {maqsad}\n"
            post += f"🔗 Portfolio-link: {link}\n\n"
            post += f"@vakansiya_ishbor_nam — Ish oluvchi va beruvchilarni uchrashtiruvchi  platforma\n\n"
            post += f"#ish_joyi #{hudud.lower()}"
            for i in ADMINS:
                await bot.send_message(chat_id=i,text=post)
            text = f"Sizning navbatingiz – {one['id']}. Kanalni kuzatishda davom eting !\n\n"
            text += f"<b>Kanallar ro'yhati</b>: \n\n"
            text += f"@vakansiya_ishbor_nam – Ish izlaganlar uchun\n"
            text += f"@ishkerak_bor – Xodim izlaganlar uchun\n"
            text += f"@elonpeshtaxta – Muhokama uchun Chat."
            await call.message.answer(text=text,reply_markup=main)
    await state.finish()

@dp.callback_query_handler(text='yoq', state=modern_job.check)
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
        await call.message.answer(f"Assalomu alaykum, {call.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",reply_markup=choose_job)
    else:
        btn = await show_channels()
        context = "Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
        await call.message.answer(context, reply_markup=btn)