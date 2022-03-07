package main

import (
	"unicode"
)

func main() {
	square := [5][5]string{
		{"a", "b", "c", "d", "e"},
		{"f", "g", "h", "i/j", "k"},
		{"l", "m", "n", "o", "p"},
		{"q", "r", "s", "t", "u"},
		{"v", "w", "x", "y", "z"},
	}

	encrypted := encrypt2("sometext", square)
	print(encrypted)
}

func encrypt1(message string, square [5][5]string) string {
	result := ""

	for _, char := range message {

		if unicode.IsSpace(char) {
			result += string(char)
			continue
		}

		rowIndex, colIndex := indexOf(string(char), square)

		if colIndex != -1 {
			if rowIndex == 4 {
				result += square[0][colIndex]
				continue
			}

			result += square[rowIndex+1][colIndex]
		}

	}
	return result
}

func encrypt2(message string, square [5][5]string) string {
	var rowIndexes []int
	var colIndexes []int

	for _, char := range message {
		i, j := indexOf(string(char), square)

		if j == -1 {
			continue
		}

		rowIndexes = append(rowIndexes, i)
		colIndexes = append(colIndexes, j)
	}

	var indexes []int

	// use for i := range
	for i := 0; i < len(rowIndexes); i += 1 {
		indexes = append(indexes, colIndexes[i])
	}

	for i := 0; i < len(rowIndexes); i += 1 {
		indexes = append(indexes, rowIndexes[i])
	}

	result := ""

	for i := 0; i < len(indexes)/2; i += 1 {
		if i != len(indexes)-1 {
			result += square[indexes[i+i+1]][indexes[i+i]]
		}
	}

	return result
}

func indexOf(whatIWant string, data [5][5]string) (int, int) {
	for rowIndex, row := range data {
		for colIndex, element := range row {
			if whatIWant == element {
				return rowIndex, colIndex
			}
		}
	}

	return 0, -1
}
