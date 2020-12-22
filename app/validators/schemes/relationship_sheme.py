from pydantic import BaseModel


class RelationshipScheme(BaseModel):
    user_id: str
    relative_id: str
