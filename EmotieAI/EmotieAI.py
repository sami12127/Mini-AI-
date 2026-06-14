# Simpele Emotie AI
# Herkent een paar emoties op basis van woorden in de tekst.

blij = ["blij", "leuk", "fijn", "happy", "gelukkig", "top"]
boos = ["boos", "irritant", "haat", "stom", "kwaad"]
verdrietig = ["verdrietig", "huilen", "down", "alleen", "rot"]
moe = ["moe", "slaap", "uitgeput", "bekaf"]
bang = ["bang", "angst", "eng", "nerveus"]


def vind_emotie(tekst):
    tekst = tekst.lower()

    for woord in blij:
        if woord in tekst:
            return "blij"
    for woord in boos:
        if woord in tekst:
            return "boos"
    for woord in verdrietig:
        if woord in tekst:
            return "verdrietig"
    for woord in moe:
        if woord in tekst:
            return "moe"
    for woord in bang:
        if woord in tekst:
            return "bang"

    return "neutraal"


# Hoofdprogramma
print("Emotie AI - typ iets en ik raad je emotie (typ 'stop' om te stoppen)")

while True:
    tekst = input("> ")

    if tekst == "stop":
        print("Tot ziens!")
        break

    emotie = vind_emotie(tekst)
    print("Ik denk dat je je", emotie, "voelt.")
