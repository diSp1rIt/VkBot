from config import *
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 194113667)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            name = vk.users.get(user_ids=[event.obj.message["from_id"]])[0]['first_name']
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f'Привет, {name}!',
                             random_id=random.randint(0, 2 ** 64))
            if 'id' in event.obj.message.keys():
                city = vk.users.get(user_ids=[event.obj.message['from_id']], fields="city")[0]['city']['title']
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'Как поживает {city}?',
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
