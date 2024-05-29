import datas
import urls
import allure
import requests


class CreateNewUserApi:

    @staticmethod
    @allure.step("Регистрация пользователя")
    def create_new_user(body):

        return requests.post(urls.CREATE_USER_URL, json=body, headers=datas.headers)


class LoginApi:

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body, save_token):

        return requests.post(urls.LOGIN_URL, json=body, headers={'Authorization': f'{save_token}'})


class UserInfoGetApi:
    @staticmethod
    @allure.step("Изменение регистрационных данных пользователя")
    def patch_user_info(body, save_token):

        return requests.patch(urls.CHANGE_USER_INFO_URL, json=body, headers={'Authorization': f'{save_token}'})


class GetIngredients:
    @staticmethod
    @allure.step("Получение ингредиентов")
    def get_ingredients():

        return requests.get(urls.GET_INGREDIENTS_URL, headers=datas.headers)


class CreateOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, save_token):

        return requests.post(urls.CREATE_ORDER_URL, json=body, headers={'Authorization': f'{save_token}'})


class GetListOfOrders:

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(save_token):

        return requests.get(urls.GET_LIST_OF_ORDERS_URL, headers={'Authorization': f'{save_token}'})


class DeleteNewUserApi:

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(save_token):

        return requests.delete(urls.DELETE_USER_URL, headers={'Authorization': f'{save_token}'})


