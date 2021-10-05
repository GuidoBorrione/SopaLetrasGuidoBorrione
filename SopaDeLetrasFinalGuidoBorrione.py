import time
def mostrar_menu():
	print('''
						@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
						+												+
						+												+
						+		Bienvenidos a mi Sopa de Letras			+
						+												+
						+												+
						@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		''')
mostrar_menu()


def temas():
	print ("""
		[1] Elejir juego al que desea jugar

		[2] Salir de la Sopa de Letras
			""")
	opcion = input("Ingresa una opción: ->  ")
			 
	if opcion != "1" and opcion != "2":
		print ("Opcion incorrecta, Ingrese una opcion valida")
		opcion = input("Ingresa una opción: ->  ")
		temas()
	elif opcion == "1":
		print("""


	
																				▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
																				▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
																				▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
																				▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
																				▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
																				▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
						@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@			▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
						+											+			▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
						+											+			▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
						+			Que Comienze el juego			+			▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
						+											+			▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒				
						+											+			▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
						@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@			▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
																				████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒





					  	[A] Buscar Verbos
						[B] Buscar Sustantivos
					 	[C] Buscar Adjetivos
						""")
		op = input("Ingrese a que Juego quieres Jugar: ->  ")
		if op == "A":
			def dificultad_Verbos():
				print("""
					NIVEL DE DIFICULTAD
					    [1] Facil
					    [2] Intermedio
					    [3] Dicifil
					  """)
				op= input("INDIQUE EL NIVEL DE DIFICULTAD ->  ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("INDIQUE EL NIVEL DE DIFICULTAD -->>>  ")
				print("")
				print("Los Verbos que tienes que encontrar a continuacion son 12 ")
				print("")		
				input("Presione Enter para iniciar el juego")



				if op == "1":
					print("""
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++					   ███████████████████████████
			     +  r  o  m  p  e  r  e  x  p  u  l  s  a  r  v  t  +					   ███████▀▀▀░░░░░░░▀▀▀███████						
				 +	s  p  r  i  s  a  e  t  a  r  o  a  j  q  d  r  +					   ████▀░░░░░░░░░░░░░░░░░▀████
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +					   ███│░░░░░░░░░░░░░░░░░░░│███
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  x  +					   ██▌│░░░░░░░░░░░░░░░░░░░│▐██
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +					   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +					   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +					   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
				 +	r  o  r  r  e  r  o  t  a  ñ  c  r  i  z  w  b  +					   ██▌░│██████▌░░░▐██████│░▐██
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +					   ███░│▐███▀▀░░▄░░▀▀███▌│░███	   
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  m  +					   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +					   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
				 +	m  o  v  e  r  p  e  r  d  e  r  o  q  e  z  h  +					   ████▄─┘██▌░░░░░░░▐██└─▄████
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++					   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████			
																						   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████						
																						   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████						
																						   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████	
																						   ███████▄░░░░░░░░░░░▄███████
																						   ██████████▄▄▄▄▄▄▄██████████		
																					       ███████████████████████████
				""")

					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el verbo que encontro:  ")
						if preg == "romper":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "reir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "caminar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "hablar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "pintar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "ganar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "rayar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "mover":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "expulsar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "perder":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "abrir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)

				elif op == "2":
					print("""
				

				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  r  o  m  p  e  r  e  x  p  u  l  s  a  r  v  t  +				
			 	 +	s  p  r  i  s  a  e  t  a  r  o  a  j  q  d  r  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  x  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +
				 +	r  o  r  r  e  r  o  t  a  ñ  c  r  i  z  w  b  +
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  m  +
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +
				 +	m  o  v  e  r  p  e  r  d  e  r  o  q  e  z  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
																				´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
																				´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
																				´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
																				´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
																				´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
																				´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
																				´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
																				´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
																				¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
																				¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
																				´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
																				´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
																				´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
																				´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
																				´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
																				´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
																				´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
																				´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´




				""")

																								
					while True:
						preg = input("Ingrese el verbo que encontro:  ")
						if preg == "romper":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "reir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "caminar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "hablar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "pintar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "ganar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "rayar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "mover":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "expulsar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "perder":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "abrir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 150:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)


				elif op == "3":
					print("""
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  r  o  m  p  e  r  e  x  p  u  l  s  a  r  v  t  +
			 	 +	s  p  r  i  s  a  e  t  a  r  o  a  j  q  d  r  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  x  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +
				 +	r  o  r  r  e  r  o  t  a  ñ  c  r  i  z  w  b  +
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  m  +
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +
				 +	m  o  v  e  r  p  e  r  d  e  r  o  q  e  z  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
																				      █████████████████████
																				    ████▀─────────────────▀████
																				  ███▀───────────────────────▀███
																				 ██▀───────────────────────────▀██
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█───█████─────────────────█████───█
																				█──██▓▓▓███─────────────███▓▓▓██──█
																				█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
																				█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
																				█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
																				▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
																				  █▄────▀█████▀─────▀█████▀────▄█
																				 ▄██───────────▄█─█▄───────────██▄
																				 ███───────────██─██───────────███
																				 ███───────────────────────────███
																				▀██──██▀██──█──█──█──██▀██──██▀
																				───▀████▀─██──█──█──█──██─▀████▀
																				────▀██▀──██──█──█──█──██──▀██▀
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				           █▄▄█▄▄█▄▄█▄▄█
				
				""")
					inicio = time.time()
					aciertos= 0
					while True:
						preg = input("Ingrese el verbo que encontro:  ")
						if preg == "romper":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "reir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "correr":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "caminar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "hablar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "pintar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "ganar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "rayar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "mover":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "expulsar":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "perder":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						elif preg == "abrir":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Sigue así, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Verbos encontrados fueron", aciertos)

			dificultad_Verbos()
			
		elif op == "B":
			def dificultad_Sustantivos():
				print("""
					NIVEL DE DIFICULTAD
					    [1] Facil
					    [2] Intermedio
					    [3] Dicifil
					  """)
				op= input("INDIQUE EL NIVEL DE DIFICULTAD ->  ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("INDIQUE EL NIVEL DE DIFICULTAD -->>>  ")
				print("")
				print("Los Sustantivos que tienes que encontrar a continuacion son 12 ")
				print("")		
				input("Presione Enter para iniciar el juego")
				


				if op == "1":
					print("""

                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  r  b  o  l  r  e  x  p  u  l  p  e  r  r  o  +
			 	 +	c  o  m  p  u  t  a  d  o  r  a  a  j  q  d  b  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  i  +
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  c  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  i  +
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +
				 +	a  t  a  e  c  o  r  o  n  a  m  a  m  f  q  l  +
				 +	h  o  j  a  e  r  o  b  a  ñ  o  r  i  z  w  e  +
				 +	g  p  e  l  o  t  a  c  l  a  d  o  n  x  e  t  +
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  a  +
				 +	r  n  i  p  u  e  r  t  a  z  a  b  r  i  r  j  +
				 +	m  o  v  e  r  p  e  r  d  e  s  i  l  l  a  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++				
				 																		   ███████████████████████████
			    																		   ███████▀▀▀░░░░░░░▀▀▀███████						
				 																		   ████▀░░░░░░░░░░░░░░░░░▀████
				 																		   ███│░░░░░░░░░░░░░░░░░░░│███
				 																		   ██▌│░░░░░░░░░░░░░░░░░░░│▐██
				 																		   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
				 																		   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
				 																		   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
				 																		   ██▌░│██████▌░░░▐██████│░▐██
				 																		   ███░│▐███▀▀░░▄░░▀▀███▌│░███	   
				 																		   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
				 																		   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
				 																		   ████▄─┘██▌░░░░░░░▐██└─▄████
				 																		   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████			
																						   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████						
																						   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████						
																						   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████	
																						   ███████▄░░░░░░░░░░░▄███████
																						   ██████████▄▄▄▄▄▄▄██████████		
																					       ███████████████████████████
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontro:  ")
						if preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "computadora":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "niño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "baño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "puerta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "teclado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "hoja":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corona":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "perro":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "bicicleta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)

				elif op == "2":
					print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  r  b  o  l  r  e  x  p  u  l  p  e  r  r  o  +
			 	 +	c  o  m  p  u  t  a  d  o  r  a  a  j  q  d  b  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  i  +
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  c  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  i  +
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +
				 +	a  t  a  e  c  o  r  o  n  a  m  a  m  f  q  l  +
				 +	h  o  j  a  e  r  o  b  a  ñ  o  r  i  z  w  e  +
				 +	g  p  e  l  o  t  a  c  l  a  d  o  n  x  e  t  +
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  a  +
				 +	r  n  i  p  u  e  r  t  a  z  a  b  r  i  r  j  +
				 +	m  o  v  e  r  p  e  r  d  e  s  i  l  l  a  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
				
																				´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
																				´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
																				´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
																				´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
																				´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
																				´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
																				´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
																				´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
																				¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
																				¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
																				´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
																				´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
																				´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
																				´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
																				´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
																				´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
																				´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
																				´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontro:  ")
						if preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "computadora":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "niño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "baño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "puerta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "teclado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "hoja":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corona":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "perro":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "bicicleta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 150:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)


				elif op == "3":
					print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  r  b  o  l  r  e  x  p  u  l  p  e  r  r  o  +
			 	 +	c  o  m  p  u  t  a  d  o  r  a  a  j  q  d  b  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  i  +
				 +	i  e  a  c  j  u  r  m  o  l  i  a  x  w  j  c  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  i  +
				 +	t  b  l  m  x  c  z  r  r  d  q  l  a  h  k  c  +
				 +	a  t  a  e  c  o  r  o  n  a  m  a  m  f  q  l  +
				 +	h  o  j  a  e  r  o  b  a  ñ  o  r  i  z  w  e  +
				 +	g  p  e  l  o  t  a  c  l  a  d  o  n  x  e  t  +
				 +  o  a  r  o  c  a  n  t  a  r  z  u  a  s  t  a  +
				 +	r  n  i  p  u  e  r  t  a  z  a  b  r  i  r  j  +
				 +	m  o  v  e  r  p  e  r  d  e  s  i  l  l  a  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
				
																   				      █████████████████████
																				    ████▀─────────────────▀████
																				  ███▀───────────────────────▀███
																				 ██▀───────────────────────────▀██
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█───█████─────────────────█████───█
																				█──██▓▓▓███─────────────███▓▓▓██──█
																				█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
																				█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
																				█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
																				▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
																				  █▄────▀█████▀─────▀█████▀────▄█
																				 ▄██───────────▄█─█▄───────────██▄
																				 ███───────────██─██───────────███
																				 ███───────────────────────────███
																				▀██──██▀██──█──█──█──██▀██──██▀
																				───▀████▀─██──█──█──█──██─▀████▀
																				────▀██▀──██──█──█──█──██──▀██▀
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				           █▄▄█▄▄█▄▄█▄▄█
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Sustantivo que encontro:  ")
						if preg == "pelota":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "computadora":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "niño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "baño":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "silla":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "puerta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "teclado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "hoja":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corona":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "perro":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "bicicleta":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "arbol":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Sustantivos encontrados fueron", aciertos)


			dificultad_Sustantivos()
			
		elif op == "C":
			def dificultad_Adjetivos():
				print("""
					NIVEL DE DIFICULTAD
					    [1] Facil
					    [2] Intermedio
					    [3] Dicifil
					  """)
				op= input("INDIQUE EL NIVEL DE DIFICULTAD ->  ")

				if op != "1" and op != "2" and op != "3":
						print ("Opcion incorrecta, Ingrese una opcion valida")
						op= input("INDIQUE EL NIVEL DE DIFICULTAD -->>>  ")
				print("")
				print("Los Adjetivos que tienes que encontrar a continuacion son 12 ")
				print("")		
				input("Presione Enter para iniciar el juego")
				
				
				if op == "1":
					print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  l  t  o  e  r  o  j  o  u  l  s  a  r  v  t  +
			 	 +	s  c  o  r  t  o  e  t  a  r  d  e  b  i  l  r  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +
				 +	g  r  a  n  d  e  r  m  f  i  n  o  x  w  j  x  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +
				 +	t  a  z  u  l  c  z  m  o  r  a  d  o  h  k  c  +
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +
				 +	r  o  j  o  v  e  n  t  a  s  u  s  t  a  d  o  +
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +
				 +  o  a  r  o  c  a  l  i  e  n  t  e  a  s  t  m  +
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +
				 +	m  o  v  e  d  i  v  e  r  t  i  d  o  u  z  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
								 														   ███████████████████████████
			    																		   ███████▀▀▀░░░░░░░▀▀▀███████						
				 																		   ████▀░░░░░░░░░░░░░░░░░▀████
				 																		   ███│░░░░░░░░░░░░░░░░░░░│███
				 																		   ██▌│░░░░░░░░░░░░░░░░░░░│▐██
				 																		   ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
				 																		   ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
				 																		   ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
				 																		   ██▌░│██████▌░░░▐██████│░▐██
				 																		   ███░│▐███▀▀░░▄░░▀▀███▌│░███	   
				 																		   ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
				 																		   ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
				 																		   ████▄─┘██▌░░░░░░░▐██└─▄████
				 																		   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████			
																						   █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████						
																						   ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████						
																						   █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████	
																						   ███████▄░░░░░░░░░░░▄███████
																						   ██████████▄▄▄▄▄▄▄██████████		
																					       ███████████████████████████
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "rojo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "debil":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "azul":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "morado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "joven":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "asustado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "caliente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "divertido":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 200:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)

				elif op == "2":
					print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  l  t  o  e  r  o  j  o  u  l  s  a  r  v  t  +
			 	 +	s  c  o  r  t  o  e  t  a  r  d  e  b  i  l  r  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +
				 +	g  r  a  n  d  e  r  m  f  i  n  o  x  w  j  x  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +
				 +	t  a  z  u  l  c  z  m  o  r  a  d  o  h  k  c  +
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +
				 +	r  o  j  o  v  e  n  t  a  s  u  s  t  a  d  o  +
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +
				 +  o  a  r  o  c  a  l  i  e  n  t  e  a  s  t  m  +
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +
				 +	m  o  v  e  d  i  v  e  r  t  i  d  o  u  z  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++				
																				´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
																				´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
																				´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
																				´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
																				´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
																				´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
																				´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
																				´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
																				´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
																				´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
																				¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
																				¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
																				´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
																				´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
																				´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
																				´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
																				´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
																				´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
																				´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
																				´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
																				´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
																				´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
																				´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "rojo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "debil":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "azul":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "morado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "joven":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "asustado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "caliente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "divertido":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 150:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)


				elif op == "3":
					print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++
			     +  a  l  t  o  e  r  o  j  o  u  l  s  a  r  v  t  +
			 	 +	s  c  o  r  t  o  e  t  a  r  d  e  b  i  l  r  +
				 +	p  a  h  k  v  b  i  i  l  a  r  h  z  e  f  a  +
				 +	g  r  a  n  d  e  r  m  f  i  n  o  x  w  j  x  +
				 +	n  r  b  o  k  s  c  o  r  r  e  r  c  g  l  v  +
				 +	t  a  z  u  l  c  z  m  o  r  a  d  o  h  k  c  +
				 +	a  t  a  e  n  a  r  o  n  i  m  a  m  f  q  h  +
				 +	r  o  j  o  v  e  n  t  a  s  u  s  t  a  d  o  +
				 +	g  a  n  a  r  a  r  x  d  q  v  y  n  x  e  n  +
				 +  o  a  r  o  c  a  l  i  e  n  t  e  a  s  t  m  +
				 +	r  a  y  a  r  o  l  a  r  z  a  b  r  i  r  j  +
				 +	m  o  v  e  d  i  v  e  r  t  i  d  o  u  z  h  +
				 ++++++++++++++++++++++++++++++++++++++++++++++++++++
																   				      █████████████████████
																				    ████▀─────────────────▀████
																				  ███▀───────────────────────▀███
																				 ██▀───────────────────────────▀██
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█─────────────────────────────────█
																				█───█████─────────────────█████───█
																				█──██▓▓▓███─────────────███▓▓▓██──█
																				█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
																				█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
																				█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
																				▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
																				  █▄────▀█████▀─────▀█████▀────▄█
																				 ▄██───────────▄█─█▄───────────██▄
																				 ███───────────██─██───────────███
																				 ███───────────────────────────███
																				▀██──██▀██──█──█──█──██▀██──██▀
																				───▀████▀─██──█──█──█──██─▀████▀
																				────▀██▀──██──█──█──█──██──▀██▀
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				          ██──█──█──█──██
																				           █▄▄█▄▄█▄▄█▄▄█

				""")
					inicio = time.time()
					aciertos = 0
					while True:
						preg = input("Ingrese el Adjetivo que encontro:  ")
						if preg == "alto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "rojo":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "debil":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "corto":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "grande":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "fino":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "azul":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "morado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "joven":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "asustado":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "caliente":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						elif preg == "divertido":
							aciertos += 1
							print("Ya tienes", aciertos, "aciertos")
							print("Muy Bien!!!!!, continua buscando...")
						else:
							print("La palabra no se encuentra en la sopa de letras, sigue intentando...")
						
						final = time.time()

						if final - inicio >= 100:
							print("")
							print("Se termino el timepo")
							break
					print("")
					print("Los Adjetivos encontrados fueron", aciertos)


			dificultad_Adjetivos()
		
		temas()	
		while op != "A" and op != "B" and op != "C":
			print ("Opcion incorrecta, ingrese una opcion valida")
			op = input("Ingrese una opción: ->  ")


	elif  opcion == "2":
		print("Saliste de la Sopa de Letras")
		print("Intentalo Pronto!!!!")
					
		exit()

temas()
