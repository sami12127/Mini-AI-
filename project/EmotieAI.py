def emotie_detector():
    """
    Hoofdfunctie voor de Emotie AI met mooie UI
    """
    ##### TEST PUSH
    # ANSI kleurcodes voor mooie output
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    
    # Print mooie welkomstbanner
    print("\n" * 2)
    print(f"{CYAN}{'═' * 70}{RESET}")
    print(f"{BOLD}{MAGENTA}{'🎭 EMOTIE AI - Hoe voel jij je vandaag? 🎭':^70}{RESET}")
    print(f"{CYAN}{'═' * 70}{RESET}")
    print()
    print(f"{YELLOW}  ✨ Ik ben een AI die probeert te begrijpen hoe je je voelt.{RESET}")
    print(f"{YELLOW}  💬 Vertel me iets, en ik zal proberen je emotie te herkennen!{RESET}")
    print()
    print(f"{BLUE}  ℹ️  Type 'stop' om te stoppen{RESET}")
    print(f"{CYAN}{'═' * 70}{RESET}")
    print()
    
    conversatie_nummer = 0
    
    while True:
        conversatie_nummer += 1
        
        # Krijg input van gebruiker met mooie formatting
        print(f"{GREEN}{BOLD}┌─ Jouw beurt #{conversatie_nummer}{RESET}")
        tekst = input(f"{GREEN}└─➤ {RESET}").strip()
        
        # Check of gebruiker wil stoppen
        if tekst.lower() == "stop":
            print()
            print(f"{CYAN}{'─' * 70}{RESET}")
            print(f"{MAGENTA}{BOLD}  🤖 Bedankt voor het chatten! Tot de volgende keer! 👋{RESET}")
            print(f"{CYAN}{'─' * 70}{RESET}")
            print()
            break
        
        # Check voor lege input
        if not tekst:
            print(f"{RED}  ⚠️  Hmm, stilte... Vertel me wat meer!{RESET}\n")
            continue
        
        # Analyseer de emotie
        emotie, zekerheid = analyseer_emotie(tekst)
        
        # Genereer reactie
        reactie = genereer_reactie(emotie, zekerheid, tekst)
        
        # Print AI reactie met mooie formatting
        print()
        print(f"{CYAN}{'─' * 70}{RESET}")
        print(f"{BOLD}{BLUE}🤖 AI Analyse:{RESET}")
        print(f"{YELLOW}   {reactie}{RESET}")
        print(f"{CYAN}{'─' * 70}{RESET}")
        print()


