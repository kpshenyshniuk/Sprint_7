import pytest
import helpers


@pytest.fixture
def registered_courier():
    """Фикстура для регистрации нового курьера"""
    credentials = helpers.generate_random_credentials(10)
    response = helpers.register_new_courier_and_return_response(credentials[0], credentials[1], credentials[2])
    assert response.status_code == 201, f"Ошибка регистрации: {response.json()}"
    return credentials[0], credentials[1]




