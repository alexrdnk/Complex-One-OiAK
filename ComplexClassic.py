class ComplexClassic:
    """Classic representation of a complex number with separate real and imaginary parts."""

    def __init__(self, real: int, imag: int = 0) -> None:
        if not isinstance(real, int) or not isinstance(imag, int):
            raise TypeError("Real and imaginary parts must be integers.")
        self.real = real
        self.imag = imag

    def __add__(self, other: 'ComplexClassic') -> 'ComplexClassic':
        return ComplexClassic(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: 'ComplexClassic') -> 'ComplexClassic':
        a, b = self.real, self.imag
        c, d = other.real, other.imag
        return ComplexClassic(a*c - b*d, a*d + b*c)

    def conjugate(self) -> 'ComplexClassic':
        return ComplexClassic(self.real, -self.imag)

    def magnitude(self) -> float:
        return (self.real**2 + self.imag**2) ** 0.5

    def to_tuple(self) -> tuple[int, int]:
        return self.real, self.imag

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ComplexClassic) and self.to_tuple() == other.to_tuple()

    def __str__(self) -> str:
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real}{sign}{abs(self.imag)}j"

    def __repr__(self) -> str:
        return f"ComplexClassic({self.real}, {self.imag})"