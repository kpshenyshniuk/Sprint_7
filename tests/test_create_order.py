import helpers
import pytest
import data

class TestCreateOrder:

    @pytest.mark.parametrize('data', [
        data.data_for_order_black_only,
        data.data_for_order_gray_only,
        data.data_for_order_black_and_gray
    ])
    def test_create_order(self, data):
        response = helpers.create_order(data)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json['track'] > 0
