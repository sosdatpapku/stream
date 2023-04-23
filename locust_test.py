from locust import HttpUser, task, between


# Класс AppUser имитирует выполнение HTTP-запросов на указанной странице используя импортированный класс HttpUser
class AppUser(HttpUser):
    wait_time = between(5, 10) # интервал выполнения HTTP-запросов на странице (в секундах)

    @task # В task описываются действия при каждом HTTP-запросе
    def get_page(self): # Функция внешнего запроса страницы
        self.client.get('/')


"""
Алгоритм воспроизведения теста
1) Запускаем наше приложение на облаке streamlit через команду
streamlit run library_func.py
2) Запускаем веб-интерфейс locust для нашего теста через команду
locust -f locust_test.py
3) Переходим по ссылке http://localhost:8089
4) В интерфейсе указываем адрес страницы веб приложения, которое требуется протестировать
"""
