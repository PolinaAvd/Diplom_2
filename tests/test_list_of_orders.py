import datas
import api
import allure
from api import GetListOfOrders
from collections import Counter
from operator import itemgetter


class TestGetListOfOrders:


    @allure.title('Получение заказов для авторизованного пользователя - 1 заказ')
    @allure.description('Cоздание пользователя, получение списка ингредиентов, создание заказа из списка ингредиентов для пользователя и получение списка заказов')
    def test_get_one_order_authorized_success(self, create_default_order, get_ingredients):
        save_token = create_default_order[0]
        response = GetListOfOrders.get_orders(save_token)
        list_of_ingedients = response.json()['orders'][0]['ingredients']
        assert response.status_code == 200 and list_of_ingedients == get_ingredients['ingredients']


    @allure.title('Получение заказов для авторизованного пользователя - 2 заказа')
    @allure.description('Cоздание пользователя, получение списка ингредиентов, создание 2ух заказов из списка ингредиентов для пользователя и получение списка заказов')
    def test_get_two_orders_authorized_success(self, create_default_order, get_ingredients):
        save_token = create_default_order[0]
        api.CreateOrder.create_order(get_ingredients, save_token)
        response = GetListOfOrders.get_orders(save_token)
        count_of_ids = response.json()['orders']
        quantity = len(Counter(map(itemgetter('_id'), count_of_ids)))
        assert response.status_code == 200 and quantity == 2
        # API для получения заказов конкретного пользователя не вернет корректное количество заказов пользователя(значение параметра 'total' в ответе запроса), порядковый номер заказа так же будет неверный.
        # Фактически количество заказов для конкретного пользователя возвращается из метода Получить ВСЕ заказы для ВСЕХ пользователей - уточнить у дизайнера, такая ли логика закладывалась.


    @allure.title('Получение заказов для неавторизованного пользователя')
    @allure.description('Получение списка ингредиентов, создание заказа из списка ингредиентов и получение списка заказов')
    def test_get_order_unauthorized_fail(self, create_default_order, get_ingredients):
        create_default_order
        response = GetListOfOrders.get_orders(None)
        assert response.status_code == 401 and response.text == datas.ERROR_GET_ORDERS_UNAUTHORIZED
