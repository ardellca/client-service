from app.api.models import ClientIn, ClientOut
from app.api.db import clients, database


async def add_client(payload: ClientIn):
    query = clients.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_client():
    query = clients.select()
    return await database.fetch_all(query=query)


async def get_client(id):
    query = clients.select().where(clients.c.id == id)
    return await database.fetch_one(query=query)


async def delete_client(id: int):
    query = clients.delete().where(clients.c.id == id)
    return await database.execute(query=query)

