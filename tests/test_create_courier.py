import helpers
import requests
import pytest

class TestCreateCourier:
    def test_create_courier(self):
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)
        response = helpers.register_new_courier_and_return_response(login, password, first_name)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json["ok"] == True

    def test_not_possible_to_create_similar_couriers(self):
        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)
        helpers.register_new_courier_and_return_response(login, password, first_name)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response_second = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        response_json = response_second.json()

        assert response_second.status_code == 409
        assert response_json["message"] == "Этот логин уже используется. Попробуйте другой."


    @pytest.mark.parametrize('login, password, first_name', [
        ('', helpers.generate_random_string(10), helpers.generate_random_string(10)),
         (helpers.generate_random_string(10), '', helpers.generate_random_string(10))
    ])
    def test_not_possible_create_courier_without_required_fields(self, login, password, first_name):
        response = helpers.register_new_courier_and_return_response(login, password, first_name)
        response_json = response.json()

        assert response.status_code == 400
        assert response_json["message"] == "Недостаточно данных для создания учетной записи"
