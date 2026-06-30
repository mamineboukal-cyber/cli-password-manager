import string , secrets
def password_generator(length):
 digits = string.digits
 letters = string.ascii_letters
 symbols = string.punctuation
 if length < 8 or length > 12 :
  return "choose lenght between 8 and 12"
 else :
  password = ""
  for _ in range(length):
     gategorie = secrets.choice([digits,letters,symbols])
     password += secrets.choice(gategorie)
  return password