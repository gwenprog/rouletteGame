def caseChoisie():
	case = insert(int, "Sur quelle case jouez-vous ?")
	while True:
		if case < 0 or case > 50 :
			print("Nombre invalide")
			break
		else:
			return case	
	
def chiffrePairOuImpair(chiffre):
		if chiffre % 2 == 0:
			affichage = " pair"
		else:
			affichage = " impair"

		return affichage
def continuer():
	continuer = input("souhaitez vous continuer ? Oui / Non:")
	if continuer == "oui" or continuer == "Oui":
		return True
	else:
		return False
def walletEmpty(wallet):
	if wallet <= 0:
		return True
	else:
		return False
def parisMoreThanWallet(wallet, paris):
	if paris > wallet:
		print("Vous ne pouvez pas parier plus que votre portefeuille")
		return True
	else:
		return False
def insert(type, sentence):
	while True:
		try:
			value = type(input(sentence))
			break
		except ValueError:
			print("le nombre saisie n'est pas correct")

	return value