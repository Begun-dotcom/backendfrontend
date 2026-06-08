from typing import List

from fastapi import APIRouter, HTTPException


from src.api.schemas import PhoneRequest, OrderList
from src.api.utils import send_telegram, send_email
from src.core.database import SessionDep
from src.dao.dao import OrderDao

admin_router = APIRouter(prefix="/api", tags=["Telegram"])


@admin_router.post("/telegram")
async def post_telegram(request: PhoneRequest, session : SessionDep):
    try:
        telegram_status = await send_telegram(request)
        email_status = await send_email(request)
        send_db = await OrderDao(session = session).add(OrderList(phone = request.phone, description=request.description))

        if not telegram_status and not email_status:
            raise HTTPException(status_code=500, detail="Не удалось отправить заявку")

        return {
            "ok": True,
            "telegram_sent": telegram_status,
            "email_sent": email_status,
            "send_db" : send_db
        }

    except Exception as e:
        print(f"Ошибка: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@admin_router.get("/order", response_model=List[OrderList])
async def get_order(session : SessionDep):
    try:
       get_orders = await OrderDao(session = session).get_others()
       return get_orders

    except Exception as e:
        print(f"Ошибка: {e}")
        raise HTTPException(status_code=500, detail=str(e))