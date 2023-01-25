import streamlit as st 
import joblib,os
import spacy
import pandas as pd
nlp = spacy.load('en_core_web_lg')
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# load Vectorizer For Gender Prediction
news_vectorizer = open("models/final_news_cv_vectorizer.pkl","rb")
news_cv = joblib.load(news_vectorizer)

# # load Model For Gender Prediction
# news_nv_model = open("models/naivebayesgendermodel.pkl","rb")
# news_clf = joblib.load(news_nv_model)

def load_prediction_models(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model



# Get the Keys
def get_key(val,my_dict):
	for key,value in my_dict.items():
		if val == value:
			return key



def main():
	"""Классификация новостей"""
	st.title("Классификация новостей")
	# st.subheader("ML App with Streamlit")
	html_temp = """
	<div style="background-color:blue;padding:10px">
	<h1 style="color:white;text-align:center;">Первичный анализ новостей с помощью бибилотеки spaCy </h1>
	</div>

	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	activity = ['Прогноз','NLP(обработка естественного языка)']
	choice = st.sidebar.selectbox("Выберите операцию",activity)


	if choice == 'Прогноз':
		st.info("Предсказание типа новостей")

		news_text = st.text_area("Введите текст на английском языке","поле ввода")
		all_ml_models = ["LR","RFOREST","NB","DECISION_TREE"]
		model_choice = st.selectbox("Выберите модель",all_ml_models)

		prediction_labels = {'предпринимательство': 0,'технологии': 1,'спорт': 2,'здоровье': 3,'политика': 4,'развлечения': 5}
		if st.button("Классификация новостей"):
			st.text("Исходный текст::\n{}".format(news_text))
			vect_text = news_cv.transform([news_text]).toarray()
			if model_choice == 'LR':
				predictor = load_prediction_models("models/newsclassifier_Logit_model.pkl")
				prediction = predictor.predict(vect_text)
				# st.write(prediction)
			elif model_choice == 'RFOREST':
				predictor = load_prediction_models("models/newsclassifier_RFOREST_model.pkl")
				prediction = predictor.predict(vect_text)
				# st.write(prediction)
			elif model_choice == 'NB':
				predictor = load_prediction_models("models/newsclassifier_NB_model.pkl")
				prediction = predictor.predict(vect_text)
				# st.write(prediction)
			elif model_choice == 'DECISION_TREE':
				predictor = load_prediction_models("models/newsclassifier_CART_model.pkl")
				prediction = predictor.predict(vect_text)
				# st.write(prediction)

			final_result = get_key(prediction,prediction_labels)
			st.success("Новости отнесены к категории:: {}".format(final_result))

	if choice == 'NLP':
		st.info("Обработка естественного языка (новости)")
		raw_text = st.text_area("Введите текст на английском языке","поле ввода")
		nlp_task = ["Токенизация","Лемматизация","NER","Теги частей речи"]
		task_choice = st.selectbox("Choose NLP Task",nlp_task)
		if st.button("Проанализировать"):
			st.info("Исходные данные::\n{}".format(raw_text))

			docx = nlp(raw_text)
			if task_choice == 'Токенизация':
				result = [token.text for token in docx ]
			elif task_choice == 'Лемматизация':
				result = ["'Token':{},'Lemma':{}".format(token.text,token.lemma_) for token in docx]
			elif task_choice == 'NER':
				result = [(entity.text,entity.label_)for entity in docx.ents]
			elif task_choice == 'Теги частей речи':
				result = ["'Токен':{},'Часть речи':{},'Зависимость':{}".format(word.text,word.tag_,word.dep_) for word in docx]

			st.json(result)

		if st.button("Таблица"):
			docx = nlp(raw_text)
			c_tokens = [token.text for token in docx ]
			c_lemma = [token.lemma_ for token in docx ]
			c_pos = [token.pos_ for token in docx ]

			new_df = pd.DataFrame(zip(c_tokens,c_lemma,c_pos),columns=['Токены','Лемма','Часть речи'])
			st.dataframe(new_df)


		if st.checkbox("Облако слов"):
			c_text = raw_text
			wordcloud = WordCloud().generate(c_text)
			plt.imshow(wordcloud,interpolation='bilinear')
			plt.axis("off")
			st.pyplot()









	st.sidebar.subheader('''Исполнители: 
	Зайцев Александр Васильевич
	Чурилов Алексей Александрович
	Зайцев Антон Александрович''')




if __name__ == '__main__':
	main()

# By Jesse E.Agbe(JCharis)
# Jesus Saves@JCharisTech