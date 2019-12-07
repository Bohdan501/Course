import string

with open('story.txt', 'r') as ff:
    text = ff.read()

with open('words.txt', 'r') as  ff1:
    words = ff1.read()

w= words.split()

text = text.strip()

for symbol in string.punctuation:
    text = text.replace(symbol, "")

a= text.split()
print(a)
#################################################################
def app_key(ak):
    letters = ak
    key = 1  # secret code

    for i in range(len(letters)):
        letter = letters[i]

        #print(letter)

        code = ord(letter)
        new_code = ord(letter) + key
        if 97 <= code <= 122:  # small letter
            if new_code > 122:
                new_code = new_code - 26
        elif 65 <= code <= 90:  # Capital letter
            if new_code > 90:
                new_code = new_code - 26
        else:
            new_code = code

        new_letter = chr(new_code)
        print(new_letter, end="")


####################################################################

for ii in a:
    app_key(ii)









