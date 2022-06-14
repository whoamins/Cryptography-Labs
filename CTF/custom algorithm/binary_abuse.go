/*
Там каждый второй символ шифровался так:
ascii код символа << 8 и прибавляем к нему ascii код следующего символа (Например, 98 << 8 = 25088 + 121 = 25209), потом с номера строки, который равен полученному число берем слово из словаря и подставляем в шифротекст.

Чтобы расшифровать, получается нам надо сделать обратную операцию: найти слово в словаре, взять его номер, отнять от него число Х, а вот тут стоп, число то мы не знаем, вот тут и начинается абуз.

Мы можем просто выполнить обратную операцию сдвига >>, без прибавления, и мы получим число, к которому прибавляли (25088). На примере, если сдвинуть 25209 >> 8 = 98, а теперь если мы сдвинем 98 << 8, то мы получим 25088!!!! Отсюда получаем следующее: 25209 - 25088 = 121, таким образом мы получаем все числа, которые стоят на четных позициях.

В рамках тест флага byuctf{testflag} это будет y c f t s f a }
А получить нечетные еще легче, мы просто берем номера строк и двигаем их  (25209 >> 8 = 98)
*/

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func readFlag() (string, error) {
	flagFile, err := os.Open("encrypted.txt")
	if err != nil {
		return "", err
	}
	defer flagFile.Close()
	scanner := bufio.NewScanner(flagFile)
	scanner.Scan()
	flag := scanner.Text()
	return flag, nil
}

func combine(flag []uint8) []uint16 {
	combined := []uint16{}
	for i := 0; i < len(flag); i += 2 {
		c := uint16(flag[i]) << 8
		if i+1 < len(flag) {
			c += uint16(flag[i+1])
		}
		combined = append(combined, c)
	}
	return combined
}

func revertCombine(flag []uint16) []uint16 {
	combined := []uint16{}
	for i := 0; i < len(flag); i += 1 {
		c := flag[i] >> 8
		combined = append(combined, c)
	}
	return combined
}

func encrypt(flag string) string {
	codex_file, err := os.Open("CROSSWD.TXT")
	if err != nil {
		return "!"
	}
	defer codex_file.Close()
	all_words := []string{}
	combined := combine([]uint8(flag))
	for _, c := range combined {
		all_words = append(all_words, encodeOne(c, codex_file))
	}
	return strings.Join(all_words, " ")
}

func encodeOne(c uint16, codex_file *os.File) string {
	codex_file.Seek(0, io.SeekStart)
	scanner := bufio.NewScanner(codex_file)
	for i := uint16(0); i < c; i++ {
		scanner.Scan()
	}
	return scanner.Text()
}

func getLineNumber(myString string) (int, error) {
	f, err := os.Open("CROSSWD.txt")

	if err != nil {
		return 0, err
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	line := 1

	for scanner.Scan() {
		if scanner.Text() == myString {
			return line, nil
		}

		line++
	}

	if err := scanner.Err(); err != nil {
	}
	return 0, nil
}

func makeThatShit(flag_data []uint16) ([]uint16, []string) {
	result_flag := revertCombine(flag_data)
	second_flag_part := []string{}

	for i, c := range result_flag {
		c = c << 8
		second_flag_part = append(second_flag_part, string(flag_data[i]-uint16(c)))
	}

	return result_flag, second_flag_part
}

func main() {
	flag, err := readFlag()

	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(encrypt(flag))

	words := strings.Fields(flag)
	fmt.Println(words)
	flag_data := []uint16{}

	for _, c := range words {
		lineNumber, _ := getLineNumber(c)
		flag_data = append(flag_data, uint16(lineNumber))
	}

	fmt.Println(flag_data)
	first, second := makeThatShit(flag_data)

	for i := 0; i < len(first); i++ {
		print(string(first[i]), second[i])
	}
}
