class Dicts:
    itemKeywordSubstitutionDict = {'all university orchestra' : 'AUO',
                                   'fy25 ' : '',
                                   'pcard verification ' : '',
                                   'auo - ' : '',
                                   'auo: ' : '',
                                   'other - auo; ' : '',
                                   "'" : '',
                                   ';' : '',
                                   ':' : '',
                                   '-' : '',
                                   '  ' : ' ',
                                  }
    
    categoryByRawCategoryKeywordDict = {
                                        'memberships' : 'REVENUE--DUES',
                                        'other student/staff revenue' : 'REVENUE--DONATIONS & FUNDRAISING',
                                        'meal' : 'SOCIAL',
                                        'car' : 'OTHER CONCERT EXPENSES',
                                        'travel' : 'OTHER CONCERT EXPENSES',
                                       }
    
    categoryByItemNameKeywordDict = {
                                     # one-offs 
                                     'theodore' : 'MUSIC',
                                     'lucks' : 'MUSIC',
                                     'knoxville' : 'MUSIC',
                                     'purchased music' : 'MUSIC',
                                     'rented music' : 'MUSIC',
                                     'rental of music' : 'MUSIC',
                                     'oracle' : 'GUEST COACHES & PERFORMERS',
                                     'tarantino' : 'GUEST COACHES & PERFORMERS',
                                     'raffle' : 'SOCIAL',
                                     'karoke' : 'SOCIAL',
                                     'coffee' : 'SOCIAL',
                                     'bagel' : 'SOCIAL',
                                     'chalk' : 'OTHER CONCERT EXPENSES',

                                     # common keywords
                                     'journal' : 'GUEST COACHES & PERFORMERS',
                                     'guest' : 'GUEST COACHES & PERFORMERS',
                                     'coach' : 'GUEST COACHES & PERFORMERS',
                                     'speak' : 'GUEST COACHES & PERFORMERS',
                                     'musical' : 'GUEST COACHES & PERFORMERS',
                                    
                                     'ja5' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'giving' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'donat' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'admin fee' : 'REVENUE--DONATIONS & FUNDRAISING',
                                    
                                     'social' : 'SOCIAL',
                                     'pizza' : 'SOCIAL',
                                     'flower' : 'SOCIAL',
                                     'shirt' : 'SOCIAL',
                                     'hoodie' : 'SOCIAL',
                                     'ticket' : 'SOCIAL',
                                     'paint' : 'SOCIAL',
                                     'custom ink' : 'SOCIAL',
                                     'sticker' : 'SOCIAL',

                                     'haul' : 'OTHER CONCERT EXPENSES',
                                     'ratchet' : 'OTHER CONCERT EXPENSES',
                                     'stream' : 'OTHER CONCERT EXPENSES',
                                     'video' : 'OTHER CONCERT EXPENSES',
                                     'record' : 'OTHER CONCERT EXPENSES',
                                     'lighting' : 'OTHER CONCERT EXPENSES',
                                     'audio' : 'OTHER CONCERT EXPENSES',
                                     'tech' : 'OTHER CONCERT EXPENSES',
                                     'advert' : 'OTHER CONCERT EXPENSES',
                                     'poster' : 'OTHER CONCERT EXPENSES',

                                     'music director' : 'CONDUCTOR HONORARIUM',
                                     'conductor' : 'CONDUCTOR HONORARIUM',
                                     'jeffrey' : 'CONDUCTOR HONORARIUM',
                                     'j.klefstad' : 'CONDUCTOR HONORARIUM',

                                     'carnegie' : 'CONCERT VENUE FEE',
                                     ' venue' : 'CONCERT VENUE FEE',
                                     'deposit' : 'CONCERT VENUE FEE',
                                     'balance payment' : 'CONCERT VENUE FEE',
                                     'piano tuning' : 'CONCERT VENUE FEE',

                                     'mute' : 'EQUIPMENT',
                                     'string' : 'EQUIPMENT',
                                     'bass' : 'EQUIPMENT',
                                     'domain' : 'EQUIPMENT',
                                     'ssl' : 'EQUIPMENT',
                                     'cabinet' : 'EQUIPMENT',
                                     'supplies' : 'EQUIPMENT',

                                     'sheet' : 'MUSIC',
                                     'score' : 'MUSIC',
                                     'piece' : 'MUSIC',
                                     'print' : 'MUSIC',
                                     'copy' : 'MUSIC',
                                     'ink' : 'MUSIC',
                                     'compos' : 'MUSIC',
                                    
                                     'allocation' : 'REVENUE--JFC',
                                     'surplus' : 'REVENUE--JFC',

                                     'fundrais' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'whipped' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'sales tax' : 'REVENUE--DONATIONS & FUNDRAISING',
                                     'mandatory benefits' : 'REVENUE--DONATIONS & FUNDRAISING',

                                     'dues' : 'REVENUE--DUES',

                                     # more general keywords
                                     'instrument' : 'EQUIPMENT',
                                     'flute' : 'EQUIPMENT',
                                     'preparation' : 'OTHER CONCERT EXPENSES',
                                     'distributors' : 'MUSIC',
                                     'services' : 'CONDUCTOR HONORARIUM',
                                    }