import pytest
import helpers


@pytest.fixture
def registered_courier():
    """Фикстура для регистрации нового курьера"""
    credentials = helpers.generate_random_credentials(10)
    response = helpers.register_new_courier_and_return_response(credentials[0], credentials[1], credentials[2])
    assert response.status_code == 201, f"Ошибка регистрации: {response.json()}"
    yield credentials[0], credentials[1]
    response_id = helpers.successfull_login_courier(credentials[0], credentials[1])
    response_json = response_id.json()
    courier_id = response_json.get("id")
    if courier_id:
        helpers.delete_courier_by_id(courier_id)

@pytest.fixture
def create_credentials_for_courier():
    login = helpers.generate_random_string(10)
    password = helpers.generate_random_string(10)
    first_name = helpers.generate_random_string(10)
    return login, password, first_name

