import csv
import math
import os
import subprocess
import time

extension = ".exe" if os.name == "nt" else ""

IMPLEMENTATIONS = [
    # "python sieve.py",
    ["bin\\sieve" + extension, "-q"],
    ["bin\\sieve" + extension, "-s", "-q"],
    ["bin\\sieve-rs" + extension, "-q"],
    ["bin\\sieve-rs" + extension, "-s", "-q"],
]

MIN = int(os.getenv("MIN", 10000))
MAX = int(os.getenv("MAX", 1000000))

def x_axis():
    min_exp = int(math.log10(MIN))
    max_exp = int(math.log10(MAX))
    yield MIN
    for exp in range(min_exp, max_exp + 1):
        pow = 10 ** exp
        for i in range(1, 10):
            x = i * pow
            if x > MIN and x < MAX:
                yield x
    if MAX > MIN:
        yield MAX

def to_float_seconds(s):
    if ":" in s:
        parts = s.split(':')
        if len(parts) == 2:
            [mins, secs] = parts
            return int(mins) * 60 + float(secs)
        else:
            [hours, mins, secs] = parts
            return int(hours) * 3600 + int(mins) * 60 + float(secs)
    else:
        return float(s)

def run(cmd):
    # print(cmd)
    start = time.time()
    result = subprocess.run(
        cmd,
        # shell=True,
        # executable="bin/sieve-rs.exe",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE
    )
    total = time.time() - start
    # stderr = result.stderr.decode()
    # output = stderr[len(cmd):]
    # a = output.split()
    # user = to_float_seconds(a[0][:-1])
    # system = to_float_seconds(a[2][:-1])
    # cpu = int(a[4][:-1])
    # total = to_float_seconds(a[6])
    # print(user, system, cpu, total)
    print(f"{cmd}: {total}")
    return total

def bench(implementation, x):
    cmd = implementation + [str(x)]
    return run(cmd)

def run_x(x):
    return [x] + list(map(lambda implementation: bench(implementation, x), IMPLEMENTATIONS))

def run_benchmarks():
    return list(map(run_x, x_axis()))

def main():
    data = run_benchmarks()
    with open('testing/timing_data.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["n", "Go dumb", "Go smart", "Rust dumb", "Rust smart"])
        for row in data:
            writer.writerow(row)
    with open('testing/timing_data_smart.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["n", "Go smart", "Rust smart"])
        for row in data:
            writer.writerow([num for i, num in enumerate(row) if i == 0 or "-s" in IMPLEMENTATIONS[i - 1]])

if __name__ == "__main__":
    main()
