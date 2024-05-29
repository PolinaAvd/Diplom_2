import pytest
import allure
from helper import UserFactory
from api import CreateNewUserApi
from api import DeleteNewUserApi
from api import GetIngredients
from api import CreateOrder

@allure.step("Создание шаблона параметров для регистрации: емейл, пароль, имя")
@pytest.fixture(scope='function')
def create_data():
    data = UserFactory.create_user_with_random_param()
    return data


@allure.step("Создание пользователя для последующей авторизации: вывод [токен пользователя, email+pass]")
@pytest.fixture(scope='function')
def default_user_create_user(create_data):
    save_token = CreateNewUserApi.create_new_user(create_data).json()["accessToken"]
    del create_data['name']
    yield [save_token, create_data]
    DeleteNewUserApi.delete_user(save_token)


@allure.step("Создание пользователя: вывод [токен пользователя, email+pass+name]")
@pytest.fixture(scope='function')
def default_user_create_user_get_name_pass_email(create_data):
    save_token = CreateNewUserApi.create_new_user(create_data).json()["accessToken"]
    yield [save_token, create_data]
    DeleteNewUserApi.delete_user(save_token)


@allure.step("Получение ингредиентов: вывод [список ингредиентов 2,1,5]")
@pytest.fixture(scope='function')
def get_ingredients():
    response = GetIngredients.get_ingredients()
    id_1 = response.json()['data'][1]['_id']
    id_2 = response.json()['data'][2]['_id']
    id_5 = response.json()['data'][5]['_id']
    dict_of_ingredients = {'ingredients': [id_2, id_1, id_5]}
    return dict_of_ingredients


@allure.step("Создание заказа: вывод [токен, ответ]")
@pytest.fixture(scope='function')
def create_default_order(default_user_create_user, get_ingredients):
    save_token = default_user_create_user[0]
    ingredients_data = get_ingredients
    response = CreateOrder.create_order(ingredients_data, save_token)
    yield [save_token, response]
    DeleteNewUserApi.delete_user(save_token)