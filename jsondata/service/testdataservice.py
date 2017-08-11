from faker import Factory

from jsondata.config.datatype import DataType

fake = Factory.create()


def get_test_data(datatype, count):
    datavals = []
    for _ in range(count):
        datavals.append(fake.__dict__.get(DataType[datatype].value)())
    return datavals


if __name__ == '__main__':
    print(fake.profile())
    print(get_test_data('EMAIL_ID', 10))
