import data
import sender_stand_request
def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]
    # Función para las pruebas positivas

def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    # Función para las pruebas negativas


def test_one_character():
    positive_assert(data.one_character)
    # Prueba 1: El número permitido de caracteres (1)

def test_maximum_characters():
    positive_assert(data.maximum_characters)
    # Prueba 2: El número permitido de caracteres (511)

def test_empty_string():
    negative_assert_code_400(data.empty_string)
    # Prueba 3: El número de caracteres es menor que la cantidad permitida (0)

def test_higher_character_plus_one():
    negative_assert_code_400(data.higher_character_plus_one)
    # Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)

def test_special_character():
    positive_assert(data.special_characters)
    # Prueba 5: Se permiten caracteres especiales

def test_characters_with_space():
    positive_assert(data.characters_with_space)
    # Prueba 6: Se permiten espacios

def test_characters_with_number():
    positive_assert(data.characters_with_number)
    # Prueba 7: Se permiten números

def test_empty_characters():
    negative_assert_code_400(data.empty_characters)
    # Prueba 8: El parámetro no se pasa en la solicitud

def test_without_string_character():
    negative_assert_code_400(data.without_string_character)
    # Prueba 9: Se ha pasado un tipo de parámetro diferente (número)