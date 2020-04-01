class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

#c = Celsius()

class Account:
    """A class computer account. Each account has a two-letter ID
    and the name of the student who is registered to the account.
    """
    num_of_accounts = 0
    def __init__(self, id):
        self.id = id
        Account.num_of_accounts += 1

    def register(self, student):
        self.student = student
        print('Registered ' + student)

    @property
    def type(self):
        return type(self)

acc_aa = Account('aa')

acc_aa.register("Peter Perfect")
#Account.register(self, "Jom Magrotker")
Account.register(acc_aa, "Jom Magrotker")
Account.register("Jom Magrotker")