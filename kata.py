#----------------------------importations---------------------------

import string
import random
import unicodedata
import pandas
from PIL import Image, ImageColor

#----------------------------fonctions---------------------------
def permutation(arg: list) -> list[list]:
    # juste une fonction qui genere toutes les permutation possible d'un ensemble
    # input ["a", "b", "lettre"] => output [["a", "b", "lettre"], ["a", "lettre", "b"], ["b", "a", "lettre"], ["b", "lettre", "a"], ["lettre", "a", "b"], ["lettre", "b", "a"]]
    pass


#----------------------------début du programme---------------------------

a = "coucou"
b = dict()
b["lettre"] = a
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
    # print de chaque ligne du poème

    if i[-1] ==",":
        # print(i)
        # print de chaque ligne du poème qui finit par une virgule
        pass

    elif i[-1] ==";":
        # print(i)
        # print de chaque ligne du poème qui finit par un point-virgule
        pass

    count_a = 0
    for letter in i:
        if letter.lower() =="a":
            count_a += 1
    # print(count_a, i)
    # print le nombre de "a" dans chaque ligne du poème

    count_e = 0
    for letter in i:
        if letter.lower() =="e":
            count_e += 1
    # print(count_e, i)
    # print le nombre de "e" dans chaque ligne du poème

    count_e = 0
    for letter in i:
        if letter.lower() =="e":
            count_e += 1

    if count_e >= 2:
        #print(count_e, i)
        # print les lignes du poème qui contiennent au moins 2 "e"
        pass

    letterCount = 0
    for letter in i:
        if letter in string.ascii_letters:
            letterCount += 1
    if letterCount > 23:
        #print(i, letterCount)
        # print les lignes du poème qui contiennent plus de 23 caractères
        pass

raven = random.sample(raven, len(raven))
for i in raven:
    #print(i)
    # print les lignes du poème dans un ordre aléatoire
    pass

