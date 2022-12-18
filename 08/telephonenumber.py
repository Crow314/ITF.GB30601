class TelephoneNumber:
    _area_code: str  # 勤務先の市外局番
    _number: str  # 勤務先の市内電話番号

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, area_code: str):
        self._area_code = area_code

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

    @property
    def telephone_number(self):
        return self._area_code + "-" + self._number

