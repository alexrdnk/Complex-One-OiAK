class ComplexRadix2j:
    """Complex number representation in radix-2j (quater-imaginary)."""

    def __init__(self, real: int, imag: int = 0) -> None:
        if not isinstance(real, int) or not isinstance(imag, int):
            raise TypeError("Real and imaginary parts must be integers.")
        if imag % 2 != 0:
            raise ValueError(f"Imaginary part must be even for radix-2j; got {imag}")
        self.digits = self._convert(complex(real, imag)) or [0]

    def _convert(self, z: complex) -> list[int]:
        if z == 0:
            return []
        base = 2j
        for d in range(4):
            q = (z - d) / base
            qr, qi = round(q.real), round(q.imag)
            if abs(q.real - qr) < 1e-9 and abs(q.imag - qi) < 1e-9:
                if (qr, qi) != (0, 0) and (qi % 2):
                    continue
                return [d] + self._convert(complex(qr, qi))
        raise ValueError(f"Cannot convert {z} to radix-2j")

    def __add__(self, other: 'ComplexRadix2j') -> 'ComplexRadix2j':
        r1, i1 = self.to_tuple()
        r2, i2 = other.to_tuple()
        return ComplexRadix2j(r1 + r2, i1 + i2)

    def __mul__(self, other: 'ComplexRadix2j') -> 'ComplexRadix2j':
        r1, i1 = self.to_tuple()
        r2, i2 = other.to_tuple()
        return ComplexRadix2j(r1*r2 - i1*i2, r1*i2 + i1*r2)

    def to_tuple(self) -> tuple[int, int]:
        r = i = 0
        base = 2j
        for k, d in enumerate(self.digits):
            v = base**k * d
            r += int(round(v.real))
            i += int(round(v.imag))
        return r, i

    def __str__(self) -> str:
        r, i = self.to_tuple()
        sign = '+' if i >= 0 else '-'
        return f"{r}{sign}{abs(i)}j"