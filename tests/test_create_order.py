from api import CreateOrder
import datas
import allure

class TestCreateOrder:


    @allure.title('Создание заказа с ингредиентами для авторизованного пользователя')
    @allure.description('Cоздание пользователя, получение списка ингредиентов, создание заказа из списка ингредиентов для пользователя')
    def test_create_order_with_authorization_success(self, create_default_order):
        response = create_default_order[1]
        assert response.status_code == 200 and 'order', 'number' in response.text


    @allure.title('Создание заказа с ингредиентами без авторизациии')
    @allure.description('Получение списка ингредиентов, создание заказа из списка ингредиентов для невторизованного пользователя')
    def test_create_order_without_authorization_success(self, get_ingredients):
        ingredients_data = get_ingredients
        response = CreateOrder.create_order(ingredients_data, None)
        assert response.status_code == 200 and 'order', 'number' in response.text


    @allure.title('Создание заказа без ингредиентов для неавторизованного пользователя')
    @allure.description('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_fail(self):
        ingredients_data = datas.empty_list_of_ingredients
        response = CreateOrder.create_order(ingredients_data, None)
        assert response.status_code == 400 and response.text == datas.ERROR_BY_SENDING_EMPTY_LIST_OF_INGREDIENTS


    @allure.title('Создание заказа с неверным хешем ингредиентов для авторизованного пользователя')
    @allure.description('Cоздание пользователя, создание заказа c неверных хешем ингредиентов для пользователя')
    def test_create_order_with_wrong_ingredient_hesh_fail(self, default_user_create_user):
        ingredients_data = datas.wrong_hash_of_ingredients
        save_data = default_user_create_user[0]
        response = CreateOrder.create_order(ingredients_data, save_data)
        assert response.status_code == 400 and response.text == datas.ERROR_BY_SENDING_WRONG_HASH_OF_INGREDIENT
        # Ожидаемый результат: Если в запросе передан невалидный хеш ингредиента, вернётся код ответа 500 Internal Server Error.
        # Фактичексий результат: Если в запросе передан невалидный хеш ингредиента, возвращаетя код ответа 400 и тескт {"success":false,"message":"One or more ids provided are incorrect"})




