import os 


filepath = os.path.join("raw_data", "givenPassage.txt")

with open(filepath) as paragraph:
	for line in paragraph:
		#calculate word count, I do not know how the example gave 122
		words = line.split(' ')
		word_count = len(words)

		#calculate sentence count, minus 1 to ignore after last '.'
		sentence_count = len(line.split('.')) - 1
		
		word_lengths = []
		for word in words:
			character_count = 0
			for character in word:
				#the example doesn't check for alphabet, but it makes more sense to me like this
				if(character.isalpha()):
					character_count += 1
			word_lengths.append(character_count)
		
		#calculate average word length
		average_word_length = sum(word_lengths) / len(word_lengths)

		#calculate average sentence length
		average_sentence_length = word_count / sentence_count

		print("Paragraph Analysis")
		print("-----------------")
		print(f"Approximate Word Count: {word_count}")
		print(f"Approximate Sentence Count: {sentence_count}")
		print(f"Average Letter Count: {average_word_length}")
		print(f"Average Sentence Length: {average_sentence_length}")
