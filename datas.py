import random

any_mail = 'anyyname@mail.ru'
any_pass = '11111'
headers = {"Content-type": "application/json"}
empty_list_of_ingredients = {'ingredients': []}
wrong_hash_of_ingredients = {'ingredients': ['609646e4dc900e00276b2870']}

ERROR_RESPONSE_USER_EXIST = '{"success":false,"message":"User already exists"}'
ERROR_RESPONSE_USER_CREATION_ONE_FIELD_EMPTY = '{"success":false,"message":"Email, password and name are required fields"}'
ERROR_EMAIL_OR_PASSWORD_INCORRECT = '{"success":false,"message":"email or password are incorrect"}'
ERROR_CHANGE_USER_WITHOUT_AUTH = '{"success":false,"message":"You should be authorised"}'
ERROR_BY_SENDING_EMPTY_LIST_OF_INGREDIENTS = '{"success":false,"message":"Ingredient ids must be provided"}'
ERROR_BY_SENDING_WRONG_HASH_OF_INGREDIENT = '{"success":false,"message":"One or more ids provided are incorrect"}'
ERROR_GET_ORDERS_UNAUTHORIZED = '{"success":false,"message":"You should be authorised"}'

SUCCESS_TRUE = '"success":true'

payload_1_empty = {
        "email": '',
        "password": f'Pass{random.randint(100, 999999)}',
        "name": "Diana"
    }

payload_2_empty = {
        "email": f"{random.randint(100, 9999999)}@gmail.com",
        "password": '',
        "name": "Diana"
    }

payload_3_empty = {
        "email": f"{random.randint(100, 9999999)}@gmail.com",
        "password": f'Pass{random.randint(100, 999999)}',
        "name": ''
    }
