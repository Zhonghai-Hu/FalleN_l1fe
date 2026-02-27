# Name: Harrison
# NetID: ki2933
# HW 4 Solution

# Keep lecturing until the user wants to quit
while True:

    # create the result waiting for store
    result = ''

    # ask user want to Encrypt or Decrypt
    encrypt_or_decrypt = input('You want Encrypt or Decrypt (enter e or d)? ')

    shift = int(input('How many shifts you want? '))
    
    #if user choice encrypt
    if encrypt_or_decrypt == 'e':
        pass

    #if user choice decrypt
    elif encrypt_or_decrypt == 'd':
        shift = 26 - shift

    else:
        print("Please enter e or d.")
        continue
    
    string = input("Enter the string to process: ")

    # shift string
    for i in string:

        # If the letters is upper
        if i.isupper():
            new_char = i
            for k in range(shift):
                if new_char == 'Z':
                    new_char = 'A'
                else:
                    new_char = chr(ord(new_char) + 1)
            result += new_char

        # If the letters is lower
        elif i.islower():
            new_char = i
            for k in range(shift):
                if new_char == 'z':
                    new_char = 'a'
                else:
                    new_char = chr(ord(new_char) + 1)
            result += new_char
            
        # If it's punctuation
        else:
            result += i

    print("Original:", string)
    print("Converted:", result)

    # Keep lecturing until the user wants to quit
    again = input('Do you want do again?(y or n) ')
    if again == 'y':
        continue
    else:
        break    
