# How Fast is Golang? | Sieve of Eratosthenes

See [this](dumb_and_smart_analysis.md) for the analysis on improvements made in this fork.

This repository houses some code used to demonstrate the speed improvement of Rust over Golang, as featured in [this Medium article](https://medium.com/@alistairisrael/how-fast-is-rust-655f6dd90ff8).

![Rust vs Go Linear Plot](img/rust_vs_go_smart_linear.png?raw=true "Rust vs Go Linear Plot")

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Showing you how to install Python or Go is out of scope of this project - you can find some great tutorials on their respective websites. The standard library of both languages should suffice. Note to run the tests in the jupyter notebook you will need jupyter, pandas and plotly installed.

### Installing

```
# Clone this repository
git clone https://github.com/aisrael/sieve-of-eratosthenes.git
cd sieve-of-eratosthenes
# Build the go executable
go build -o bin/sieve sieve.go
# Build the Rust executable in 'release' profile
rustc -C debuginfo=0 -C opt-level=3 src/sieve.rs -o bin/sieve-rs
```

The `rustc` flags build the Rust executable as if we had used Cargo and ran `cargo --release`. Without them, Rust will compile with debug information and without optimisations by default, which results in an implementation that's slower than Go.

### Running

Each one of `sieve.rs`, `sieve.go`, and `sieve.py` find the primes below n where n is the first command line argument. To run each individually (assuming you've followed the installation steps above) run:

```
# Go
bin/sieve [n]
# Python
python3 sieve.py [n]
# Rust
bin/sieve-rs [n]
```

In the [testing](testing) folder there is a jupyter notebook and a csv of data. These allow you to reproduce the tests conducted to demonstrate Go's speed (and have some pretty graphs).

#### Running the benchmarking script

Alternatively, you can run

```
python bench.py
```

To run each of the implementations with a configurable range using the `MIN` and `MAX` environment variables. The script itself computes the 'steps' for _x_ axis values using the base power of 10, multiplied by 1..9:

```
MIN=100 MAX=10000 python bench.py
```

Will run the benchmarks for 100, 200, ..., 800, 900, 1000, 2000, ..., 8000, 9000, then 10000 primes.

The output is then written to `testing/timing_data.csv` suitable for display in Jupyter notebook.

## Contributing

This is/was a small project to prove a point. I won't be accepting changes unless I've done something very silly on the speed side and I get a load of PRs! :)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
