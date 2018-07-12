from astropy import units as u


class Quantity:
    def __init__(self, value=0., unit=""):
        self.u = str(unit)
        self.v = value

    def value(self):
        return self.v * u.Unit(self.u)

    def converted(self, target_unit):
        return self.value().to(target_unit)

    def si_val(self, target_unit):
        return self.converted(target_unit).value

    def __repr__(self):
        return """quantity: {value} {unit}""".format(value=self.v, unit=self.u)

    def __truediv__(self, other):
        return Quantity(self.v/other.v,str(u.Unit(self.u) / u.Unit(other.u)))

    def __mul__(self, other):
        return Quantity(self.v * other.v, str(u.Unit(self.u) * u.Unit(other.u)))

    def __eq__(self, other):
        return self.value() == other.value()