#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.readlines()

greetings = starting_letter[0]
for i in range(len(names)):
    name = names[i].strip()
    new_greetings = greetings.replace("[name]", name)
    starting_letter[0] = new_greetings
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        file.writelines(starting_letter)
