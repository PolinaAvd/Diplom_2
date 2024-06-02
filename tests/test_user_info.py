import datas
from api import UserInfoGetApi
import allure

class TestUserInfo:

    @allure.title('Измененение данных пользоваеля c авторизацией')
    @allure.description('Cоздание пользователя, изменение параметров email, password, name, проверка статуса ответа и тела ответа')
    def test_change_user_info_with_token_success(self, default_user_create_user_get_name_pass_email, create_data):
        save_token = default_user_create_user_get_name_pass_email[0]
        data_after_changes = create_data
        response = UserInfoGetApi.patch_user_info(data_after_changes, save_token)
        assert response.status_code == 200 and data_after_changes['email'] in response.text and data_after_changes['name'] in response.text
    @allure.title('Измененение данных пользоваеля без авторизации')
    @allure.description('Cоздание пользователя, изменение параметров email, password, name, проверка статуса ответа и тела ответа - токен не отправлен')
    def test_change_user_info_without_token_fail(self, default_user_create_user_get_name_pass_email, create_data):
        data_after_changes = create_data
        response = UserInfoGetApi.patch_user_info(data_after_changes, None)
        assert response.status_code == 401 and datas.ERROR_CHANGE_USER_WITHOUT_AUTH in response.text