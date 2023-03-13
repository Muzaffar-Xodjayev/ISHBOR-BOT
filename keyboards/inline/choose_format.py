from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

choose_job = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ish Kerak', callback_data="ish_kerak"),
            InlineKeyboardButton(text='Hodim Kerak', callback_data="hodim_kerak")
        ]
    ]
)

choose_how = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Zamonaviy Kasb ( IT )', callback_data="zamonaviy_kasb"),
            InlineKeyboardButton(text='Boshqa Ish', callback_data="boshqa_ish")
        ]
    ]
)

check_post = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xa', callback_data="xa"),
            InlineKeyboardButton(text="Yo'q", callback_data="yoq")
        ]
    ]
)

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏠 Bosh Sahifa', callback_data="bosh_sahifa"),
        ]
    ]
)

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Bekor qilish',callback_data="bekor_qilish")
        ]
    ]
)