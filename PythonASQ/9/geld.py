class Geld:
    __basis = 'EUR'
    __exchange_rates = {
    'EUR': 1,
    'USD': 1.09,
    'GBP': 0.85,
    'JPY': 168.98
    }
    
    @classmethod
    def basis(cls):
        return cls.__basis
    
    @classmethod
    def setNewBasis(cls, new_basis):
        if new_basis not in cls.__exchange_rates:
            raise ValueError('Unbekannte Währung')
        exchange_rate_basis = cls.__exchange_rates[new_basis]
        for key in cls.__exchange_rates:
            cls.__exchange_rates[key] = cls.__exchange_rates[key] / exchange_rate_basis
        cls.__basis = new_basis
    
    @classmethod
    def exchange_rates(cls):
        return cls.__exchange_rates
    
    @classmethod
    def add_exchange_rates(cls, rate: tuple[str, float]):
        if rate[0] in cls.__exchange_rates:
            raise ValueError('Wechselkurs bereits vorhanden')
        cls.__exchange_rates[rate[0]] = rate[1]
    
    @property
    def base_currency(self):
        return Geld.basis()
    
    @base_currency.setter
    def base_currency(self, new_basis):
        Geld.setNewBasis(new_basis)
    
    def __init__(self, value = 0, currency = 'EUR'):
        if currency not in Geld.exchange_rates():
            raise ValueError('Unbekannte Währung')
        self.__value = value
        self.__currency = currency
        
    def change_currency(self, new_currency):
        if new_currency not in Geld.exchange_rates():
            raise ValueError('Unbekannte Währung')
        self.__value = self.value / Geld.exchange_rates()[self.__currency] * Geld.exchange_rates()[new_currency]
        self.__currency = new_currency
    
    def add(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann zu Geld addiert werden')
        self.__value += other.valueInEuro() * Geld.exchange_rates()[self.__currency]
    
    def sub(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann von Geld subtrahiert werden')
        self.__value -= other.valueInEuro() * Geld.exchange_rates()[self.__currency]
    
    def valueInEuro(self):
        return self.__value / Geld.exchange_rates()[self.__currency]
    
    @property
    def value(self):
        return str(self)
    
    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError('Wert darf nicht negativ sein')
        self.__value = value
    
    def __str__(self):
        return f'{round(self.__value,2):.2f} {self.__currency}'
    
    def __repr__(self):
        return f'Geld({self.__value}, {self.__currency})'
    
    def __eq__(self, other):
        return self.__value == other.wert and self.__currency == other.waehrung
    
    def __add__(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann zu Geld addiert werden')
        return Geld(self.__value + other.valueInEuro() * Geld.exchange_rates()[self.__currency], self.__currency)
    
    def __sub__(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann von Geld subtrahiert werden')
        return Geld(self.__value - other.valueInEuro() * Geld.exchange_rates()[self.__currency], self.__currency)

# Test
g1 = Geld(100, 'EUR')
g1.base_currency = 'USD'
g2 = Geld(100, 'USD')
print(g1 - g2)