alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  encrypted_text=""
  for letter in text:
    shifted_index = alphabet.index(letter) + shift
    letter = alphabet[shifted_index % len(alphabet)]
    encrypted_text += letter
  print(f"The encoded text is {encrypted_text}.")

def decrypt(text, shift):
  decrypted_text=""
  for letter in text:
    shifted_index = alphabet.index(letter) - shift
    letter = alphabet[shifted_index % len(alphabet)]
    decrypted_text += letter
  print(f"The decoded text is {decrypted_text}.")


if(direction == 'encode'):
  encrypt(text, shift)
elif(direction == 'decode'):
  decrypt(text, shift)
else:
  print("Opção escolhida incorreta.")