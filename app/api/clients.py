from fastapi import APIRouter, HTTPException
from typing import List
from app.api.models import ClientOut, ClientIn
from app.api import db_manager

clients = APIRouter()

@clients.post('/', response_model=ClientOut, status_code=201)
async def create_client(payload: ClientIn):
    client_id = await db_manager.add_client(payload)

    response = {
        'id': client_id,
        **payload.dict()
    }

    return response


@clients.get('/', response_model=List[ClientOut])
async def get_clients():
    return await db_manager.get_all_clients()


@clients.get('/{id}/', response_model=ClientOut)
async def get_client(id: int):
    company = await db_manager.get_client(id)
    if not company:
        raise HTTPException(status_code=404, detail="Client not found")
    return company


@clients.delete('/{id}/', response_model=None)
async def delete_client(id: int):
    company = await db_manager.client(id)
    if not company:
        raise HTTPException(status_code=404, detail="Client not found")
    return await db_manager.delete_client(id)