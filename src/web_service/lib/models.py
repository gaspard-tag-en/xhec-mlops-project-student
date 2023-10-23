from pydantic import BaseModel


class InputData(BaseModel):
    Sex: int
    Length: int
    Diameter: int
    Height: int
    Whole_weight: int
    Shucked_weight: int
    Viscera_weight: int
    Shell_weight: int


class AbaloneAge(BaseModel):
    age: float
