package main

import "fmt"

func main(){
	a := 10
	b := &a
	array := [3]int{1, 2, 3}
	dict := make( map[string]int )
	dict["age"] = 123
	fmt.Println(array)
	fmt.Println(dict["age"])
	fmt.Println(*b)
}