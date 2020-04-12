import vk_api
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
    response = vk.friends.get(fields='bdate')
    if response['items']:
        for i in sorted(response['items'], key=lambda x: x['last_name']):
            print(i['last_name'], end=' ')
            print(i['first_name'], end='')
            if 'bdate' in i.keys():
                print(f' {i["bdate"]}')
            else:
                print()


if __name__ == '__main__':
    main()
