import library_func  # импорт скрипта library_func.py


def main():

    try:
        api_for = 'vk.API(access_token=token)'  # адрес токена вк
    except BaseException:
        api_for = None

    library_func.main_for_all(api_for)

    return None


if __name__ == '__main__':
    main()
