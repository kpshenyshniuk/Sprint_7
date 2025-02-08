import conftest
import data
import helpers
import requests
import pytest

class TestCreateCourier:
    def test_create_courier(self, create_credentials_for_courier):
        login, password, first_name = create_credentials_for_courier
        response = helpers.register_new_courier_and_return_response(login, password, first_name)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json["ok"] == True

    def test_not_possible_to_create_similar_couriers(self, create_credentials_for_courier):
        login, password, first_name = create_credentials_for_courier
        helpers.register_new_courier_and_return_response(login, password, first_name)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response_second = requests.post(data.create_courier_url, data=payload)
        response_json = response_second.json()

        assert response_second.status_code == 409
        assert response_json["message"] == data.error_create_already_created_user


    @pytest.mark.parametrize('login, password, first_name', [
        ('', helpers.generate_random_string(10), helpers.generate_random_string(10)),
         (helpers.generate_random_string(10), '', helpers.generate_random_string(10))
    ])
    def test_not_possible_create_courier_without_required_fields(self, login, password, first_name):
        response = helpers.register_new_courier_and_return_response(login, password, first_name)
        response_json = response.json()

        assert response.status_code == 400
        assert response_json["message"] == data.error_create_courier_without_required_fields
