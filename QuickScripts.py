import os
import json
import datetime
from PairLists import *

#needed for Katakana still
def reformatSelf():
    for x in os.listdir("Database/Hiragana/"):
        path = f"Database/Hiragana/{x}"
        
        object = json.load(open(path, "r", encoding="utf-8"))
        print(object["kana"])
        
        f = open(path, "w", encoding="utf-8")
        f.write(json.dumps(object))

def popSelf():    
    for x in os.listdir("Database/Katakana/"):
        path = f"Database/Katakana/{x}"
        
        object = json.load(open(path, "r", encoding="utf-8"))
        print(object["kana"])
        
        i = giveIndexOfElement(object["similar"], object["kana"])
        print(object["similar"][i], "popped")
        object["similar"].pop(i)
        
        f = open(path, "w", encoding="utf-8")
        f.write(json.dumps(object))
    
def applyWeightToAll(weight):
    for x in os.listdir("Database/Katakana/"):
        path = f"Database/Katakana/{x}"
        
        object = json.load(open(path, "r", encoding="utf-8"))
        print(object["kana"])
        
        for y in object["similar"]:
            y[1] = weight
            print(y)
        
        f = open(path, "w", encoding="utf-8")
        f.write(json.dumps(object))
        
def addAttributeToObject():
    for x in os.listdir("Database/Katakana/"):
        path = f"Database/Katakana/{x}"
        
        object = json.load(open(path, "r", encoding="utf-8"))
        print(object["kana"])
        
        newObject = {
            "kana": object["kana"],
            "romaji": object["romaji"],        
            "similar": [["ア", "a"],["イ", "i"],["ウ", "u"],["エ", "e"],["オ", "o"],["カ", "ka"],["キ", "ki"],["ク", "ku"],["ケ", "ke"],["コ", "ko"],["サ", "sa"],["シ", "shi"],["ス", "su"],["セ", "se"],["ソ", "so"],["タ", "ta"],["チ", "chi"],["ツ", "tsu"],["テ", "te"],["ト", "to"],["ナ", "na"],["ニ", "ni"],["ヌ", "nu"],["ネ", "ne"],["ノ", "no"],["ハ", "ha"],["ヒ", "hi"],["フ", "fu"],["ヘ", "he"],["ホ", "ho"],["マ", "ma"],["ミ", "mi"],["ム", "mu"],["メ", "me"],["モ", "mo"],["ヤ", "ya"],["ユ", "yu"],["ヨ", "yo"],["ラ", "ra"],["リ", "ri"],["ル", "ru"],["レ", "re"],["ロ", "ro"],["ワ", "wa"],["ヲ", "wo"],["ン", "n"],["ガ", "ga"],["ギ", "gi"],["グ", "gu"],["ゲ", "ge"],["ゴ", "go"],["ザ", "za"],["ジ", "ji"],["ズ", "zu"],["ゼ", "ze"],["ゾ", "zo"],["ダ", "da"],["ヂ", "ji"],["ヅ", "zu"],["デ", "de"],["ド", "do"],["バ", "ba"],["ビ", "bi"],["ブ", "bu"],["ベ", "be"],["ボ", "bo"],["パ", "pa"],["ピ", "pi"],["プ", "pu"],["ペ", "pe"],["ポ", "po"],["キャ", "kya"],["キュ", "kyu"],["キョ", "kyo"],["シャ", "sha"],["シュ", "shu"],["ショ", "sho"],["チャ", "cha"],["チュ", "chu"],["チョ", "cho"],["ニャ", "nya"],["ニュ", "nyu"],["ニョ", "nyo"],["ヒャ", "hya"],["ヒュ", "hyu"],["ヒョ", "hyo"],["ミャ", "mya"],["ミュ", "myu"],["ミョ", "myo"],["リャ", "rya"],["リュ", "ryu"],["リョ", "ryo"],["ギャ", "gya"],["ギュ", "gyu"],["ギョ", "gyo"],["ジャ", "ja"],["ジュ", "ju"],["ジョ", "jo"],["ビャ", "bya"],["ビュ", "byu"],["ビョ", "byo"],["ピャ", "pya"],["ピュ", "pyu"],["ピョ", "pyo"]],
            "date": "02/21/25 18:24:56"
            }
        print(object["kana"])
        f = open(path, "w", encoding="utf-8")
        f.write(json.dumps(newObject))

def jsonMake(file, object):
    f = open(file, "w", encoding="utf-8")
    f.write(json.dumps(object))
    f.close()
    
def jsonAppend(file, element):
    object = json.load(open(file,"r", encoding="utf-8"))
    object.append(element)
    f = open(file, "w", encoding="utf-8")
    f.write(json.dumps(object))
    f.close()
           
def makeSimilarList(type):
    elements = json.load(open(f"Database/{type.capitalize()}Order.json"))
    newElements = []
    for element in elements:
        newElements.append([element, 50])
    return newElements

def appendToSimilar(path, element):
    for x in os.listdir(path):
        object = json.load(open(f"{path}{x}"))
        object["similar"].append([element, 50])
        jsonMake(f"{path}{x}", object)
    
                            
def makeEntry(type, kanji = "-", meaning = "-", onReadings = [], kunReadings = [], kana = "-", romaji = "-", date = datetime.datetime.now().strftime("%x %X")):
    match type:
        case "vocab":
            VocabObject = {
                "kanji" : kanji,
                "meaning": meaning,
                "kana" : kana,
                "similar" : makeSimilarList(type),
                "date" : date
            }
            appendToSimilar(f"Database/{type.capitalize()}/", kanji)
            jsonMake(f"Database/Vocab/{kanji}.json", VocabObject)
            jsonAppend(f"Database/{type.capitalize()}Order.json", kanji)
            
        case "kanji":
            KanjiObject = {
                "kanji" : kanji,
                "meaning": meaning,
                "onreadings": onReadings,
                "kunreadings": kunReadings,
                "similar" : makeSimilarList(type),
                "date" : date
            }
            print(KanjiObject)
            appendToSimilar(f"Database/{type.capitalize()}/", kanji)
            jsonMake(f"Database/Kanji/{kanji}.json", KanjiObject)
            jsonAppend(f"Database/{type.capitalize()}Order.json", kanji)
            
        case "katakana":
            KatakanaObject = {
                "kana" : kana,
                "romaji" : romaji,
                "similar" : makeSimilarList(type),
                "date" : date
            }
            appendToSimilar(f"Database/{type.capitalize()}/", kana)
            jsonMake(f"Database/Katakana/{kana}.json", KatakanaObject)
            jsonAppend(f"Database/{type.capitalize()}Order.json", kana)
            
        case "hiragana":
            HiraganaObject = {
                "kana" : kana,
                "romaji" : romaji,
                "similar" : makeSimilarList(type),
                "date" : date
            }
            appendToSimilar(f"Database/{type.capitalize()}/", kana)
            jsonMake(f"Database/Hiragana/{kana}.json", HiraganaObject)
            jsonAppend(f"Database/{type.capitalize()}Order.json", kana)
        
object = json.load(open("Database/KanjiGrade3.json", "r", encoding="utf-8"))
existing = os.listdir("Database/Kanji/")
for x in object:
    if f"{x[0]}.json" not in existing:
        makeEntry("kanji", kanji = x[0], meaning = x[1], onReadings = x[2], kunReadings = x[3])
    else:
        print("\n\n\n\n\n", x[0], "skipped\n\n\n\n\n")
        
#object = json.load(open("Cache/Users/496394472419098645.json", "r", encoding="utf-8"))
#for x in object["learnedHiragana"]:
#    print(x)
#applyWeightToAll(50)

