from textblob import TextBlob

def correct_grammer(text):
	blob = TextBlob(text);
	corrected_text = str(blob.correct())
	return corrected_text

text = input("enter")
corrected_text = correct_grammer(text)
print(f"corrected: {corrected_text}")
