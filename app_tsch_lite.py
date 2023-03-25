import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud

matplotlib.use("Agg")

nlp_rus = spacy.load('ru_core_news_lg')  # модель для русского язык


def main():
    """"""
    #st.title('!!! Добро пожаловать !!!')

    st.markdown("<h1 style='text-align: center;'>!!! Добро пожаловать !!!</h1>", unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h1 style="color:white;text-align:center;">Анализ текста с помощью библиотеки spaCy </h1>
    </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)

    st.info("Обработка естественного языка (на русском языке)")
    raw_text = st.text_area("Введите текст на русском языке", "поле ввода")
    if st.button("Проанализировать"):
        docx = nlp_rus(raw_text)
        c_tokens = [token.text for token in docx]
        c_lemma = [token.lemma_ for token in docx]
        c_pos = [token.pos_ for token in docx]
        c_dep = [token.dep_ for token in docx]
        c_ent = [token.ent_type_ for token in docx]

        new_df = pd.DataFrame(zip(c_tokens, c_lemma, c_pos, c_dep, c_ent),
                              columns=['Токены', 'Лемма', 'Часть речи', 'Зависимость', 'Сущность'])
#------------------------------------------------
        listNoun = []
        listVerb = []
        listFin = []
        listNoun = [token.lemma_ for token in docx if token.pos_ == "NOUN"]
        listVerb = [token.lemma_ for token in docx if token.pos_ == "VERB"]
        listFin = listNoun + listVerb

        c_text = ' '.join(listFin)
        wordcloud = WordCloud(colormap='Set2').generate(c_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.set_option('deprecation.showPyplotGlobalUse', False)  # чтобы убрать предупреждение
        st.pyplot()

        count_df = pd.DataFrame(c_pos, columns=['Количество элементов'])
        xxxx = pd.DataFrame(count_df['Количество элементов'].value_counts()).T
        st.dataframe(xxxx)
        st.dataframe(new_df)

    st.sidebar.subheader('''Исполнители: группа №12: 
    Зайцев Александр Васильевич
    Чурилов Алексей Александрович
    Зайцев Антон Александрович''')


if __name__ == '__main__':
    main()
