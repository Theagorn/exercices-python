
import string

#----------------------------début du programme---------------------------

a = "coucou"
b = dict()
b["c"] = a
b["d"] = dict()
b["e"] = []
b["e"].extend([2, None, "hello", 42])


# print(b["e"][2])
# print(b)
# print(type(b["e"]))

#----------------------------fin du 1er kata---------------------------

lettres = list(string.ascii_lowercase)

for i in range(4,27):
    b["d"][lettres[i-4]] = i
    # print(lettres[i-4], " = ", i)

b["f"] = b["d"].values()
# print(b["f"])

try:
    b["f"].extend(b["e"])
    print(b["f"])

except AttributeError as e:
    print("ouf")

#----------------------------fin du 2ème kata---------------------------

raven = (
'Deep into that darkness peering,',
'Long I stood there, wondering, fearing,',
'Doubting, dreaming dreams no mortals',
'Ever dared to dream before;',
'But the silence was unbroken,',
'And the stillness gave no token,',
'And the only word there spoken',
'Was the whispered word, "Lenore!"',
'This I whispered, and an echo',
'Murmured back the word, "Lenore!"',
'Merely this, and nothing more.',
)

for i in raven:
    # print(i)

    if i[-1] ==",":
        # print(i)
        pass

    elif i[-1] ==";":
        # print(i)
        pass

    count_a = 0
    # for "a" in i:
    #     count_a += 1
    #     print(count_a)