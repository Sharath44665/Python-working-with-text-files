#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
contents=[]
with open(file="../Mail Merge Project Start/Input/Names/invited_names.txt") as myfile:
    contents= myfile.readlines()
    for names in range (len(contents)):
        val=contents[names].replace("\n", "")
        contents[names]=val
for names in contents:
    with open(file="../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as starting_file:
        all_lines = starting_file.readlines()
        # another_file.seek(0)
        # another_file.truncate(0)
        for value in range(len(all_lines)):
            if value == 0:
                replace_val = all_lines[value].replace("[name]", names)
                # another_file.write(replace_val)
                all_lines[0] = replace_val
                # print(replace_val)

        file_name = f"../Mail Merge Project Start/Output/ReadyToSend/{names}.txt"

        with open(file=file_name, mode="w+") as final_text:
            for list_val in all_lines:
                final_text.write(list_val)




#Replace the [name] placeholder with the actual name.

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp