import datas
from api import LoginApi
import allure


class TestLogin:

    @allure.title('Логин под существующим пользователем')
    @allure.description('Cоздание пользователя, авторизация, проверка статуса ответа и тела ответа')
    def test_login_default_user_success(self, default_user_create_user):
        data = default_user_create_user
        response = LoginApi.login_user(data[1], data[0])
        assert response.status_code == 200 and datas.SUCCESS_TRUE, 'accessToken' in response.text

    @allure.title('Логин под существующим пользователем')
    @allure.description('Cоздание пользователя, авторизация с некоректным email, проверка статуса ответа и тела ответа')
    def test_login_with_wrong_email_fail(self, default_user_create_user):
        data = default_user_create_user[1]
        data['email'] = datas.any_mail
        response = LoginApi.login_user(data, default_user_create_user[0])
        assert response.status_code == 401 and response.text == datas.ERROR_EMAIL_OR_PASSWORD_INCORRECT

    @allure.title('Логин под существующим пользователем')
    @allure.description('Cоздание пользователя, авторизация с некоректным password, проверка статуса ответа и тела ответа')
    def test_login_with_wrong_password_fail(self, default_user_create_user):
        data = default_user_create_user[1]
        data['password'] = datas.any_pass
        response = LoginApi.login_user(data, default_user_create_user[0])
        assert response.status_code == 401 and response.text == datas.ERROR_EMAIL_OR_PASSWORD_INCORRECT
