def  Longwstword(sen):

    sen = sen.split(" ")

    
    for i in sen:
        for j in i:
            if j.isalnum():
                print(j)


print(Longwstword("I love you")