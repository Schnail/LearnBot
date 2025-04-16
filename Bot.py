import os
import random
import json
import datetime
import discord
from discord.ext import commands
from openai import OpenAI
from PairLists import *


Keys = open("Keys.txt","rt")
OPENAI_API_KEY = Keys.readline().strip("\n")
SCHNECKBOT_TOKEN = Keys.readline().strip("\n")


client = OpenAI(api_key = OPENAI_API_KEY)


description = "I can see everything you do. Do not underestimate me."

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.reactions = True
intents.voice_states = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents, help_command=commands.MinimalHelpCommand())

#-----------------------------------------------------------------------


def generateExercise(type = "random", user = None):
    if user == None:
        raise ValueError("user can not be None")
    
    match type:
        case "random":
            type = random.choice(["vocab1", "vocab2", "kanji1", "kanji2", "hiragana1", "hiragana2", "katakana1", "katakana2"])
        case "vocab":
            type = random.choice(["vocab1", "vocab2"])
        case "kanji":
            type = random.choice(["kanji1", "kanji2"])
        case "kana":
            type = random.choice(["hiragana1", "hiragana2", "katakana1", "katakana2"])
        case "katakana":
            type = random.choice(["katakana1", "katakana2"])
        case "hiragana":
            type = random.choice(["hiragana1", "hiragana2"])
        case _:
            print (f"{type} is not a valid type")      
    
    match type:
        case "hiragana1":
            answerPath = selectFromLearnedList(user, "hiragana")
            element = jsonRead(answerPath, "kana")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "hiragana", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Hiragana/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "kana"
            searched = "romaji"
            return {
                "type": "hiragana",
                "question": f"Select the sound this character makes: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }
            
        case "hiragana2":
            answerPath = selectFromLearnedList(user, "hiragana")
            element = jsonRead(answerPath, "kana")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "hiragana", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Hiragana/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "romaji"
            searched = "kana"
            return {
                "type": "hiragana",
                "question": f"Select the Hiragana character that makes this sound: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }
            
        case "katakana1":
            answerPath = selectFromLearnedList(user, "katakana")
            element = jsonRead(answerPath, "kana")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "katakana", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Katakana/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "kana"
            searched = "romaji"
            return {
                "type": "katakana",
                "question": f"Select the sound this character makes: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }
            
        case "katakana2":
            answerPath = selectFromLearnedList(user, "katakana")
            element = jsonRead(answerPath, "kana")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "katakana", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Katakana/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "romaji"
            searched = "kana"
            return {
                "type": "katakana",
                "question": f"Select the Katakana character that makes this sound: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }
            
        case "kanji1":
            answerPath = selectFromLearnedList(user, "kanji")
            element = jsonRead(answerPath, "kanji")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "kanji", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Kanji/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "kanji"
            searched = "meaning"
            return {
                "type": "kanji",
                "question": f"What is the meaning of this character: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }
            
        case "kanji2":
            answerPath = selectFromLearnedList(user, "kanji")
            element = jsonRead(answerPath, "kanji")
            similarList = jsonRead(answerPath, "similar")
            choices = removeChoicesFromSimilar(user, "kanji", similarList, element)
            SubjectPaths = []
            for x in range(0, 3):
                element = pickWeightedRandom(choices, getTotalWeight(choices))
                SubjectPaths.append(f"Database/Kanji/{element[0]}.json")
                choices.remove(element)
                
            rshift = random.randrange(0,4)     
            SubjectPaths.insert(rshift, answerPath)
            given = "meaning"
            searched = "kanji"
            return {
                "type": "kanji",
                "question": f"Select the Kanji that has this meaning: **{jsonRead(SubjectPaths[0 + rshift],given)}**",
                "options":[f"1️⃣: **{jsonRead(SubjectPaths[0],searched)}**", f"2️⃣: **{jsonRead(SubjectPaths[1],searched)}**", f"3️⃣: **{jsonRead(SubjectPaths[2],searched)}**", f"4️⃣: **{jsonRead(SubjectPaths[3],searched)}**"],
                "answer": rshift,
                "optionfiles": SubjectPaths,
                "searchedversion": searched
                }


def selectFromLearnedList(user, type):
    translateType = {
        "hiragana": "learnedHiragana",
        "katakana": "learnedKatakana",
        "kanji": "learnedKanji",
        "vocab": "learnedVocab"
    }
    
    userObject = json.load(open(f"Cache/Users/{user.id}.json"))
    totalweight = getTotalWeight(userObject[translateType[type]])
    elementcount = len(userObject[translateType[type]])
    if totalweight / elementcount < 50 and elementcount < len(os.listdir(f"Database/{type.capitalize()}/")):
        element = json.load(open(f"Database/{type.capitalize()}Order.json"))[elementcount]
        userObject[translateType[type]].append([element, 53])
        jsonMake(f"Cache/Users/{user.id}.json", userObject)
        print(f"MILESTONE: new {type} added to {user.name}'s learned list: {element}")
    else:
        element = pickWeightedRandom(userObject[translateType[type]], totalweight)[0]
        
    return f"Database/{type.capitalize()}/{element}.json"


def removeChoicesFromSimilar(user, type, similarList, element):
    translateType = {
        "hiragana": "learnedHiragana",
        "katakana": "learnedKatakana",
        "kanji": "learnedKanji",
        "vocab": "learnedVocab"
    }
    userObject = json.load(open(f"Cache/Users/{user.id}.json"))
    elementcount = len(userObject[translateType[type]])
    
    if elementcount < 3:
        defaultOrder = json.load(open(f"Database/{type.capitalize()}Order.json"))
        defaultOrder.remove(element)
        return makePairList(defaultOrder[0:4],[50,50,50,50])
    
    else:
        learnedchars = seperatePairList(userObject[translateType[type]])[0]
        print(learnedchars)
        print(similarList)
        choices = similarList.copy()
        for x in similarList:
            remove = True
            for y in learnedchars:
                if x[0] == y:
                    remove = False
                    
            if remove:            
                choices.remove(x)
                       
        return choices
    
    


async def resolveRegen(requestId, selection, user, channel):
    match selection:
        case 0:
            print("user added weird reaction")
            return None
        case 1:
            oldExercise = jsonRead(f"Cache/users/{user.id}.json", "pendingExercise")
            await voidCache(f"Cache/Active/{oldExercise}.json")
            type = jsonRead(f"Cache/KillRequests/{requestId}.json", "type")
            await createInstance(user, channel, type)
            print("regenerated exercise")
            
        case 2:
            print("void request")
    
    await voidCache(f"Cache/KillRequests/{requestId}.json")

      
async def resolveExercise(exerciseId, selection, user, channel):
    print(f"resolveExercise: User '{user.name}' resolved Exercise '{exerciseId}' in channel '{channel.name}'")
    ExerciseFile = f"Cache/Active/{exerciseId}.json"
    ExerciseStats = json.load(open(ExerciseFile, "r", encoding="utf-8"))
    rshift = ExerciseStats["answer"]
    type = ExerciseStats["type"]
    optionfiles = ExerciseStats["optionfiles"]
    solutionfile = optionfiles[rshift]
    correctChoice = jsonRead(solutionfile,ExerciseStats["searchedversion"])
    
    translateTypeSolved = {
        "hiragana": "solvedHiragana",
        "katakana": "solvedKatakana",
        "kanji": "solvedKanji",
        "vocab": "solvedVocab"
    }
    translateTypeElement = {
        "hiragana": "kana",
        "katakana": "kana",
        "kanji": "kanji",
        "vocab": "kanji"
    }
    translateTypeLearned = {
        "hiragana": "learnedHiragana",
        "katakana": "learnedKatakana",
        "kanji": "learnedKanji",
        "vocab": "learnedVocab"
    }
    
    correctelementObject = json.load(open(solutionfile, "r", encoding="utf-8"))
    correctelement = correctelementObject[translateTypeElement[type]]
    
            
    match selection:
        case 0:
            print("user added weird reaction")
            return None
        case 5:
            print("selected solve")
            embedVar = discord.Embed(title=f"❓ The Answer was **'{correctChoice}'**", description = "Do you want to generate a new Card?", color = 0x5534eb)
            await promptMessage(user, channel, type, embedVar, exerciseId, reactions = ["🔁", "❗"], prompttype = "regen")
            jsonMake(f"Cache/Inactive/{exerciseId}.json", ExerciseStats)
            os.remove(ExerciseFile)
        case 6:
            if type == "kanji":
                print("selected info")
                embedVar = discord.Embed(title=f"Kanji Info: '{correctelement}'", description = "", color = 0x5534eb)
                embedVar.add_field(name = f"Meaning: **{correctelementObject["meaning"]}**", value = "", inline = False)
                embedVar.add_field(name = "On-Readings:", value = f"**{str(correctelementObject["onreadings"]).strip("[]").replace(", ", "\n")}**", inline = True)
                embedVar.add_field(name = "", value = "", inline = True)
                embedVar.add_field(name = "Kun-Readings:", value = f"**{str(correctelementObject["kunreadings"]).strip("[]").replace(", ", "\n")}**", inline = True)
                await promptMessage(user, channel, type, embedVar, exerciseId, reactions = ["❌"], prompttype = "info")
            else:
                print("user added weird reaction")
                return None
            
        case _:
            
            jsonMake(f"Cache/Inactive/{exerciseId}.json", ExerciseStats)
            os.remove(ExerciseFile)
             
            correctAnswerGiven = rshift + 1 == selection
            UserFile = f"Cache/Users/{user.id}.json"
            UserStats = json.load(open(UserFile, "r", encoding="utf-8"))
            optionfiles.pop(rshift)
            
            numTruth = 0
            increment = -1
            
            if correctAnswerGiven:
                embedVar = discord.Embed(title="✅ Correct Answer!", description = "Do you want to generate a new Card?", color = 0xa4de28)
                await promptMessage(user, channel, type, embedVar, exerciseId, reactions = ["🔁", "❗"], prompttype = "regen")                      
            else:
                embedVar = discord.Embed(title="❌ Wrong Answer!", description = f"The correct choice would have been **'{correctChoice}'**.\nBut don't give up! Do you want to try another Card?", color = 0xeb345b)
                await promptMessage(user, channel, type, embedVar, exerciseId, reactions = ["🔁", "❗"], prompttype = "regen")
                increment = 1
                numTruth = 1
            
            #increment learningprogress of element in userstats
            UserStats[translateTypeSolved[type]][numTruth] = UserStats[translateTypeSolved[type]][numTruth] + 1
            i = giveIndexOfElement(UserStats[translateTypeLearned[type]], correctelement)
            UserStats[translateTypeLearned[type]][i][1] = clamp(UserStats[translateTypeLearned[type]][i][1] + increment, 1, 100)
            bsortPairList(UserStats[translateTypeLearned[type]])
            jsonMake(UserFile, UserStats)
                
            solution = json.load(open(solutionfile, "r", encoding="utf-8"))
               
            for optionfile in optionfiles:
                option = json.load(open(optionfile, "r", encoding="utf-8"))
                
                #increment solution list for every iteration/option
                element = option[translateTypeElement[type]]
                print(giveIndexOfElement(solution["similar"], element))
                i = giveIndexOfElement(solution["similar"], element)
                solution["similar"][i][1] = clamp(solution["similar"][i][1] + increment, 1, 100)
                bsortPairList(solution["similar"])
                
                #increment every option once
                element = solution[translateTypeElement[type]]
                i = giveIndexOfElement(option["similar"], element)
                option["similar"][i][1] = clamp(option["similar"][i][1] + increment, 1, 100)
                bsortPairList(option["similar"])
                jsonMake(optionfile, option)
            jsonMake(solutionfile, solution)    

                       
    

            
def hasActive(user):
    oldExerciseId = jsonRead(f"Cache/Users/{user.id}.json","pendingExercise")
    return f"{oldExerciseId}.json" in os.listdir("Cache/Active/")


async def voidCache(requestPath):
    oldRequest = json.load(open(requestPath,"r", encoding="utf-8"))
    channel = await bot.fetch_channel(oldRequest["channel"])
    message = await channel.fetch_message(oldRequest["message"])
    await message.delete()    
    os.remove(requestPath)


async def killRequest(user, channel, type):   
    oldRequestId = jsonRead(f"Cache/Users/{user.id}.json","pendingKillRequest")
    if f"{oldRequestId}.json" in os.listdir("Cache/KillRequests/"):
        await voidCache(f"Cache/KillRequests/{oldRequestId}.json")
        
    embedVar = discord.Embed(title=f"{user.name}, you still have a pending Exercise.", description = "Do you want to remove it and generate a new one?", color = 0xeb345b)    
    InstanceMessage = await channel.send(embed = embedVar)
    reactions = ["✅", "❌"]
    
    await reactionsAdd(InstanceMessage, reactions)
    
    Instance = {
    "channel": channel.id,
    "message": InstanceMessage.id,
    "author": user.id,
    "type": type
    }
    
    jsonMake(f"Cache/KillRequests/{InstanceMessage.id}.json", Instance)
    jsonChange(f"Cache/Users/{user.id}.json", "pendingKillRequest", f"{InstanceMessage.id}")
    
async def promptMessage(user, channel, type, embedVar, exerciseId, reactions = ["🔁"], prompttype = "regen"):   
    oldRequestId = jsonRead(f"Cache/Users/{user.id}.json","pendingPrompt")
    if f"{oldRequestId}.json" in os.listdir("Cache/Prompts/"):
        await voidCache(f"Cache/Prompts/{oldRequestId}.json")
   
    InstanceMessage = await channel.send(embed = embedVar)
    
    await reactionsAdd(InstanceMessage, reactions)
    
    Instance = {
    "channel": channel.id,
    "message": InstanceMessage.id,
    "author": user.id,
    "type": type,
    "prompttype": prompttype,
    "exerciseId": exerciseId
    }
    
    jsonMake(f"Cache/Prompts/{InstanceMessage.id}.json", Instance)
    jsonChange(f"Cache/Users/{user.id}.json", "pendingPrompt", f"{InstanceMessage.id}")
    
    
async def createInstance(user, channel, type):
    
    if registeredUser(user):
        if hasActive(user):
            await killRequest(user, channel, type)
            return False
    else:
        makeUser(user)
        
    Exercise = generateExercise(type, user)
    
    embedVar = discord.Embed(title=f"{(Exercise["type"].capitalize())} exercise for {user.name}", description = Exercise["question"], color = 0x5534eb)
    embedVar.add_field(name = Exercise["options"][0], value = "", inline = True)
    embedVar.add_field(name = "", value = "", inline = True)
    embedVar.add_field(name = Exercise["options"][1], value = "", inline = True)
    embedVar.add_field(name = "", value = "", inline = False)
    embedVar.add_field(name = Exercise["options"][2], value = "", inline = True)
    embedVar.add_field(name = "", value = "", inline = True)
    embedVar.add_field(name = Exercise["options"][3], value = "", inline = True)
    

    InstanceMessage = await channel.send(embed = embedVar)
    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "❓"]
    if Exercise["type"] == "kanji":
        reactions.append("🔎")
    
    await reactionsAdd(InstanceMessage, reactions)
    
    Instance = {
        "message": InstanceMessage.id,
        "channel": channel.id,
        "author": user.id
        }
    Instance.update(Exercise)
    
    jsonMake(f"Cache/Active/{InstanceMessage.id}.json", Instance)
    jsonChange(f"Cache/Users/{user.id}.json", "pendingExercise", f"{InstanceMessage.id}")
    

def registeredUser(user):
    return f"{user.id}.json" in os.listdir("Cache/Users")

def makeUser(user):
    userObject = {
        "name": user.name,
        "id": user.id,
        "lerningscore": 0,
        "grade": 1,
        "solvedVocab": [0,0],
        "solvedKanji": [0,0],
        "solvedHiragana": [0,0],
        "solvedKatakana": [0,0],
        "learnedVocab": [["konnichiwa", 50]],
        "learnedKanji": [["一", 50]],
        "learnedHiragana": [["あ", 50]],
        "learnedKatakana": [["ア", 50]],
        "pendingExercise": "path",
        "pendingKillRequest": "path",
        "pendingPrompt": "path"
    }
    jsonMake(f"Cache/Users/{user.id}.json", userObject)
    
   
async def reactionsAdd(message, reactions = []):
    for x in reactions:
        await message.add_reaction(x)
        
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
                        
def generateVocab():
    Response = ""
    NewEntry = json.load(Response)

        
def jsonRead(file, parm):
    newvalue = json.load(open(file,"r", encoding="utf-8"))
    return newvalue[parm]

def jsonChange(file, parm, value):
    newvalue = json.load(open(file,"r", encoding="utf-8"))
    newvalue[parm] = value
    f = open(file, "w", encoding="utf-8")
    f.write(json.dumps(newvalue))
    f.close()
    return value

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
    
def pickFiles(path, N = 1):
    choices = os.listdir(path)
    picks = []
    
    for x in range(0, N):
        pick = random.choice(choices)
        picks.append(path + "/" + pick)
        choices.remove(pick)
        
    return picks


def calculatePercent(val1, val2):
    if val1 == 0:
        return 0
    return 100 * (val1 / (val1 + val2))
    

async def generateLearnerProfile(user, channel):
    userObject = json.load(open(f"Cache/Users/{user.id}.json"))
       
    HiraganaSolved = userObject["solvedHiragana"][0]
    HiraganaAccuracy = round(calculatePercent(HiraganaSolved, userObject["solvedHiragana"][1]), 1)
    HiraganaProgress = len(userObject["learnedHiragana"])
    HiraganaMastery = round(0.02*(100-(getTotalWeight(userObject["learnedHiragana"]) / len(userObject["learnedHiragana"])))-1, 2)
    
    KatakanaSolved = userObject["solvedKatakana"][0]
    KatakanaAccuracy = round(calculatePercent(KatakanaSolved, userObject["solvedKatakana"][1]), 1)
    KatakanaProgress = len(userObject["learnedKatakana"])
    KatakanaMastery = round(0.02*(100-(getTotalWeight(userObject["learnedKatakana"]) / len(userObject["learnedKatakana"])))-1, 2)
    
    KanjiSolved = userObject["solvedKanji"][0]
    KanjiAccuracy = round(calculatePercent(KanjiSolved, userObject["solvedKanji"][1]), 1)
    KanjiProgress = len(userObject["learnedKanji"])
    KanjiMastery = round(0.02*(100-(getTotalWeight(userObject["learnedKanji"]) / len(userObject["learnedKanji"])))-1, 2)
    
    VocabSolved = userObject["solvedVocab"][0]
    VocabAccuracy = round(calculatePercent(VocabSolved, userObject["solvedVocab"][1]), 1)
    VocabProgress = len(userObject["learnedVocab"])
    VocabMastery = round(0.02*(100-(getTotalWeight(userObject["learnedVocab"]) / len(userObject["learnedVocab"])))-1, 2)
    
    learningscore = round((HiraganaSolved * HiraganaAccuracy * (9 * HiraganaMastery + 1) * 0.01) + (KatakanaSolved * KatakanaAccuracy * (9 * KatakanaMastery + 1) * 0.01) + (KanjiSolved * KanjiAccuracy * (9 * KanjiMastery + 1) * 0.03) + (VocabSolved * VocabAccuracy * (9 * VocabMastery + 1) * 0.05), 2)
    
    embedVar = discord.Embed(title=f"{user.name}'s Profile", description = "", color = 0x5534eb, thumbnail = user.avatar.url)
    embedVar.add_field(name = f"Learningscore: **{learningscore}**", value = "", inline = False)
    embedVar.add_field(name = "Hiragana", value = "Progress:\nSolved Cards:\nAccuracy:\nMastery:", inline = True,)
    embedVar.add_field(name = "\u200B", value = f"**{HiraganaProgress}/104**\n**{HiraganaSolved}**\n**{HiraganaAccuracy}%**\n**{HiraganaMastery}**", inline = True,)
    embedVar.add_field(name = "", value = "", inline = False,)
    embedVar.add_field(name = "Katakana", value = "Progress:\nSolved Cards:\nAccuracy:\nMastery:", inline = True,)
    embedVar.add_field(name = "\u200B", value = f" **{KatakanaProgress}/104**\n**{KatakanaSolved}**\n**{KatakanaAccuracy}%**\n**{KatakanaMastery}**", inline = True,)
    embedVar.add_field(name = "", value = "", inline = False,)
    embedVar.add_field(name = "Kanji", value = "Progress:\nSolved Cards:\nAccuracy:\nMastery:", inline = True,)
    embedVar.add_field(name = "\u200B", value = f"**{KanjiProgress}/{len(os.listdir("Database/Kanji/"))}**\n**{KanjiSolved}**\n**{KanjiAccuracy}%**\n**{KanjiMastery}**", inline = True,)
    embedVar.add_field(name = "", value = "", inline = False,)
    embedVar.add_field(name = "Vocabulary (coming soon)", value = "Progress:\nSolved Cards:\nAccuracy:\nMastery:", inline = True,)
    embedVar.add_field(name = "\u200B", value = f"**{VocabProgress}/1**\n**{VocabSolved}**\n**{VocabAccuracy}%**\n**{VocabMastery}**", inline = True,)
    
    await channel.send(embed = embedVar)
    
async def generateTutorial(channel):
    embedVar1 = discord.Embed(title="Guide", description = "How to practice Japanese with Schneckbot", color = 0x5534eb, )
    embedVar1.add_field(name = "Commands:", value = "!tutorial: Shows this Guide.\n!practice: Generates an Exercise Card of the given Type.\n!profile: Shows the given users Profile. Shows your Profile if no user is specified.", inline = False)
    
    embedVar2 = discord.Embed(title="Practice", description = "Alternative commands: !japanese, !learn", color = 0x5534eb)
    embedVar2.add_field(name = "Generates an Exercise Card", value = "You can specify the type of exercise you want to do by including the type after the command e.g. '!learn hiragana'\n Valid types are:\n 'hiragana', 'katakana', 'kana', 'kanji', 'vocab'", inline = False)
    embedVar2.add_field(name = "Solve", value = "You can solve the card by reacting to the card with the corresponding Emoji. Reacting with ❓ will solve the Card without affecting your Userstats. After resolving a card you can generate a new Card of the same Type by reacting with 🔁 to the resolve Notification.", inline = False)
    embedVar2.add_field(name = "Kanji", value = "If you are practicing Kanji you will have the option to react with 🔎 to recive information on the Kanji's different readings.", inline = False)
    embedVar2.add_field(name = "Report", value = "If a Exercise seems like it has an Error of any kind, you can report it by reacting with ❗ on the resolve Notification so I can take a look at it. This doesn't work anymore if you already generated a new Card.", inline = False)
    embedVar2.set_image(url = "https://cdn.discordapp.com/attachments/1293565494393049138/1344302820685512785/image.png")
    
    embedVar3 = discord.Embed(title="Profile", description = "Alternative commands: !user, !stats", color = 0x5534eb)
    embedVar3.add_field(name = "Shows the given users Profile.", value = "Shows your Profile if no user is specified.", inline = False)
    embedVar3.set_image(url = "https://cdn.discordapp.com/attachments/1293565494393049138/1344305741716132070/image.png")
    
    await channel.send(embed=embedVar1)
    await channel.send(embed=embedVar2) 
    await channel.send(embed=embedVar3) 
#-----------------------------------------------------------------------

@bot.command(aliases=["japanese", "learn"], category = "learning", brief="Generates an Exercise Card of the given Type.", description="Generates an Exercise Card of the given Type for the user.\nValid Types: ['hiragana', 'katakana', 'kana', 'kanji', 'vocab']")
async def practice(ctx, type = "kana"): #change to random later
    await createInstance(ctx.author, ctx.channel, type)
    await ctx.message.delete()

@bot.command(aliases=["user", "stats"], category = "learning", brief="Shows the given users Profile.", description= "Shows the given users Profile. Shows your Profile if no user is specified.")
async def profile(ctx):
    if len(ctx.message.mentions) >= 1:
        await ctx.send("Try '!profile @User'")
    elif not ctx.message.mentions:
        await generateLearnerProfile(ctx.author, ctx.message.channel)
    else:
        await generateLearnerProfile(ctx.message.mentions[0], ctx.message.channel)
    
@bot.command(aliases= ["intro", "info", "guide"], category = "learning", brief="Shows the Tutorial for the learning functionality.", description="Shows the Tutorial for the learning functionality.")
async def tutorial(ctx):
    await generateTutorial(ctx.message.channel)
    


#-----------------------------------------------------------------------   
 
@bot.event
async def on_ready():
    print("Bot Ready")
    for x in os.listdir("Cache/KillRequests/"):
        os.remove(f"Cache/KillRequests/{x}")
    for x in os.listdir("Cache/Prompts/"):
        os.remove(f"Cache/Prompts/{x}")
    for x in os.listdir("Cache/Active/"):
        os.remove(f"Cache/Active/{x}")
    for x in os.listdir("Cache/Inactive/"):
        os.remove(f"Cache/Inactive/{x}")
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if user.id == bot.user.id:
        print("bot reaction")
        return False
    
    if f"{reaction.message.id}.json" in os.listdir("Cache/Active/"):
        path = f"Cache/Active/{reaction.message.id}.json"
        Instance = json.load(open(path,"r", encoding="utf-8"))
        if Instance["author"] == user.id:
            selection = 0
            dict = {
                "1️⃣":1,  
                "2️⃣":2,
                "3️⃣":3,
                "4️⃣":4,
                "❓":5,
                "🔎":6
                }
            selection = dict[reaction.emoji]
            await resolveExercise(Instance["message"], selection, user, reaction.message.channel)
            if reaction.emoji == "🔎":
                await reaction.remove(user)
        else:
            await reaction.remove(user)
            print("exercise reaction removed:", Instance["author"], user.id)
            
    if f"{reaction.message.id}.json" in os.listdir("Cache/KillRequests/"):
        path = f"Cache/KillRequests/{reaction.message.id}.json"
        Instance = json.load(open(path,"r", encoding="utf-8"))
        print(Instance["author"] == user.id)
        if Instance["author"] == user.id:
            selection = 0
            dict = {
                "✅":1,  
                "❌":2
                }
            selection = dict[reaction.emoji]
            await resolveRegen(Instance["message"], selection, user, reaction.message.channel)
        else:
            await reaction.remove(user)
            print("kill reaction removed", Instance["author"], user.id)
            
    if f"{reaction.message.id}.json" in os.listdir("Cache/Prompts/"):
        path = f"Cache/Prompts/{reaction.message.id}.json"
        Instance = json.load(open(path,"r", encoding="utf-8"))
        
        if Instance["author"] == user.id:
            if reaction.emoji == "🔁" and Instance["prompttype"] == "regen":
                await reaction.message.clear_reactions()
                type = jsonRead(f"Cache/Prompts/{Instance["message"]}.json", "type")
                await createInstance(user, reaction.message.channel, type)
                print("generated new exercise")
                os.remove(f"Cache/Inactive/{Instance["exerciseId"]}.json")   
                os.remove(path)
            elif reaction.emoji == "❗" and Instance["prompttype"] == "regen":
                exercise = json.load(open(f"Cache/Inactive/{Instance["exerciseId"]}.json"))
                jsonMake(f"Cache/Reported/{Instance["exerciseId"]}.json", exercise)
                print("reported exercise")
                await reaction.message.channel.send("Card was reported.")
            elif reaction.emoji == "❌" and Instance["prompttype"] == "info":
                await voidCache(f"Cache/Prompts/{reaction.message.id}.json")
                
            else:
                await reaction.remove(user)
            
        else:
            await reaction.remove(user)
            print("prompt reaction removed", Instance["author"], user.id)
        

#-----------------------------------------------------------------------

bot.run(token = SCHNECKBOT_TOKEN, reconnect = True)