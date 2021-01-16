alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text=""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    print(f"The old position was {position}.")
    new_position = position + shift_amount
    print(f"The new position is {new_position % len(alphabet)}.")
    end_text += alphabet[new_position % len(alphabet)]
  print(f"The {cipher_direction}d text is {end_text}.")


caesar(text, shift, direction)