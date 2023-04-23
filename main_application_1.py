import lite_ap # импорт скрипта lite_ap.py

def main():
    
    try:
        api_for = 'vk.API(access_token=token)'  # адрес токена вк
    except:  
        api_for = None

    lite_ap.main_for_all(api_for)
    
    return None

if __name__ == '__main__':
    main()