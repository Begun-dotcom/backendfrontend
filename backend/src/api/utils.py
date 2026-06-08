import asyncio
from email.message import EmailMessage

import aiohttp
import smtplib

from src.config import setting


async def send_telegram(request):
    try:
        message = f"📞 Новая заявка!\nТелефон: {request.phone}\nОписание: {request.description}"

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    setting.VERCEL_PROXY_URL,
                    json={
                        "chat_id": setting.CHAT_ID,
                        "text": message,
                        "parse_mode": "HTML"
                    }
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    print(f"Прокси ошибка: {response.status} - {error_text}")
                    return False  # ← просто возвращаем False

        return True  # ← успех

    except Exception as e:
        print(f"Ошибка: {e}")
        return False  # ← возвращаем False, а не raise


async def send_email(request):
    try:
        message = f"📞 Новая заявка!\nТелефон: {request.phone}\nОписание: {request.description}"

        # Настройки SMTP для Yandex
        SMTP_HOST = "smtp.yandex.ru"
        SMTP_PORT = 465
        SMTP_USER = "DmitrySorokin88"
        SMTP_PASSWORD = "bhvaoitsslyehmlz"
        TO_EMAIL = "DmitrySorokin88@yandex.ru"

        # Создаём письмо
        msg = EmailMessage()
        msg["Subject"] = "Новая заявка с сайта"
        msg["From"] = f"{SMTP_USER}@yandex.ru"
        msg["To"] = TO_EMAIL

        msg.set_content(message)
        # Отправка
        def _send():
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)

        await asyncio.to_thread(_send)
        return True

    except Exception as e:
        print(f"Ошибка: {e}")
        return False