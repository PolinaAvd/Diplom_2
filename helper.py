import random

class UserFactory:
    @staticmethod
    def create_user_with_random_param():

        return {
            "email": f'{random.randint(0, 99999999)}@mail.ru',
            "password": f'{random.randint(0, 99999999)}',
            "name": 'Diana'

        }


