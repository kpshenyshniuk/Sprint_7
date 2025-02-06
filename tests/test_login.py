import helpers
import pytest

class TestLogin:
    def test_login_courier(self):
        credentials = helpers.generate_random_credentials(10)
        helpers.register_new_courier_and_return_response(credentials[0], credentials[1],credentials[2] )
        response = helpers.successfull_login_courier(credentials[0], credentials[1])
        response_json = response.json()

        assert response.status_code == 200
        assert "id" in response_json
        assert response_json['id'] > 0

    @pytest.mark.parametrize('login, password',
        [('', 'somepassword'),
        ('someusername', '')
    ])
    def test_unsuccessfull_login_without_required_fields(self, registered_courier, login, password):
        valid_username, valid_password = registered_courier
        login = valid_username if login == 'someusername' else login
        password = valid_password if password == 'somepassword' else password
        response = helpers.successfull_login_courier(login, password)
        response_json = response.json()

        assert response.status_code == 400
        assert response_json["message"] == "Недостаточно данных для входа"

    @pytest.mark.parametrize('login, password', [
        ('invalid_username@', 'valid_password'),
        ('valid_username', 'invalid_password@')
    ])
    def test_unsuccessfull_login_with_wrong_username_password(self, registered_courier, login, password):
        valid_username, valid_password = registered_courier
        login = valid_username if login == 'valid_username' else login
        password = valid_password if password == 'valid_password' else password
        response = helpers.successfull_login_courier(login, password)
        response_json = response.json()

        assert response.status_code == 404
        assert response_json["message"] == "Учетная запись не найдена"
