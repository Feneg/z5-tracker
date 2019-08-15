'''
Default settings
'''

from .itemobj import i

__all__ = 'ITEMS',


ITEMS = (
    i('Bombs (5)', (), (), ()),
    i('Deku Nuts (5)', (), (), ()),
    i('Bombchus (10)', (), (), ()),
    i('Boomerang', (0, 2), ('Boomerang',), ('boomerang',)),
    i('Deku Stick (1)', (), (), ()),
    i('Lens of Truth', (1, 2), ('Lens of Truth',), ('lens',)),
    i('Hammer', (3, 2), ('Megaton Hammer',), ('hammer',)),
    i('Cojiro', (), ('<stub>',), ('<stub>',)),
    i('Bottle', (4, 6), ('Bottles',)*4, tuple(zip(('bottle',)*4, range(1, 5)))),
    i('Bottle with Milk', (), (), ()),
    i('Bottle with Letter', (1, 3), ("Ruto's Letter",), ('bottle_letter',)),
    i('Deliver Letter', (), ('<stub>',), ('<stub>',)),
    i('Sell Big Poe', (), ('<stub>',), ('<stub>',)),
    i('Magic Bean', (2, 2), ('Magic Beans',)*10,
       tuple(zip(('bean',)*10, range(1, 11)))),
    i('Skull Mask', (), ('<stub>',), ('<stub>',)),
    i('Spooky Mask', (), ('<stub>',), ('<stub>',)),
    i('Keaton Mask', (), ('<stub>',), ('<stub>',)),
    i('Bunny Hood', (), ('<stub>',), ('<stub>',)),
    i('Mask of Truth', (), ('<stub>',), ('<stub>',)),
    i('Pocket Egg', (5, 3),
      ('Pocket Egg (Adult)', 'Pocket Cucco', 'Cojiro', 'Odd Mushroom',
       'Odd Potion', "Poacher's Saw", "Broken Goron's Sword", 'Prescription',
       'Eyeball Frog', "World's Finest Eye Drops", 'Claim Check', 'Done'),
      ('egg', 'cucco', 'cojiro', 'mushroom', 'medicine', 'saw', 'broken_sword',
       'perscription', 'frog', 'eyedrops', 'claim', 'sword3'),
      link=(('Pocket Cucco', 2), ('Cojiro', 3), ('Odd Mushroom', 4),
            ('Odd Potion', 5), ('Poachers Saw', 6), ('Broken Sword', 7),
            ('Prescription', 8), ('Eyeball Frog', 9), ('Eyedrops', 10),
            ('Claim Check', 11))),
    i('Pocket Cucco', (), ('<stub>',), ('<stub>',)),
    i('Odd Mushroom', (), ('<stub>',), ('<stub>',)),
    i('Odd Potion', (), ('<stub>',), ('<stub>',)),
    i('Poachers Saw', (), ('<stub>',), ('<stub>',)),
    i('Broken Sword', (), ('<stub>',), ('<stub>',)),
    i('Prescription', (), ('<stub>',), ('<stub>',)),
    i('Eyeball Frog', (), ('<stub>',), ('<stub>',)),
    i('Eyedrops', (), ('<stub>',), ('<stub>',)),
    i('Claim Check', (), ('<stub>',), ('<stub>',)),
    i('Kokiri Sword', (0, 4), ('Kokiri Sword',), ('sword1',)),
    i('Deku Shield', (3, 4), ('Deku Shield',), ('shield1',),
      link=(('Buy Deku Shield', 1),)),
    i('Hylian Shield', (4, 4), ('Hylian Shield',), ('shield2',)),
    i('Mirror Shield', (5, 4), ('Mirror Shield',), ('shield3',)),
    i('Goron Tunic', (0, 5), ('Goron Tunic',), ('redtunic',)),
    i('Zora Tunic', (1, 5), ('Zora Tunic',), ('bluetunic',)),
    i('Iron Boots', (2, 5), ('Iron Boots',), ('ironboots',)),
    i('Hover Boots', (3, 5), ('Hover Boots',), ('hoverboots',)),
    i('Stone of Agony', (4, 5), ('Stone of Agony',), ('agony',)),
    i('Gerudo Membership Card', (5, 5), ('Gerudo Membership Card',),
      ('gerudocard',)),
    i('Heart Container', (), (), ()),
    i('Piece of Heart', (), (), ()),
    i('Boss Key', (), (), ()),
    i('Compass', (), (), ()),
    i('Map', (), (), ()),
    i('Small Key', (), (), ()),
    i('Weird Egg', (4, 3),
      ('Weird Egg (Child)', "Zelda's Letter", 'Mask Quest', 'Keaton Mask',
       'Mask Quest', 'Skull Mask', 'Mask Quest', 'Spooky Mask', 'Mask Quest',
       'Bunny Hood', 'Mask Quest', 'Mask of Truth'),
      ('egg', 'letter', 'sold_out', 'keaton', 'sold_out', 'skull', 'sold_out',
       'spooky', 'sold_out', 'bunny', 'sold_out', 'truth')),
    i('Recovery Heart', (), (), ()),
    i('Arrows (5)', (), (), ()),
    i('Arrows (10)', (), (), ()),
    i('Arrows (30)', (), (), ()),
    i('Rupee (1)', (), (), ()),
    i('Rupee (5)', (), (), ()),
    i('Rupee (20)', (), (), ()),
    i('Heart Container (Boss)', (), (), ()),
    i('Milk', (), (), ()),
    i('Goron Mask', (), (), ()),
    i('Zora Mask', (), (), ()),
    i('Gerudo Mask', (), (), ()),
    i('Rupees (50)', (), (), ()),
    i('Rupees (200)', (), (), ()),
    i('Biggoron Sword', (2, 4), ('Biggoron Sword',), ('sword3',)),
    i('Fire Arrows', (4, 0), ('Fire Arrows',), ('firearrow',)),
    i('Ice Arrows', (4, 1), ('Ice Arrows',), ('icearrow',)),
    i('Light Arrows', (4, 2), ('Light Arrows',), ('lightarrow',)),
    i('Gold Skulltula Token', (5, 6), ('Gold Skulltula Token',)*100,
      tuple(zip(('skulltula_token',)*101, range(1, 101)))),
    i('Dins Fire', (5, 0), ("Din's Fire",), ('din',)),
    i('Nayrus Love', (5, 2), ("Nayru's Love",), ('nayru',)),
    i('Farores Wind', (5, 1), ("Farore's Wind",), ('farore',)),
    i('Deku Nuts (10)', (), (), ()),
    i('Bombs (10)', (), (), ()),
    i('Bombs (20)', (), (), ()),
    i('Deku Seeds (30)', (), (), ()),
    i('Bombchus (5)', (), (), ()),
    i('Bombchus (20)', (), (), ()),
    i('Rupee (Treasure Chest Game)', (), (), ()),
    i('Piece of Heart (Treasure Chest Game)', (), (), ()),
    i('Ice Trap', (), (), ()),
    i('Progressive Hookshot', (3, 1), ('Hookshot', 'Longshot'),
       ('hookshot', 'longshot')),
    i('Progressive Strength Upgrade', (0, 6),
      ("Goron's Bracelet", 'Silver Gauntlets', 'Golden Gauntlets'),
      ('lift1', 'lift2', 'lift3')),
    i('Bomb Bag', (2, 0), ('Bombs',)*3,
       tuple(zip(('bomb',)*3, (20, 30, 40)))),
    i('Bow', (3, 0), ('Bow',)*3,
       tuple(zip(('bow',)*3, (30, 40, 50)))),
    i('Slingshot', (0, 1), ('Slingshot',)*3,
       tuple(zip(('slingshot',)*3, (30, 40, 50)))),
    i('Progressive Wallet', (2, 6),
      ("Child's Wallet", "Adult's Wallet", "Giant's Wallet", "Tycoon's Wallet"),
      ('wallet', 'wallet1', 'wallet2', 'wallet3'), default=1),
    i('Progressive Scale', (1, 6), ('Silver Scale', 'Golden Scale'),
      ('scale1', 'scale2')),
    i('Deku Nut Capacity', (1, 0), ('Deku Nuts',)*3,
      tuple(zip(('nut',)*3, (20, 30, 40)))),
    i('Deku Stick Capacity', (0, 0), ('Deku Sticks',)*3,
       tuple(zip(('stick',)*3, (10, 20, 30))),
      link=(('Buy Deku Stick (1)', 1),)),
    i('Bombchus', (2, 1), ('Bombchus',), ('bombchu',)),
    i('Magic Meter', (3, 6), ('Magic', 'Double Magic'), ('magic1', 'magic2')),
    i('Ocarina', (1, 1), ('Fairy Ocarina', 'Ocarina of Time'),
       ('fairyocarina', 'ocarina')),
    i('Bottle with Red Potion', (), (), ()),
    i('Bottle with Green Potion', (), (), ()),
    i('Bottle with Blue Potion', (), (), ()),
    i('Bottle with Fairy', (), (), ()),
    i('Bottle with Fish', (), (), ()),
    i('Bottle with Blue Fire', (), (), ()),
    i('Bottle with Bugs', (), (), ()),
    i('Bottle with Big Poe', (2, 3), ('Big Poes',)*10,
       tuple(zip(('bottle_bigpoe',)*10, range(1, 11)))),
    i('Bottle with Poe', (), (), ()),
    i('Boss Key (Forest Temple', (), (), ()),
    i('Boss Key (Fire Temple', (), (), ()),
    i('Boss Key (Water Temple', (), (), ()),
    i('Boss Key (Spirit Temple', (), (), ()),
    i('Boss Key (Shadow Temple', (), (), ()),
    i('Boss Key (Ganons Temple', (), (), ()),
    i('Compass (Deku Tree)', (), (), ()),
    i('Compass (Dodongos Cavern)', (), (), ()),
    i('Compass (Jabu Jabus Belly)', (), (), ()),
    i('Compass (Forest Temple', (), (), ()),
    i('Compass (Fire Temple', (), (), ()),
    i('Compass (Water Temple', (), (), ()),
    i('Compass (Spirit Temple', (), (), ()),
    i('Compass (Shadow Temple', (), (), ()),
    i('Compass (Bottom of the Well)', (), (), ()),
    i('Compass (Ice Cavern)', (), (), ()),
    i('Map (Deku Tree)', (), (), ()),
    i('Map (Dodongos Cavern)', (), (), ()),
    i('Map (Jabu Jabus Belly)', (), (), ()),
    i('Map (Forest Temple', (), (), ()),
    i('Map (Fire Temple', (), (), ()),
    i('Map (Water Temple', (), (), ()),
    i('Map (Spirit Temple', (), (), ()),
    i('Map (Shadow Temple', (), (), ()),
    i('Map (Bottom of the Well)', (), (), ()),
    i('Map (Ice Cavern)', (), (), ()),
    i('Small Key (Forest Temple', (), (), ()),
    i('Small Key (Fire Temple', (), (), ()),
    i('Small Key (Water Temple', (), (), ()),
    i('Small Key (Spirit Temple', (), (), ()),
    i('Small Key (Shadow Temple', (), (), ()),
    i('Small Key (Bottom of the Well)', (), (), ()),
    i('Small Key (Gerudo Training Grounds)', (), (), ()),
    i('Small Key (Gerudo Fortress)', (), ('<stub>',)*4,
      tuple(zip(('<stub>',)*4, range(4)))),
    i('Small Key (Ganons Castle)', (), (), ()),
    i('Double Defense', (), (), ()),
    i('Magic Bean Pack', (), (), ()),
    i('Zeldas Letter', (), ('<stub>',), ('<stub>',)),
    i('Time Travel', (1, 4), ('Master Sword',), ('sword2',)),
    i('Epona', (), ('<stub>',), ('<stub>',)),
    i('Carpenter Rescue', (), ('<stub>',), ('<stub>',)),
    i('Gerudo Fortress Gate Open', (), ('<stub>',), ('<stub>',)),
    i('Goron City Woods Warp Open', (), ('<stub>',), ('<stub>',)),
    i('Drain Well', (), ('<stub>',), ('<stub>',)),
    i('Links Cow', (), ('<stub>',), ('<stub>',)),

    i('Kokiri Forest Open', (), ('<stub>',), ('<stub>',)),
    i('Forest Temple Jo and Beth', (), ('<stub>',), ('<stub>',)),
    i('Forest Temple Amy and Meg', (), ('<stub>',), ('<stub>',)),
    i('Child Water Temple', (), ('<stub>',), ('<stub>',)),
    i('Lake Refill', (), ('<stub>',), ('<stub>',)),
    i('Forest Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Fire Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Water Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Shadow Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Spirit Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Light Trial Clear', (), ('<stub>',), ('<stub>',)),
    i('Triforce', (), ('<stub>',), ('<stub>',)),

    i('Deku Stick Drop', (), (), ()),
    i('Deku Nut Drop', (), (), ()),
    i('Blue Fire', (3, 3), ('Blue Fire',), ('bottle_fire',)),
    i('Fairy', (), (), ()),
    i('Fish', (0, 3), ('Fish',), ('bottle_fish',)),
    i('Bugs', (), (), ()),
    i('Big Poe', (), (), ()),
    i('Bombchu Drop', (), ('<stub>',), ('<stub>',), link=(('Bombchus', 1),)),

    i('Scarecrow Song', (), ('<stub>',), ('<stub>',)),
    i('Minuet of Forest', (0, 9), ('Minuet of Forest',), ('minuet',)),
    i('Bolero of Fire', (1, 9), ('Bolero of Fire',), ('bolero',)),
    i('Serenade of Water', (2, 9), ('Serenade of Water',), ('serenade',)),
    i('Requiem of Spirit', (3, 9), ('Requiem of Spirit',), ('requiem',)),
    i('Nocturne of Shadow', (4, 9), ('Nocturne of Shadow',), ('nocturne',)),
    i('Prelude of Light', (5, 9), ('Prelude of Light',), ('prelude',)),
    i('Zeldas Lullaby', (0, 8), ("Zelda's Lullaby",), ('zelda_colored',)),
    i('Eponas Song', (1, 8), ("Epona's Song",), ('epona_colored',)),
    i('Sarias Song', (2, 8), ("Saria's Song",), ('saria_colored',)),
    i('Suns Song', (3, 8), ("Sun's Song",), ('sun_colored',)),
    i('Song of Time', (4, 8), ('Song of Time',), ('time_colored',)),
    i('Song of Storms', (5, 8), ('Song of Storms',), ('storms_colored',)),

    i('Buy Deku Nut (5)', (), (), ()),
    i('Buy Arrows (30)', (), (), ()),
    i('Buy Arrows (50)', (), (), ()),
    i('Buy Bombs (5) [25]', (), (), ()),
    i('Buy Deku Nut (10)', (), (), ()),
    i('Buy Deku Stick (1)', (), ('<stub>',), ('<stub>',)),
    i('Buy Bombs (10)', (), (), ()),
    i('Buy Fish', (), (), ()),
    i('Buy Red Potion [30]', (), (), ()),
    i('Buy Green Potion', (), (), ()),
    i('Buy Blue Potion', (), (), ()),
    i('Buy Hylian Shield', (), (), ()),
    i('Buy Deku Shield', (), ('<stub>',), ('<stub>',)),
    i('Buy Goron Tunic', (), (), ()),
    i('Buy Zora Tunic', (), (), ()),
    i('Buy Heart', (), (), ()),
    i('Buy Bombchu (10)', (), (), ()),
    i('Buy Bombchu (20)', (), (), ()),
    i('Buy Bombchu (5)', (), (), ()),
    i('Buy Deku Seeds', (), (), ()),
    i('Sold Out', (), (), ()),
    i('Buy Blue Fire', (), (), ()),
    i('Buy Bottle Bug', (), (), ()),
    i('Buy Poe', (), (), ()),
    i('Buy Fairy\'s Spirit', (), (), ()),
    i('Buy Arrows (10)', (), (), ()),
    i('Buy Bombs (20)', (), (), ()),
    i('Buy Bombs (30)', (), (), ()),
    i('Buy Bombs (5) [35]', (), (), ()),
    i('Buy Red Potion [40]', (), (), ()),
    i('Buy Red Potion [50]', (), (), ()),

    i('Kokiri Emerald', (0, 10), ("Kokiri's Emerald",), ('emerald',)),
    i('Goron Ruby', (1, 10), ("Goron's Ruby",), ('ruby',)),
    i('Zora Sapphire', (2, 10), ("Zora's Sapphire",), ('sapphire',)),
    i('Light Medallion', (0, 11), ('Light Medallion',), ('lightmedallion',)),
    i('Forest Medallion', (1, 11), ('Forest Medallion',), ('forestmedallion',)),
    i('Fire Medallion', (2, 11), ('Fire Medallion',), ('firemedallion',)),
    i('Water Medallion', (3, 11), ('Water Medallion',), ('watermedallion',)),
    i('Shadow Medallion', (4, 11), ('Shadow Medallion',), ('shadowmedallion',)),
    i('Spirit Medallion', (5, 11), ('Spirit Medallion',), ('spiritmedallion',)),
)
