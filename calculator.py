import time
from ComplexClassic import ComplexClassic
from ComplexRadix2j import ComplexRadix2j
from ComplexRadixJm1 import ComplexRadixJm1


def choose_representation():
    print("Choose complex number representation:")
    print("1. Classic")
    print("2. Radix-2j")
    print("3. Radix-(j-1)")
    return input("Enter choice (1/2/3): ").strip()


def choose_operation():
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Multiplication (*)")
    return input("Enter operation (1/2): ").strip()


def read_complex(prompt="complex number") -> tuple[int,int]:
    print(f"Enter the {prompt}:")
    real = int(input("  Real part: "))
    imag = int(input("  Imaginary part: "))
    return real, imag


def calculate():
    rep = choose_representation()
    op = choose_operation()
    r1, i1 = read_complex("first complex number")
    r2, i2 = read_complex("second complex number")

    cls = {
        "1": ComplexClassic,
        "2": ComplexRadix2j,
        "3": ComplexRadixJm1
    }.get(rep, ComplexClassic)

    x = cls(r1, i1)
    y = cls(r2, i2)

    t0 = time.perf_counter()
    if op == "1":
        result = x + y
        sym = '+'
    else:
        result = x * y
        sym = '*'
    duration = time.perf_counter() - t0

    print(f"\nResult: ({x}) {sym} ({y}) = {result}")
    print(f"Time taken: {duration:.6f} s")