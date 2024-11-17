import asyncio
from telethon.sync import TelegramClient

#просимо користувача ввести всі необхідні дані
api_id = int(input('Enter your API ID: '))
api_hash = input('Enter your API Hash: ')
chat_id = input('Enter Chat ID: ')
message = input('Enter the message you want to send: ')


async def main(chat_id, message):
    #створюємо сесію, тут у користувача попросять авторизуватися
    async with TelegramClient('first', api_id, api_hash) as client:
        #отримуємо учасників чату, якщо вони є
        participants = await client.get_participants(chat_id)
        if participants:
            print(f"{len(participants)} participants found in the chat:")
            for idx, participant in enumerate(participants, start=1):
                print(f"{idx}. First name: {participant.first_name or 'N/A'}, ID: {participant.id}")
        else:
            print("There are no members in the chat or an error occurred while receiving them.")
        #відправляємо повідомлення
        await client.send_message(chat_id, message)
#запускаємо функцію
asyncio.run(main(chat_id, message))
