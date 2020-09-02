test = "3.49648e+07|3.5e+07"


l = test.strip("{}").split("|")
        # Get string without 0's
l1, l2 = str(l[0]).replace("e+", "").replace("0", ""), str(l[1]).replace("e+", "").replace("0", "")

i =3.5 * pow(10, 22)

print(int(i))