def analyseer_emotie(tekst):
    """
    Analyseert de tekst en bepaalt de emotie
    Returns: (emotie, zekerheid_score)
    """
    
    tekst_lower = tekst.lower()
    
    # Score dictionary voor verschillende emoties
    scores = {
        "blij": 0,
        "boos": 0,
        "verdrietig": 0,
        "gestrest": 0,
        "verveeld": 0,
        "enthousiast": 0,
        "moe": 0,
        "verliefd": 0,
        "bang": 0,
        "verward": 0,
        "ziek": 0
    }
    
    # === BLIJHEID ===
    blije_woorden = [
        "blij", "happy", "gelukkig", "fijn", "leuk", "geweldig", "super", 
        "fantastisch", "top", "yes", "yeah", "joepie", "hoera",
        "genieten", "lachen", "lol", "plezier", "yay", "jaaa", "nice",
        "gewoon goed", "perfect", "heerlijk", "zalig", "mooi", "prachtig",
        "vrolijk", "opgewekt", "stralend", "uitgelaten", "positief",
        "tevreden", "dankbaar", "blessed", "geluk", "goed nieuws",
        "gefeliciteerd", "hoezee", "joehoe", "jeej", "awesome", "cool",
        "vet", "gaaf", "chill", "relaxed", "lekker", "goed gevoel",
        "trots", "succesvol", "gelukt", "eindelijk", "wauw", "goed gedaan",
        "toppertje", "kippenvel", "geweldig nieuws", "fantastisch nieuws"
    ]
    
    # === BOOSHEID ===
    boze_woorden = [
        "boos", "kwaad", "irritant", "pissed", "geïrriteerd", "vervelend",
        "stomme", "idioot", "verschrikkelijk", "haat", "grr", "wtf",
        "onzin", "belachelijk", "rotzooi", "shit", "damn", "fuck",
        "woedend", "woest", "razend", "nijdig", "getergd", "gepikeerd",
        "chagrijnig", "knorrig", "gefrustreerd", "frustratie", "ergeren",
        "ergerlijk", "klote", "kut", "bullshit", "waardeloos",
        "stom", "dom", "achterlijk", "debiel", "mongo", "kanker",
        "tering", "godverdomme", "krijg de pest", "gestoord", 
        "vreselijk", "afschuwelijk", "walgelijk", "misselijk makend",
        "kutzooi", "zooi", "bagger", "puinhoop", "drama", "gedoe",
        "geneuzel", "gelul", "gezeik", "gezeur", "gejank", "geklaag",
        "argh", "pfff", "bah", "vies", "smerig", "kotsmisselijk",
        "heb schijt aan", "fuck off", "rot op", "zeik", "lul niet",
    ]
    
    # === VERDRIET ===
    verdrietige_woorden = [
        "verdrietig", "down", "depri", "somber", "rot", "naar",
        "eenzaam", "alleen", "huilen", "pijn", "gemist", "verloren",
        "teleurgesteld", "jammer", "sneu", "triest", "moeilijk", "zwaar",
        "depressief", "hopeloos", "leeg", "ongelukkig", "droevig",
        "ellendig", "beroerd", "neerslachtig", "gedeprimeerd", "moedeloos",
        "bedroefd", "gekwetst", "zeer", "wounded", "heartbroken", "kapot",
        "gebroken", "afgewezen", "alleen gelaten", "verlaten", "gedumpt",
        "mislukt", "gefaald", "mislukking", "verlies", "gemis", "rouw",
        "treuren", "betreuren", "spijt", "schuldig", "schaamte", "schamen",
        "waardeloos voelen", "nutteloos", "betekenisloos", "zinloos",
        "niemand", "niks", "niets", "leeg vanbinnen", "gat", "donker",
        "zwart gat", "abyss", "dieptepunt", "bodem", "shit feeling",
        "tranen", "gehuil", "janken", "depressie", "somberheid"
    ]
    
    # === STRESS ===
    stress_woorden = [
        "stress", "druk", "hectisch", "deadline", "chaos", "overweldigd",
        "veel te doen", "panic", "te veel", "help", "deadlines", "examen",
        "toets", "tentamen", "zenuwachtig", "gespannen", "pressure",
        "spanning", "aanspanning", "gestrest", "onder druk", "tijdgebrek",
        "geen tijd", "haast", "snel", "rennen", "racen", "jachtig",
        "rusteloos", "onrustig", "nerveus", "kriebels", "zenuwen",
        "examenstress", "werkdruk", "overuren", "teveel werk", "overwerkt",
        "burn-out", "burnout", "opgebrand", "uitgeput mentaal",
        "geen energie meer", "kan niet meer", "bezwijken",
        "bezorgd", "zorgen", "piekeren", "tobben", "malen", "stress level",
        "hoofd vol", "te veel gedachten", "overweldiging", "angst voor",
        "bang dat", "wat als", "performance anxiety", "faalangst", "presteren",
        "time pressure", "druk druk druk", "strak schema", "overvol"
    ]
    
    # === VERVELING ===
    verveling_woorden = [
        "verveeld", "saai", "boring", "niks te doen", "meh", "whatever",
        "boeiend", "niks aan de hand", "doodsaai",
        "droog", "oubollig", "melig", "flauw", "sloom",
        "traag", "duf", "eentonig", "monotoon", "hetzelfde", "repetitief",
        "eindeloos", "sleur", "routine", "herhaling", "steeds hetzelfde",
        "genoeg van", "zat van", "over", "done", "beu",
        "ongeïnspireerd", "uninspired", "lege agenda", "niks om handen",
        "doelloos", "zinloos rondhangen", "tijd verdrijven", "killing time",
        "wachten", "aan het wachten", "tik tok", "klok kijken", "uren duren",
        "nietsdoen", "niks doen", "liggen", "chillen zonder doel",
        "bleh", "boeuh", "zucht", "gaaap van verveling"
    ]
    
    # === ENTHOUSIASME ===
    enthousiaste_woorden = [
        "enthousiast", "excited", "zin", "kan niet wachten", "spannend",
        "wauw", "wow", "gaaf", "vet", "awesome", "amazing",
        "incredible", "unbelievable", "te gek", "sick", "lit", "fire",
        "hyped", "hype", "pumped", "ready", "klaar voor", "bring it on",
        "lets go", "letsgo", "omg", "oh my god", "jeeej", "joepie",
        "hoera", "yesss", "finally", "eindelijk", "yes yes yes",
        "zo blij", "super blij", "mega blij", "insane", "crazy good",
        "wild", "energie", "energiek", "vol energie", "bouncing",
        "springerig", "opgewonden", "opwinding", "anticipation",
        "uitkijken naar", "verheugen", "voorpret", "kan bijna niet wachten",
        "countdown", "bijna zover", "soon", "binnenkort", "straks",
        "superfijn", "megacool", "tof", "dikke prima"
    ]
    
    # === MOEHEID ===
    moe_woorden = [
        "moe", "slaperig", "uitgeput", "tired", "slaap", "wakker",
        "gapen", "bed", "rustig aan", "kapot", "doodmoe", "bekaf",
        "afgepeigerd", "op", "energieloos", "lusteloos", "slap", "futloos",
        "lamlendig", "suffig", "wazig", "duizelig", "ogen dicht",
        "oogjes toe", "slapen", "dutje", "powernap", "nap", "siësta",
        "rust nodig", "pauze nodig", "break nodig", "even liggen",
        "even zitten", "uitrusten", "recovering", "herstel nodig",
        "niet uitgeslapen", "te weinig geslapen", "slapeloze nacht",
        "insomnia", "wakker gelegen", "niet kunnen slapen", "omgevallen",
        "zombie", "walking dead", "half dood", "zwaar", "zwarte ogen",
        "wallen", "geen fut", "draai door", "battery low",
        "geen zin", "geen energie", "leeg", "uitgeteld", "knock-out",
        "gesloopt", "compleet op", "niks meer over", "uitgewoond",
        "knikkebollen", "in slaap vallen", "wegdommelen", "doodop"
    ]
    
    # === VERLIEFDHEID ===
    verliefde_woorden = [
        "verliefd", "love", "crush", "date", "liefde", "hart", "schattig",
        "leuk iemand", "iemand ontmoet", "vlinders", "kus", "zoenen",
        "knuffelen", "romantisch", "romance", "relationship", "relatie",
        "verkering", "gezoend", "gekust", "gevreeën", "intimate",
        "butterflies", "vlinders in buik", "kriebels", "hartjes",
        "hearts", "verliefd worden", "falling in love", "lovesick",
        "smoorverliefd", "hopeloos verliefd", "tot over oren",
        "lover", "geliefde", "lief", "schat", "babe", "honey",
        "partner", "date night", "romantic", "connection",
        "chemistry", "klik", "match", "the one", "soulmate",
        "perfect samen", "meant to be", "feelings", "gevoelens voor",
        "denk steeds aan", "mis je", "verlang naar", "hunkering",
        "verliefd op", "gek op", "dol op", "smoor", "bezeten van"
    ]
    
    # === ANGST ===
    bange_woorden = [
        "bang", "scary", "eng", "angstig", "zorgen", "ongerust",
        "nerveus", "bezorgd", "what if", "wat als", "angst", "fear",
        "frightened", "terrified", "doodsbang", "paniek", "panicky",
        "paniekaanval", "hartkloppingen", "zweten", "trillen", "beven",
        "schrikken", "shock", "trauma", "getraumatiseerd", "nachtmerrie",
        "nightmare", "griezelig", "creepy", "unheimisch", "akelig",
        "onheilspellend", "dreigend", "bedreigend", "gevaarlijk", "risico",
        "unsafe", "onveilig", "kwetsbaar", "vulnerable", "wantrouwen",
        "argwaan", "achterdochtig", "paranoia", "paranoïde", "achtervolgd",
        "stalker", "bedreiging", "threat", "horror", "schrik", "vrees",
        "fobie", "phobia", "claustrofobie", "hoogtevrees", "angststoornis",
        "anxiety", "anxious", "worried", "worry", "concerns",
        "panieking", "in paniek", "hysterisch", "hyperventileren"
    ]
    
    # === VERWARRING ===
    verwarde_woorden = [
        "verward", "snap het niet", "confused", "huh", "wat", "waarom",
        "begrijp niet", "weet niet", "geen idee", "unclear", "onduidelijk",
        "vaag", "vague", "abstract", "cryptisch", "raadsel", "puzzel",
        "mysterie", "mysterious", "vreemd", "weird", "strange", "bizar",
        "raar", "gek", "doesn't make sense", "slaat nergens op",
        "contradictie", "tegenstrijdig", "paradox", "inconsistent",
        "onlogisch", "illogisch", "no clue", "lost", "verdwaald",
        "zwemmen", "am zwemmen", "dizzy", "chaotisch",
        "chaos in hoofd", "wirwar", "kluwen", "knoop", "ingewikkeld",
        "complicated", "complex", "te moeilijk", "te ingewikkeld",
        "brain fog", "mist", "wazig", "blurry", "onduidelijke gedachten",
        "twijfel", "onzekerheid", "uncertain", "ambiguity", "dubbelzinnig",
        "hoezo", "eh", "uh", "uhm", "eeh", "wacht even", "hold on",
        "he", "pardon", "sorry what", "kom ik niet uit"
    ]
    
    # === ZIEKTE / FYSIEK ONWEL ===
    zieke_woorden = [
        "ziek", "misselijk", "kotsen", "overgeven", "braken", "kokhals",
        "nausea", "buikpijn", "maagpijn", "krampen", "pijn", "zeer",
        "hoofdpijn", "migraine", "koorts", "fever", "griep", "flu",
        "verkouden", "cold", "hoesten", "kuchen", "niezen", "snotteren",
        "loopneus", "keelpijn", "zere keel", "sore throat", "heesheid",
        "hees", "schor", "benauwdheid", "benauwt", "kortademig", "corona",
        "covid", "positief getest", "sick", "ill", "unwell", "onwel",
        "niet lekker", "niet fit", "niet goed", "beroerd voelen",
        "ellendig voelen", "draaierig", "flauw",
        "bijna flauwgevallen", "zwak", "slap gevoel", "rillerig", "rillingen",
        "koude rillingen", "warm", "heet", "zweten", "zweeterig",
        "diarree", "buikloop", "constipatie", "verstopping", "obstipatie",
        "opgezet", "opgeblazen", "blozend", "rode vlekken", "uitslag",
        "jeuk", "jeuken", "krabben", "allergisch", "allergie", "dokter",
        "ziekenhuis", "emergency", "spoed", "ambulance", "medicijnen",
        "pillen", "paracetamol", "ibuprofen", "antibiotica", "rust",
        "herstel", "beterschap", "recover", "recovery", "healing",
        "ziek thuis", "ziekmelden", "koude", "griepje", "viraal"
    ]
    
    # Tel woorden voor elke emotie
    for woord in blije_woorden:
        if woord in tekst_lower:
            scores["blij"] += 2
    
    for woord in boze_woorden:
        if woord in tekst_lower:
            scores["boos"] += 2
    
    for woord in verdrietige_woorden:
        if woord in tekst_lower:
            scores["verdrietig"] += 2
    
    for woord in stress_woorden:
        if woord in tekst_lower:
            scores["gestrest"] += 2
    
    for woord in verveling_woorden:
        if woord in tekst_lower:
            scores["verveeld"] += 2
    
    for woord in enthousiaste_woorden:
        if woord in tekst_lower:
            scores["enthousiast"] += 2
    
    for woord in moe_woorden:
        if woord in tekst_lower:
            scores["moe"] += 2
    
    for woord in verliefde_woorden:
        if woord in tekst_lower:
            scores["verliefd"] += 2
    
    for woord in bange_woorden:
        if woord in tekst_lower:
            scores["bang"] += 2
    
    for woord in verwarde_woorden:
        if woord in tekst_lower:
            scores["verward"] += 2
    
    for woord in zieke_woorden:
        if woord in tekst_lower:
            scores["ziek"] += 2
    
    # === INTERPUNCTIE ANALYSE ===
    # Uitroeptekens = enthousiasme of boosheid
    uitroeptekens = tekst.count("!")
    if uitroeptekens > 0:
        scores["enthousiast"] += uitroeptekens
        scores["boos"] += uitroeptekens * 0.5
    
    # Veel vraagtekens = verwarring
    vraagtekens = tekst.count("?")
    if vraagtekens > 1:
        scores["verward"] += vraagtekens
    
    # Punten puntjes = verdriet of verveling
    if "..." in tekst:
        scores["verdrietig"] += 1
        scores["verveeld"] += 1
        scores["moe"] += 1
    
    # HOOFDLETTERS = BOOSHEID of ENTHOUSIASME
    hoofdletters = sum(1 for c in tekst if c.isupper())
    if hoofdletters > len(tekst) * 0.5 and len(tekst) > 3:
        scores["boos"] += 2
        scores["enthousiast"] += 1
    
    # === EMOJI DETECTIE ===
    if "😊" in tekst or "😀" in tekst or "😃" in tekst or "🙂" in tekst or "😄" in tekst:
        scores["blij"] += 3
    if "😢" in tekst or "😭" in tekst or "☹️" in tekst or "😞" in tekst:
        scores["verdrietig"] += 3
    if "😡" in tekst or "😠" in tekst or "🤬" in tekst or "😤" in tekst:
        scores["boos"] += 3
    if "😴" in tekst or "🥱" in tekst or "😪" in tekst:
        scores["moe"] += 3
    if "❤️" in tekst or "💕" in tekst or "😍" in tekst or "🥰" in tekst or "💖" in tekst:
        scores["verliefd"] += 3
    if "😰" in tekst or "😨" in tekst or "😱" in tekst or "🥺" in tekst:
        scores["bang"] += 3
    if "🤢" in tekst or "🤮" in tekst or "🤒" in tekst or "🤕" in tekst or "😷" in tekst:
        scores["ziek"] += 3
    if "😕" in tekst or "🤔" in tekst or "😵" in tekst or "🤨" in tekst:
        scores["verward"] += 3
    if "🥳" in tekst or "🎉" in tekst or "🎊" in tekst or "✨" in tekst:
        scores["enthousiast"] += 3
    
    # Vind hoogste score
    max_score = max(scores.values())
    
    # Als geen duidelijke emotie gedetecteerd
    if max_score == 0:
        return "neutraal", 0
    
    # Vind emotie met hoogste score
    top_emotie = max(scores, key=scores.get)
    
    # Bereken zekerheid (0-100)
    totaal_score = sum(scores.values())
    if totaal_score > 0:
        zekerheid = int((max_score / totaal_score) * 100)
    else:
        zekerheid = 0
    
    return top_emotie, zekerheid


