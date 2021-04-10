import os 


filepath = os.path.join("raw_data", "givenPassage.txt")

with open(filepath) as paragraph:
	for line in paragraph:
		#calculate word count 
		words = line.split(' ')
		word_count = len(words)

		#calculate sentence count, minus 1 to ignore after last '.'
		sentence_count = len(line.split('.')) - 1
		
		word_lengths = []
		for word in words:
			character_count = 0
			for character in word:
				if(character.isalpha())
					character_count += 1
			word_lengths.append(character_count)












		print(word_count)
		print(sentence_count)
		print(word_lengths)
