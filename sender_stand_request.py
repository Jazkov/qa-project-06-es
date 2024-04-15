import configuration
import requests
import data

#  Función para crear un nuevo usuario o usuaria
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body)

# Diccionario para conservar los datos de origen
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Función para recordar el token de autenticación
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

# Función para crear un kit para el usuario o usuaria
def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                          json=kit_body,
                          headers=headers)