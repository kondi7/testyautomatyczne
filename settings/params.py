from pydantic import BaseSettings


class Base(BaseSettings):
    TEST_URL: str = "https://parabank.parasoft.com/parabank/index.htm"
    FIRST_NAME: str = "Heniek"
    LAST_NAME: str = "Keineh"
    ADDRESS: str = "Kaczowata 55"
    CITY: str = "Kaszatanowo"
    STATE: str = "Mazowieckie"
    ZIP_CODE: str = "05-840"
    PHONE: str = "123-456-789"
    SSN: str = "1234043043"
    USERNAME: str = "heniek55"
    PASSWORD: str = "klemens1"
    EMAIL: str = "heniek55@siema.pl"
    MESSAGE: str = "eeeeeeeeelo"
    AMOUNT: str = "5"

settings = Base()
