from locust import HttpUser, task, between

# Locust используется для тестирования производительности работы web-приложения на облаке Streamlit
class AppUser(HttpUser):
    wait_time = between(5,10)
    
    @task
    def home_page(self):
        self.client.get('/')
"""
Locust используется для тестирования производительности работы 
web-приложения на облаке Streamlit.
Имитируем параллельное использование 
приложения несколькими пользователями


USAGE

streamlit run app_tsch.py 
locust -f locust_test.py
And go to the link http://localhost:8089
"""