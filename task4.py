import asyncio
from telethon import TelegramClient, errors

# Запит у користувача API ID, API Hash, токен бота та ID групи в командному
api_id = int(input("Введіть ваш API ID: "))
api_hash = input("Введіть ваш API Hash: ")
bot_token = input("Введіть токен вашого бота: ")
chat_id = input("Введіть ID чату/користувача для відправки повідомлення: ")
message_to_send = 'Сообщение отправилось в чат.'  # Повідомлення, яке надсилається

async def get_participants(client, chat_id):
    try:
        participants = await client.get_participants(chat_id)
        if participants:
            print("Список учасників:")
            for index, user in enumerate(participants, start=1):
                print(f"{index}. {user.first_name} - {user.id}")
        else:
            print("У групі немає учасників або не вдалося отримати список учасників.")
    except errors.ChatAdminRequiredError:
        print("Потрібні права адміністратора для отримання учасників цього чату.")
    except Exception as e:
        print(f"Помилка при отриманні учасників: {e}")

async def send_message(client, chat_id, message):
    try:
        result = await client.send_message(chat_id, message)
        print(f"Повідомлення надіслано до чату з ID {chat_id}: {result.message}")
    except errors.PeerIdInvalidError:
        print("Невірний ID чату або користувача.")
    except Exception as e:
        print(f"Помилка при відправці повідомлення: {e}")

async def main():
    async with TelegramClient('my_bot', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)

        # Отримання списку учасників
        await get_participants(client, chat_id)

        # Відправка повідомлення
        await send_message(client, chat_id, message_to_send)

# Запуск асинхронної функції
asyncio.run(main())