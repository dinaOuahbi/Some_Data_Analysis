# Built a basic calculator
def calculator():
    num1 = float(input("Enter your number 1 : "))
    operator = input("Enter the desire operator : ")
    num2 = float(input("Enter your second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    else:
        print("Invalid operator")

# Built gessing game
def guess_game():
    secret_word = "prompt"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while secret_word != guess and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter your gessing word : ")
            guess_count+=1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses. You lose !")
    else:
        print("You win !")

# Built a translator (vowel ==> g)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="G"
            else:
                translation+="g"
        else:
            translation+=letter
    return translation 

prompt = input("Enter your phrase : ")
#print(translate(prompt))



