from pytest import fixture
from settings.params import settings


@fixture
def user_data() -> dict:
    return {
        "first_name": settings.FIRST_NAME,
        "last_name": settings.LAST_NAME,
        "address": settings.ADDRESS,
        "city": settings.CITY,
        "state": settings.STATE,
        "zip_code": settings.ZIP_CODE,
        "phone": settings.PHONE,
        "ssn": settings.SSN,
        "username": settings.USERNAME,
        "password": settings.PASSWORD,
        "email": settings.EMAIL,
        "message": settings.MESSAGE,
        "amount": settings.AMOUNT,
    }
