import streamlit as st
import joblib
import os
import numpy as np
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

nlp = spacy.load('en_core_web_lg')  # модель для английского языка


def main():
    """Классификация новостей"""
    st.title("Классификация новостей")
    # st.subheader("ML App with Streamlit")
    html_temp = """
	<div style="background-color:blue;padding:10px">
	<h1 style="color:white;text-align:center;">Первичный анализ новостей с помощью библиотеки spaCy </h1>
	</div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)

    st.info("Обработка естественного языка (новости)")
    raw_text = st.text_area("Введите текст на английском языке", "поле ввода")
    nlp_task = ["NOUN", "VERB", "NOUN+VERB"]
    task_choice = st.selectbox("Choose NLP Task", nlp_task)
    if st.button("Проанализировать"):
        st.info("Исходные данные::\n{}".format(raw_text))

        docx = nlp(raw_text)

        listNoun = []
        listVerb = []
        listFin = []
        if task_choice == 'NOUN':
            listNoun = [token.lemma_ for token in docx if token.pos_ == "NOUN"]
        elif task_choice == 'VERB':
            listVerb = [token.lemma_ for token in docx if token.pos_ == "VERB"]
        elif task_choice == 'NOUN+VERB':
            listNoun = [token.lemma_ for token in docx if token.pos_ == "NOUN"]
            listVerb = [token.lemma_ for token in docx if token.pos_ == "VERB"]

        listFin = listNoun + listVerb
        c_text = ' '.join(listFin)



        stopw = ['russian', 'the']  # стоп-слова
        wordcloud = WordCloud(colormap='Set2', stopwords=stopw).generate(c_text)
        # mask=image #опция для WordCloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.set_option('deprecation.showPyplotGlobalUse', False)  # чтобы убрать предупреждение
        st.pyplot()

st.sidebar.subheader('''Исполнители: группа №12: 
        Зайцев Александр Васильевич
        Чурилов Алексей Александрович
        Зайцев Антон Александрович''')

if __name__ == '__main__':
    main()

#        if st.checkbox("Облако слов"):
#        original_image = Image.open('pic.png', 'r')
#        image = original_image.resize([2000, 2000], Image.ANTIALIAS)
#        image = np.array(image)
