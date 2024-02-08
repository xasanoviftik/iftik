"""
1-mashq
"""

# def outer():
#     message = "local"
#     def inner():
#         nonlocal message

#         message = "nonlocal"

#         print(f"iner: {message}")

#     inner()

#     print(f"outer: {message}")
# outer()


"""
2-mashq
"""
# def abs(x):

#     if x < 0:
#         return -x
#     else:
#         return x

# print(abs(-11))
# print(abs(21))
# print(abs(0))

# print(abs(-3) == abs(-3))
# print(abs(0) == abs(0))
# print(abs(21) == abs(21))


"""
3-mashq
"""
# gruppa ="N35"

# def change():
#     global gruppa 

#     gruppa = "N36"

#     print(gruppa)

# change()

"""
4-mashq
"""

def palindrome(text):
    new_text = ""
    r_text = ""
    for i in text:
        if i.isalpha():
            new_text += i.lower()
    r_text = new_text[::-1]
    if r_text == new_text:
        return True
    else:
        return False
print(palindrome("Go hang a salami I'm a lasagna hog."))
    
print(palindrome("Was it a rat I saw?"))