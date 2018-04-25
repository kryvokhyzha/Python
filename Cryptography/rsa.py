from random import choice

# Вычисление простых чисел #
def getPrime(minN, maxN, flag = False, primes = []):
	for num in range(minN, maxN):
		for get in range(2,num):
			if num % get == 0:
				flag = True
				break
		if not flag:
			primes.append(num)
		flag = False
	return primes

# Подбор открытой экспоненты #
def getPubExp(minN, maxN, Fn, pubExp = []):
	for e in range(minN, maxN):
		d = int((1 + 2 * Fn) / e)
		if d * e == 1 + 2 * Fn:
			pubExp.append(e)
	return pubExp

# Подбор натурального числа k #
def getNumK(minN, maxN, Fn, e, numK = []):
	for k in range(minN, maxN):
		d = int((1 + k * Fn) / e)
		if d * e == 1 + k * Fn:
			numK.append(k)
	return numK

# Получение приватной экспоненты #
def getPrivExp(e, n, Fn, k):
	d = int((1 + k * Fn) / e)
	if d * e != 1 + k * Fn:
		raise SystemExit
	return d

# Генерация ключей #
def generateKeys(minP, maxP, maxN):
	primes = getPrime(minP,maxP)
	
	p, q = choice(primes), choice(primes)
	if p == q: return generateKeys(minP, maxP, maxN)

	n, Fn = p*q, (p-1)*(q-1)
	try:
		pubExp = getPubExp(2, maxN, Fn)[0]
		numK = getNumK(2, maxN, Fn, pubExp)[0]
		privExp = getPrivExp(pubExp, n, Fn, numK)

	except: return generateKeys(minP, maxP, maxN)

	return ([pubExp,n], [privExp,n])

# Шифрование / Расшифрование #
def encryptDecrypt(key, message):
	return message ** key[0] % key[1]

# Проверка выборочной опции #
def choiceMode(mode):
	if mode == 'G':
		keys = generateKeys(50,500,25)
		return "Public_key: [%d.%d]\nPrivate_key: [%d.%d]"%\
		(keys[0][0], keys[0][1], keys[1][0], keys[1][1])
	else:
		try:
			message = int(input("Write the number: "))
			key = [int(k) for k in input("Write the key: ").split(".")]
		except KeyboardInterrupt: 
			print(); raise SystemExit
		return "Final message: " + str(encryptDecrypt(key, message))

while True:
	try:
		cryptMode = input("[G]enerate_[C]ipher: ").upper()
	except KeyboardInterrupt: 
		print(); raise SystemExit
	if cryptMode not in ['G','C']:
		print("Error: mode is not Found!"); raise SystemExit
	print(choiceMode(cryptMode),'\n')
