def add_space_before_capitals(s):
    result = ""
    for i, char in enumerate(s):
        if char.isupper() and i != 0:
            result += " " + char
        else:
            result += char
    return result

user_input = input("جمله را وارد کنید: ")

print(add_space_before_capitals(user_input))