package main

import (
	"fmt"
	"time"
)


var nom, prenom string
var age int
var datenaissance string

func main() {
	getnameandAge()
	fmt.Println("Bonjour", nom, prenom, "Vous avez", age, "ans")

	getanneenaissance()
	fmt.Println("vous êtes né en cette date", datenaissance)
}


func getnameandAge() {
	fmt.Println("entrez votre nom :")
	fmt.Scanln(&nom)
	fmt.Println("entrez votre prenom :")
	fmt.Scanln(&prenom)
	fmt.Println("entrez votre age :")
	fmt.Scanln(&age)
}

func getanneenaissance() {
	fmt.Print("Entrez votre date de naissance (format: YYYY-MM-DD) : ")
	fmt.Scanln(&datenaissance)

	// Convertir la chaîne en objet de type time.Time
	dateNaissance, err := time.Parse("2006-01-02", datenaissance)
	if err != nil {
		fmt.Println("Erreur de format de date :", err)
		return
}
	fmt.Println("Votre date de naissance est :", dateNaissance.Format("2 janvier 2006"))
}