lower_s, super_s, = 0, 0
stroka = 'som eBO DYo nce TOL Dme the wor ldi sgo nna'
stroka = stroka.split()
len_stroki = len(stroka)
for podstr in stroka:
    super_c = 0
    lower_c = 0
    for bukva in podstr:
        if bukva.isupper():
            super_c += 1
        else:
            lower_c += 1
    if super_c > lower_c:
        super_s += 1
    else:
        lower_s += 1
    #print(super_c, lower_c)
one = round(super_s/len_stroki * 100)
two = round(lower_s/len_stroki * 100)
print("Заглавных букв: {0}%, Строчных букв: {1}%".format(one,two))









