import pytest
from app.api.models import ClientIn, ClientOut

clients = ClientIn(
    name='Anonim',
    surname='Anonimus',
    age='22',
    phone='+7987654321'
)


def test_create_client(client: ClientIn = clients):
    assert dict(client) == {'name': client.name,
                              'surname': client.surname,
                              'age': client.age,
                              'phone': client.phone
                              }


def test_update_client_age(clients: ClientIn = clients):
    client_upd = ClientOut(
        name='Anton',
        surname='Russian',
        age='21',
        phone='+7123456789',
        id=1
    )
    assert dict(client_upd) == {'name': clients.name,
                              'surname': clients.surname,
                              'age': clients.age,
                              'phone': clients.phone,
                              'id': client_upd.id
                              }


def test_update_client_genre(employee: ClientIn = clients):
    client_upd = ClientOut(
        name='Anton',
        surname='Russian',
        age='21',
        phone='+7123456789',
        id=1
    )
    assert dict(client_upd) == {'name': clients.name,
                              'surname': clients.surname,
                              'age': clients.age,
                              'phone': clients.phone,
                              'id': client_upd.id
                              }
