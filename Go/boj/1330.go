package main

import "fmt"

func main() {
	var i1, i2 int
	fmt.Scan(&i1, &i2)
	if i1 > i2 {
		fmt.Println(">")
	} else if i1 < i2 {
		fmt.Println("<")
	} else if i1 == i2 {
		fmt.Println("==")
	}
}