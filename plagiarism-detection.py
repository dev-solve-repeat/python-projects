from difflib import SequenceMatcher

with open('plagiarism-files/demo1.txt') as fileOne, open('plagiarism-files/demo2.txt') as fileTwo:

    data_file1 = fileOne.read()
    data_file2 = fileTwo.read()

    matches = SequenceMatcher(None, data_file1, data_file2).ratio()

    print(f" The plagiarized content is {matches * 100}% ")