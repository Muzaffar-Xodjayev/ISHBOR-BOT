from aiogram import types
from aiogram.types import CallbackQuery,ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.simple_job import simple
from states.modern_job import modern_job
from states.need_worker import worker
from keyboards.inline.choose_format import *
from keyboards.default.contact import menu,otmen
from loader import bot,dp,db

# start simple_job
try:
    @dp.message_handler(commands=['start', 'admin'], state=simple.fio)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.yosh)
    async def with_state1(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.kasbi)
    async def with_state2(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.tajriba)
    async def with_state3(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.telegram)
    async def with_state4(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.aloqa)
    async def with_state5(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.murojat_vaqti)
    async def with_state6(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.maqsad)
    async def with_state7(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=simple.hudud)
    async def with_state7(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.fio)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.yosh)
    async def with_state1(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.kasbi)
    async def with_state2(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.tajriba)
    async def with_state3(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.telegram)
    async def with_state4(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.aloqa)
    async def with_state5(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.murojat_vaqti)
    async def with_state6(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.maqsad)
    async def with_state7(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"
        await message.poll
        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    @dp.message_handler(commands=['help'], state=simple.hudud)
    async def with_state7(message: types.Message, state: FSMContext):
        await message.answer(f"🆘 Yordam Bo'limi", reply_markup=ReplyKeyboardRemove(True))
        msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
              f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
              f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
              f"<b>Botni ishlash tartibi batafsil videoda tushuntirilgan 👇</b>\n\n"

        await message.reply(msg)
        await message.answer_video("https://t.me/NAMANGANLIKLAR_UZ/82399")
        await state.finish()


    # @dp.callback_query_handler(text="cc", state=simple.fio)
    # async def intro(call: CallbackQuery, state: FSMContext):
    #     await call.message.delete()
    #     await call.message.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await call.message.answer(
    #         f"Assalomu alaykum, {call.message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.callback_query_handler(text="cc", state=simple.yosh)
    # async def intro1(call: CallbackQuery, state: FSMContext):
    #     await call.message.delete()
    #     await call.message.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await call.message.answer(
    #         f"Assalomu alaykum, {call.message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.kasbi)
    # async def intro2(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.tajriba)
    # async def intro3(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.telegram)
    # async def intro4(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.aloqa)
    # async def intro5(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.murojat_vaqti)
    # async def intro6(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.maqsad)
    # async def intro7(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
    #
    #
    # @dp.message_handler(text="cc", state=simple.hudud)
    # async def intro8(msg: types.Message, state: FSMContext):
    #     await msg.answer("Bekor Qilindi.", reply_markup=ReplyKeyboardRemove(True))
    #     await state.finish()
    #     await msg.answer(
    #         f"Assalomu alaykum, {msg.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
    #         reply_markup=choose_job)
except:
    pass
# end simple_job


try:
    @dp.message_handler(commands=['start', 'admin'], state=modern_job.fio)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.yosh)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.mutaxasisligi)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()

    @dp.message_handler(commands=['start', 'admin'], state=modern_job.resume)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.tajriba)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.telegram)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.aloqa)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.hudud)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.murojat_vaqti)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.maqsad)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


    @dp.message_handler(commands=['start', 'admin'], state=modern_job.portfolio_link)
    async def with_state(message: types.Message, state: FSMContext):
        await message.answer(f"🏚 Bosh Sahifa", reply_markup=ReplyKeyboardRemove(True))
        await message.answer(
            f"Assalomu alaykum, {message.from_user.full_name}!\n<b>Ishbor | Kerak Bot</b>iga xush kelibsiz!",
            reply_markup=choose_job)
        await state.finish()


except:
    pass