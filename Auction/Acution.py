from art import logo

print(logo)

print("Welcome to secret auction program !!")
bit = {}
play = True

while play:
    name = input("\nWhat is your name : ")
    amount = int(input("\nEnter your bit : Rs "))

    bit[name] = amount

    should_continue = input("\nAre there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "yes":
        play = True
    else:
        play = False

highest_bit = 0
for key in bit:
    if bit[key] > highest_bit:
        highest_bit = bit[key]
        biter_name = key
print(f"Highest bit is : {highest_bit} \nWinner name is : {biter_name}")
