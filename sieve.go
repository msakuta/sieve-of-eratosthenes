package main

import (
	"fmt"
	"os"
	"strconv"
	"math"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please enter one or more arguments, an integer limit",
			"to the size of the primes generated.")
		return
	}

	smart := false
	smart2 := false
	smart3 := false
	quiet := false
	n := 0

	for i := 1; i < len(os.Args); i++ {
		if os.Args[i] == "-s" {
			smart = true
			continue
		}
		if os.Args[i] == "-s2" {
			smart2 = true
			continue
		}
		if os.Args[i] == "-s3" {
			smart3 = true
			continue
		}
		if os.Args[i] == "-q" {
			quiet = true
			continue
		}
		nTemp, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		n = nTemp
	}

	if n < 2 {
		fmt.Println("The integer limit must be greater than or equal to two.")
		os.Exit(2)
	}

	if smart3 {
		smart_primes3(n, quiet)
	} else if smart2 {
		smart_primes2(n, quiet)
	} else if smart {
		smart_primes(n, quiet)
	} else {
		dumb_primes(n, quiet)
	}
}

func dumb_primes(n int, quiet bool) {
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
			if !quiet {
				fmt.Println(primes[i])
			}
		}
	}
}

func smart_primes(n int, quiet bool) {
	primes := make([]bool, n)

	for i := 0; i < n; i++ {
		primes[i] = true
	}

	for factor := 2; factor < n; factor++ {
		if primes[factor] {
			var multiple = 2
			for factor*multiple < n {
				primes[factor*multiple] = false
				multiple += 1
			}
		}
	}

	for i := 0; i < len(primes); i++ {
		if primes[i] {
			if !quiet {
				fmt.Println(i)
			}
		}
	}
}

func smart_primes2(n int, quiet bool) {
	primes := make([]bool, n)

	for i := 0; i < n; i++ {
		primes[i] = true
	}

	slimit := int(math.Sqrt(float64(n)))
	for factor := 2; factor < slimit; factor++ {
		if primes[factor] {
			var multiple = 2
			for factor*multiple < n {
				primes[factor*multiple] = false
				multiple += 1
			}
		}
	}

	for i := 0; i < len(primes); i++ {
		if primes[i] {
			if !quiet {
				fmt.Println(i)
			}
		}
	}
}

func smart_primes3(n int, quiet bool) {
	primes := make([]bool, n)

	for i := 0; i < n; i++ {
		primes[i] = true
	}

	slimit := int(math.Sqrt(float64(n)))
	for factor := 2; factor < slimit; factor++ {
		if primes[factor] {
			var multiple = factor
			for factor*multiple < n {
				primes[factor*multiple] = false
				multiple += 1
			}
		}
	}

	for i := 0; i < len(primes); i++ {
		if primes[i] {
			if !quiet {
				fmt.Println(i)
			}
		}
	}
}

func sieve(primes []int, factor int) {
	for index, value := range primes {
		if value != 0 && value != factor {
			if value%factor == 0 {
				primes[index] = 0
			}
		}
	}
}
