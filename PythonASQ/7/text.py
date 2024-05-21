import re

debug = True

def worthäufigkeit(text: str, minLength = 0) -> list[tuple[str,int]]:
    text = text.lower()
    nonLetterPattern = re.compile(r"[^a-zäöüß]")
    text = nonLetterPattern.sub(" ", text)
    multispacesPattern = re.compile(r"\s+")
    text = multispacesPattern.sub(" ", text).strip()
    dictionary = {}
    words = text.split(" ")
    for word in words:
        if len(word) >= minLength:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return sorted(dictionary.items(), key = lambda x: x[1], reverse = True)

def getNumSentences(text: str) -> int:
    sentencePattern = re.compile(r"[.!?]")
    return len(sentencePattern.findall(text))

def getASW(words: list[str]) -> float:
    vocalsPattern = re.compile(r"[aeiouäöü]+")
    numVocals = 0
    for word in words:
        numVocalsInWord = len(vocalsPattern.findall(word))
        numVocals += numVocalsInWord if numVocalsInWord > 1 else 1
    if debug:
        print("numVocals:",numVocals)
    return numVocals / len(words)

def lesbarkeit(text: str) -> float:
    numSentences = getNumSentences(text)
    
    # Preprocessing: Remove all non-letter characters and multiple spaces
    text = text.lower()
    LetterPattern = re.compile(r"[^a-zäöüß]")
    text = LetterPattern.sub(" ", text)
    multispacesPattern = re.compile(r"\s+")
    text = multispacesPattern.sub(" ", text).strip()
    words = text.split(" ")
    
    numWords = len(words)
    ASL = numWords / numSentences
    
    ASW = getASW(words)
    
    if debug:
        print("ASL:",ASL)
        print("ASW:",ASW)
    
    return 206.835 - 1.015 * ASL - 84.6 * ASW
    
print(worthäufigkeit("Hallo, wie geht es dir? dir$#%&/()=1234"))
print(lesbarkeit("Hallo, wie geht es dir? Ich habe dich schon lange nicht mehr gesehen. Wie war dein Urlaub?"))