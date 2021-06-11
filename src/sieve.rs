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
    let smart2 = args.iter().any(|arg| arg == "-s2");
    let quiet = args.iter().any(|arg| arg == "-q");

    let n: usize = args
        .iter()
        .fold(None, |n, arg| {
            if n.is_none() {
                arg.parse::<usize>().ok()
            } else {
                n
            }
        })
        .expect("No valid unsigned integer argument found");

    if n < 2 {
        println!("The integer limit must be greater than or equal to two.")
    }

    let primes = if smart2 {
        smart_primes2(n)
    } else if smart {
        smart_primes(n)
    } else {
        dumb_primes(n)
    };

    if !quiet {
        for prime in primes {
            println!("{}", prime);
        }
    }
}

fn dumb_primes(n: usize) -> Vec<usize> {
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

    primes
        .iter()
        .filter_map(|b| if *b != 0 { Some(*b) } else { None })
        .collect()
}

fn smart_primes(n: usize) -> Vec<usize> {
    let mut primes = vec![true; n];
    primes[0] = false;
    primes[1] = false;

    for factor in 2..n {
        if primes[factor] {
            let mut multiple = 2;
            while factor * multiple < n {
                primes[factor * multiple] = false;
                multiple += 1;
            }
        }
    }

    primes
        .iter()
        .enumerate()
        .filter_map(|(i, b)| if *b { Some(i) } else { None })
        .collect()
}

fn smart_primes2(n: usize) -> Vec<usize> {
    let mut primes = vec![true; n];
    primes[0] = false;
    primes[1] = false;

    for factor in 2..(n as f64).sqrt() as usize {
        if primes[factor] {
            let mut multiple = 2;
            while factor * multiple < n {
                primes[factor * multiple] = false;
                multiple += 1;
            }
        }
    }

    primes
        .iter()
        .enumerate()
        .filter_map(|(i, b)| if *b { Some(i) } else { None })
        .collect()
}


#[test]
fn test_sieves() {
    assert_eq!(dumb_primes(10000), smart_primes(10000));
}

#[test]
fn test_sieves2() {
    assert_eq!(dumb_primes(10000), smart_primes2(10000));
}
