from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str = 'Male'  # default value
    age: int
    address: Address



address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(** address_dict)

patient_dict = {'name': 'nitish', 'age' : 35, 'address': address1}

patient1 = Patient( ** patient_dict)


temp1 = patient1.model_dump(exclude_unset=True)   # convert pydantic model to a python dictionary 

print('dictionary:', temp1)
print(type(temp1))              # dict 

