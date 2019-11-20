def resta(kostos, poso):
	nomismata = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100, 200, 500]
	diafora = float(poso) - float(kostos)
	if diafora < 0:
		print("Το ποσό δεν επαρκεί")
		return []


	if diafora == 0:
		print("Δεν δίνουμε ρέστα")
		return []


	resta = []
	nomismata.sort(reverse=True)

	for nomisma in nomismata:
		while diafora >= nomisma:
			resta.append(nomisma)
			diafora -= nomisma
		if diafora == 0:
			break
	return resta

def human_friendly(nomismata):
	resta_human = {}
	for nomisma in nomismata:
		if nomisma in resta_human:
			resta_human[nomisma] +=1
		else:
			resta_human[nomisma] =1
	return resta_human

def main():
	kostos = input("Πόσο κοστίζει η υπηρεσία ή το είδος που πουλάμε; ")
	poso = input("Τι ποσό μας έδωσε ο πελάτης; ")
	nomismata = resta(kostos, poso)
	print('-'*80)
	print("Νομίσματα που πρέπει να επιστέψουμε: ")
	for nomisma in nomismata:
		print(nomisma)

if __name__=="__main__":
	main()
