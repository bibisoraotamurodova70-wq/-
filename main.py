import asyncio
import random
from aiogram import Bot, Dispatcher

# --- SOZLAMALAR ---
# Siz bergan bot tokeni joylashtirildi
BOT_TOKEN = "8629414647:AAHDwvOBAWAIGFIbJJpJIqn9Wgw1Tfczq1Q"

# Telegram guruh havolasidan olingan guruh ID raqami
# Eslatma: Bot guruhda ADMIN bo'lishi shart!
GROUP_CHAT_ID = -1002340538604  

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- TESTLAR BAZASI ---
# Bu yerga o'zingiz xohlagancha yangi testlarni xuddi shu formatda qo'shib ketaverasiz
TESTLAR_BAZASI = [
    {
        "savol": "🇬🇧 Sanctionable — so'zining tarjimasini toping:",
        "variantlar": ["deraza", "yaxshi", "ruxsat etilgan", "kocha"],
        "togri_indeks": 2  # "ruxsat etilgan" indeksi 2 da turibdi (0, 1, 2, 3)
    },
    {
        "savol": "🇬🇧 Book — so'zining tarjimasini toping:",
        "variantlar": ["Kitob", "Ruchka", "Parta", "O'qituvchi"],
        "togri_indeks": 0  # "Kitob" indeksi 0 da
    },
    {
        "savol": "🇬🇧 Computer — so'zining tarjimasini toping:",
        "variantlar": ["Telefon", "Kompyuter", "Televizor", "Sichqoncha"],
        "togri_indeks": 1  # "Kompyuter" indeksi 1 da
    }
]

# --- AVTOMATIK TEST TASHLOVCHI FUNKSIYA ---
async def avto_test_yuboruvchi():
    while True:
        try:
            # Bazadan bitta tasodifiy testni tanlab olamiz
            test = random.choice(TESTLAR_BAZASI)
            
            # Guruhga Telegram Quiz (Viktorina) shaklida yuborish
            await bot.send_poll(
                chat_id=GROUP_CHAT_ID,
                question=test["savol"],
                options=test["variantlar"],
                type="quiz",
                correct_option_id=test["togri_indeks"],
                is_anonymous=False  # Kim qaysi variantni tanlaganini ko'rish uchun
            )
            print("Test guruhga muvaffaqiyatli yuborildi!")
            
            # 1. Test guruhda 1 daqiqa (60 soniya) turadi
            await asyncio.sleep(60) 
            
            # 2. Keyin guruhga hech narsa tashlamasdan 15 daqiqa (15 * 60 soniya) dam oladi
            print("Bot 15 daqiqalik dam olish rejimiga o'tdi...")
            await asyncio.sleep(15 * 60)
            
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            await asyncio.sleep(10)  # Agar xatolik bo'lsa, 10 soniya kutib qayta urunadi

# --- BOTNI ISHGA TUSHIRISH ---
async def main():
    # Bot yoqilishi bilan avtomatik test tashlash siklini orqa fonda ishga tushiramiz
    asyncio.create_task(avto_test_yuboruvchi())
    
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
