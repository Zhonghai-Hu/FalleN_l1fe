password = ["root"]
username = ["root"]
a = 0

while a<3:

    input_1 = input("login or create an account: ")

    if input_1 == "login":
        found = 0
        u_try = input('please enter your username')
        p_try = input('please enter your password')

        for i in range(len(username)):

            if username[i] == u_try and password[i] == p_try:
                print('welcome')
                found = 1
                break

        if found != 1:
            print("not a valable password or username")
            a+= 1

        else:
            break

    elif input_1 == "create":
        u_try = input('please enter your username')
        p_try = input('please enter your password')
        password.append(p_try)
        username.append(u_try)
        continue
    
    else:
        break