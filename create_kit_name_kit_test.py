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


def test_kit_creation_1():
    positive_assert(data.kit_body1)
    # Prueba 1: El número permitido de caracteres (1)

def test_kit_creation_2():
    positive_assert(data.kit_body2)
    # Prueba 2: El número permitido de caracteres (511)

def test_kit_creation_3():
    negative_assert_code_400(data.kit_body3)
    # Prueba 3: El número de caracteres es menor que la cantidad permitida (0)

def test_kit_creation_4():
    negative_assert_code_400(data.kit_body4)
    # Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)

def test_kit_creation_5():
    positive_assert(data.kit_body5)
    # Prueba 5: Se permiten caracteres especiales

def test_kit_creation_6():
    positive_assert(data.kit_body6)
    # Prueba 6: Se permiten espacios

def test_kit_creation_7():
    positive_assert(data.kit_body7)
    # Prueba 7: Se permiten números

def test_kit_creation_8():
    negative_assert_code_400(data.kit_body8)
    # Prueba 8: El parámetro no se pasa en la solicitud

def test_kit_creation_9():
    negative_assert_code_400(data.kit_body9)
    # Prueba 9: Se ha pasado un tipo de parámetro diferente (número)