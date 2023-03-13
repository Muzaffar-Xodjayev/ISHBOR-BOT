from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin = InlineKeyboardMarkup(row_width=2)
btn = InlineKeyboardButton("💼 Ish kerak", callback_data="ish_statistika")
btn1 = InlineKeyboardButton("👤 Xodim Kerak",callback_data="xodim_statistika")
btn2 = InlineKeyboardButton("🧮 Umumiy",callback_data="umumiy_statistika")
admin.add(btn,btn1,btn2)