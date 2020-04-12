import vk_api
from time import strftime, ctime, strptime
from config import *


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(fields='date, text', count=100)
    if response['items']:
        for i in response['items']:
            print('{' + i['text'] + '};')
            print(strftime('date: {%Y-%m-%d}, time: {%X}', strptime(ctime(i['date']))))
            print()


if __name__ == '__main__':
    main()
