import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud
import vk  # импорт специализированной библиотеки для парсинга текста

matplotlib.use("Agg")


def remove_incor_symbols(text_incor):
    # функция, оставляющая в строке только русские буквы и пробелы

    text_incor = text_incor.lower()

    cor_symbols = [" "]

    for i in range(ord('а'), ord('я')):
        cor_symbols.append(chr(i))

    text_cor = ""

    for symbol in text_incor:
        if symbol in cor_symbols:
            text_cor += symbol

    return(text_cor)


def text_analizator_rus(text_in):
    '''функция выполняет анализ текста и
    возвращает датафрейм с его характеристиками'''

    text = remove_incor_symbols(text_in)

    nlp_rus = spacy.load('ru_core_news_md')  # модель для русского языка
    analysis_result = nlp_rus(text)

    c_tokens = [token.text for token in analysis_result]
    c_lemma = [token.lemma_ for token in analysis_result]
    c_pos = [token.pos_ for token in analysis_result]
    c_dep = [token.dep_ for token in analysis_result]
    c_ent = [token.ent_type_ for token in analysis_result]

    df_columns = ['Токены', 'Лемма', 'Часть речи', 'Зависимость', 'Сущность']
    df_data = zip(c_tokens, c_lemma, c_pos, c_dep, c_ent)
    df_analys_res = pd.DataFrame(data=df_data, columns=df_columns)

    return df_analys_res


def make_word_cloud(text):
    # функция выводит "облако слов"

    wordcloud = WordCloud(colormap='Set2').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # чтобы убрать предупреждение
    st.pyplot()

    return None


def text_analizer_rus_st(text_in, part_of_speach=["NOUN", "VERB"]):
    '''функция выполняет анализ текста и выводит результат с использованием
библиотеки streamlit'''

    res_of_analys = text_analizator_rus(text_in)

    words = res_of_analys.loc[res_of_analys['Часть речи']
                              .isin(part_of_speach), 'Токены'].tolist()
    string_for_cloud = ' '.join(words)
    make_word_cloud(string_for_cloud)

    st.dataframe(res_of_analys['Часть речи'].value_counts().T)
    st.dataframe(res_of_analys)

    return None


def main():
    """"""
# st.title('!!! Добро пожаловать !!!')

    st.markdown("""
    <h1 style='text-align: center;'>
    !!! Добро пожаловать !!!</h1>""",
                unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h1 style="color:white;text-align:center;">
    Анализ текста с помощью библиотеки spaCy </h1>
    </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)

    st.info("Обработка естественного языка (на русском языке)")
    raw_text = st.text_area("Введите текст на русском языке", "поле ввода")
    if st.button("Проанализировать"):
        try:
            text_analizer_rus_st(raw_text)
        except:
            st.markdown('Введённые данные некорректны')

    st.info("Обработка естественного языка (VK)")
    token = st.text_input(
        'Установите Ваш токен из Вашего приложения в vk (данное действие может быть небезопасно)', 'Например 2b83a7172b63a7656ghb7178428708a0522b632b63a7873f7c594b6fda2224149cvd0e'
        )
    count = st.slider('Сколько новостных заголовков извлечь?', 1, 100, 5)
    domain = st.text_input(
        'Введите короткий адрес пользователя или сообщества', 'habr'
        )

    if st.button("Проанализировать новостные заголовки"):

        try:
            api = vk.API(access_token=token)  # адрес токена вк
            posts = api.wall.get(domain=domain, count=count, v=5.151)
            # -15755094, 20629724

            all_news = []  # список для добавления всех заголовков новостями
            for post in posts['items']:
                all_news.append(post['text'])  # добавляю все заголовки в один

            text_analizer_rus_st(str(all_news))
            # подаём на функцию данные одновременно переводя их в тип str

        except:
            st.markdown('Что-то пошло не так')

    st.sidebar.subheader('''Исполнители: группа №2:
    Зайцев Александр Васильевич
    Чурилов Алексей Александрович
    Зайцев Антон Александрович
    Гаврилин Пётр Александрович''')

    return None


if __name__ == '__main__':
    main()