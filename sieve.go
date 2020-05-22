package main

import (
	"os"
	"fmt"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Please enter exactly one argument, an integer limit",
					"to the size of the primes generated.")
		return
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	if n < 2 {
		fmt.Println("The integer limit must be greater than or equal to two.")
	}

	var primes []int

	for i := 2; i <= n; i++ {
		primes = append(primes, i)
	}

	for i := 0; i < len(primes); i++ {
		if primes[i] != 0 {
			sieve(primes, primes[i])
		}
	}

	for i := 0; i < len(primes); i++ {
		if primes[i] != 0 {
			fmt.Println(primes[i])
		}
	}
}

func sieve(primes []int, factor int) {
	for index, value := range(primes) {
		if value != 0 && value != factor {
			if value % factor == 0 {
				primes[index] = 0
			}
		}
	}
}
