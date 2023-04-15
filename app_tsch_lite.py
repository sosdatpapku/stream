import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud


matplotlib.use("Agg")


# функция выполняет анализ текста и возвращает датафрейм с его характеристиками
def text_analizator_rus(text):

    nlp_rus = spacy.load('ru_core_news_lg')  # модель для русского языка
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

    wordcloud = WordCloud(colormap='Set2').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # чтобы убрать предупреждение
    st.pyplot()

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

        res_of_analys = text_analizator_rus(raw_text)

        words = res_of_analys.loc[res_of_analys['Часть речи']
                                  .isin(["NOUN", "VERB"]), 'Токены'].tolist()
        string_for_cloud = ' '.join(words)
        make_word_cloud(string_for_cloud)

        st.dataframe(res_of_analys['Часть речи'].value_counts().T)
        st.dataframe(res_of_analys)

        st.sidebar.subheader('''Исполнители: группа №2:
    Зайцев Александр Васильевич
    Чурилов Алексей Александрович
    Зайцев Антон Александрович
    Гаврилин Пётр Александрович''')

    return None


if __name__ == '__main__':
    main()
