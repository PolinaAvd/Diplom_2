import pytest
import datas
import allure
from api import CreateNewUserApi, DeleteNewUserApi


class TestCreateUser:


    @allure.title('Cоздать уникального пользователя')
    @allure.description('Cоздать уникального пользователя, проверка статуса ответа и тела ответа')
    def test_create_new_user_success(self, create_data):
        data = create_data
        response = CreateNewUserApi.create_new_user(data)
        assert response.status_code == 200 and datas.SUCCESS_TRUE, create_data['email'] in response.text
        DeleteNewUserApi.delete_user(response.json()["accessToken"])


    @allure.title('Cоздать пользователя, который уже зарегистрирован')
    @allure.description('Cоздать уникального пользователя, повторно создать пользователя с теми же данными, проверка статуса ответа и тела ответа')
    def test_create_user_two_times_fail(self, create_data):
        data = create_data
        save_token = CreateNewUserApi.create_new_user(data).json()["accessToken"]
        created_user_response = CreateNewUserApi.create_new_user(data)
        assert created_user_response.status_code == 403 and created_user_response.text == datas.ERROR_RESPONSE_USER_EXIST
        DeleteNewUserApi.delete_user(save_token)


    @allure.title('Cоздать пользователя и не заполнить одно из обязательных полей')
    @allure.description('Cоздать уникального пользователя, не заполнить одно из полей при регистрации, проверка статуса ответа и тела ответа')
    @pytest.mark.parametrize('payload', [datas.payload_1_empty, datas.payload_2_empty, datas.payload_3_empty])
    def test_create_user_one_field_empty_fail(self, payload):
        result = CreateNewUserApi.create_new_user(payload)
        assert result.status_code == 403 and result.text == datas.ERROR_RESPONSE_USER_CREATION_ONE_FIELD_EMPTY
