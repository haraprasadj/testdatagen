from enum import Enum


class DataType(Enum):
    NAME = 'name'
    PHONE_NUMER = 'phone_number'
    EMAIL_ID = 'email'
    ADDRESS = 'address'
    COMPANY = 'company'
    DATE = 'date'
    DATE_TIME = 'date_time'
    RANDOM_TEXT = 'bs'

if __name__=='__main__':
    for name, member in DataType.__members__.items():
        print(name, name)

