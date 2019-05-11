file1 = open("word_list",'r')
file2 = open("BadWords.txt", 'r')

curses = set()
words = file1.read()
curses = file2.read()
white_list = []
curses = curses.split("\n")
words = words.split("\n")

file1.close()
file2.close()



for curse in curses:
	for word in words:
		if curse in word and curse != word:
			if not word in curses:
				white_list.append(word + "\n")
				print(curse + "\t" + word)


			

fileout = open("whitelist.txt",'w')
for i in white_list:
	fileout.write(i)

fileout.close()



	



