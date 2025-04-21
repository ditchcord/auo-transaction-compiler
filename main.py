#
# Jason H. Wells - wellsjason543 at gmail dot com - jwellsuhhuh (Discord)
# updated 2025/04/21
# 
# "Finance Record CSV" is the exported finance record of everything downloaded from TartanConnect
#

import csv
import os
from os.path import isfile
from datetime import datetime

# dollars -> str
# cents -> int
class Helpers:
    @staticmethod
    def normalizeDollarsFormatting(dollars: str) -> str:
        if '.' not in dollars:
            return dollars + '.00'
        elif dollars[-1] == '.':
            return dollars + '00'
        elif dollars[-2] == '.':
            return dollars + '0'
        elif dollars[-3] == '.':
            return dollars
        else:
            raise TypeError(f'Invalid Dollars Format: {dollars}')

    # requires normalized dollars
    @staticmethod
    def dollarsToCents(dollars: str) -> int:
        return int(dollars[:-3] + dollars[-2:])

    @staticmethod
    def centsToDollars(cents: int) -> str:
        start = str(cents)[:-2]
        end = str(cents)[-2:]

        if start == '': start = '0'
        return start + '.' + end
    
    @staticmethod
    def daysSince2000(date: str):
        # Split the date string by '/'
        month, day, year = map(int, date.split('/'))
        date: datetime = datetime(year, month, day)
        
        daysSince2000 = (date - datetime(2000, 1, 1)).days
        
        return daysSince2000

def getFilename():
    while True:
        csvFilename = input('Finance Record CSV: ')
        if not csvFilename.endswith('.csv'): csvFilename += '.csv'
        if isfile(csvFilename):
            print()
            return csvFilename
        else:
            print('Invalid file name\n')

# RUN IN PLACE
def keepUsefulColumns(allData: list[list]):
    keptColumns = (0,9,11,15,17) # account, item Name, TartanConnect category, amount, date

    rowNumber = 0
    for row in allData:
        newRow = [row[index] for index in keptColumns]
        allData[rowNumber] = newRow
        rowNumber += 1

def moveDatesToFirstColumn(allData: list[list]):
    # date, account, item name, TartanConnect Category, amount
    for row in allData:
        row.insert(0, row.pop(4))

def splitGiftAndAgency(allData: list[list]):
    agencyData: list[list] = []
    giftData: list[list] = []

    for row in allData[1:]:
        if row[1].startswith('Agency'):
            agencyData.append(row)
        else: giftData.append(row)
    
    return agencyData, giftData

# RUN IN PLACE
def removeTimestampFromDates(data: list[list]):
    for row in data:
        cutoffIndex = row[0].find(' ')
        if cutoffIndex == -1:
            continue
        row[0] = row[0][:cutoffIndex]

# converts all money format to xx.xx
def normalizeDollars(data: list[list]):
    for row in data:
        row[4] = Helpers.normalizeDollarsFormatting(row[4])

def flattenCashnetItemNames(data: list[list]):
    for row in data:
        if row[2].startswith('ECOM'):
            receiptNumber = row[2].split('-')[5]
            row[2] = receiptNumber

# RUN IN PLACE
def sortChronologically(data: list[list]):
    # append days since 2000 to first column of each row so it can be sorted
    for row in data:
        row.insert(0, Helpers.daysSince2000(row[0]))
    
    data.sort()

    # delete the temporary column used for the sort
    for row in data:
        del row[0]

# delete transactions that are immediately followed by equivalent opposite transaction
def removeExceptions(data: list[list]): # RUN IN PLACE
    rowsToDelete = []
    rowNumber = 0
    while rowNumber < len(data)-1:
        if Helpers.dollarsToCents(data[rowNumber][4]) == -Helpers.dollarsToCents(data[rowNumber+1][4]):
            rowsToDelete.extend([rowNumber, rowNumber+1])
            rowNumber += 2
        else:
            rowNumber += 1
    
    rowsToDelete.reverse() # delete in backwards order to avoid messing subsequent indexes
    for rowNumber in rowsToDelete:
        del data[rowNumber]

def appendBalances(data: list[list]): # RUN IN PLACE
    balanceInCents = 0
    for row in data:
        balanceInCents += (Helpers.dollarsToCents(row[4]))
        row.append(Helpers.centsToDollars(balanceInCents))

def change2ndColumnToCategory(data: list[list]):
    # keyPhrase, category
    dictByTartanConnectCategory = {
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

    
    for row in data:
        categoryFound = False
        # search for key phrase matches in tartan connect category
        for keyPhrase in dictByTartanConnectCategory:
            if keyPhrase in row[3].lower():
                row[1] = dictByTartanConnectCategory[keyPhrase]
                categoryFound = True
                break
        if categoryFound: continue
        
        # search for key phrase matches in item name
        for keyPhrase in dictByItemName:
            if keyPhrase in row[2].lower():
                row[1] = dictByItemName[keyPhrase]
                categoryFound = True
                break
        if categoryFound: continue
    
        # no key phrase found - apply default category
        accountName: str = data[0][1]
        if 0 < Helpers.dollarsToCents(row[4]):
            if accountName == 'Gift Account':
                row[1] = 'REVENUE--DONATIONS & FUNDRAISING' # default gift revenue category
            else: row[1] = 'REVENUE--JFC' # default agency revenue category
        else:
            row[1] = 'INSTRUMENTS & SUPPLIES & OTHERS' # default agency/gift expense category

def removeTartanConnectCategory(data: list[list]):
    for row in data:
        del row[3]

# RUN IN PLACE
def addHeadings(data):
    headings = ['Date','Category','Item','Amount','Remaining Balance']
    data.insert(0,headings)

# creates /private/[dateTimeNow] folder and returns folder path
def createFolderInPrivate() -> str:
    dateTimeNow = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    path = f'private/{dateTimeNow}'
    os.makedirs(path)
    return path

def exportFile(data: list[list], dataName: str, folderName: str): # filename DOES NOT include .csv
    filename = f'{dataName}.csv'

    with open(f'{folderName}/{filename}', 'w') as file:
        csvWriter = csv.writer(file,delimiter=',')
        csvWriter.writerows(data)

def main():
    csvFilename = getFilename()
    allData: list[list] = list(csv.reader(open(csvFilename)))

    keepUsefulColumns(allData)
    moveDatesToFirstColumn(allData)
    agencyData, giftData = splitGiftAndAgency(allData)
    
    for data in agencyData, giftData:
        # cleanup data formats
        removeTimestampFromDates(data)
        normalizeDollars(data)
        flattenCashnetItemNames(data)

        sortChronologically(data)
        removeExceptions(data)

        # add useful information
        appendBalances(data)
        change2ndColumnToCategory(data)

        # remove un-needed data
        removeTartanConnectCategory(data)
        
        addHeadings(data)


    # export full accounting records
    path = createFolderInPrivate() # folder inside private folder to keep gitignored
    exportFile(agencyData, 'agency', path)
    exportFile(giftData, 'gift', path)

    # export category records
    for accountName, data in (('agency',agencyData[1:]), ('gift',giftData[1:])):
        categories: dict[str, list[list]] = dict()
        for row in data:
            if row[1] not in categories:
                categories[row[1]] = [row]
            else:
                categories[row[1]].append(row)
        
        for category in categories:
            addHeadings(categories[category])
            exportFile(categories[category], f'{accountName}[{category}]', path)


if __name__ == '__main__':
    main()