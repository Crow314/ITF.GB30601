from telephonenumber import TelephoneNumber


class Person:
    _name: str  # 名前
    _company: str  # 勤務先の会社名
    _office_telephone: TelephoneNumber

    def __init__(self, name: str, company: str,
        office_area_code: str, office_number: str) -> None:

        self._name = name
        self._company = company
        self._office_telephone = TelephoneNumber()

        self._office_telephone.area_code = office_area_code
        self._office_telephone.number = office_number

    @property
    def name(self) -> str:
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def office_telephone_number(self):
        return self._office_telephone.telephone_number
