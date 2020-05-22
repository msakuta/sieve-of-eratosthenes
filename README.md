# How Fast is Golang? | Sieve of Eratosthenes

This repository houses some code used to demonstrate the speed improvement of Golang over Python, as featured in a Medium article.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Showing you how to install Python or Go is out of scope of this project - you can find some great tutorials on their respective websites. The standard library of both languages should suffice.

### Installing

```
# Clone this repository
git clone https://github.com/8F3E/sieve-of-eratosthenes.git
cd sieve-of-eratosthenes
# Build the go executable
go build -o bin/sieve sieve.go
```

### Running

Both `sieve.go` and `sieve.py` find the primes below n where n is the first command line argument. To run each individually (assuming you've followed the installation steps above) run:

```
# Go
bin/sieve [n]
# Python
python3 sieve.py [n]
```

In the [testing](testing) folder there is a jupyter notebook and a csv of data. These allow you to reproduce the tests conducted to demonstrate Go's speed (and have some pretty graphs).

## Contributing

This is/was a small project to prove a point. I won't be accepting changes unless I've done something very silly on the speed side and I get a load of PRs! :)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
