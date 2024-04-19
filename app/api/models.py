from pydantic import BaseModel
from typing import List, Optional

class ClientIn(BaseModel):
    name: str
    surname: str
    age: int
    phone: str


class ClientOut(ClientIn):
    id: int
