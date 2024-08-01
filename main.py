#  MATH333
#  Abhyuday Singh
#  Test 1


#  Question 3

pn = 1

# for _ in range(0, 5):
#     px = pn * ((1 + ((7 - (pn ** 5))//(pn ** 2))) ** 3)
#     pn = px
#     pn = round(pn, 5)
#     print(len(str(pn)), pn)

for _ in range(0, 10):
    px = pn + ((7 - (pn ** 5))/(5 * (pn ** 4)))
    pn = px
    pn = round(pn, 5)
    print(_, len(str(pn)), pn)






