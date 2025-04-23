class ComplexRadixJm1:
    """Complex number representation in radix-(j-1) (base -1+1j)."""

    def __init__(self, real: int, imag: int = 0) -> None:
        if not isinstance(real, int) or not isinstance(imag, int):
            raise TypeError("Real and imaginary parts must be integers.")
        self.digits: list[int] = []
        if real == 0 and imag == 0:
            self.digits = [0]
            return
        z = complex(real, imag)
        base = -1 + 1j
        while z != 0:
            for d in (0, 1):
                q = (z - d) / base
                qr, qi = round(q.real), round(q.imag)
                if abs(q.real - qr) < 1e-9 and abs(q.imag - qi) < 1e-9:
                    self.digits.append(d)
                    z = complex(qr, qi)
                    break
            else:
                raise ValueError(f"Cannot convert {real}+{imag}j to radix-(j-1)")
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __add__(self, other: 'ComplexRadixJm1') -> 'ComplexRadixJm1':
        r1, i1 = self.to_tuple()
        r2, i2 = other.to_tuple()
        return ComplexRadixJm1(r1 + r2, i1 + i2)

    def __mul__(self, other: 'ComplexRadixJm1') -> 'ComplexRadixJm1':
        r1, i1 = self.to_tuple()
        r2, i2 = other.to_tuple()
        return ComplexRadixJm1(r1*r2 - i1*i2, r1*i2 + i1*r2)

    def to_tuple(self) -> tuple[int, int]:
        r = i = 0
        base = -1 + 1j
        for k, d in enumerate(self.digits):
            v = base**k * d
            r += int(round(v.real))
            i += int(round(v.imag))
        return r, i

    def __str__(self) -> str:
        r, i = self.to_tuple()
        sign = '+' if i >= 0 else '-'
        return f"{r}{sign}{abs(i)}j"