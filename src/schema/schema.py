from pydantic import BaseModel, Field


class SignupSchema(BaseModel):
    email: str = Field(pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}")
    password: str = Field(min_length=6, max_length=20)