raven_more = [
    "Once upon a midnight dreary, while I pondered, weak and weary",
    "Over many a quaint and curious volume of forgotten lore—",
    "While I nodded, nearly napping, suddenly there came a tapping,",
    "As of some one gently rapping, rapping at my chamber door.",
    "“’Tis some visitor,” I muttered, “tapping at my chamber door—",
    "Only this and nothing more.”",

    "Ah, distinctly I remember it was in the bleak December;",
    "And each separate dying ember wrought its ghost upon the floor.",
    "Eagerly I wished the morrow;—vainly I had sought to borrow",
    "From my books surcease of sorrow—sorrow for the lost Lenore—",
    "For the rare and radiant maiden whom the angels fruit Lenore—",
    "fruitless here for evermore.",

    "And the silken, sad, uncertain rustling of each purple curtain",
    "Thrilled me—filled me with fantastic terrors never felt before;",
    "So that now, to still the beating of my heart, I stood repeating",
    "“’Tis some visitor entreating entrance at my chamber door—",
    "Some late visitor entreating entrance at my chamber door;—",
    "This it is and nothing more.”",

    "Presently my soul grew stronger; hesitating then no longer,",
    "“Sir,” said I, “or Madam, truly your forgiveness I implore;",
    "But the fact is I was napping, and so gently you came rapping,",
    "And so faintly you came tapping, tapping at my chamber door,",
    "That I scarce was sure I heard you”—here I opened wide the door;—",
    "Darkness there and nothing more.,",

    "Deep into that darkness peering, long I stood there wondering, fearing,",
    "Doubting, dreaming dreams no mortal ever dared to dream before;",
    "But the silence was unbroken, and the stillness gave no token,",
    "And the only word there spoken was the whispered word, “Lenore?”",
    "This I whispered, and an echo murmured back the word, “Lenore!”—",
    "Merely this and nothing more.",

    "Back into the chamber turning, all my soul within me burning,",
    "Soon again I heard a tapping somewhat louder than before.",
    "“Surely,” said I, “surely that is something at my window lattice;",
    "Let me see, then, what thereat is, and this mystery explore—",
    "Let my heart be still a moment and this mystery explore;—",
    "’Tis the wind and nothing more!”",

    "Open here I flung the shutter, when, with many a flirt and flutter,",
    "In there stepped a stately Raven of the saintly days of yore;",
    "Not the least obeisance made he; not a minute stopped or stayed he;",
    "But, with mien of lord or lady, perched above my chamber door—",
    "Perched upon a bust of Pallas just above my chamber door—",
    "Perched, and sat, and nothing more.",

    "Then this ebony bird beguiling my sad fancy into smiling,",
    "By the grave and stern decorum of the countenance it wore,",
    "“Though thy crest be shorn and shaven, thou,” I said, “art sure no craven,",
    "Ghastly grim and ancient Raven wandering from the Nightly shore—",
    "Tell me what thy lordly fruit is on the Night’s Plutonian shore!”",
    "Quoth the Raven “Nevermore.”",

    "Much I marvelled this ungainly fowl to hear discourse so plainly,",
    "Though its answer little meaning—little relevancy bore;",
    "For we cannot help agreeing that no living human being",
    "Ever yet was blessed with seeing bird above his chamber door—",
    "Bird or beast upon the sculptured bust above his chamber door,",
    "With such fruit as “Nevermore.”",

    "But the Raven, sitting lonely on the placid bust, spoke only",
    "That one word, as if his soul in that one word he did outpour.",
    "Nothing farther then he uttered—not a feather then he fluttered—",
    "Till I scarcely more than muttered “Other friends have flown before—",
    "On the morrow he will leave me, as my Hopes have flown before.”",
    "Then the bird said “Nevermore.”",

    "Startled at the stillness broken by reply so aptly spoken,",
    "“Doubtless,” said I, “what it utters is its only stock and store",
    "Caught from some unhappy master whom unmerciful Disaster",
    "Followed fast and followed faster till his songs one burden bore—",
    "Till the dirges of his Hope that melancholy burden bore",
    "Of ‘Never—nevermore’.”",

    "But the Raven still beguiling all my fancy into smiling,",
    "Straight I wheeled a cushioned seat in front of bird, and bust and door;",
    "Then, upon the velvet sinking, I betook myself to linking",
    "Fancy unto fancy, thinking what this ominous bird of yore—",
    "What this grim, ungainly, ghastly, gaunt, and ominous bird of yore",
    "Meant in croaking “Nevermore.”",

    "This I sat engaged in guessing, but no syllable expressing",
    "To the fowl whose fiery eyes now burned into my bosom’s core;",
    "This and more I sat divining, with my head at ease reclining",
    "On the cushion’s velvet lining that the lamp-light gloated o’er,",
    "But whose velvet-violet lining with the lamp-light gloating o’er,",
    "She shall press, ah, nevermore!",

    "Then, methought, the air grew denser, perfumed from an unseen censer",
    "Swung by Seraphim whose foot-falls tinkled on the tufted floor.",
    "“Wretch,” I cried, “thy God hath lent thee—by these angels he hath sent thee",
    "Respite—respite and nepenthe from thy memories of Lenore;",
    "Quaff, oh quaff this kind nepenthe and forget this lost Lenore!”",
    "Quoth the Raven “Nevermore.”",

    "“Prophet!” said I, “thing of evil!—prophet still, if bird or devil!—",
    "Whether Tempter sent, or whether tempest tossed thee here ashore,",
    "Desolate yet all undaunted, on this desert land enchanted—",
    "On this home by Horror haunted—tell me truly, I implore—",
    "Is there—is there balm in Gilead?—tell me—tell me, I implore!”",
    "Quoth the Raven “Nevermore.”",

    "“Prophet!” said I, “thing of evil!—prophet still, if bird or devil!",
    "By that Heaven that bends above us—by that God we both adore—",
    "Tell this soul with sorrow laden if, within the distant Aidenn,",
    "It shall clasp a sainted maiden whom the angels fruit Lenore—",
    "Clasp a rare and radiant maiden whom the angels fruit Lenore.”",
    "Quoth the Raven “Nevermore.”",

    "“Be that word our sign of parting, bird or fiend!” I shrieked, upstarting—",
    "“Get thee back into the tempest and the Night’s Plutonian shore!",
    "Leave no black plume as a token of that lie thy soul hath spoken!",
    "Leave my loneliness unbroken!—quit the bust above my door!",
    "Take thy beak from out my heart, and take thy form from off my door!”",
    "Quoth the Raven “Nevermore.”",

    "And the Raven, never flitting, still is sitting, still is sitting",
    "On the pallid bust of Pallas just above my chamber door;",
    "And his eyes have all the seeming of a demon’s that is dreaming,",
    "And the lamp-light o’er him streaming throws his shadow on the floor;",
    "And my soul from out that shadow that lies floating on the floor",
    "Shall be lifted—nevermore!"

]

