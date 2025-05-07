#
# Jason H. Wells - wellsjason543 at gmail dot com - jwellsuhhuh (Discord)
#

import csv
import os
from os.path import isfile
from datetime import datetime
import re

from money import Money

class Helpers:
    @staticmethod
    def keywordSubstitution(string: str, substitutionDict: dict[str,str]): # substitute keywords
        for keyword in substitutionDict:
            # use re to find non-case-sensitive instances of keyword and substitute it
            insensitiveKeyword: re.Pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            string = insensitiveKeyword.sub(substitutionDict[keyword], string)
        return string
    
    @staticmethod
    def removeDuplicateSubstrings(string: str, minimumSubstringLength: int): # recursively remove all duplicate substrings
        stringLength = len(string)

        # Check all substrings from large to small (25 chars smallest)
        for substringLength in range(stringLength // 2, minimumSubstringLength, -1): 
            for startIndex in range(stringLength - substringLength + 1):
                substring = string[startIndex : startIndex + substringLength]
                # Check if the substring appears more than once
                if 1 < string.count(substring):
                    # delete second occurrence of longest duplicate substring
                    firstEnd = string.find(substring) + len(substring)
                    secondStart = string.find(substring, firstEnd)
                    secondEnd = secondStart + len(substring)
                    string = string[:secondStart] + string[secondEnd:]
                    
                    # recursively find new duplicate substrings
                    return Helpers.removeDuplicateSubstrings(string, minimumSubstringLength)
        
        # all substrings checked and no duplicates
        return string

class Transaction:
    def __init__(self, transactionData: list):
        self.account: str = transactionData[0]
        self.amount: Money = Money(transactionData[15]) 
        self.date: datetime = Transaction.processDate(transactionData[17])
        self.itemName: str = Transaction.flattenItemName(transactionData[9])
        self.category: str = Transaction.updateCategory(transactionData[11], self.itemName, self.amount, self.account)
    
    def __repr__(self): # NOT ACTUAL REPR
        return f'Transaction({self.account},{self.date},{self.category},{self.itemName},{self.amount}'

    @staticmethod
    def processDate(rawDate: str) -> datetime:
        # remove timestamp
        cutoffIndex = rawDate.find(' ')
        date = rawDate[:cutoffIndex] if cutoffIndex != -1 else rawDate
        
        # convert to datetime
        month, day, year = date.split('/')
        return datetime(int(year),int(month),int(day))

    @staticmethod
    def flattenItemName(rawItemName: str) -> str:
        # flatten cashnet items to just say receipt number
        if rawItemName.startswith('ECOM'):
            receiptNumber = rawItemName.split('-')[5]
            return receiptNumber
        
        # flatten gift donations to just say donator's name
        if 'JA5' in rawItemName:
            return rawItemName.split('^')[0] # only save donator's name

        # strip non alphanumeric characters
        itemName = rawItemName.strip(' -:;')

        # remove repetitive keywords
        substitutionDict: dict[str, str] = {'all university orchestra' : 'AUO',
                                            'fy25 ' : '',
                                            'pcard verification ' : '',
                                            'auo - ' : '',
                                            'auo: ' : '',
                                            'other - auo; ' : '',
                                            "'" : '',
                                            ';' : '',
                                            '  ' : ' ',
                                           }
        
        itemName = Helpers.keywordSubstitution(itemName, substitutionDict)

        # remove duplicate substrings
        return Helpers.removeDuplicateSubstrings(itemName, 25) # 25 chars smallest substring to remove

    @staticmethod
    def updateCategory(rawCategory: str, itemName: str, amount: Money, account: str) -> str:
        # search for key phrase matches in tartan connect category
        for keyPhrase in Categories.dictByRawCategory:
            if keyPhrase in rawCategory.lower():
                return Categories.dictByRawCategory[keyPhrase]
        
        # search for key phrase matches in item name
        for keyPhrase in Categories.dictByItemName:
            if keyPhrase in itemName.lower():
                return Categories.dictByItemName[keyPhrase]
    
        # no key phrase found - apply default category
        if amount.inCents < 0: 
            return 'INSTRUMENTS & SUPPLIES & OTHERS' # default agency/gift expense category
        if account == 'Gift Account':
            return 'REVENUE--DONATIONS & FUNDRAISING' # default gift revenue category
        else: 
            return 'REVENUE--JFC' # default agency revenue category

class Categories:
    dictByRawCategory = {
                         'memberships' : 'REVENUE--DUES',
                         'other student/staff revenue' : 'REVENUE--DONATIONS & FUNDRAISING',
                         'meal' : 'SOCIALS & GIFTS & MERCH',
                         'car' : 'OTHER CONCERT EXPENSES',
                         'travel' : 'OTHER CONCERT EXPENSES',
                        }
    
    dictByItemName = {
                      # one-offs 
                      'theodore' : 'MUSIC',
                      'lucks' : 'MUSIC',
                      'knoxville' : 'MUSIC',
                      'oracle' : 'GUEST COACHES & PERFORMERS',
                      'tarantino' : 'GUEST COACHES & PERFORMERS',
                      'raffle' : 'SOCIALS & GIFTS & MERCH',
                      'karoke' : 'SOCIALS & GIFTS & MERCH',
                      'coffee' : 'SOCIALS & GIFTS & MERCH',
                      'bagel' : 'SOCIALS & GIFTS & MERCH',
                      'chalk' : 'OTHER CONCERT EXPENSES',

                      # common keywords
                      'journal' : 'GUEST COACHES & PERFORMERS',
                      'guest' : 'GUEST COACHES & PERFORMERS',
                      'coach' : 'GUEST COACHES & PERFORMERS',
                      'speak' : 'GUEST COACHES & PERFORMERS',
                    
                      'ja5' : 'REVENUE--DONATIONS & FUNDRAISING',
                      'giving' : 'REVENUE--DONATIONS & FUNDRAISING',
                      'donat' : 'REVENUE--DONATIONS & FUNDRAISING',
                      'admin fee' : 'REVENUE--DONATIONS & FUNDRAISING',
                    
                      'social' : 'SOCIALS & GIFTS & MERCH',
                      'flower' : 'SOCIALS & GIFTS & MERCH',
                      'shirt' : 'SOCIALS & GIFTS & MERCH',
                      'hoodie' : 'SOCIALS & GIFTS & MERCH',
                      'ticket' : 'SOCIALS & GIFTS & MERCH',
                      'custom ink' : 'SOCIALS & GIFTS & MERCH',
                      'paint' : 'SOCIALS & GIFTS & MERCH',

                      'haul' : 'OTHER CONCERT EXPENSES',
                      'ratchet' : 'OTHER CONCERT EXPENSES',
                      'stream' : 'OTHER CONCERT EXPENSES',
                      'video' : 'OTHER CONCERT EXPENSES',
                      'record' : 'OTHER CONCERT EXPENSES',
                      'lighting' : 'OTHER CONCERT EXPENSES',
                      'tech' : 'OTHER CONCERT EXPENSES',
                      'advert' : 'OTHER CONCERT EXPENSES',
                      'poster' : 'OTHER CONCERT EXPENSES',

                      'klefstad' : 'CONDUCTOR HONORARIUM',
                      'music director' : 'CONDUCTOR HONORARIUM',
                      'conductor' : 'CONDUCTOR HONORARIUM',
                      'mandatory benefits' : 'CONDUCTOR HONORARIUM',
                      'jeffrey' : 'CONDUCTOR HONORARIUM',

                      'dues received' : 'REVENUE--DUES',

                      'carnegie' : 'CONCERT VENUE FEE',
                      'venue' : 'CONCERT VENUE FEE',
                      'deposit' : 'CONCERT VENUE FEE',
                      'balance payment' : 'CONCERT VENUE FEE',
                      'piano tuning' : 'CONCERT VENUE FEE',
                      'sailor' : 'CONCERT VENUE FEE',

                      'mute' : 'INSTRUMENTS & SUPPLIES & OTHERS',
                      'string' : 'INSTRUMENTS & SUPPLIES & OTHERS',
                      'bass' : 'INSTRUMENTS & SUPPLIES & OTHERS',

                      'sheet' : 'MUSIC',
                      'score' : 'MUSIC',
                      'piece' : 'MUSIC',
                      'print' : 'MUSIC',
                      'copy' : 'MUSIC',
                      'ink' : 'MUSIC',
                      'compos' : 'MUSIC',
                      'rented music' : 'MUSIC',
                    
                      'allocation' : 'REVENUE--JFC',
                      'surplus' : 'REVENUE--JFC',

                      'domain' : 'INSTRUMENTS & SUPPLIES & OTHERS',
                      'cabinet' : 'INSTRUMENTS & SUPPLIES & OTHERS',

                      'fundrais' : 'REVENUE--DONATIONS & FUNDRAISING',
                      'whipped' : 'REVENUE--DONATIONS & FUNDRAISING',
                      'sales tax' : 'REVENUE--DONATIONS & FUNDRAISING',

                      # more general keywords
                      'instrument' : 'INSTRUMENTS & SUPPLIES & OTHERS',
                      'preparation' : 'OTHER CONCERT EXPENSES',
                      'distributors' : 'MUSIC',
                      'flute' : 'INSTRUMENTS & SUPPLIES & OTHERS',
                      'gift' : 'SOCIALS & GIFTS & MERCH',
                      'orchestra-' : 'GUEST COACHES & PERFORMERS',
                      'services' : 'CONDUCTOR HONORARIUM',
                     }

def getFilename():
    while True:
        csvFilename = input('\nFinance Record CSV: ')
        print()

        if not csvFilename.endswith('.csv'): csvFilename += '.csv'
        if not isfile(csvFilename):
            # try searching private folder
            csvFilename = f'private/{csvFilename}'
            if not isfile(csvFilename):
                print('Invalid file name')
                continue
        
        return csvFilename 

def splitGiftAndAgency(allTransactions: list[Transaction]):
    agencyTransactions: list[Transaction] = []
    giftTransactions: list[Transaction] = []

    for transaction in allTransactions:
        if transaction.account == 'Agency Account':
            agencyTransactions.append(transaction)
        else:
            giftTransactions.append(transaction)
    
    return agencyTransactions, giftTransactions

def sortChronologically(transactions: list[Transaction]):
    # sort by "date" attribute in each Transaction object
    transactions.sort(key=lambda transaction: transaction.date)

# RUN IN PLACE
def convertDatetimesBackToStrings(data):
    for row in data:
        row[0] = row[0].strftime('%Y/%m/%d')

# RUN IN PLACE
def removeExceptions(transactions: list[Transaction]): 
    # find immediate transaction pairs that are equivalent and opposite to each other
    indexesToDelete = []
    index = 0
    while index < len(transactions)-1:
        if transactions[index].amount.inCents == -transactions[index+1].amount.inCents:
            indexesToDelete.extend([index, index+1])
            index += 2
        else:
            index += 1
    
    # delete in backwards order to avoid messing subsequent indexes
    indexesToDelete.reverse() 
    for index in indexesToDelete:
        del transactions[index]

# RUN IN PLACE
def appendBalances(transactions: list[Transaction]):
    balance = Money('0')
    for transaction in transactions:
        balance += transaction.amount
        transaction.balance = balance # create new attribute for the Transaction object

# RUN IN PLACE
def discardNonCurrentFY(agencyTransactions: list[Transaction], giftTransactions: list[Transaction]):
    while True:
        isDiscarding = input('Discard transactions from previous fiscal years? (y/n): ')
        match isDiscarding:
            case 'y':
                for transactions in agencyTransactions, giftTransactions:
                    latestDate: datetime = transactions[-1].date
                    if latestDate < datetime(latestDate.year,8,1): # spring semester
                        cutoffDate = datetime(latestDate.year-1,8,1)
                    else: # fall semester
                        cutoffDate = datetime(latestDate.year,8,1)
                    
                    # purge first index of list until cutoff is reached
                    date: datetime = transactions[0].date
                    while date < cutoffDate:
                        del transactions[0]
                        date = transactions[0].date
                return

            case 'n':
                return # do nothing
            case _:
                print('Invalid response\n')

# creates /private/[dateTimeNow] folder and returns folder path
def createFolderInPrivate() -> str:
    dateTimeNow = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    path = f'private/{dateTimeNow}'
    os.makedirs(path)
    return path

def exportFile(transactions: list[Transaction], filename: str, folderPath: str, categoryRecord=False):
    # unpack Transaction objects into lists
    data: list[list] = []
    if categoryRecord:
        for transaction in transactions:
            data.append([transaction.date.strftime('%Y/%m/%d'), 
                         transaction.itemName, 
                         transaction.amount.inDollars])
        headings = ['Date','Item Name','Amount']
    else:
        for transaction in transactions:
            data.append([transaction.date.strftime('%Y/%m/%d'), 
                         transaction.category, 
                         transaction.itemName,
                         transaction.amount.inDollars, 
                         transaction.balance.inDollars])
        headings = ['Date','Category','Item Name','Amount','Remaining Balance']   
    
    # insert headings
    data.insert(0,headings)
    
    # create file and write csv data
    with open(f'{folderPath}/{filename}', 'w') as file:
        csvWriter = csv.writer(file,delimiter=',')
        csvWriter.writerows(data)

def exportCategoryRecords(accountName: str, transactions: list[Transaction], path):
    categories: dict[str, list[Transaction]] = dict()
    for transaction in transactions:
        if transaction.category not in categories:
            categories[transaction.category] = [transaction]
        else:
            categories[transaction.category].append(transaction)
    
    for category in categories:
        exportFile(categories[category], f'{accountName}[{category}].csv', path, categoryRecord=True)

def main():
    # parse the .csv from TartanConnect
    csvFilename = getFilename()
    with open(csvFilename) as file:
        allTransactionData: list[list] = list(csv.reader(file))

    # create a list of Transaction objects using each row of the csv
    allTransactions: list[Transaction] = []
    for transactionData in allTransactionData[1:]:
        allTransactions.append(Transaction(transactionData))
    
    # split Agency and Gift transactions into separate lists
    agencyTransactions, giftTransactions = splitGiftAndAgency(allTransactions)
    
    # cleanup process for each account
    for transactions in agencyTransactions, giftTransactions:
        sortChronologically(transactions)
        removeExceptions(transactions) # delete immediate transaction pairs that are equivalent and opposite to each other
        appendBalances(transactions)
    
    # discard everything from previous years? user prompted y/n
    discardNonCurrentFY(agencyTransactions, giftTransactions)

    # export full accounting records
    path = createFolderInPrivate() # folder inside private folder to keep gitignored
    exportFile(agencyTransactions, 'agency.csv', path)
    exportFile(giftTransactions, 'gift.csv', path)

    # export category records
    exportCategoryRecords('agency', agencyTransactions, path)
    exportCategoryRecords('gift', giftTransactions, path)

if __name__ == '__main__':
    main()