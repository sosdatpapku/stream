
<img src="https://user-images.githubusercontent.com/104712265/214668687-3699e2f3-9a11-4996-9cef-10f622956ad2.svg" alt="python" style="width: 40px; height: 40px;">      <img src="https://user-images.githubusercontent.com/104712265/214669069-ab16be66-b989-4dc6-9a64-12594563e051.svg" alt="spacy" style="width: 40px; height: 40px;">      <img src="https://user-images.githubusercontent.com/104712265/214669302-2879d187-b953-4413-90ec-b838af9ef6bc.svg" alt="streamlit" style="width: 40px; height: 40px;">  

**Команда №2**  
- Чурилов Алексей Александрович  
- Зайцев Александр Васильевич  
- Зайцев Антон Александрович
- Гаврилин Пётр Александрович

**Документация**  

[1. Развёртывания приложения](https://github.com/m6129/stream/blob/anton_2/docs/1.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D1%82%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.md)  
[2. Как получить токен приложения во Вконтакте.md](https://github.com/m6129/stream/blob/anton_2/docs/2.%20%D0%9A%D0%B0%D0%BA%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%20%20%D0%B2%D0%BE%20%D0%92%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5.md)  
[3.Использование приложения.md](https://github.com/m6129/stream/blob/anton_2/docs/3.%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.md)  
[4. Проведение нагрузочного тестирования посредством библиотеки Locust.md](https://github.com/m6129/stream/blob/anton_2/docs/4.%20%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BE%D1%87%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%BE%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%BE%D0%BC%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8%20Locust.md)  
Не работатет  

![visitor badge](https://visitor-badge.glitch.me/badge?page_id=m6129&left_color=red&right_color=green)  

![](https://visitor-badge.glitch.me/badge?page_id=m6129)










Удаляем, то что ниже???

Программа будет полезна при анализе текстов разного объема и содержания, т.к. включает в себя несколько функций:

1) Генерация облака слов

2) Подсчет частей речи в заданном тексте

3) Токенизация, лемматизация, выявление зависимостей при синтаксическом разборе предложения и выявление именованных сущностей

Данная модель использует самую большую модель (lg) spaCy на [английском](https://spacy.io/models/en) и [русском](https://spacy.io/models/ru) языках  

Нами реализовано 2 варианта программы:
Усеченная версия (app_tsch_lite.py), работающая только с текстом на русском языке развернута на облаке [streamlit](https://stream.streamlit.app/).
Полная версия (app_tsch_hard.py) работает с текстом на русском и английском языках, развернута на [Яндекс.Облако](http://158.160.13.46:8501/).

При проверке работы программы использовалась библиоткека [locust](https://locust.io) для нагрузочного тестирования.

Изменения из форка stream_petr
