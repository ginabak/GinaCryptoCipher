# GINA BAK
# FOR FUNNNNNN :)

# Global constant ;), the alphabet never changes! :), and neither does the invalid characters ;)
# constant_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
constant_alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
constant_invalid = "[]!@#$%^&*()_-=+;'{}\|/.,?123456 7890"


'''
This is the main function, responsible for the user interface.
@ params        none
@ returns       none
'''

def main():
    user_choice = ""
    fibonacci = []
    encrypted_word = ""
    word_list = []
    check = ""
    
    while (user_choice != "QUIT"):
        print("\n\tMAIN MENU\n -------------------------\nWELCOME TO THE SUPER SIMPLE CRYPTO-HELPER\n")
        print("\nPLEASE NOTE:\n\tTo quit this program, just write quit!")
        print("\nPLEASE NOTE:\n\tThis is a super simple program, one word at a time! #simpleisbest\n")
        print("\nYour current encrypted/secret word is: "+ encrypted_word)

        # This validates the user input
        while (user_choice != "QUIT"):
            user_choice = input("\n\nPlease write the word you would like to encrypt: ").upper()
            if user_choice == "QUIT":
                # Who doesn't want to be greeted out? 
                print("Thanks for coming bye! :)")
                exit()

            for i in range (len(user_choice)):
                if user_choice[i] in constant_invalid:
                    print("OOPSY, you can't have any special characters or spaces!")
                    check = ""
                    break
                if user_choice[i] not in constant_invalid:
                    check = "YAY"
            print(check)

            if check == "YAY":
                break
            continue       

        counter = 0
        for i in range(len(user_choice)):
            counter += 1
            #This will put each letter into the list word_list
            word_list.append(user_choice[i])

        fibonacci = recursive_fibonacci(counter)
        encrypted_word = encrypt(constant_alphabet, fibonacci, word_list)
        print("The secret word is now: " + encrypted_word)
        user_choice = ""
        fibonacci = []
        word_list = []



'''
This is the recursive_fibonacci function, responsible for creating the fibonacci sequence
@ params        n (which is an integer, the length of the string given by user)
@ returns       sequence (variable that contains an list of integers, determined by the length of the word given by the user!)
'''
def recursive_fibonacci(n):
    # Gotta always have a base case when you do a recurrrrrsive call :)
    if n < 0:
        return []

    elif n <= 2:
        return [1, 1][:n]

    else:
        sequence = recursive_fibonacci(n-1)
        sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2])
        return sequence
        print("In case you were wondering, this is your fibonacci sequence,\nbased on the length of the word you wanted to encrypt!\n" + str(recursive_fibonacci(n)))




'''
This is the encrypt function, responsible for encrypting the word given by the user!
@ params        constant_alphabet, fibonacci list, word
@ returns       string (the encrypted string/word)
'''
def encrypt(alphabet, fibonacci, word):
  string_word = ""
  encrypted_word=[]
  index_list = []
  formatted_list = []

  # This will help me retrieve where the alphabet is located from the given word :)
  for i in range (len(word)):
    for j in range(len(constant_alphabet)):
      if word[i] in constant_alphabet[j]:
        index_list.append([j])
      else:
        continue

  #print (index_list)

  # This is so that it's no longer in a nested list
  for i in range (len(index_list)):
    formatted_list.append(index_list[i][0])

  #print (formatted_list)

  # This is will now take the fibonacci at the given index & add it to the list to help encrypt! :)
  for i in range(len(fibonacci)):
    formatted_list[i] += fibonacci[i]

  # This grabs the letter from the constant_alphabet so that it can now encrypt! Almost there
#   for i in range (len(formatted_list)):
#     print(formatted_list[i])
#     while (formatted_list[i] > 25):
#       new_number = formatted_list[i]-26
#       formatted_list[i] = new_number
#       print("This is the new number" + str(new_number))
#       continue

        #if new_number <=25:
        #new_number = new_number-26
        #formatted_list[i] = new_number

    #if new_number <=25:
    #encrypted_word.append(constant_alphabet[new_number])
    #break


    # THANK GOODNESS FOR MODULO %%%%%%% - I DIDN'T HAVE TO HAVE THAT LONG FOR & WHILE LOOP ABOVE
    encrypted_word.append(constant_alphabet[formatted_list[i]%26])
    print(encrypted_word)

  for i in range (len(encrypted_word)):
    string_word += encrypted_word[i]
    #print(string_word)

  #print(string_word)
  return string_word




main()