def genereer_reactie(emotie, zekerheid, originele_tekst):
    """
    Genereert een gepaste reactie gebaseerd op de gedetecteerde emotie
    """
    
    # Emotie emoji's
    emotie_emojis = {
        "blij": "😊",
        "boos": "😤",
        "verdrietig": "😢",
        "gestrest": "😰",
        "verveeld": "😑",
        "enthousiast": "🚀",
        "moe": "😴",
        "verliefd": "💕",
        "bang": "😨",
        "verward": "🤔",
        "ziek": "🤒",
        "neutraal": "😐"
    }
    
    # Reacties per emotie
    reacties = {
        "blij": [
            "Wat fijn dat je je blij voelt! Blijf genieten!",
            "Yes! Positieve vibes! Vertel, wat maakt je zo blij?",
            "Super om te horen dat het goed met je gaat!",
            "Blijdschap is aanstekelijk! Ik voel me nu ook vrolijker!"
        ],
        "boos": [
            "Ik merk dat je boos bent... Wil je erover praten?",
            "Dat klinkt frustrerend! Soms helpt het om even te ventileren.",
            "Oei, ik voel de boosheid hier! Neem even een pauze als dat helpt.",
            "Boosheid is een normale emotie. Adem even diep in en uit!"
        ],
        "verdrietig": [
            "Ik hoor dat je verdrietig bent... Dat is moeilijk.",
            "Het spijt me dat je je zo voelt. Wil je erover praten?",
            "Verdriet mag er zijn. Je bent niet alleen!",
            "Soms hebben we gewoon een rotdag. Morgen is een nieuwe dag!"
        ],
        "gestrest": [
            "Wow, dat klinkt als veel stress! Pak je het stap voor stap aan?",
            "Stress herken ik! Probeer even een pauze te nemen.",
            "Je kan dit aan! Eén ding tegelijk.",
            "Misschien helpt het om even wat anders te doen? Een wandeling?"
        ],
        "verveeld": [
            "Verveling detected! Zoek je iets leuks om te doen?",
            "Meh... saai hè? Misschien tijd voor iets nieuws!",
            "Verveling is tijdelijk! Binnenkort gebeurt er vast iets leuks.",
            "Verveeld? Perfect moment om iets creatiefs te proberen!"
        ],
        "enthousiast": [
            "WOW! Ik voel je enthousiasme! Vertel meer!",
            "Yes! Die energie! Waar ben je zo enthousiast over?",
            "Super spannend! Ik word ook enthousiast nu!",
            "Zo veel energie! Geweldig! Geniet ervan!"
        ],
        "moe": [
            "Je klinkt moe... Misschien tijd voor een powernap?",
            "Rust is belangrijk! Luister naar je lichaam.",
            "Moeheid is een signaal. Zorg goed voor jezelf!",
            "Even bijkomen kan wonderen doen. Pak je rust!"
        ],
        "verliefd": [
            "Awww, verliefdheid! Wat romantisch!",
            "Liefde in de lucht! Vlinders in je buik?",
            "Zo schattig! Verliefd zijn is een mooi gevoel!",
            "Oeh la la! Vertel, wie is de gelukkige?"
        ],
        "bang": [
            "Ik merk dat je bang of ongerust bent... Dat is begrijpelijk.",
            "Angst kan overweldigend zijn. Je bent niet alleen!",
            "Soms helpt het om je zorgen te delen. Ik luister!",
            "Angstige gedachten zijn vaak erger dan de realiteit. Je kan dit!"
        ],
        "verward": [
            "Hmm, je klinkt verward... Kan ik helpen verduidelijken?",
            "Verwarring is normaal! Laten we het samen uitzoeken.",
            "Niet alles hoeft meteen duidelijk te zijn. Geef het tijd!",
            "Verward? Stel gerust vragen, daar zijn ze voor!"
        ],
        "ziek": [
            "Oh nee! Je voelt je ziek... Beterschap!",
            "Dat klinkt niet lekker... Rust goed uit en drink veel water!",
            "Neem het rustig aan! Je lichaam heeft herstel nodig.",
            "Ziek zijn is vervelend. Hopelijk voel je je snel beter!"
        ],
        "neutraal": [
            "Hmm, ik kan niet goed inschatten hoe je je voelt...",
            "Interessant! Vertel me meer, dan kan ik je beter begrijpen.",
            "Ik ben nog aan het leren... Kun je me meer vertellen?",
            "Je emotie is niet helemaal duidelijk voor mij. Geef me meer context!"
        ]
    }
    
    # Kies een reactie
    index = len(originele_tekst) % len(reacties[emotie])
    basis_reactie = reacties[emotie][index]
    
    # Bouw de volledige reactie
    emoji = emotie_emojis[emotie]
    
    # Zekerheid visualisatie
    if zekerheid > 75:
        zekerheid_label = "Zeer zeker"
        zekerheid_bar = "█" * 10
    elif zekerheid > 50:
        zekerheid_label = "Redelijk zeker"
        zekerheid_bar = "█" * 7 + "░" * 3
    elif zekerheid > 25:
        zekerheid_label = "Enigszins zeker"
        zekerheid_bar = "█" * 5 + "░" * 5
    else:
        zekerheid_label = "Onzeker"
        zekerheid_bar = "█" * 3 + "░" * 7
    
    output = f"{emoji} Emotie: {emotie.upper()}\n"
    output += f"   Zekerheid: {zekerheid}% [{zekerheid_bar}] {zekerheid_label}\n"
    output += f"   \n"
    output += f"   💬 {basis_reactie}"
    
    return output


# Start de AI
emotie_detector()