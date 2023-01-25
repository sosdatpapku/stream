import streamlit as st
import joblib
import os
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
    nlp_task = ["Токенизация", "Лемматизация", "NER", "Теги частей речи"]
    task_choice = st.selectbox("Choose NLP Task", nlp_task)
    if st.button("Проанализировать"):
        st.info("Исходные данные::\n{}".format(raw_text))

        docx = nlp(raw_text)
        if task_choice == 'Токенизация':
            result = [token.text for token in docx]
        elif task_choice == 'Лемматизация':
            result = ["'Token':{},'Lemma':{}".format(token.text, token.lemma_) for token in docx]
        elif task_choice == 'NER':
            result = [(entity.text, entity.label_) for entity in docx.ents]
        elif task_choice == 'Теги частей речи':
            result = ["'Токен':{},'Часть речи':{},'Зависимость':{}".format(word.text, word.tag_, word.dep_) for word in
                      docx]

        st.json(result)

    if st.button("Таблица"):
        docx = nlp(raw_text)
        c_tokens = [token.text for token in docx]
        c_lemma = [token.lemma_ for token in docx]
        c_pos = [token.pos_ for token in docx]

        new_df = pd.DataFrame(zip(c_tokens, c_lemma, c_pos), columns=['Токены', 'Лемма', 'Часть речи'])
        st.dataframe(new_df)

    if st.checkbox("Облако слов"):
        c_text = raw_text
        wordcloud = WordCloud().generate(c_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.set_option('deprecation.showPyplotGlobalUse', False) #чтобы убрать предупреждение
        st.pyplot()

    st.sidebar.subheader('''Исполнители: группа №12: 
	Зайцев Александр Васильевич
	Чурилов Алексей Александрович
	Зайцев Антон Александрович''')


if __name__ == '__main__':
    main()
