class Dicts:
    itemKeywordSubstitutionDict = {'all university orchestra' : 'AUO',
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
    
    categoryToKeywordsDict = { 
                              # NOTE: category only added once TWO (2) keywords from a single category are detected in an item name
                              'GUEST SERVICES' : ['journal', 'import', 'guest musician', 'taylor', 'taylor', 'bassist', 'bassist',
                                                  'coach', 'coach', 'musician', 'guest speaker', 'guest speaker', 'speaking', 
                                                  'speaking', 'presentation', 'presentation', 'musical services', 
                                                  'musical services', 'musical performance', 'musical performance', 'oracle', 
                                                  'oracle', 'tarantino', 'tarantino', 'guest services', 'guest services'],
                                                  # 2x coach, oracle, taylor, speaking, guest speaker, musical services, ...
                                                  # ... tarantino, guest services, musical performance, bassist intentional

                              'CONDUCTOR HONORARIUM' : ['music director', 'direct', 'directing', 'fee for services', 'klefstad',
                                                        'provided to auo', 'to jeffrey'],

                              'EQUIPMENT' : ['tape', 'mutes', 'mutes', 'strings', 'replacement', 'bass', 'bass', 'domain', 
                                             'website', 'ssl', 'cabinet', 'kiltie', 'repair', 'flute', 'english horn', 'supplies', 
                                             'instrument', 'masks', 'renew', 'storage', 'box', 'maintenance', 'closet'],
                                             # 2x mutes, bass intentional

                              'MUSIC' : ['theodore', 'lucks', 'lucks', 'knoxville', 'rent', 'purchased music', 'purchased music', 
                                         'renting music', 'music sheets', 'music sheets', 'music pieces', 'music pieces', 
                                         'rental of music', 'rental of music', 'print', 'cop', '3rd', 'charge', 'tartan ink', 
                                         'compos', 'rented music', 'compos', 'flute choir music', 'music to be used', 
                                         'music to be used', 'sheet music', 'sheet music', 'score', 'needs music'],
                                         # cop = copy or copier
                                         # 2x compos (compose/composition), music sheets, music pieces, lucks, sheet music, ...
                                         # ... purchased music, music to be used, rental of music intentional  

                              'OTHER CONCERT EXPENSES' : ['haul', 'gas', 'ratchet', 'stream', 'video', 'record',
                                                          'lighting', 'flowers', 'audio', 'ab tech', 'ab tech', 'advert', 'poster', 
                                                          'poster', 'chalk', 'preparation', 'performance', 'raffle', 'concert',
                                                          'equipment'],
                                                          # 2x poster, ab tech intentional
                                                          # haul = uhaul/u-haul
                            
                              'CONCERT VENUE' : ['deposit', 'soldiers', 'carnegie', 'bellefield', 'rental', 
                                                 'balance payment', 'balance payment', ' venue', 'final payment',
                                                 'down payment'],
                                                #  2x balance payment intentional
                                                #  ' venue' = only venue, not revenue
                            
                              'SOCIAL' : ['social', 'pizza', 'shirts', 'shirts', 'hoodies', 'tickets', 'paint', 'paint', 
                                          'custom', 'tote', 'stickers', 'bagles', 'bagels', 'karoke', 'coffee', 'members', 
                                          'fresh prints', 'breakfast', 'order', 'icebreaker', 'refund of sales tax'], 
                                          # 2x shirts, paint intentional
                                          # bagel misspelled, karaoke misspelled           
                        
                              'REVENUE' : ['ja5', 'giving', 'donat', 'admin fee', 'allocation', 'surplus', 'fundrais', 'jfc',
                                           'whipped cream', 'sales tax', 'calculation', 'mandatory benefits', 'dues', 
                                           'contributions'],
                                           # donat = donate/donation, funrais = fundraiser/fundraising
                             }
    
    TCCategoryToCategoryDict = {
                                'memberships' : 'REVENUE',
                                'other student/staff revenue' : 'REVENUE',
                                'meal' : 'SOCIAL',
                                'car' : 'OTHER CONCERT EXPENSES',
                                'travel' : 'OTHER CONCERT EXPENSES',
                                'contributions' : 'REVENUE',
                                'office supplies' : 'EQUIPMENT',
                                'rental-facilities' : 'CONCERT VENUE'
                               }