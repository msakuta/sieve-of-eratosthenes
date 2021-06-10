fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() <= 2 {
        println!(
            "Please enter one or more arguments, an integer limit \
            to the size of the primes generated."
        );
        return;
    }

    let smart = args.iter().any(|arg| arg == "-s");
    let quiet = args.iter().any(|arg| arg == "-q");

    let n: usize = args.iter().fold(None, |n, arg|
        if n.is_none() {
            arg.parse::<usize>().ok()
        } else {
            n
        }).expect("No valid unsigned integer argument found");

    if n < 2 {
        println!("The integer limit must be greater than or equal to two.")
    }

    if smart {
        smart_primes(n, quiet);
    } else {
        dumb_primes(n, quiet);
    }
}

fn dumb_primes(n: usize, quiet: bool) {
    let mut primes: Vec<usize> = Vec::new();

    for i in 2..=n {
        primes.push(i);
    }

    for i in 0..primes.len() {
        let factor = primes[i];
        if factor != 0 {
            sieve(&mut primes, factor);
        }
    }

    for i in 0..primes.len() {
        if primes[i] != 0 {
            if !quiet {
                println!("{}", primes[i])
            }
        }
    }
}

fn smart_primes(n: usize, quiet: bool) {
    let mut primes = vec![true; n];

    for factor in 2..n {
        if primes[factor] {
            let mut multiple = 2;
            while factor * multiple < n {
                primes[factor * multiple] = false;
                multiple += 1;
            }
        }
    }

    for (i, b) in primes.iter().enumerate() {
        if *b {
            if !quiet {
                println!("{}", i);
            }
        }
    }
}

fn sieve(primes: &mut Vec<usize>, factor: usize) {
    for i in 0..primes.len() {
        let value = primes[i];
        if value != 0 && value != factor {
            if value % factor == 0 {
                primes[i] = 0;
            }
        }
    }
}
