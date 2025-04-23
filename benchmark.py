import time
import random
import csv
import argparse
import matplotlib.pyplot as plt
from ComplexClassic import ComplexClassic
from ComplexRadix2j import ComplexRadix2j
from ComplexRadixJm1 import ComplexRadixJm1


def run_benchmark(reps: int):
    results = []
    for cls in (ComplexClassic, ComplexRadix2j, ComplexRadixJm1):
        name = cls.__name__
        data = [(random.randint(-10000, 10000), random.randint(-10000, 10000)) for _ in range(reps)]
        # addition
        t0 = time.perf_counter()
        for a, b in data:
            _ = cls(a, 0) + cls(b, 0)
        add_time = time.perf_counter() - t0
        # multiplication
        t0 = time.perf_counter()
        for a, b in data:
            _ = cls(a, 0) * cls(b, 0)
        mul_time = time.perf_counter() - t0
        results.append((name, 'add', add_time))
        results.append((name, 'mul', mul_time))

    # write CSV
    csv_file = 'benchmark.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Representation', 'Operation', 'Time'])
        writer.writerows(results)
    print(f"CSV written to {csv_file}")

    # plot
    for op in ('add', 'mul'):
        names = [r for r, o, _ in results if o == op]
        times = [t for _, o, t in results if o == op]
        plt.figure()
        plt.bar(names, times)
        plt.title(f"Benchmark: {op}")
        plt.xlabel('Representation')
        plt.ylabel('Time (s)')
        plt.tight_layout()
        img = f"{op}.png"
        plt.savefig(img)
        print(f"Plot saved to {img}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark complex arithmetic representations")
    parser.add_argument('--reps', type=int, default=10000, help='Number of random ops')
    args = parser.parse_args()
    run_benchmark(args.reps)
