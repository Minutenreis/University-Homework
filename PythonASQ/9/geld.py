class Geld:
    __exchange_rates_eur = {
    'EUR': 1,
    'USD': 1.09,
    'GBP': 0.85,
    'JPY': 168.98
    }
    
    @classmethod
    def exchange_rates_eur(cls):
        return cls.__exchange_rates_eur
    
    @classmethod
    def add_exchange_rates_eur(cls, rate: tuple[str, float]):
        if rate[0] in cls.__exchange_rates_eur:
            raise ValueError('Wechselkurs bereits vorhanden')
        cls.__exchange_rates_eur[rate[0]] = rate[1]
    
    def __init__(self, value = 0, currency = 'EUR'):
        if currency not in Geld.exchange_rates_eur():
            raise ValueError('Unbekannte Währung')
        self.__value = value
        self.__currency = currency
        
    def change_currency(self, new_currency):
        if new_currency not in Geld.exchange_rates_eur():
            raise ValueError('Unbekannte Währung')
        self.__value = self.__value * Geld.exchange_rates_eur[self.__currency] / Geld.exchange_rates_eur[new_currency]
        self.__currency = new_currency
    
    def add(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann zu Geld addiert werden')
        self.__value += other.valueInEuro() / Geld.exchange_rates_eur[self.__currency]
    
    def sub(self, other):
        if type(other) != Geld:
            raise TypeError('Nur Geld kann von Geld subtrahiert werden')
        self.__value -= other.valueInEuro() / Geld.exchange_rates_eur[self.__currency]
    
    def valueInEuro(self):
        return self.__value * Geld.exchange_rates_eur[self.__currency]
    
    @property
    def value(self):
        return str(self)
    
    @value.setter
    def value(self, value):
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
        return Geld(self.__value + other.valueInEuro() / Geld.exchange_rates_eur[self.__currency], self.__currency)

# Test
g1 = Geld(100, 'USD')
print(g1)
g1.value = 200
print(g1)