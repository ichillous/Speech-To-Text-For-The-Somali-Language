# abdulnaser sheikh
# May 08th, 2022


# the purpose of this python script is to
# convert Somali words into their basic phonetics

somaliAphabet = [x.strip() for x in open(r'C:\Users\abdulnaser sheikh\Desktop\phonetic dictionary\SomaliAlphabet.txt','r')]


def getPhonetic(word,result):

	result = result

	word = word.replace("-","")
	word = word.replace(".","")
	word = word.replace(";","")

	for aphabet in somaliAphabet:

		if word.startswith(aphabet):
			result += aphabet + " "
			word = word[len(aphabet):]

			break

	if len(word) > 0:
		return getPhonetic(word,result)

	return result


counter = 0

word = "hooyo"
print("{} {}".format(word,getPhonetic(word,"")))

exit(0)
for word in [x.strip() for x in open(r'C:\Users\abdulnaser sheikh\Desktop\phonetic dictionary\SomaliDictionary.txt','r')]:
	print("{} {}".format(word,getPhonetic(word,"")))
	counter += 1
