import csv
import math
import os
import subprocess
import time

extension = ".exe" if os.name == "nt" else ""

IMPLEMENTATIONS = [
    # "python sieve.py",
    {"title": "Go dumb", "cmd": ["bin/sieve" + extension, "-q"]},
    {"title": "Go smart", "cmd": ["bin/sieve" + extension, "-s", "-q"]},
    {"title": "Go smart2", "cmd": ["bin/sieve" + extension, "-s2", "-q"]},
    {"title": "Go smart3", "cmd": ["bin/sieve" + extension, "-s3", "-q"]},
    {"title": "Rust dumb", "cmd": ["bin/sieve-rs" + extension, "-q"]},
    {"title": "Rust smart", "cmd": ["bin/sieve-rs" + extension, "-s", "-q"]},
    {"title": "Rust smart2", "cmd": ["bin/sieve-rs" + extension, "-s2", "-q"]},
    {"title": "Rust smart3", "cmd": ["bin/sieve-rs" + extension, "-s3", "-q"]},
]

MIN = int(os.getenv("MIN", 10000))
MAX = int(os.getenv("MAX", 1000000))
SMART_ONLY = int(os.getenv("SMART_ONLY", "1")) != 0

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

def run_x(x, fil):
    return [x] + list(map(lambda implementation: bench(implementation["cmd"], x), filter(fil, IMPLEMENTATIONS)))

def run_benchmarks(fil):
    return list(map(lambda x: run_x(x, fil), x_axis()))

def main():
    if SMART_ONLY:
        fil = lambda x: 0 <= x["title"].find("smart")
    else:
        fil = lambda x: True
    data = run_benchmarks(fil)
    with open(f'testing/timing_data{"_smart" if SMART_ONLY else ""}.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["n"] + [entry["title"] for entry in IMPLEMENTATIONS if fil(entry)])
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()
