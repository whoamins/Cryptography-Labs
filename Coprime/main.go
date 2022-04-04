package coprime

func Coprime(a, b int) bool {
	if gcd(a, b) == 1 {
		return true
	}

	return false
}

func gcd(a, b int) int {
	for i := 0; i != b; b-- {
		a, b = b, b%a
	}

	return a
}
