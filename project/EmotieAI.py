def emotie_detector():
    """
    Hoofdfunctie voor de Emotie AI met mooie UI
    """
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
        "ziek": 0,
        "beschaamd": 0,
        "overweldigd": 0,
        "rustig": 0
    }
    
    # ============================================================================
    # STAP 1: STERKE UITDRUKKINGEN & WOORDCOMBINATIES (HOGE SCORES)
    # ============================================================================
    
    # === BLIJHEID - STERKE UITDRUKKINGEN ===
    blije_uitdrukkingen = [
        ("kan niet stoppen met lachen", 5),
        ("niet stoppen met lachen", 5),
        ("zo blij", 4),
        ("echt blij", 4),
        ("mega blij", 4),
        ("super blij", 4),
        ("ontzettend blij", 4),
        ("heel blij", 4),
        ("ik heb het gehaald", 5),
        ("het is gelukt", 4),
        ("alles gaat goed", 4),
        ("gaat ineens goed", 4),
        ("leukste nieuws", 5),
        ("beste nieuws", 5),
        ("geweldig nieuws", 4),
        ("fantastisch nieuws", 4),
        ("yes yes yes", 5),
        ("eindelijk gelukt", 4),
        ("ik ben gelukkig", 4),
        ("zo gelukkig", 4),
    ]
    
    # === VERDRIET - STERKE UITDRUKKINGEN ===
    verdrietige_uitdrukkingen = [
        ("voel me leeg", 5),
        ("voelt leeg", 5),
        ("voel me zo leeg", 5),
        ("gewoon leeg", 4),
        ("echt zwaar", 4),
        ("vandaag was zwaar", 4),
        ("heel zwaar", 4),
        ("ik mis", 5),
        ("mis iemand", 5),
        ("mis hem", 5),
        ("mis haar", 5),
        ("nergens zin in", 5),
        ("geen zin in", 4),
        ("niks zin in", 4),
        ("wil huilen", 5),
        ("moet huilen", 5),
        ("aan het huilen", 5),
        ("voel me rot", 4),
        ("voel me down", 4),
        ("voel me verdrietig", 5),
        ("ben verdrietig", 5),
        ("alles gaat mis", 5),
        ("niemand begrijpt", 4),
        ("zo alleen", 5),
        ("heel alleen", 5),
    ]
    
    # === BOOSHEID - STERKE UITDRUKKINGEN ===
    boze_uitdrukkingen = [
        ("wat een onzin", 5),
        ("dit is onzin", 5),
        ("zo moe van", 5),
        ("echt moe van", 5),
        ("word moe van", 5),
        ("zo klaar met", 5),
        ("ben klaar met", 5),
        ("echt klaar met", 5),
        ("helemaal klaar", 5),
        ("doet altijd moeilijk", 4),
        ("altijd moeilijk", 4),
        ("zo irritant", 4),
        ("echt irritant", 4),
        ("mega irritant", 4),
        ("verschrikkelijk irritant", 5),
        ("ik haat", 5),
        ("wat de fuck", 5),
        ("what the fuck", 5),
        ("godverdomme", 5),
        ("krijg de pest", 5),
        ("tering", 4),
        ("kanker", 4),
        ("kut", 4),
        ("klote", 4),
        ("deze shit", 4),
        ("dit gedoe", 4),
        ("zo boos", 5),
        ("echt boos", 5),
    ]
    
    # === ANGST/STRESS - STERKE UITDRUKKINGEN ===
    angstige_uitdrukkingen = [
        ("voel me nerveus", 5),
        ("zo nerveus", 5),
        ("echt nerveus", 5),
        ("bang dat ik", 5),
        ("ben bang dat", 5),
        ("ga verpesten", 5),
        ("niet op tijd", 4),
        ("krijg het niet af", 4),
        ("hoofd staat niet stil", 5),
        ("kan niet slapen", 4),
        ("niet meer slapen", 4),
        ("zo gestrest", 5),
        ("echt gestrest", 5),
        ("mega stress", 5),
        ("in paniek", 5),
        ("panieking", 5),
        ("wat als", 4),
        ("stel dat", 4),
    ]
    
    # === VERWARRING - STERKE UITDRUKKINGEN ===
    verwarde_uitdrukkingen = [
        ("weet niet wat ik moet voelen", 5),
        ("snap het niet meer", 5),
        ("begrijp het niet", 4),
        ("snap het niet", 4),
        ("weet het niet", 3),
        ("twijfel aan alles", 5),
        ("aan alles twijfelen", 5),
        ("ligt het aan mij", 4),
        ("misschien aan mij", 4),
        ("geen idee", 3),
        ("waarom", 2),
        ("hoezo", 3),
    ]
    
    # === BESCHAAMD - STERKE UITDRUKKINGEN ===
    beschaamde_uitdrukkingen = [
        ("zo gênant", 5),
        ("echt gênant", 5),
        ("mega gênant", 5),
        ("super gênant", 5),
        ("door de grond", 5),
        ("door grond zakken", 5),
        ("wil verdwijnen", 4),
        ("waarom zei ik", 5),
        ("had ik maar", 4),
        ("zo ongemakkelijk", 5),
        ("echt ongemakkelijk", 5),
        ("voel me ongemakkelijk", 5),
        ("schaam me", 5),
        ("zo beschaamd", 5),
    ]
    
    # === VERVELING/APATHIE - STERKE UITDRUKKINGEN ===
    verveelde_uitdrukkingen = [
        ("meh", 4),
        ("boeit me niet", 5),
        ("boeit niet", 4),
        ("kan me niks schelen", 4),
        ("maakt niet uit", 5),
        ("alles is saai", 5),
        ("zo saai", 4),
        ("echt saai", 4),
        ("geen energie voor", 4),
        ("doe maar wat", 4),
        ("whatever", 4),
        ("maakt mij niet uit", 5),
    ]
    
    # === PASSIEF AGRESSIEF ===
    passief_agressieve_uitdrukkingen = [
        ("ja hoor", 4),
        ("tuurlijk", 3),
        ("prima hoor", 4),
        ("doe maar", 4),
        ("laat maar", 5),
        ("is goed hoor", 4),
        ("nee is goed", 5),
    ]
    
    # === OVERWELDIGD ===
    overweldigde_uitdrukkingen = [
        ("weet niet waar ik moet beginnen", 5),
        ("niet waar beginnen", 5),
        ("alles tegelijk", 5),
        ("komt tegelijk", 5),
        ("trek dit niet", 5),
        ("kan dit niet aan", 5),
        ("te veel", 4),
        ("helemaal op", 5),
        ("compleet op", 5),
        ("ik red het niet", 5),
    ]
    
    # === VERLIEFDHEID - STERKE UITDRUKKINGEN ===
    verliefde_uitdrukkingen = [
        ("moet steeds denken aan", 5),
        ("steeds aan denken", 5),
        ("word blij als ik", 4),
        ("blij als ik zie", 4),
        ("warm vanbinnen", 5),
        ("voel me warm", 4),
        ("denk dat ik verliefd ben", 5),
        ("volgens mij verliefd", 5),
        ("ben verliefd", 5),
        ("zo verliefd", 5),
    ]
    
    # === RUSTIG/TEVREDEN - STERKE UITDRUKKINGEN ===
    rustige_uitdrukkingen = [
        ("eigenlijk best oké", 4),
        ("best oké", 4),
        ("voel me kalm", 5),
        ("ben kalm", 4),
        ("eindelijk rust", 5),
        ("rust in hoofd", 5),
        ("rust in mijn hoofd", 5),
        ("ben chill", 4),
        ("gewoon chill", 4),
        ("niks aan de hand", 4),
        ("alles is goed", 4),
    ]
    
    # === ENTHOUSIASME - STERKE UITDRUKKINGEN ===
    enthousiaste_uitdrukkingen = [
        ("ik heb het gehaald", 5),
        ("yes yes yes", 5),
        ("kan niet wachten", 5),
        ("zo excited", 5),
        ("mega excited", 5),
        ("super excited", 5),
        ("te gek", 4),
        ("echt te gek", 5),
        ("zo gaaf", 4),
        ("echt gaaf", 4),
        ("let's go", 4),
        ("letsgo", 4),
    ]
    
    # Tel uitdrukkingen
    for uitdrukking, score in blije_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["blij"] += score
    
    for uitdrukking, score in verdrietige_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["verdrietig"] += score
    
    for uitdrukking, score in boze_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["boos"] += score
    
    for uitdrukking, score in angstige_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["bang"] += score
            scores["gestrest"] += score * 0.7
    
    for uitdrukking, score in verwarde_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["verward"] += score
    
    for uitdrukking, score in beschaamde_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["beschaamd"] += score
    
    for uitdrukking, score in verveelde_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["verveeld"] += score
    
    for uitdrukking, score in passief_agressieve_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["boos"] += score * 0.8
            scores["verveeld"] += score * 0.5
    
    for uitdrukking, score in overweldigde_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["overweldigd"] += score
            scores["gestrest"] += score * 0.6
    
    for uitdrukking, score in verliefde_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["verliefd"] += score
    
    for uitdrukking, score in rustige_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["rustig"] += score
    
    for uitdrukking, score in enthousiaste_uitdrukkingen:
        if uitdrukking in tekst_lower:
            scores["enthousiast"] += score
    
    # ============================================================================
    # STAP 2: LOSSE WOORDEN (LAGERE SCORES)
    # ============================================================================
    
    # === BLIJHEID ===
    blije_woorden = [
        "blij", "happy", "gelukkig", "fijn", "leuk", "geweldig", "super", 
        "fantastisch", "top", "yes", "yeah", "joepie", "hoera",
        "genieten", "lachen", "lol", "plezier", "yay", "jaaa", "nice",
        "perfect", "heerlijk", "zalig", "mooi", "prachtig",
        "vrolijk", "opgewekt", "stralend", "uitgelaten", "positief",
        "tevreden", "dankbaar", "blessed", "geluk", "goed nieuws",
        "gefeliciteerd", "hoezee", "joehoe", "jeej", "awesome", "cool",
        "vet", "gaaf", "chill", "relaxed", "lekker", "goed gevoel",
        "trots", "succesvol", "gelukt", "eindelijk", "wauw", "goed gedaan",
        "toppertje", "kippenvel"
    ]
    
    # === BOOSHEID ===
    boze_woorden = [
        "boos", "kwaad", "irritant", "pissed", "geïrriteerd", "vervelend",
        "stomme", "idioot", "verschrikkelijk", "haat", "grr", "wtf",
        "onzin", "belachelijk", "rotzooi", "shit", "damn", "fuck",
        "woedend", "woest", "razend", "nijdig", "getergd", "gepikeerd",
        "chagrijnig", "knorrig", "gefrustreerd", "frustratie", "ergeren",
        "ergerlijk", "klote", "kut", "bullshit", "waardeloos",
        "stom", "dom", "achterlijk", "debiel", "mongo",
        "godverdomme", "krijg de pest", "gestoord", 
        "vreselijk", "afschuwelijk", "walgelijk", "misselijk makend",
        "kutzooi", "zooi", "bagger", "puinhoop", "drama", "gedoe",
        "geneuzel", "gelul", "gezeik", "gezeur", "gejank", "geklaag",
        "argh", "pfff", "bah", "vies", "smerig",
        "rot op", "zeik", "lul niet", "tering", "kanker"
    ]
    
    # === VERDRIET ===
    verdrietige_woorden = [
        "verdrietig", "down", "depri", "somber", "rot", "naar",
        "eenzaam", "alleen", "huilen", "pijn", "gemist", "verloren",
        "teleurgesteld", "jammer", "sneu", "triest", "moeilijk", "zwaar",
        "depressief", "hopeloos", "leeg", "ongelukkig", "droevig",
        "ellendig", "beroerd", "neerslachtig", "gedeprimeerd", "moedeloos",
        "bedroefd", "gekwetst", "heartbroken", "kapot",
        "gebroken", "afgewezen", "verlaten", "gedumpt",
        "mislukt", "gefaald", "mislukking", "verlies", "gemis", "rouw",
        "spijt", "schuldig", "schaamte",
        "nutteloos", "betekenisloos", "zinloos",
        "niemand", "niks", "niets", "donker",
        "tranen", "janken", "depressie", "somberheid"
    ]
    
    # === STRESS ===
    stress_woorden = [
        "stress", "druk", "hectisch", "deadline", "chaos", "overweldigd",
        "veel te doen", "panic", "te veel", "help", "deadlines", "examen",
        "toets", "tentamen", "zenuwachtig", "gespannen", "pressure",
        "spanning", "gestrest", "onder druk", "tijdgebrek",
        "geen tijd", "haast", "snel", "rennen", "racen", "jachtig",
        "rusteloos", "onrustig", "nerveus", "kriebels", "zenuwen",
        "examenstress", "werkdruk", "overuren", "teveel werk", "overwerkt",
        "burn-out", "burnout", "opgebrand",
        "bezorgd", "zorgen", "piekeren", "tobben", "malen",
        "hoofd vol", "faalangst", "presteren"
    ]
    
    # === VERVELING ===
    verveling_woorden = [
        "verveeld", "saai", "boring", "niks te doen", "whatever",
        "boeiend", "doodsaai", "droog", "flauw", "sloom",
        "traag", "eentonig", "monotoon", "sleur", "routine",
        "beu", "ongeïnspireerd", "doelloos",
        "wachten", "gaaap"
    ]
    
    # === ENTHOUSIASME ===
    enthousiaste_woorden = [
        "enthousiast", "excited", "zin", "spannend",
        "wauw", "wow", "amazing",
        "incredible", "unbelievable", "sick", "lit", "fire",
        "hyped", "hype", "pumped", "ready", "bring it on",
        "omg", "oh my god", "yesss",
        "insane", "crazy good",
        "wild", "energie", "energiek"
    ]
    
    # === MOEHEID ===
    moe_woorden = [
        "moe", "slaperig", "uitgeput", "tired", "slaap",
        "gapen", "bed", "kapot", "doodmoe", "bekaf",
        "afgepeigerd", "op", "energieloos", "slap", "futloos",
        "suffig", "wazig", "duizelig",
        "zombie", "walking dead", "battery low",
        "geen energie", "uitgeteld", "gesloopt"
    ]
    
    # === VERLIEFDHEID ===
    verliefde_woorden = [
        "verliefd", "love", "crush", "date", "liefde", "hart", "schattig",
        "vlinders", "kus", "zoenen",
        "knuffelen", "romantisch", "romance", "relationship", "relatie",
        "butterflies", "hartjes",
        "hearts", "lovesick",
        "smoorverliefd"
    ]
    
    # === ANGST ===
    bange_woorden = [
        "bang", "scary", "eng", "angstig", "ongerust",
        "bezorgd", "angst", "fear",
        "frightened", "terrified", "doodsbang", "paniek",
        "paniekaanval", "schrikken", "shock", "trauma",
        "nachtmerrie", "nightmare", "griezelig", "creepy",
        "gevaarlijk", "onveilig", "kwetsbaar",
        "paranoia", "fobie", "anxiety", "anxious", "worried"
    ]
    
    # === VERWARRING ===
    verwarde_woorden = [
        "verward", "confused", "huh", "onduidelijk",
        "vaag", "abstract", "raadsel",
        "vreemd", "weird", "strange", "bizar", "raar", "gek",
        "lost", "verdwaald", "chaotisch",
        "ingewikkeld", "complicated", "complex",
        "twijfel", "onzekerheid", "uncertain",
        "eh", "uh", "uhm", "pardon"
    ]
    
    # === ZIEKTE ===
    zieke_woorden = [
        "ziek", "misselijk", "kotsen", "overgeven", "braken",
        "buikpijn", "maagpijn", "pijn",
        "hoofdpijn", "migraine", "koorts", "fever", "griep", "flu",
        "verkouden", "cold", "hoesten", "niezen",
        "keelpijn", "corona", "covid", "sick", "ill", "onwel",
        "niet lekker", "beroerd voelen", "zwak"
    ]
    
    # Tel losse woorden (lagere scores dan uitdrukkingen)
    for woord in blije_woorden:
        if woord in tekst_lower:
            scores["blij"] += 1.5
    
    for woord in boze_woorden:
        if woord in tekst_lower:
            scores["boos"] += 1.5
    
    for woord in verdrietige_woorden:
        if woord in tekst_lower:
            scores["verdrietig"] += 1.5
    
    for woord in stress_woorden:
        if woord in tekst_lower:
            scores["gestrest"] += 1.5
    
    for woord in verveling_woorden:
        if woord in tekst_lower:
            scores["verveeld"] += 1.5
    
    for woord in enthousiaste_woorden:
        if woord in tekst_lower:
            scores["enthousiast"] += 1.5
    
    for woord in moe_woorden:
        if woord in tekst_lower:
            scores["moe"] += 1.5
    
    for woord in verliefde_woorden:
        if woord in tekst_lower:
            scores["verliefd"] += 1.5
    
    for woord in bange_woorden:
        if woord in tekst_lower:
            scores["bang"] += 1.5
    
    for woord in verwarde_woorden:
        if woord in tekst_lower:
            scores["verward"] += 1.5
    
    for woord in zieke_woorden:
        if woord in tekst_lower:
            scores["ziek"] += 1.5
    
    # ============================================================================
    # STAP 3: INTERPUNCTIE & STYLING ANALYSE
    # ============================================================================
    
    # Uitroeptekens = enthousiasme of boosheid
    uitroeptekens = tekst.count("!")
    if uitroeptekens >= 2:
        scores["enthousiast"] += uitroeptekens * 1.5
        scores["boos"] += uitroeptekens * 0.8
    elif uitroeptekens == 1:
        scores["enthousiast"] += 1
        scores["boos"] += 0.5
    
    # Veel vraagtekens = verwarring
    vraagtekens = tekst.count("?")
    if vraagtekens >= 2:
        scores["verward"] += vraagtekens * 1.5
    elif vraagtekens == 1:
        scores["verward"] += 0.5
    
    # Punten puntjes = verdriet, verveling, moeheid
    if "..." in tekst:
        scores["verdrietig"] += 2
        scores["verveeld"] += 1.5
        scores["moe"] += 1.5
    
    # HOOFDLETTERS = BOOSHEID of ENTHOUSIASME
    hoofdletters = sum(1 for c in tekst if c.isupper())
    if hoofdletters > len(tekst) * 0.6 and len(tekst) > 5:
        scores["boos"] += 3
        scores["enthousiast"] += 2
    elif hoofdletters > len(tekst) * 0.4 and len(tekst) > 5:
        scores["boos"] += 2
        scores["enthousiast"] += 1.5
    
    # Herhaalde letters = emotie intensiteit
    import re
    # Bijvoorbeeld "zoooo", "jaaaa", "neee"
    herhalingen = re.findall(r'(.)\1{2,}', tekst_lower)
    if len(herhalingen) > 0:
        scores["enthousiast"] += len(herhalingen) * 1.5
        scores["boos"] += len(herhalingen) * 1
        scores["verdrietig"] += len(herhalingen) * 0.8
    
    # ============================================================================
    # STAP 4: EMOJI DETECTIE
    # ============================================================================
    
    if "😊" in tekst or "😀" in tekst or "😃" in tekst or "🙂" in tekst or "😄" in tekst or "😁" in tekst:
        scores["blij"] += 4
    if "😢" in tekst or "😭" in tekst or "☹️" in tekst or "😞" in tekst or "😔" in tekst:
        scores["verdrietig"] += 4
    if "😡" in tekst or "😠" in tekst or "🤬" in tekst or "😤" in tekst:
        scores["boos"] += 4
    if "😴" in tekst or "🥱" in tekst or "😪" in tekst:
        scores["moe"] += 4
    if "❤️" in tekst or "💕" in tekst or "😍" in tekst or "🥰" in tekst or "💖" in tekst or "💘" in tekst:
        scores["verliefd"] += 4
    if "😰" in tekst or "😨" in tekst or "😱" in tekst or "🥺" in tekst:
        scores["bang"] += 4
    if "🤢" in tekst or "🤮" in tekst or "🤒" in tekst or "🤕" in tekst or "😷" in tekst:
        scores["ziek"] += 4
    if "😕" in tekst or "🤔" in tekst or "😵" in tekst or "🤨" in tekst or "😵‍💫" in tekst:
        scores["verward"] += 4
    if "🥳" in tekst or "🎉" in tekst or "🎊" in tekst or "✨" in tekst or "🚀" in tekst:
        scores["enthousiast"] += 4
    if "😳" in tekst or "🫣" in tekst:
        scores["beschaamd"] += 4
    if "😑" in tekst or "😐" in tekst or "🙄" in tekst:
        scores["verveeld"] += 4
    if "😂" in tekst or "🤣" in tekst:
        scores["blij"] += 3
        scores["enthousiast"] += 2
    
    # ============================================================================
    # STAP 5: CONTEXT-AWARE ANALYSE
    # ============================================================================
    
    # Negatie detectie - "niet" + positief woord = negatief
    if "niet" in tekst_lower:
        # Als er positieve woorden na "niet" komen, verlaag blijdschap
        for woord in ["goed", "leuk", "fijn", "blij", "happy"]:
            if f"niet {woord}" in tekst_lower or f"niet zo {woord}" in tekst_lower:
                scores["blij"] = max(0, scores["blij"] - 3)
                scores["verdrietig"] += 2
    
    # Zinnen met "waarom" zijn vaak gefrustreerd of verward
    if "waarom" in tekst_lower:
        scores["verward"] += 1.5
        scores["boos"] += 1
    
    # ============================================================================
    # STAP 6: BEPAAL WINNENDE EMOTIE
    # ============================================================================
    
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
    
    # Boost zekerheid als het verschil tussen top 2 groot is
    sorted_scores = sorted(scores.values(), reverse=True)
    if len(sorted_scores) > 1 and sorted_scores[0] > 0:
        verschil = sorted_scores[0] - sorted_scores[1]
        if verschil > 5:
            zekerheid = min(100, zekerheid + 10)
    
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
        "neutraal": "😐",
        "beschaamd": "😳",
        "overweldigd": "🤯",
        "rustig": "😌"
    }
    
    # Reacties per emotie
    reacties = {
        "blij": [
            "Wat fijn dat je je blij voelt! Blijf genieten!",
            "Yes! Positieve vibes! Vertel, wat maakt je zo blij?",
            "Super om te horen dat het goed met je gaat!",
            "Blijdschap is aanstekelijk! Ik voel me nu ook vrolijker!",
            "Geweldig! Die blijdschap straalt er helemaal vanaf!",
        ],
        "boos": [
            "Ik merk dat je boos bent... Wil je erover praten?",
            "Dat klinkt frustrerend! Soms helpt het om even te ventileren.",
            "Oei, ik voel de boosheid hier! Neem even een pauze als dat helpt.",
            "Boosheid is een normale emotie. Adem even diep in en uit!",
            "Ik snap dat je gefrustreerd bent. Dat mag er zijn!",
        ],
        "verdrietig": [
            "Ik hoor dat je verdrietig bent... Dat is moeilijk.",
            "Het spijt me dat je je zo voelt. Wil je erover praten?",
            "Verdriet mag er zijn. Je bent niet alleen!",
            "Soms hebben we gewoon een rotdag. Morgen is een nieuwe dag!",
            "Dat klinkt zwaar. Zorg goed voor jezelf vandaag.",
        ],
        "gestrest": [
            "Wow, dat klinkt als veel stress! Pak je het stap voor stap aan?",
            "Stress herken ik! Probeer even een pauze te nemen.",
            "Je kan dit aan! Eén ding tegelijk.",
            "Misschien helpt het om even wat anders te doen? Een wandeling?",
            "Zo veel op je bord! Adem even rustig en maak een lijstje.",
        ],
        "verveeld": [
            "Verveling detected! Zoek je iets leuks om te doen?",
            "Meh... saai hè? Misschien tijd voor iets nieuws!",
            "Verveling is tijdelijk! Binnenkort gebeurt er vast iets leuks.",
            "Verveeld? Perfect moment om iets creatiefs te proberen!",
            "Snap het, soms is alles gewoon... meh.",
        ],
        "enthousiast": [
            "WOW! Ik voel je enthousiasme! Vertel meer!",
            "Yes! Die energie! Waar ben je zo enthousiast over?",
            "Super spannend! Ik word ook enthousiast nu!",
            "Zo veel energie! Geweldig! Geniet ervan!",
            "Wow die hype! Ik voel het helemaal!",
        ],
        "moe": [
            "Je klinkt moe... Misschien tijd voor een powernap?",
            "Rust is belangrijk! Luister naar je lichaam.",
            "Moeheid is een signaal. Zorg goed voor jezelf!",
            "Even bijkomen kan wonderen doen. Pak je rust!",
            "Zo op? Ga lekker even liggen als dat kan!",
        ],
        "verliefd": [
            "Awww, verliefdheid! Wat romantisch!",
            "Liefde in de lucht! Vlinders in je buik?",
            "Zo schattig! Verliefd zijn is een mooi gevoel!",
            "Oeh la la! Vertel, wie is de gelukkige?",
            "Die verliefdheid! Ik word er warm van!",
        ],
        "bang": [
            "Ik merk dat je bang of ongerust bent... Dat is begrijpelijk.",
            "Angst kan overweldigend zijn. Je bent niet alleen!",
            "Soms helpt het om je zorgen te delen. Ik luister!",
            "Angstige gedachten zijn vaak erger dan de realiteit. Je kan dit!",
            "Dat klinkt spannend... Adem even rustig, je hebt dit!",
        ],
        "verward": [
            "Hmm, je klinkt verward... Kan ik helpen verduidelijken?",
            "Verwarring is normaal! Laten we het samen uitzoeken.",
            "Niet alles hoeft meteen duidelijk te zijn. Geef het tijd!",
            "Verward? Stel gerust vragen, daar zijn ze voor!",
            "Snap dat het onduidelijk is. Soms duurt het even voordat dingen klikken.",
        ],
        "ziek": [
            "Oh nee! Je voelt je ziek... Beterschap!",
            "Dat klinkt niet lekker... Rust goed uit en drink veel water!",
            "Neem het rustig aan! Je lichaam heeft herstel nodig.",
            "Ziek zijn is vervelend. Hopelijk voel je je snel beter!",
            "Klinkt niet fijn! Pak lekker de rust, beterschap!",
        ],
        "neutraal": [
            "Hmm, ik kan niet goed inschatten hoe je je voelt...",
            "Interessant! Vertel me meer, dan kan ik je beter begrijpen.",
            "Ik ben nog aan het leren... Kun je me meer vertellen?",
            "Je emotie is niet helemaal duidelijk voor mij. Geef me meer context!",
        ],
        "beschaamd": [
            "Oh nee, dat klinkt gênant... Maar iedereen heeft van die momenten!",
            "Beschaamd zijn is zo menselijk! Over een tijdje lach je erom.",
            "Awkward moment? Die heeft iedereen. Je bent niet de enige!",
            "Ik snap dat je je ongemakkelijk voelt. Dat gaat over!",
            "Die schaamte herken ik! Maar niemand denkt er zo lang over na als jij denkt.",
        ],
        "overweldigd": [
            "Wow, dat is veel tegelijk! Even een stapje terug nemen?",
            "Overweldigd... snap ik. Probeer het in kleine stukjes te verdelen.",
            "Dat is echt veel op je bord! Begin met één ding tegelijk.",
            "Ik voel de overload! Misschien even een lijstje maken?",
            "Zo veel tegelijk... adem even. Je hoeft niet alles nu te doen.",
        ],
        "rustig": [
            "Fijn dat je je rustig voelt! Geniet van dat moment.",
            "Kalmte is zo waardevol! Mooi dat je dat hebt.",
            "Lekker rustig in je hoofd, dat is fijn!",
            "Chill vibe! Precies wat je nodig hebt soms.",
            "Rust in je hoofd... dat is zo belangrijk. Fijn!",
        ]
    }
    
    # Kies een reactie
    index = len(originele_tekst) % len(reacties[emotie])
    basis_reactie = reacties[emotie][index]
    
    # Bouw de volledige reactie
    emoji = emotie_emojis[emotie]
    
    # Zekerheid visualisatie
    if zekerheid >= 80:
        zekerheid_label = "Zeer zeker"
        zekerheid_bar = "█" * 10
    elif zekerheid >= 65:
        zekerheid_label = "Redelijk zeker"
        zekerheid_bar = "█" * 8 + "░" * 2
    elif zekerheid >= 50:
        zekerheid_label = "Vrij zeker"
        zekerheid_bar = "█" * 6 + "░" * 4
    elif zekerheid >= 35:
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
if __name__ == "__main__":
    emotie_detector()