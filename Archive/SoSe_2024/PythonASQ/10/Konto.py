from datetime import datetime

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
        self._value = value
        self._currency = currency
        
    def change_currency(self, new_currency):
        if new_currency not in Geld.exchange_rates():
            raise ValueError('Unbekannte Währung')
        self._value = self.value / Geld.exchange_rates()[self._currency] * Geld.exchange_rates()[new_currency]
        self._currency = new_currency
    
    def add(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann zu Geld addiert werden')
        self._value += other.valueInEuro() * Geld.exchange_rates()[self._currency]
    
    def sub(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann von Geld subtrahiert werden')
        self._value -= other.valueInEuro() * Geld.exchange_rates()[self._currency]
    
    def valueInEuro(self):
        return round(self._value / Geld.exchange_rates()[self._currency],2)
    
    @property
    def value(self):
        return str(self)
    
    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError('Wert darf nicht negativ sein')
        self._value = value
        
    # += ist implizit mit definiert durch __add__
    def __add__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann zu Geld addiert werden')
        if self._currency != other._currency:
            raise ValueError('Währungen müssen gleich sein')
        return Geld(self._value + other._value, self._currency)
    
    # -= ist implizit mit definiert durch __sub__
    def __sub__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann von Geld subtrahiert werden')
        if self._currency != other._currency:
            raise ValueError('Währungen müssen gleich sein')
        return Geld(self._value - other._value, self._currency)
    
    def __str__(self):
        return f'{round(self._value,2):.2f} {self._currency}'
    
    def __repr__(self):
        return f'Geld({self._value}, {self._currency})'
    
    def __eq__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann mit Geld verglichen werden')
        return self.valueInEuro() == other.valueInEuro()
    
    def __lt__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann mit Geld verglichen werden')
        return self.valueInEuro() < other.valueInEuro()
    
    def __le__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann mit Geld verglichen werden')
        return self.valueInEuro() <= other.valueInEuro()
    
    def __gt__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann mit Geld verglichen werden')
        return self.valueInEuro() > other.valueInEuro()
    
    def __ge__(self, other):
        if not isinstance(other, Geld):
            raise TypeError('Nur Geld kann mit Geld verglichen werden')
        return self.valueInEuro() >= other.valueInEuro()

class Konto(Geld):
    def __init__(self, kontoinhaberIn: str, value = 0, currency = 'EUR'):
        Geld.__init__(self, value, currency)
        self.__kontoinhaberIn = kontoinhaberIn
        self.transaktionsregister = []
        
    @property
    def kontoinhaberIn(self):
        return self.__kontoinhaberIn
    
    def add(self, geld):
        if not isinstance(geld, Geld):
            raise TypeError('Nur Geld kann aufs Konto eingezahlt werden')
        if isinstance(geld, Konto):
            raise TypeError('Konten können nicht addiert werden')
        self.transaktionsregister.append(f'{geld} wurde am {datetime.now().strftime("%c")} auf das Konto eingezahlt')
        self._value += geld.valueInEuro() * Geld.exchange_rates()[self._currency]
    
    def sub(self, geld):
        if not isinstance(geld, Geld):
            raise TypeError('Nur Geld kann vom Konto abgehoben werden')
        if isinstance(geld, Konto):
            raise TypeError('Konten können nicht subtrahiert werden')
        self.transaktionsregister.append(f'{geld} wurde am {datetime.now().strftime("%c")} vom Konto abgehoben')
        self._value -= geld.valueInEuro() * Geld.exchange_rates()[self._currency]
    
    def getTransactions(self, searchStr : str=None):
        if searchStr:
            return "\n".join([transaction for transaction in self.transaktionsregister if searchStr in transaction])
        return "\n".join(self.transaktionsregister)
    
    def __str__(self):
        return f'Konto: {super().__str__()}'
    
    def __repr__(self):
        return f'Konto({self._value}, {self._currency})'
    # I'd argue that all compare functions should not be implemented for Konto, as I don't see a practical reason
    # I'd argue that you should only add Geld to Konto by its methods instead of creating a new Konto object each time
    # misusing __add__ to add something inPlace seems severly wrong to me
    def __eq__(self, other):
        return self.valueInEuro() == other.valueInEuro() and self.kontoinhaberIn == other.kontoinhaber

geld = Geld(100, 'EUR')
geld3 = Geld(100, 'EUR')
print(geld3 != geld)
konto = Konto('Max Mustermann', 100, 'EUR')
konto.add(geld)
print(konto.valueInEuro(), "EUR")
print(konto.getTransactions())
geld2 = Geld(50, 'USD')
konto.sub(geld2)
print(konto.valueInEuro(), "EUR")
print(konto.getTransactions())
print(konto.getTransactions('50'))

    