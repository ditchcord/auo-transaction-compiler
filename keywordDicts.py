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
                                        'memberships' : 'REVENUE',
                                        'other student/staff revenue' : 'REVENUE',
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
                                     'presentation' : 'GUEST COACHES & PERFORMERS',
                                     'raffle' : 'SOCIAL',
                                     'karoke' : 'SOCIAL', # karaoke misspelled
                                     'coffee' : 'SOCIAL',
                                     'bagel' : 'SOCIAL',
                                     'chalk' : 'OTHER CONCERT EXPENSES',
                                     'services for concert' : 'OTHER CONCERT EXPENSES',
                                     'rental of soldiers' : 'CONCERT VENUE FEE',

                                     # common keywords
                                     'social' : 'SOCIAL',
                                     'pizza' : 'SOCIAL',
                                     'flower' : 'SOCIAL',
                                     'shirt' : 'SOCIAL',
                                     'hoodie' : 'SOCIAL',
                                     'ticket' : 'SOCIAL',
                                     'paint' : 'SOCIAL',
                                     'custom ink' : 'SOCIAL',
                                     'sticker' : 'SOCIAL',

                                     'journal' : 'GUEST COACHES & PERFORMERS',
                                     'guest' : 'GUEST COACHES & PERFORMERS',
                                     'coach' : 'GUEST COACHES & PERFORMERS',
                                     'speak' : 'GUEST COACHES & PERFORMERS',
                                     'musical' : 'GUEST COACHES & PERFORMERS',
                                    
                                     'ja5' : 'REVENUE',
                                     'giving' : 'REVENUE',
                                     'donat' : 'REVENUE', # donate/donation
                                     'admin fee' : 'REVENUE',

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
                                     
                                     'equipment' : 'EQUIPMENT',
                                     'tape' : 'EQUIPMENT',
                                     'mute' : 'EQUIPMENT',
                                     'string' : 'EQUIPMENT',
                                     'bass' : 'EQUIPMENT',
                                     'domain' : 'EQUIPMENT',
                                     'ssl' : 'EQUIPMENT',
                                     'cabinet' : 'EQUIPMENT',
                                     'kiltie' : 'EQUIPMENT',
                                     'repair' : 'EQUIPMENT',

                                     'carnegie music' : 'CONCERT VENUE FEE',
                                     ' venue' : 'CONCERT VENUE FEE', # only venue, not revenue
                                     'deposit' : 'CONCERT VENUE FEE',
                                     'balance payment' : 'CONCERT VENUE FEE',
                                     'piano tuning' : 'CONCERT VENUE FEE',

                                     'sheet music' : 'MUSIC',
                                     'music sheet' : 'MUSIC',
                                     'music piece' : 'MUSIC',
                                     'score' : 'MUSIC',
                                     'print' : 'MUSIC',
                                     'copy' : 'MUSIC',
                                     'copier' : 'MUSIC',
                                     'ink' : 'MUSIC',
                                     'compos' : 'MUSIC', # compose/composition
                                    
                                     'allocation' : 'REVENUE',
                                     'surplus' : 'REVENUE',
                                     'fundrais' : 'REVENUE', # fundraiser/fundraising
                                     'whipped' : 'REVENUE',
                                     'sales tax' : 'REVENUE',
                                     'mandatory benefits' : 'REVENUE',
                                     'dues' : 'REVENUE',

                                     # more general keywords
                                     'music ' : 'MUSIC',
                                     'instrument' : 'EQUIPMENT',
                                     'flute' : 'EQUIPMENT',
                                     'supplies' : 'EQUIPMENT',
                                     'preparation' : 'OTHER CONCERT EXPENSES',
                                     'distributors' : 'MUSIC',
                                     'services' : 'CONDUCTOR HONORARIUM',
                                    }