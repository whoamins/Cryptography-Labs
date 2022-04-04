package main

func main() {
	number := 17
	print(isPrime(number))
}

func isPrime(number int) bool {
	if number > 1 {
		for i := 2; i < number; i++ {
			if (number % i) == 0 {
				// print(number, " is not a prime number")
				return false
			}
		}
		return true
	}

	return false
}
