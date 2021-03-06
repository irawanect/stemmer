import re
TEXT = """Kami belajar tanpa lelah.
Kami& tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa#muda.
Itu karena kami ingin kelak istri dan anak kami bahagia"""

def tokenize(text):
	text= text.lower()
	text = re.sub(r'[^a-z0-9 -]',' ', text, flags = re.IGNORECASE|re.MULTILINE) #karakter selain a-z 0-9 -, diganti dengan spasi kosong#
	text = re.sub(r'( +)', ' ',text, flags = re.IGNORECASE|re.MULTILINE) #( +) menandakan spasi berlebih akan diganti dengan spasi 1
	tokens = text.split(" ")
	return tokens

print (tokenize(TEXT))