# print les lignes supplémentaires du poème dans un ordre aléatoire
raven_more = random.sample(raven_more, len(raven_more))
for i in raven_more:
    #print(i)
    pass

#----------------------------fin du 3ème kata---------------------------

def operation(n):
    global compte
    if compte + n < 0:
        raise ValueError("Solde insuffisant")
    compte += n

compte = 0.0

operation(100)
operation(-30)
try:
    operation(-100)
except ValueError:
    print("pas assez de sous")

#print(compte)
# print la valeur de "compte" après les deux appels de la fonction "operation"

#----------------------------fin du 4ème kata---------------------------

cmd = {
    "client": "bob",
    "products": [
        {"product": "apple", "unit_price": 1, "qt": 5},
        {"product": "sausage", "unit_price": 16.4, "qt": 72},
        {"product": "water in plastic bottle", "unit_price": 0.75, "qt": 12},
        {"product": "macbook pro", "unit_price": 2000.99, "qt": 1},
        {"product": "paper", "unit_price": 2, "qt": 3},
    ]
}

cmd2 = {
    "client": "John Wish",
    "products": [
        {"product": "gros flingue", "unit_price": 1, "qt": 100},
        {"product": "grosse voiture", "unit_price": 1, "qt": 1},
        {"product": "petit chien", "unit_price": 1000, "qt": 0},
        {"product": "plus gros flingues", "unit_price": 2, "qt": 10},
        {"product": "costume blindé", "unit_price": 1, "qt": 3},
				{"product": "alcool divers", "unit_price": 12.5, "qt": 5}
    ]
}

total = 0.0

for item in cmd2["products"]:
    if len(item["product"])%2 == 0:
        item["unit_price"] *= 0.83

    if item["product"][0] == "a" or item["product"][0] == "p":
        total += item["unit_price"] * item["qt"] * 1.055
    else:
        total += item["unit_price"] * item["qt"] * 1.2

# total *= 1.2  # ajout d'une TVA de 20%
#print(total)

#----------------------------fin du 5ème kata---------------------------

f = [a + b for a in string.ascii_lowercase for b in string.ascii_lowercase]
g = [a + b + lettre for a in string.ascii_lowercase for b in string.ascii_lowercase for lettre in string.ascii_lowercase]
h = {key: random.randint(1,12) for key in g}

# print(h)
# print(sum(h.values())/len(h))

#----------------------------fin du 6ème kata---------------------------

# x = int(input("Choisissez un premier nombre :"))
# y = int(input("Choisissez un second nombre :"))
# grille = "#" * x

# for i in range(y):
    # print(grille)

#-----------------------------fin du kata 6.6---------------------------

