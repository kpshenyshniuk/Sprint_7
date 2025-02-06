import requests
import random
import string

def register_new_courier_and_return_response(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    return response

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_credentials(length):
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for i in range(length))
    password = ''.join(random.choice(letters) for i in range(length))
    first_name = ''.join(random.choice(letters) for i in range(length))
    return [login, password, first_name]


def successfull_login_courier(login, password):
    payload = {
        'login' : login,
        'password' : password
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    return response

def create_order(data):
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data)
    return response

def get_list_orders_by_courier_id(id):
    response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId= + {id}')
    return response
