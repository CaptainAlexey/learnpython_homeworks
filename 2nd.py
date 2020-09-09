def comparison_str(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == "learn":
        return 3
    else:
        return "Вторая длиннее первой"

print(comparison_str(0, "Hello"))
print(comparison_str(0, 1))
print(comparison_str("Hello", "Hello"))
print(comparison_str("FantaSprite", "Hello"))
print(comparison_str("Fans", "Hello world"))
print(comparison_str("Name", "learn"))

    