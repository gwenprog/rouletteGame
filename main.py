# coding: utf-8
import random
from components import *
import time

wallet = 0
#Démarage du jeux
def main_loop():
	
	global wallet
	#Boucle de jeux			
	while True:
		print()
		if wallet == 0:
			wallet = insert(float, "Quel est le montant de votre portefeuille ?")
		else:
			time.sleep(0.5)	
			paris = insert(float,"Combien voulez vous parier ?")
			time.sleep(0.5) 
			if parisMoreThanWallet(wallet, paris):
				continue
			else:
				while True:
					case_choisie = caseChoisie()
					#Mise à jour du portefeuille
					wallet -= paris
					wallet = float(wallet)
							
					#tirage de la roulette
					nb = random.randint(0, 50)
					time.sleep(0.5)
					print("La roulette tourne... \n Le nombre tiré est le:  {} !".format(nb))
							
					#Si le portefeuille est à zéro
					if walletEmpty(wallet) == True: 
						print("Vous avez perdu tout votre argent. Vous ne pouvez plus jouer")
						quit()
					#Sinon, continuer le programme
					else:
						#Verifier si case_choisie == chiffre aléatoire
						if case_choisie == nb:
							print("Vous avez trouvé le bon chiffre, votre paris est multiplié par 3")
							paris = wallet + paris*3
							wallet = paris
							print("Votre portefeuille contient: {}€".format(wallet))

							if continuer() == False:
									print("Vous repartez avec: {}€ Féliciation !".format(wallet))
									quit()
							else:
								print("Votre portefeuille contient: {}€".format(wallet))
								main_loop()

						#Si ils ne sont pas égaux	
						else:
						#Verif couleur == case choisie
							if chiffrePairOuImpair(case_choisie) == chiffrePairOuImpair(nb):
								paris = paris * 1.5
								wallet += paris
								float(wallet)
								print("Vous n'avez pas trouvé le bon chiffre mais le bon type de case, votre paris est donc multiplié par 1.5. Votre portefeuille contient {}€".format(wallet))
										
										
								#On demande au joueur s'il veut continuer	
								if continuer() == False:
									print("Vous repartez avec: {}€ Féliciation !".format(wallet))
									quit()
								else:
									print("Votre portefeuille contient: {}€".format(wallet))
									main_loop()
							else: 
								wallet - paris
								print("Vous avez perdu...")
								if walletEmpty(wallet) == True: 
									print("Vous n'avez plus d'argent")
									quit()
								else:
									print("Il vous reste {}€".format(wallet))
									if continuer() == False:
										print("Vous repartez avec: {}€ Féliciation !".format(wallet))
										quit()
									else:
										continue


								#print("Portefeuille: {}".format(wallet))		
				
											
				
if __name__ == '__main__':
	
    main_loop()
