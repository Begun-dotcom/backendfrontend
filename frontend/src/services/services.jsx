import React from 'react'
import axios from 'axios';


export const Services = {
    async send_content(phone, description) {
        try {
            const response = await axios.post(`/api/telegram`, {
                phone: phone,
                description: description
            });

            if (response.status === 200 && response.data.ok) {
                console.log("✅ Успешное отправление");

                if (response.data.telegram_sent) {
                    console.log('✅ Уведомление в Telegram');
                }
                if (response.data.email_sent) {
                    console.log('✅ Письмо отправлено');
                }
                if (response.data.send_db) {
                    console.log('✅ Запись добавлена в БД');
                }
                if (!response.data.telegram_sent && !response.data.email_sent) {
                    console.warn('⚠️ Ни один канал не сработал');
                }

                return response.data;
            }

        } catch (error) {
            if (error.response?.status === 500) {
                console.error('❌ Ошибка сервера:', error.response?.data?.detail);
            } else {
                console.error('❌ Ошибка отправки:', error.message);
            }
            throw error;
        }
    }
}