package main

func Coprime(a, b int) bool {
	if gcd(a, b) == 1 {
		return true
	}

	return false
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

func main() {
	print(Coprime(30, 1))
}
