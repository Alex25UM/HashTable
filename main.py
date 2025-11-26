#Author: Alexander Al Dahhan
#Date: November 25th, 2025
#Collaborators: None
#Assignment: Hash table

#Copy pasted from the brightspace file
import csv
import time

class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.min_duration = line[6]
        self.production_company = line[7]
        self.quote = line[8]
        pass

def hashFunction1(stringData):
    index = 0
    for letter in stringData:
        index = index * 7 + ord(letter)
    return index

def hashFunction2(stringData):
    index = 0
    counter = 0
    for letter in stringData:
        counter += 1
        if counter % 2 == 0:
            index = index + ord(letter)
        else:
            index = index * ord(letter)

    return index

def hashFunction3(stringData):
    newString = stringData[::-1]
    index = 0
    for i in range(len(newString)):
        index += ord(newString[i]) * 3
        index += ord(newString[i]) * 5
    return index

size = 10000
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"
counter = 0

startTime1 = time.time()
startTime2 = time.time()

titleColissions = 0
quoteColissions = 0
with open(file, 'r', newline='',  encoding="utf8") as csvfile:
    print("Opening")
    reader = csv.reader(csvfile)
    for row in reader:
        if counter != 0:
            movie = DataItem(row)

            titleKey = hashFunction3(movie.movie_name)
            titleIndx = titleKey % size #just keeps the index within the bounds of the table

            while hashTitleTable[titleIndx] is not None:
                titleColissions += 1
                titleIndx = (titleIndx + 1) % size

            hashTitleTable[titleIndx] = movie

            quoteKey = hashFunction3(movie.quote)
            quoteIndx = quoteKey % size

            while hashQuoteTable[quoteIndx] is not None:
                quoteColissions += 1
                quoteIndx = (quoteIndx + 1) % size

            hashQuoteTable[quoteIndx] = movie

        counter += 1
        if counter == size:
            break

endTime1 = time.time()
endTime2 = time.time()

title_wasted = hashTitleTable.count(None)
quote_wasted = hashQuoteTable.count(None)

print("Method used: hashfunction3")
print("Rows inserted:", counter)
print("Title Hash Table colissions:", titleColissions)
print("Quote Hash Table colissions:", quoteColissions)
print("Title empty spots:", title_wasted)
print("Quote empty spots:", quote_wasted)
print("Title timer:", abs(startTime1 - endTime1), "seconds")
print("Quote timer:", abs(startTime2 - endTime2), "seconds")