def palindrome(phrase):
    phrase = "".join(lettre for lettre in unicodedata.normalize("NFD", phrase) if unicodedata.category(lettre) != "Mn")
    phrase_reduite = ""
    for i in phrase:
        if i.isalnum():
            phrase_reduite += i.lower()
    inverse = "".join(reversed(phrase_reduite))

    if phrase_reduite == inverse:
        print("-> True")
        return True
    else:
        print("-> False")
        return False

# palindrome('bob')
# # → True
# palindrome('kevin')
# # → False
# palindrome('La mariée ira mal')
# # → True
# palindrome('le marié aussi')
# # → False
# palindrome('Engage le jeu que je le gagne')
# # → True
# palindrome('Ta bête te bat')
# # → True
# palindrome('Eh ! ça va, la vache ?')
# # → True
# # ... etc.

#-----------------------------fin du kata 6.7---------------------------

class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, fruit, definition):
        self.entries[fruit] = definition

    def look(self, fruit):
        if fruit in self.entries:
            return self.entries[fruit]
        else:
            return "Can't find entry for " + fruit



d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
# print(d.look('Apple'))
# # → A fruit that grows on trees
# print(d.look('Banana'))
# # → Can't find entry for Banana

#----------------------------fin du kata 7-------------------------------

def chocoSplit(x, y):
    split = 0
    if x <= 0 or y <= 0:
        print("# -> 0")
    else:
        print("# ->", x * y - 1)

# chocoSplit(1, 2) # → 1
# chocoSplit(3, 1) # → 2
# chocoSplit(0, 3) # → 0
# chocoSplit(2, 2) # → 3
# chocoSplit(3, 3)
# chocoSplit(2, 3)
# chocoSplit(5, 4)

#----------------------------fin du kata 7.628-------------------------------

color_data = [{
"time_start": "1:38:01",
"time_end": "18:48:05",
"color": "#640c0b"
}, {
"time_start": "7:50:25",
"time_end": "10:41:37",
"color": "#a61276"
}, {
"time_start": "0:47:40",
"time_end": "11:05:24",
"color": "#922553"
}, {
"time_start": "7:22:26",
"time_end": "9:08:07",
"color": "#8af9f7"
}, {
"time_start": "0:05:20",
"time_end": "12:06:49",
"color": "#1fc771"
}, {
"time_start": "4:32:28",
"time_end": "11:02:06",
"color": "#d7718e"
}, {
"time_start": "6:00:10",
"time_end": "9:53:21",
"color": "#27f414"
}, {
"time_start": "0:04:30",
"time_end": "9:25:44",
"color": "#7e79b6"
}, {
"time_start": "0:24:42",
"time_end": "12:27:28",
"color": "#6eb31b"
}, {
"time_start": "7:06:52",
"time_end": "22:36:25",
"color": "#a03827"
}]

tableau = pandas.DataFrame(color_data)
tableau["time_start"] = pandas.to_timedelta(tableau["time_start"])
tableau["time_end"] = pandas.to_timedelta(tableau["time_end"])
tableau["duration"] = tableau["time_end"] - tableau["time_start"]
tableau_trié = tableau.sort_values("duration")
# print(tableau_trié["color"].tolist())

height_per_line = 50
max_duration_min = int(tableau_trié["duration"].dt.total_seconds().max() / 60)
img_width = max_duration_min
img_height = 500 # height_per_line * len(tableau_trié)
scale = 0.5

img = Image.new("RGB", (img_width, img_height), "#ffffff")

for i, row in enumerate(tableau_trié.itertuples()):
    # print(i, row)
    color = ImageColor.getcolor(row.color, "RGB")
    length = int(row.duration.total_seconds() / 60 * scale)
    x_start = int(row.time_start.total_seconds() / 60 * scale)
    y_start = i * height_per_line
    y_end = y_start + height_per_line
    # print(x_start, y_start, length, color)
    for y in range(y_start, y_end):
        for x in range(x_start, x_start + length):
            img.putpixel((x, y), color)

img.show()