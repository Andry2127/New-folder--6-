from typing import List, Dict, Union, Optional, Annotated
# from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl, EmailStr, field_validator, Field


class BookModel(BaseModel):
    index: int = Field(..., description="Book ID")
    name: str = Field(..., description="new spell")
    author: str = Field(..., description="new spell")
    date: Optional[int] = Field(None, description="Рік видання")  
    quantity: Optional[int] = Field(None, description="Доступна кількість")



class BookModellResponse(BaseModel):
    index: int = Field(..., description="Book ID")
    name: str = Field(..., description="new spell")
    author: str = Field(..., description="new spell")
    date: Optional[int] = Field(None, description="Рік видання")
    quantity: Optional[int] = Field(None, description="Доступна кількість")





class UserModel(BaseModel):
    # name: str = "Alex"
    # name: str = Field(default="Alex", examples=["Alex", "Alex12"], description="Username")
    name: Annotated[str, Field(default="Alex", examples=["Alex","Alex12"], description="Username", min_length=2)]
    login: Annotated[str, Field(..., description="Login", min_length=3)]
    password: Annotated[str, Field(..., examples=["zXc&52"], description="password", min_lenght=6 )]
    email: Annotated[EmailStr, Field(..., example="example@gmail.com", description="your email")]
    phone: Annotated[str, Field(None, examples=["+380 12 345 67 89"], description="Phone number", min_length=9)]
    # created: Annotated[datetime, Field(default=datetime.now())]

    @field_validator("password")
    def check_password(cls, value: str):
        if value == "zXc&52":
            raise ValueError("Dont use example paswword!!! 100-7")
        

        if any([value.isdigit(), value.isalpha()]):
            raise ValueError("Password must contain at least one letter and number ")
        
        is_upper = False 
        is_lower = False
        for char in value:
            if not is_upper and char.islower():
                is_upper =True
            if not is_lower and char.isupper():
                is_lower = True
            if all([is_lower, is_upper]):
                break
        else:
            raise ValueError("password must contain Upper and Lower case letter")
        return value
    

    @field_validator("phone")
    def check_phone(cls, value: str):
        if value == "+380 12 345 67 89":
            raise ValueError("Dont use example phone number")
        
        if any(char.isalpha() for char in value):
            raise ValueError("Phone number should not contain letters")

        return value      
        





class EventModel(BaseModel):
    index: int = Field(..., description="ID")
    name: str = Field(..., description="Name")
    palce: str = Field(..., description="place")
    date: Annotated[str, Field(..., examples="2001-10-21", description="date")] 
    description: Optional[str] = Field(None, description="description")



class EventModellResponse(BaseModel):
    index: int = Field(..., description="ID")
    name: str = Field(..., description="Name")
    palce: str = Field(..., description="place")
    date: Annotated[str, Field(..., description="date")] 
    description: Optional[str] = Field(None, description="description")



# user = UserModel(
#     name= "Kaneki",
#     login= "Kenn",
#     password= "Ghoul993",
#     email= "ghoul@gmail.com",
#     phone= "+380 12 345 66 89"


# )

# print(user)



# class BookModels(BaseModel):
#     name: Annotated[str, Field(description="name of the book")]
#     created: Annotated[Union[datetime, str], Field(..., examples="2001 10 21", description="book release date")]

#     @field_validator("created")
#     def check_created(cls, value: Union[str, datetime]):
#         if isinstance(value, str):
#             return datetime.strptime(value, "%Y %m %d")
#         return value




# book = BookModels(
#     name="Green",
#     # created="2002-12-12"
#     created="2002 12 12"


    
# )



# print(book)






