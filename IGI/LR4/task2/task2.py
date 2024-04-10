from .TextOperator import TextOperator
import zipfile

def task2():
    top = TextOperator()
    with open('task2/text.txt', 'r') as f:
        text = f.read()
        top.text = text
    with open('task2/output.txt', 'w') as f:
        print(f"Sentences count: {top.sentencesCount()}\n")
        f.write(f"Sentences count: {top.sentencesCount()}\n")

        print(f"Declaritive sentences count: {top.declSentCount()}\n")
        f.write(f"Declaritive sentences count: {top.declSentCount()}\n")

        print(f"Exclamation sentences count: {top.exclSentCount()}\n")
        f.write(f"Exclamation sentences count: {top.exclSentCount()}\n")
        
        print(f"Interrogative sentences count: {top.interrogSentCount()}\n")
        f.write(f"Interrogative sentences count: {top.interrogSentCount()}\n")

        print(f"Median of sentences size: {top.medSentSize()}\n")
        f.write(f"Median of sentences size: {top.medSentSize()}\n")
    
        print(f"Median word: {top.medWordSize()}\n")
        f.write(f"Median word: {top.medWordSize()}\n")

        print(f"Emojis count: {top.emojisCount()}\n")
        f.write(f"Emojis count: {top.emojisCount()}\n")

        print(f"Words count: {top.wordsCount()}\n")
        f.write(f"Words count: {top.wordsCount()}\n")

        print(f"Word list: {top.getWordsList()}\n")
        f.write(f"Word list: {top.getWordsList()}\n")

        print(f"Change by pattern '_[a-z][A-Z]_': {top.findCapit()}\n")
        f.write(f"Change by pattern '_[a-z][A-Z]_': {top.findCapit()}\n")

        print(f"Count of words with size less than 7: {top.wordsCountLess7()}\n")
        f.write(f"Count of words with size less than 7: {top.wordsCountLess7()}\n")

        print(f"Smallest word ends with 'a': {top.findSmallestWordEndsWithA()}\n")
        f.write(f"Smallest word ends with 'a': {top.findSmallestWordEndsWithA()}\n")

        print(f"Sorted list of words: {top.sortWordsInDesc()}\n")
        f.write(f"Sorted list of words: {top.sortWordsInDesc()}\n")
    
    with zipfile.ZipFile("task2/myzip.zip", 'w') as myzip:
        myzip.write("task2/output.txt")