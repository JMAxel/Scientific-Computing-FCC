def arithmetic_arranger(problems, answer = False):
	
	#Checa o número de parâmetros recebidos para o cálculo
	if len(problems) > 5:
		return "Error: Too many problems."
	
	#Divide todos os parâmetros para organizar
	first_number = []
	second_number = []
	operator = []
	for problem in problems:
		pieces = problem.split()
		first_number.append(pieces[0])
		operator.append(pieces[1])
		second_number.append(pieces[2])
	
	#Checa o operador
	if "+" not in operator and "-" not in operator:
		return "Error: Operator must be '+' or '-'."
	
	#Checa os algarísmos
	for i in range(len(first_number))