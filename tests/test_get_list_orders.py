import data
import helpers

class TestListOrders:
    def test_get_list_orders_by_courier_id(self):
        credentials = helpers.generate_random_credentials(10)
        helpers.register_new_courier_and_return_response(credentials[0], credentials[1], credentials[2])
        response = helpers.successfull_login_courier(credentials[0], credentials[1])
        response_json = response.json()
        courier_id = response_json.get('id')
        response = helpers.get_list_orders_by_courier_id(courier_id)
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)
