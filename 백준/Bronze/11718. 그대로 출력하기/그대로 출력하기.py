user_input = ""
user_output = ""
for i in range(100):
    try:
        user_input = input()
        if not user_input:
            raise EOFError
            continue
        user_output += user_input
        user_output += '\n'
    except EOFError:
        break

print(user_output[:len(user_output)-1])