from faker import Factory

from commons.config.datatype import DataType

fake = Factory.create()


def get_test_data(datatype):
    return str(fake.__dict__.get(DataType[datatype].value)())


if __name__ == '__main__':
    print(fake.__dict__)
    print(fake.address())
    print(get_test_data('EMAIL_ID'))
