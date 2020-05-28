fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() != 2 {
        println!(
            "Please enter exactly one argument, an integer limit \
            to the size of the primes generated."
        );
        return;
    }

    let n: i32 = args[1].parse().unwrap();

    if n < 2 {
        println!("The integer limit must be greater than or equal to two.")
    }

    let mut primes: Vec<i32> = Vec::new();

    for i in 2..=n {
        primes.push(i);
    }

    {
        let mut i = 0;
        while i < primes.len() {
            let factor = primes[i];
            sieve(&mut primes, factor);
            i += 1;
        }
    }

    for i in 0..primes.len() {
        println!("{}", primes[i])
    }
}

fn sieve(primes: &mut Vec<i32>, factor: i32) {
    let mut i = 0;
    while i < primes.len() {
        let value = primes[i];
        if value != factor {
            if value % factor == 0 {
                primes.remove(i);
            }
        }
        i += 1;
    }
}
