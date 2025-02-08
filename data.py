base_url = 'https://qa-scooter.praktikum-services.ru'
create_courier_url = base_url + '/api/v1/courier'

error_create_already_created_user = "Этот логин уже используется. Попробуйте другой."
error_create_courier_without_required_fields = "Недостаточно данных для создания учетной записи"
error_login_courier_without_required_fields = "Недостаточно данных для входа"
error_login_with_invalid_credentials = "Учетная запись не найдена"

data_for_order_black_only = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

data_for_order_gray_only = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GRAY"
    ]
}

data_for_order_black_and_gray = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK",
        "GRAY"
    ]
}
