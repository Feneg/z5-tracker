'''
Location mapping database.
'''

__all__ = 'ITEMLOCATIONS', 'SKULLTULALOCATIONS'


ITEMLOCATIONS = {

    # Overworld
    "Kokiri Sword Chest": {
        'maps': ('item_child',),
        'coordinates': (991, 2092),
        'type': 'chest'},
    "Deku Baba Sticks": {
        'maps': (),
        'coordinates': (),
        'type': 'enemy'},
    "Deku Baba Nuts": {
        'maps': (),
        'coordinates': (),
        'type': 'enemy'},
    "Links Pocket": {
        'maps': (),
        'coordinates': (),
        'type': 'standard'},
    "Mido House": {
        'maps': ('item_child',),
        'coordinates': (902, 2133),
        'type': 'chest'},
    "Kokiri Shop": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (917, 2220),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Skull Kid": {
        'maps': ('item_child',),
        'coordinates': (785, 2085),
        'type': 'npc'},
    "Ocarina Memory Game": {
        'maps': ('item_child',),
        'coordinates': (810, 2232),
        'type': 'npc'},
    "Target in Woods": {
        'maps': ('item_child',),
        'coordinates': (777, 2192),
        'type': 'npc'},
    "LW Deku Scrub Deku Stick Upgrade": {
        'maps': ('item_child',),
        'coordinates': (927, 1970),
        'type': 'deku'},
    "LW Deku Scrub Deku Nuts": {
        'maps': ('item_child',),
        'coordinates': (710, 2038),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LW Deku Scrub Deku Sticks": {
        'maps': ('item_child',),
        'coordinates': (750, 2038),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Song from Saria": {
        'maps': ('item_child',),
        'coordinates': (626, 2160),
        'type': 'song'},
    "Gift from Saria": {
        'maps': ('item_child',),
        'coordinates': (883, 1930),
        'type': 'npc'},
    "Song from Ocarina of Time": {
        'maps': ('item_child',),
        'coordinates': (440, 1439),
        'type': 'song'},
    "Ocarina of Time": {
        'maps': ('item_child',),
        'coordinates': (440, 1479),
        'type': 'free'},
    "Underwater Bottle": {
        'maps': ('item_child',),
        'coordinates': (1263, 1049),
        'type': 'free'},
    "Lake Hylia Sun": {
        'maps': ('item_adult',),
        'coordinates': (1435, 1080),
        'type': 'chest'},
    "Lake Hylia Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (1160, 961),
        'type': 'heart'},
    "Diving in the Lab": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 961),
        'type': 'npc'},
    "Child Fishing": {
        'maps': ('item_child',),
        'coordinates': (1215, 1270),
        'type': 'npc'},
    "Adult Fishing": {
        'maps': ('item_adult',),
        'coordinates': (1215, 1270),
        'type': 'npc'},
    "Gerudo Valley Waterfall Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (520, 701),
        'type': 'heart'},
    "Gerudo Valley Crate Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (633, 654),
        'type': 'heart'},
    "Gerudo Valley Hammer Rocks Chest": {
        'maps': ('item_adult',),
        'coordinates': (581, 601),
        'type': 'chest'},
    "Gerudo Fortress Rooftop Chest": {
        'maps': ('item_adult',),
        'coordinates': (318, 544),
        'type': 'chest'},
    "Horseback Archery 1000 Points": {
        'maps': ('item_adult',),
        'coordinates': (418, 620),
        'type': 'npc'},
    "Horseback Archery 1500 Points": {
        'maps': ('item_adult',),
        'coordinates': (458, 620),
        'type': 'npc'},
    "Gerudo Fortress North F1 Carpenter": {
        'maps': (),
        'coordinates': (),
        'type': 'standard'},
    "Gerudo Fortress North F2 Carpenter": {
        'maps': (),
        'coordinates': (),
        'type': 'standard'},
    "Gerudo Fortress South F1 Carpenter": {
        'maps': (),
        'coordinates': (),
        'type': 'standard'},
    "Gerudo Fortress South F2 Carpenter": {
        'maps': (),
        'coordinates': (),
        'type': 'standard'},
    "Gerudo Fortress Carpenter Rescue": {
        'maps': ('item_adult',),
        'coordinates': (358, 524),
        'type': 'npc'},
    "Gerudo Fortress Membership Card": {
        'maps': ('item_adult',),
        'coordinates': (358, 564),
        'type': 'npc'},
    "Haunted Wasteland Structure Chest": {
        'maps': ('item_adult',),
        'coordinates': (343, 380),
        'type': 'chest'},
    "Colossus Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (305, 160),
        'type': 'heart'},
    "Sheik at Colossus": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (347, 128),
        'type': 'song'},
    "Desert Colossus Fairy Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (297, 276),
        'type': 'fairy'},
    "Zelda": {
        'maps': ('item_adult',),
        'coordinates': (279, 1519),
        'type': 'npc'},
    "Master Sword Pedestal": {
        'maps': ('item_child',),
        'coordinates': (279, 1559),
        'type': 'free'},
    "Sheik at Temple": {
        'maps': ('item_adult',),
        'coordinates': (279, 1559),
        'type': 'song'},
    "Malon Egg": {
        'maps': ('item_child',),
        'coordinates': (246, 1420),
        'type': 'npc'},
    "Zeldas Letter": {
        'maps': ('item_child',),
        'coordinates': (173, 1408),
        'type': 'npc'},
    "Impa at Castle": {
        'maps': ('item_child',),
        'coordinates': (173, 1448),
        'type': 'song'},
    "Hyrule Castle Fairy Reward": {
        'maps': ('item_child',),
        'coordinates': (236, 1505),
        'type': 'fairy'},
    "Ganons Castle Fairy Reward": {
        'maps': ('item_adult',),
        'coordinates': (206, 1520),
        'type': 'fairy'},
    "10 Big Poes": {
        'maps': ('item_adult',),
        'coordinates': (390, 1464),
        'type': 'npc'},
    "Castle Town Bazaar": {
        'maps': ('item_child',),
        'coordinates': (355, 1503),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Child Shooting Gallery": {
        'maps': ('item_child',),
        'coordinates': (299, 1427),
        'type': 'npc'},
    "Castle Town Bombchu Bowling": {
        'maps': ('item_child',),
        'coordinates': (314, 1387),
        'type': 'npc'},
    "Castle Town Potion Shop": {
        'maps': ('item_child',),
        'coordinates': (315, 1503),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Treasure Chest Game": {
        'maps': ('item_child',),
        'coordinates': (360, 1416),
        'type': 'npc'},
    "Castle Town Bombchu Shop": {
        'maps': ('item_child',),
        'coordinates': (360, 1376),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Dog Lady": {
        'maps': ('item_child',),
        'coordinates': (355, 1463),
        'type': 'npc'},
    "Man on Roof": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (371, 1830),
        'type': 'npc'},
    "Anju as Adult": {
        'maps': ('item_adult',),
        'coordinates': (451, 1867),
        'type': 'npc'},
    "Anjus Chickens": {
        'maps': ('item_child',),
        'coordinates': (431, 1867),
        'type': 'npc'},
    "Sheik in Kakariko": {
        'maps': ('item_adult',),
        'coordinates': (387, 1734),
        'type': 'song'},
    "10 Gold Skulltula Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 280),
        'type': 'npc'},
    "20 Gold Skulltula Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 320),
        'type': 'npc'},
    "30 Gold Skulltula Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 360),
        'type': 'npc'},
    "40 Gold Skulltula Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 400),
        'type': 'npc'},
    "50 Gold Skulltula Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 440),
        'type': 'npc'},
    "Impa House Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (451, 1827),
        'type': 'heart'},
    "Windmill Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (356, 1915),
        'type': 'heart'},
    "Song at Windmill": {
        'maps': ('item_adult',),
        'coordinates': (396, 1915),
        'type': 'song'},
    "Kakariko Bazaar": {
        'maps': ('item_adult',),
        'coordinates': (347, 1780),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Adult Shooting Gallery": {
        'maps': ('item_adult',),
        'coordinates': (411, 1837),
        'type': 'npc'},
    "Kakariko Potion Shop Front": {
        'maps': ('item_adult',),
        'coordinates': (331, 1824),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Graveyard Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (335, 1980),
        'type': 'heart'},
    "Gravedigging Tour": {
        'maps': ('item_child',),
        'coordinates': (342, 2030),
        'type': 'npc'},
    "Shield Grave Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (382, 2030),
        'type': 'sub'},
    "Heart Piece Grave Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (350, 2070),
        'type': 'sub'},
    "Composer Grave Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (333, 2110),
        'type': 'sub'},
    "Song from Composer Grave": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (373, 2110),
        'type': 'song'},
    "Hookshot Chest": {
        'maps': ('item_adult',),
        'coordinates': (342, 2030),
        'type': 'sub'},
    "Dampe Race Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (302, 2030),
        'type': 'sub'},
    "Death Mountain Bombable Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (221, 1744),
        'type': 'chest'},
    "DM Trail Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (190, 1664),
        'type': 'heart'},
    "Goron City Leftmost Maze Chest": {
        'maps': ('item_adult',),
        'coordinates': (98, 1556),
        'type': 'chest'},
    "Goron City Left Maze Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (78, 1596),
        'type': 'chest'},
    "Goron City Right Maze Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (118, 1596),
        'type': 'chest'},
    "Goron City Pot Freestanding PoH": {
        'maps': ('item_child',),
        'coordinates': (70, 1684),
        'type': 'heart'},
    "Rolling Goron as Child": {
        'maps': ('item_child',),
        'coordinates': (110, 1684),
        'type': 'npc'},
    "Link the Goron": {
        'maps': ('item_adult',),
        'coordinates': (110, 1684),
        'type': 'npc'},
    "Goron City Stick Pot": {
        'maps': (),
        'coordinates': (),
        'type': 'free'},
    "Goron Shop": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (128, 1646),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Darunias Joy": {
        'maps': ('item_child',),
        'coordinates': (90, 1646),
        'type': 'npc'},
    "DM Crater Wall Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (66, 1834),
        'type': 'heart'},
    "Biggoron": {
        'maps': ('item_adult',),
        'coordinates': (100, 1790),
        'type': 'npc'},
    "DMC Deku Scrub Bombs": {
        'maps': ('item_child',),
        'coordinates': (26, 1744),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "DM Crater Volcano Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (26, 1754),
        'type': 'heart'},
    "Sheik in Crater": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (26, 1834),
        'type': 'song'},
    "Crater Fairy Reward": {
        'maps': ('item_adult',),
        'coordinates': (66, 1874),
        'type': 'fairy'},
    "Mountain Summit Fairy Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (66, 1744),
        'type': 'fairy'},
    "Magic Bean Salesman": {
        'maps': (),
        'coordinates': (),
        'type': 'npc'},
    "Frog Ocarina Game": {
        'maps': ('item_child',),
        'coordinates': (481, 2184),
        'type': 'npc'},
    "Frogs in the Rain": {
        'maps': ('item_child',),
        'coordinates': (481, 2144),
        'type': 'npc'},
    "Zora River Lower Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (474, 2037),
        'type': 'heart'},
    "Zora River Upper Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (425, 2347),
        'type': 'heart'},
    "Diving Minigame": {
        'maps': ('item_child',),
        'coordinates': (429, 2556),
        'type': 'npc'},
    "Zoras Domain Torch Run": {
        'maps': ('item_child',),
        'coordinates': (442, 2610),
        'type': 'chest'},
    "King Zora Moves": {
        'maps': (),
        'coordinates': (373, 2550),
        'type': 'npc'},
    "Zoras Domain Stick Pot": {
        'maps': (),
        'coordinates': (),
        'type': 'free'},
    "Zoras Domain Nut Pot": {
        'maps': (),
        'coordinates': (),
        'type': 'free'},
    "King Zora Thawed": {
        'maps': ('item_adult',),
        'coordinates': (373, 2550),
        'type': 'npc'},
    "Zoras Fountain Iceberg Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (292, 2554),
        'type': 'heart'},
    "Zoras Fountain Bottom Freestanding PoH": {
        'maps': ('item_adult',),
        'coordinates': (319, 2514),
        'type': 'heart'},
    "Zora Shop": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (499, 2619),
        'type': 'shop',
        'restriction': 'shopsanity'},
    "Zoras Fountain Fairy Reward": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (333, 2553),
        'type': 'fairy'},
    "Epona": {
        'maps': (),
        'coordinates': (),
        'type': 'npc'},
    "Song from Malon": {
        'maps': ('item_child',),
        'coordinates': (647, 1295),
        'type': 'song'},
    "Talons Chickens": {
        'maps': ('item_child',),
        'coordinates': (580, 1348),
        'type': 'npc'},
    "Lon Lon Tower Freestanding PoH": {
        'maps': ('item_child',),
        'coordinates': (690, 1227),
        'type': 'heart'},
    "Sheik Forest Song": {
        'maps': ('item_adult',),
        'coordinates': (626, 2160),
        'type': 'song'},
    "Kokiri Forest Storms Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (845, 2192),
        'type': 'sub'},
    "Lost Woods Generic Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (777, 2149),
        'type': 'sub'},
    "Deku Theater Skull Mask": {
        'maps': ('item_child',),
        'coordinates': (730, 2078),
        'type': 'sub'},
    "Deku Theater Mask of Truth": {
        'maps': ('item_child',),
        'coordinates': (730, 2118),
        'type': 'sub'},
    "LW Grotto Deku Scrub Arrows": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (724, 2260),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LW Grotto Deku Scrub Deku Nut Upgrade": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (724, 2220),
        'type': 'deku'},
    "SFM Grotto Deku Scrub Red Potion": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (626, 2220),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "SFM Grotto Deku Scrub Green Potion": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (626, 2260),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Wolfos Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (710, 2180),
        'type': 'sub'},
    "LLR Grotto Deku Scrub Deku Nuts": {
        'maps': ('item_child',),
        'coordinates': (690, 1375),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LLR Grotto Deku Scrub Bombs": {
        'maps': ('item_child',),
        'coordinates': (670, 1415),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LLR Grotto Deku Scrub Arrows": {
        'maps': ('item_child',),
        'coordinates': (710, 1335),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Remote Southern Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (925, 1427),
        'type': 'sub'},
    "Field Near Lake Outside Fence Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (997, 1206),
        'type': 'sub'},
    "HF Grotto Deku Scrub Piece of Heart": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (999, 1141),
        'type': 'deku'},
    "Field West Castle Town Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (440, 1372),
        'type': 'sub'},
    "Tektite Grotto Freestanding PoH": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (481, 1152),
        'type': 'sub'},
    "Redead Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (406, 1774),
        'type': 'sub'},
    "Kakariko Back Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (326, 1865),
        'type': 'sub'},
    "Mountain Storms Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (158, 1705),
        'type': 'sub'},
    "Goron Grotto Deku Scrub Deku Nuts": {
        'maps': ('item_adult',),
        'coordinates': (115, 1689),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Goron Grotto Deku Scrub Bombs": {
        'maps': ('item_adult',),
        'coordinates': (75, 1689),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Goron Grotto Deku Scrub Arrows": {
        'maps': ('item_adult',),
        'coordinates': (35, 1689),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Top of Crater Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (42, 1794),
        'type': 'sub'},
    "DMC Grotto Deku Scrub Deku Nuts": {
        'maps': ('item_adult',),
        'coordinates': (146, 1830),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "DMC Grotto Deku Scrub Bombs": {
        'maps': ('item_adult',),
        'coordinates': (126, 1870),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "DMC Grotto Deku Scrub Arrows": {
        'maps': ('item_adult',),
        'coordinates': (106, 1910),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Zora River Plateau Open Grotto Chest": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (540, 2092),
        'type': 'sub'},
    "ZR Grotto Deku Scrub Red Potion": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (560, 2052),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "ZR Grotto Deku Scrub Green Potion": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (580, 2012),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LH Grotto Deku Scrub Deku Nuts": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1309, 870),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LH Grotto Deku Scrub Bombs": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1289, 830),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "LH Grotto Deku Scrub Arrows": {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1329, 830),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Desert Grotto Deku Scrub Red Potion": {
        'maps': ('item_adult',),
        'coordinates': (245, 200),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Desert Grotto Deku Scrub Green Potion": {
        'maps': ('item_adult',),
        'coordinates': (285, 200),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Valley Grotto Deku Scrub Red Potion": {
        'maps': ('item_adult',),
        'coordinates': (630, 605),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Valley Grotto Deku Scrub Green Potion": {
        'maps': ('item_adult',),
        'coordinates': (630, 565),
        'type': 'deku',
        'restriction': 'scrubshuffle'},

    # Deku Tree
    "Deku Tree Lobby Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (565, 1283),
        'type': 'chest'},
    "Deku Tree Compass Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (140, 769),
        'type': 'chest'},
    "Deku Tree Compass Room Side Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (260, 760),
        'type': 'chest'},
    "Deku Tree Basement Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (1280, 1350),
        'type': 'chest'},
    "Deku Tree Slingshot Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (480, 350),
        'type': 'chest'},
    "Deku Tree Slingshot Room Side Chest": {
        'maps': ('Deku Tree',),
        'coordinates': (390, 470),
        'type': 'chest'},
    "Queen Gohma Heart": {
        'maps': ('Deku Tree',),
        'coordinates': (1580, 1590),
        'type': 'chest'},
    "Queen Gohma": {
        'maps': ('Deku Tree',),
        'coordinates': (1530, 1650),
        'type': 'chest'},

    # Dodongo's Cavern
    "Dodongos Cavern Map Chest": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1530, 930),
        'type': 'chest'},
    "Dodongos Cavern Compass Chest": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1460, 110),
        'type': 'chest'},
    "DC Deku Scrub Deku Sticks": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1580, 760),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "DC Deku Scrub Deku Shield": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1640, 2760),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Dodongos Cavern Bomb Flower Platform": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (790, 1470),
        'type': 'chest'},
    "DC Deku Scrub Deku Seeds": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (600, 2030),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "DC Deku Scrub Deku Nuts": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (640, 2150),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Dodongos Cavern Bomb Bag Chest": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (630, 1680),
        'type': 'chest'},
    "Dodongos Cavern End of Bridge Chest": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (360, 1070),
        'type': 'chest'},
    "Chest Above King Dodongo": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1200, 1450),
        'type': 'chest'},
    "King Dodongo Heart": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1100, 980),
        'type': 'chest'},
    "King Dodongo": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1090, 1040),
        'type': 'chest'},

    # Jabu Jabus Belly's Belly
    "Boomerang Chest": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (830, 2600),
        'type': 'chest'},
    "Jabu Deku Scrub Deku Nuts": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1250, 730),
        'type': 'deku',
        'restriction': 'scrubshuffle'},
    "Jabu Jabus Belly Map Chest": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (450, 1450),
        'type': 'chest'},
    "Jabu Jabus Belly Compass Chest": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (460, 2150),
        'type': 'chest'},
    "Barinade Heart": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1070, 2120),
        'type': 'chest'},
    "Barinade": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1040, 2200),
        'type': 'chest'},

    # Forest Temple
    "Forest Temple First Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (1850, 180),
        'type': 'chest'},
    "Forest Temple Chest Behind Lobby": {
        'maps': ('Forest Temple',),
        'coordinates': (1520, 1740),
        'type': 'chest'},
    "Forest Temple Well Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (2280, 1500),
        'type': 'chest'},
    "Forest Temple Map Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (1080, 1520),
        'type': 'chest'},
    "Forest Temple Outside Hookshot Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (1750, 2340),
        'type': 'chest'},
    "Forest Temple Falling Room Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (2040, 2420),
        'type': 'chest'},
    "Forest Temple Block Push Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (1420, 320),
        'type': 'chest'},
    "Forest Temple Boss Key Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (560, 1350),
        'type': 'chest'},
    "Forest Temple Floormaster Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (1000, 490),
        'type': 'chest'},
    "Forest Temple Bow Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (610, 2010),
        'type': 'chest'},
    "Forest Temple Red Poe Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (490, 1880),
        'type': 'chest'},
    "Forest Temple Blue Poe Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (650, 2260),
        'type': 'chest'},
    "Forest Temple Near Boss Chest": {
        'maps': ('Forest Temple',),
        'coordinates': (2560, 310),
        'type': 'chest'},
    "Phantom Ganon Heart": {
        'maps': ('Forest Temple',),
        'coordinates': (2340, 1240),
        'type': 'chest'},
    "Phantom Ganon": {
        'maps': ('Forest Temple',),
        'coordinates': (2290, 1200),
        'type': 'chest'},

    # Fire Temple
    "Fire Temple Chest Near Boss": {
        'maps': ('Fire Temple',),
        'coordinates': (2400, 960),
        'type': 'chest'},
    "Fire Temple Fire Dancer Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (2040, 2210),
        'type': 'chest'},
    "Fire Temple Boss Key Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (2190, 1920),
        'type': 'chest'},
    "Fire Temple Big Lava Room Bombable Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (3020, 1880),
        'type': 'chest'},
    "Fire Temple Big Lava Room Open Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (2650, 3330),
        'type': 'chest'},
    "Volvagia Heart": {
        'maps': ('Fire Temple',),
        'coordinates': (2160, 660),
        'type': 'chest'},
    "Volvagia": {
        'maps': ('Fire Temple',),
        'coordinates': (2120, 510),
        'type': 'chest'},
    "Fire Temple Boulder Maze Lower Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (1890, 2800),
        'type': 'chest'},
    "Fire Temple Boulder Maze Upper Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (1820, 2640),
        'type': 'chest'},
    "Fire Temple Boulder Maze Side Room": {
        'maps': ('Fire Temple',),
        'coordinates': (1480, 3470),
        'type': 'chest'},
    "Fire Temple Boulder Maze Bombable Pit": {
        'maps': ('Fire Temple',),
        'coordinates': (2240, 3120),
        'type': 'chest'},
    "Fire Temple Scarecrow Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (820, 3250),
        'type': 'chest'},
    "Fire Temple Map Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (1500, 2000),
        'type': 'chest'},
    "Fire Temple Compass Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (1100, 1540),
        'type': 'chest'},
    "Fire Temple Highest Goron Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (1650, 900),
        'type': 'chest'},
    "Fire Temple Megaton Hammer Chest": {
        'maps': ('Fire Temple',),
        'coordinates': (270, 140),
        'type': 'chest'},

    # Water Temple
    "Water Temple Map Chest": {
        'maps': ('Water Temple',),
        'coordinates': (1970, 2690),
        'type': 'chest'},
    "Water Temple Compass Chest": {
        'maps': ('Water Temple',),
        'coordinates': (1700, 2920),
        'type': 'chest'},
    "Water Temple Torches Chest": {
        'maps': ('Water Temple',),
        'coordinates': (2220, 2550),
        'type': 'chest'},
    "Water Temple Dragon Chest": {
        'maps': ('Water Temple',),
        'coordinates': (890, 1430),
        'type': 'chest'},
    "Water Temple Central Bow Target Chest": {
        'maps': ('Water Temple',),
        'coordinates': (2280, 1400),
        'type': 'chest'},
    "Water Temple Boss Key Chest": {
        'maps': ('Water Temple',),
        'coordinates': (1290, 2390),
        'type': 'chest'},
    "Morpha Heart": {
        'maps': ('Water Temple',),
        'coordinates': (970, 2670),
        'type': 'chest'},
    "Morpha": {
        'maps': ('Water Temple',),
        'coordinates': (930, 2740),
        'type': 'chest'},
    "Water Temple Central Pillar Chest": {
        'maps': ('Water Temple',),
        'coordinates': (2630, 2000),
        'type': 'chest'},
    "Water Temple Cracked Wall Chest": {
        'maps': ('Water Temple',),
        'coordinates': (1980, 2380),
        'type': 'chest'},
    "Water Temple Dark Link Chest": {
        'maps': ('Water Temple',),
        'coordinates': (170, 1700),
        'type': 'chest'},
    "Water Temple River Chest": {
        'maps': ('Water Temple',),
        'coordinates': (760, 1930),
        'type': 'chest'},

    # Spirit Temple
    "Spirit Temple Child Left Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1310, 140),
        'type': 'chest'},
    "Spirit Temple Child Right Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1370, 660),
        'type': 'chest'},
    "Spirit Temple Nut Crate": {
        'maps': (),
        'coordinates': (),
        'type': 'free'},
    "Spirit Temple Child Climb East Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (340, 1280),
        'type': 'chest'},
    "Spirit Temple Child Climb North Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (280, 1210),
        'type': 'chest'},
    "Spirit Temple Compass Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1320, 950),
        'type': 'chest'},
    "Spirit Temple Early Adult Right Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1120, 1440),
        'type': 'chest'},
    "Spirit Temple First Mirror Right Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (520, 2100),
        'type': 'chest'},
    "Spirit Temple First Mirror Left Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (460, 2100),
        'type': 'chest'},
    "Spirit Temple Map Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (320, 1600),
        'type': 'chest'},
    "Spirit Temple Sun Block Room Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (2280, 2100),
        'type': 'chest'},
    "Spirit Temple Statue Hand Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1610, 2480),
        'type': 'chest'},
    "Spirit Temple NE Main Room Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1500, 2890),
        'type': 'chest'},
    "Silver Gauntlets Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (2710, 2410),
        'type': 'chest'},
    "Mirror Shield Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (2710, 2920),
        'type': 'chest'},
    "Spirit Temple Near Four Armos Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (1840, 3380),
        'type': 'chest'},
    "Spirit Temple Hallway Left Invisible Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (2460, 3440),
        'type': 'chest'},
    "Spirit Temple Hallway Right Invisible Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (2460, 3370),
        'type': 'chest'},
    "Spirit Temple Boss Key Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (90, 890),
        'type': 'chest'},
    "Spirit Temple Topmost Chest": {
        'maps': ('Spirit Temple',),
        'coordinates': (370, 340),
        'type': 'chest'},
    "Twinrova Heart": {
        'maps': ('Spirit Temple',),
        'coordinates': (250, 2810),
        'type': 'chest'},
    "Twinrova": {
        'maps': ('Spirit Temple',),
        'coordinates': (420, 2640),
        'type': 'chest'},

    # Shadow Temple
    "Shadow Temple Map Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (550, 3130),
        'type': 'chest'},
    "Shadow Temple Hover Boots Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (850, 2700),
        'type': 'chest'},
    "Shadow Temple Compass Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (550, 5020),
        'type': 'chest'},
    "Shadow Temple Early Silver Rupee Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (210, 4480),
        'type': 'chest'},
    "Shadow Temple Invisible Blades Visible Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (700, 5870),
        'type': 'chest'},
    "Shadow Temple Invisible Blades Invisible Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (750, 5990),
        'type': 'chest'},
    "Shadow Temple Falling Spikes Lower Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (1640, 4760),
        'type': 'chest'},
    "Shadow Temple Falling Spikes Upper Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (1740, 4830),
        'type': 'chest'},
    "Shadow Temple Falling Spikes Switch Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (1610, 4970),
        'type': 'chest'},
    "Shadow Temple Invisible Spikes Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (1430, 4070),
        'type': 'chest'},
    "Shadow Temple Freestanding Key": {
        'maps': ('Shadow Temple',),
        'coordinates': (1470, 3646),
        'type': 'chest'},
    "Shadow Temple Wind Hint Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (970, 4440),
        'type': 'chest'},
    "Shadow Temple After Wind Enemy Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (910, 3640),
        'type': 'chest'},
    "Shadow Temple After Wind Hidden Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (940, 3790),
        'type': 'chest'},
    "Shadow Temple Spike Walls Left Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (2060, 240),
        'type': 'chest'},
    "Shadow Temple Boss Key Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (2000, 430),
        'type': 'chest'},
    "Shadow Temple Hidden Floormaster Chest": {
        'maps': ('Shadow Temple',),
        'coordinates': (2330, 1210),
        'type': 'chest'},
    "Bongo Bongo Heart": {
        'maps': ('Shadow Temple',),
        'coordinates': (2290, 2800),
        'type': 'chest'},
    "Bongo Bongo": {
        'maps': ('Shadow Temple',),
        'coordinates': (2260, 2930),
        'type': 'chest'},

    # Bottom of the Well
    "Bottom of the Well Front Left Hidden Wall": {
        'maps': ('Bottom of the Well',),
        'coordinates': (630, 870),
        'type': 'chest'},
    "Bottom of the Well Front Center Bombable": {
        'maps': ('Bottom of the Well',),
        'coordinates': (620, 970),
        'type': 'chest'},
    "Bottom of the Well Right Bottom Hidden Wall": {
        'maps': ('Bottom of the Well',),
        'coordinates': (620, 1240),
        'type': 'chest'},
    "Bottom of the Well Center Large Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (530, 920),
        'type': 'chest'},
    "Bottom of the Well Center Small Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (530, 1180),
        'type': 'chest'},
    "Bottom of the Well Back Left Bombable": {
        'maps': ('Bottom of the Well',),
        'coordinates': (100, 620),
        'type': 'chest'},
    "Bottom of the Well Freestanding Key": {
        'maps': ('Bottom of the Well',),
        'coordinates': (450, 110),
        'type': 'chest'},
    "Bottom of the Well Defeat Boss": {
        'maps': ('Bottom of the Well',),
        'coordinates': (790, 1560),
        'type': 'chest'},
    "Bottom of the Well Invisible Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (780, 1680),
        'type': 'chest'},
    "Bottom of the Well Underwater Front Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (780, 1010),
        'type': 'chest'},
    "Bottom of the Well Underwater Left Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (400, 510),
        'type': 'chest'},
    "Bottom of the Well Basement Chest": {
        'maps': ('Bottom of the Well',),
        'coordinates': (1560, 1900),
        'type': 'chest'},
    "Bottom of the Well Locked Pits": {
        'maps': ('Bottom of the Well',),
        'coordinates': (330, 1510),
        'type': 'chest'},
    "Bottom of the Well Behind Right Grate": {
        'maps': ('Bottom of the Well',),
        'coordinates': (400, 1480),
        'type': 'chest'},
    "Bottom of the Well Stick Pot": {
        'maps': (),
        'coordinates': (),
        'type': 'free'},

    # Ice Caverns
    "Ice Cavern Map Chest": {
        'maps': ('Ice Cavern',),
        'coordinates': (240, 1990),
        'type': 'chest'},
    "Ice Cavern Compass Chest": {
        'maps': ('Ice Cavern',),
        'coordinates': (1070, 1530),
        'type': 'chest'},
    "Ice Cavern Iron Boots Chest": {
        'maps': ('Ice Cavern',),
        'coordinates': (620, 510),
        'type': 'chest'},
    "Ice Cavern Freestanding PoH": {
        'maps': ('Ice Cavern',),
        'coordinates': (1020, 1730),
        'type': 'chest'},
    "Sheik in Ice Cavern": {
        'maps': ('Ice Cavern',),
        'coordinates': (580, 510),
        'type': 'chest'},

    # Gerudo Training Grounds
    "Gerudo Training Grounds Lobby Left Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1540, 730),
        'type': 'chest'},
    "Gerudo Training Grounds Lobby Right Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1540, 910),
        'type': 'chest'},
    "Gerudo Training Grounds Stalfos Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1500, 170),
        'type': 'chest'},
    "Gerudo Training Grounds Beamos Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1630, 1440),
        'type': 'chest'},
    "Gerudo Training Grounds Hidden Ceiling Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1470, 1180),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Path First Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1080, 580),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Path Second Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (880, 660),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Path Third Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (890, 720),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Path Final Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1050, 820),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Right Central Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1080, 920),
        'type': 'chest'},
    "Gerudo Training Grounds Maze Right Side Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1020, 980),
        'type': 'chest'},
    "Gerudo Training Grounds Freestanding Key": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1080, 1270),
        'type': 'chest'},
    "Gerudo Training Grounds Underwater Silver Rupee Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1060, 1730),
        'type': 'chest'},
    "Gerudo Training Grounds Hammer Room Clear Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (470, 1430),
        'type': 'chest'},
    "Gerudo Training Grounds Hammer Room Switch Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (590, 1430),
        'type': 'chest'},
    "Gerudo Training Grounds Eye Statue Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (570, 870),
        'type': 'chest'},
    "Gerudo Training Grounds Near Scarecrow Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (1330, 1170),
        'type': 'chest'},
    "Gerudo Training Grounds Before Heavy Block Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (540, 290),
        'type': 'chest'},
    "Gerudo Training Grounds Heavy Block First Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (200, 240),
        'type': 'chest'},
    "Gerudo Training Grounds Heavy Block Second Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (160, 170),
        'type': 'chest'},
    "Gerudo Training Grounds Heavy Block Third Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (110, 250),
        'type': 'chest'},
    "Gerudo Training Grounds Heavy Block Fourth Chest": {
        'maps': ('Gerudo Training Grounds',),
        'coordinates': (70, 170),
        'type': 'chest'},

    # Ganon's Castle
    "GC Deku Scrub Bombs": {
        'maps': ('Ganons Castle',),
        'coordinates': (2720, 2060),
        'type': 'chest',
        'restriction': 'scrubshuffle'},
    "GC Deku Scrub Arrows": {
        'maps': ('Ganons Castle',),
        'coordinates': (2770, 1990),
        'type': 'chest',
        'restriction': 'scrubshuffle'},
    "GC Deku Scrub Red Potion": {
        'maps': ('Ganons Castle',),
        'coordinates': (2770, 1920),
        'type': 'chest',
        'restriction': 'scrubshuffle'},
    "GC Deku Scrub Green Potion": {
        'maps': ('Ganons Castle',),
        'coordinates': (2720, 1850),
        'type': 'chest',
        'restriction': 'scrubshuffle'},
    "Ganons Castle Forest Trial Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (2400, 2140),
        'type': 'chest'},
    "Ganons Castle Forest Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Castle Fire Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Castle Water Trial Left Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1620, 2580),
        'type': 'chest'},
    "Ganons Castle Water Trial Right Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1850, 2580),
        'type': 'chest'},
    "Ganons Castle Water Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Castle Shadow Trial First Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1090, 1980),
        'type': 'chest'},
    "Ganons Castle Shadow Trial Second Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (660, 2470),
        'type': 'chest'},
    "Ganons Castle Shadow Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Castle Spirit Trial First Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (2310, 1130),
        'type': 'chest'},
    "Ganons Castle Spirit Trial Second Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (2450, 1050),
        'type': 'chest'},
    "Ganons Castle Spirit Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Castle Light Trial First Left Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1860, 1210),
        'type': 'chest'},
    "Ganons Castle Light Trial Second Left Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1900, 1120),
        'type': 'chest'},
    "Ganons Castle Light Trial Third Left Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1860, 990),
        'type': 'chest'},
    "Ganons Castle Light Trial First Right Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1650, 1210),
        'type': 'chest'},
    "Ganons Castle Light Trial Second Right Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1610, 1120),
        'type': 'chest'},
    "Ganons Castle Light Trial Third Right Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1650, 990),
        'type': 'chest'},
    "Ganons Castle Light Trial Invisible Enemies Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1750, 1120),
        'type': 'chest'},
    "Ganons Castle Light Trial Lullaby Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1710, 930),
        'type': 'chest'},
    "Ganons Castle Light Trial Clear": {
        'maps': (),
        'coordinates': (),
        'type': 'chest'},
    "Ganons Tower Boss Key Chest": {
        'maps': ('Ganons Castle',),
        'coordinates': (1850, 3670),
        'type': 'chest'},

    # The final destination
    "Ganon": {
        'maps': ('item_adult',),
        'coordinates': (50, 1440),
        'type': 'ganon'},

    # Gossip stones
    'Kokiri Forest Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (890, 2095),
        'type': 'stone'},
    'Deku Tree Gossip Stone (Left)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (790, 2400),
        'type': 'stone'},
    'Deku Tree Gossip Stone (Right)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (840, 2550),
        'type': 'stone'},
    'Sacred Forest Meadow Maze Gossip Stone (Lower)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (670, 2180),
        'type': 'stone'},
    'Sacred Forest Meadow Saria Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (620, 2120),
        'type': 'stone'},
    'Lost Woods Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (940, 1930),
        'type': 'stone'},
    'Temple of Time Gossip Stone (Left)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (320, 1543),
        'type': 'stone'},
    'Hyrule Castle Malon Gossip Stone': {
        'maps': ('item_child',),
        'coordinates': (270, 1465),
        'type': 'stone'},
    'Hyrule Castle Rock Wall Gossip Stone': {
        'maps': ('item_child',),
        'coordinates': (210, 1360),
        'type': 'stone'},
    'Castle Storms Grotto Gossip Stone': {
        'maps': ('item_child',),
        'coordinates': (196, 1520),
        'type': 'stone'},
    'Graveyard Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (380, 2150),
        'type': 'stone'},
    'Goron City Medigoron Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (158, 1606),
        'type': 'stone'},
    'Goron City Maze Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (50, 1636),
        'type': 'stone'},
    'Dodongos Cavern Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (230, 1700),
        'type': 'stone'},
    'Death Mountain Trail Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (140, 1790),
        'type': 'stone'},
    'Death Mountain Crater Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (105, 1830),
        'type': 'stone'},
    'Zoras River Plateau Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (470, 2100),
        'type': 'stone'},
    'Zoras River Waterfall Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (470, 2400),
        'type': 'stone'},
    'Zoras Domain Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (373, 2590),
        'type': 'stone'},
    'Lake Hylia Lab Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1220, 870),
        'type': 'stone'},
    'Lake Hylia Gossip Stone (Southwest)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1520, 930),
        'type': 'stone'},
    'Lake Hylia Gossip Stone (Southeast)': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1520, 1190),
        'type': 'stone'},
    'Zoras Fountain Jabu Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (359, 2510),
        'type': 'stone'},
    'Zoras River Plateau Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (313, 2593),
        'type': 'stone'},
    'Field Valley Grotto Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (680, 950),
        'type': 'stone'},
    'Gerudo Valley Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (530, 661),
        'type': 'stone'},
    'Desert Colossus Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (370, 50),
        'type': 'stone'},
    'Generic Grotto Gossip Stone': {
        'maps': ('item_child', 'item_adult'),
        'coordinates': (1200, 480),
        'type': 'stone'}
}


SKULLTULALOCATIONS = {
    "GS Kokiri Know It All House": {
        'maps': ('skulls_child',),
        'coordinates': (958, 2055),
        'type': 'night'},
    "GS Kokiri Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (917, 2256),
        'type': 'bean'},
    "GS Kokiri House of Twins": {
        'maps': ('skulls_adult',),
        'coordinates': (981, 2262),
        'type': 'night'},
    "GS Lost Woods Bean Patch Near Bridge": {
        'maps': ('skulls_child',),
        'coordinates': (824, 2062),
        'type': 'bean'},
    "GS Lost Woods Bean Patch Near Stage": {
        'maps': ('skulls_child',),
        'coordinates': (740, 2142),
        'type': 'bean'},
    "GS Lake Hylia Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (1179, 1002),
        'type': 'bean'},
    "GS Lake Hylia Lab Wall": {
        'maps': ('skulls_child',),
        'coordinates': (1207, 930),
        'type': 'night'},
    "GS Lake Hylia Small Island": {
        'maps': ('skulls_child',),
        'coordinates': (1405, 1132),
        'type': 'night'},
    "GS Lake Hylia Giant Tree": {
        'maps': ('skulls_adult',),
        'coordinates': (1415, 1009),
        'type': 'night'},
    "GS Lab Underwater Crate": {
        'maps': ('skulls_adult',),
        'coordinates': (1229, 959),
        'type': 'tree'},
    "GS Gerudo Valley Small Bridge": {
        'maps': ('skulls_child',),
        'coordinates': (560, 806),
        'type': 'night'},
    "GS Gerudo Valley Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (594, 667),
        'type': 'bean'},
    "GS Gerudo Valley Behind Tent": {
        'maps': ('skulls_adult',),
        'coordinates': (517, 635),
        'type': 'night'},
    "GS Gerudo Valley Pillar": {
        'maps': ('skulls_adult',),
        'coordinates': (581, 571),
        'type': 'night'},
    "GS Gerudo Fortress Archery Range": {
        'maps': ('skulls_adult',),
        'coordinates': (306, 660),
        'type': 'night'},
    "GS Gerudo Fortress Top Floor": {
        'maps': ('skulls_adult',),
        'coordinates': (375, 544),
        'type': 'night'},
    "GS Wasteland Ruins": {
        'maps': ('skulls_adult',),
        'coordinates': (313, 360),
        'type': 'high'},
    "GS Desert Colossus Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (347, 88),
        'type': 'bean'},
    "GS Desert Colossus Tree": {
        'maps': ('skulls_adult',),
        'coordinates': (433, 157),
        'type': 'night'},
    "GS Desert Colossus Hill": {
        'maps': ('skulls_adult',),
        'coordinates': (322, 233),
        'type': 'night'},
    "GS Hyrule Castle Tree": {
        'maps': ('skulls_child',),
        'coordinates': (246, 1409),
        'type': 'tree'},
    "GS Outside Ganon's Castle": {
        'maps': ('skulls_adult',),
        'coordinates': (206, 1490),
        'type': 'spider'},
    "GS Castle Market Guard House": {
        'maps': ('skulls_child',),
        'coordinates': (390, 1464),
        'type': 'tree'},
    "GS Kakariko House Under Construction": {
        'maps': ('skulls_child',),
        'coordinates': (401, 1837),
        'type': 'night'},
    "GS Kakariko Skulltula House": {
        'maps': ('skulls_child',),
        'coordinates': (427, 1767),
        'type': 'night'},
    "GS Kakariko Guard's House": {
        'maps': ('skulls_child',),
        'coordinates': (347, 1774),
        'type': 'night'},
    "GS Kakariko Tree": {
        'maps': ('skulls_child',),
        'coordinates': (387, 1734),
        'type': 'tree'},
    "GS Kakariko Watchtower": {
        'maps': ('skulls_child',),
        'coordinates': (341, 1814),
        'type': 'night'},
    "GS Kakariko Above Impa's House": {
        'maps': ('skulls_adult',),
        'coordinates': (418, 1767),
        'type': 'night'},
    "GS Graveyard Wall": {
        'maps': ('skulls_child',),
        'coordinates': (380, 2065),
        'type': 'night'},
    "GS Graveyard Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (335, 2000),
        'type': 'bean'},
    "GS Mountain Trail Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (252, 1684),
        'type': 'bean'},
    "GS Mountain Trail Bomb Alcove": {
        'maps': ('skulls_child', 'skulls_adult'),
        'coordinates': (278, 1728),
        'type': 'spider'},
    "GS Mountain Trail Path to Crater": {
        'maps': ('skulls_adult',),
        'coordinates': (190, 1694),
        'type': 'night'},
    "GS Mountain Trail Above Dodongo's Cavern": {
        'maps': ('skulls_adult',),
        'coordinates': (158, 1744),
        'type': 'night'},
    "GS Goron City Boulder Maze": {
        'maps': ('skulls_child',),
        'coordinates': (68, 1591),
        'type': 'tree'},
    "GS Goron City Center Platform": {
        'maps': ('skulls_adult',),
        'coordinates': (90, 1646),
        'type': 'spider'},
    "GS Death Mountain Crater Crate": {
        'maps': ('skulls_child',),
        'coordinates': (80, 1796),
        'type': 'tree'},
    "GS Mountain Crater Bean Patch": {
        'maps': ('skulls_child',),
        'coordinates': (66, 1871),
        'type': 'bean'},
    "GS Zora River Tree": {
        'maps': ('skulls_child',),
        'coordinates': (545, 1935),
        'type': 'tree'},
    "GS Zora River Ladder": {
        'maps': ('skulls_child',),
        'coordinates': (458, 2360),
        'type': 'tree'},
    "GS Zora River Near Raised Grottos": {
        'maps': ('skulls_adult',),
        'coordinates': (540, 2060),
        'type': 'night'},
    "GS Zora River Above Bridge": {
        'maps': ('skulls_adult',),
        'coordinates': (465, 2280),
        'type': 'night'},
    "GS Zora's Fountain Tree": {
        'maps': ('skulls_child',),
        'coordinates': (310, 2519),
        'type': 'tree'},
    "GS Zora's Fountain Above the Log": {
        'maps': ('skulls_child',),
        'coordinates': (350, 2519),
        'type': 'night'},
    "GS Zora's Domain Frozen Waterfall": {
        'maps': ('skulls_adult',),
        'coordinates': (418, 2558),
        'type': 'night'},
    "GS Zora's Fountain Hidden Cave": {
        'maps': ('skulls_adult',),
        'coordinates': (310, 2585),
        'type': 'high'},
    "GS Lon Lon Ranch Tree": {
        'maps': ('skulls_child',),
        'coordinates': (617, 1363),
        'type': 'tree'},
    "GS Lon Lon Ranch Rain Shed": {
        'maps': ('skulls_child',),
        'coordinates': (677, 1325),
        'type': 'night'},
    "GS Lon Lon Ranch House Window": {
        'maps': ('skulls_child',),
        'coordinates': (610, 1323),
        'type': 'night'},
    "GS Lon Lon Ranch Back Wall": {
        'maps': ('skulls_child',),
        'coordinates': (663, 1197),
        'type': 'night'},
    "GS Lost Woods Above Stage": {
        'maps': ('skulls_adult',),
        'coordinates': (740, 2142),
        'type': 'high'},
    "GS Sacred Forest Meadow": {
        'maps': ('skulls_adult',),
        'coordinates': (664, 2230),
        'type': 'night'},
    "GS Hyrule Field Near Gerudo Valley": {
        'maps': ('skulls_child', 'skulls_adult'),
        'coordinates': (658, 972),
        'type': 'high'},
    "GS Hyrule Field near Kakariko": {
        'maps': ('skulls_child', 'skulls_adult'),
        'coordinates': (406, 1552),
        'type': 'high'},
    "GS Hyrule Castle Grotto": {
        'maps': ('skulls_child',),
        'coordinates': (206, 1479),
        'type': 'spider'},
    "GS Deku Tree Compass Room": {
        'maps': ('Deku Tree',),
        'coordinates': (220, 660),
        'type': 'spider'},
    "GS Deku Tree Basement Vines": {
        'maps': ('Deku Tree',),
        'coordinates': (1150, 1280),
        'type': 'spider'},
    "GS Deku Tree Basement Gate": {
        'maps': ('Deku Tree',),
        'coordinates': (1320, 1010),
        'type': 'spider'},
    "GS Deku Tree Basement Back Room": {
        'maps': ('Deku Tree',),
        'coordinates': (750, 490),
        'type': 'spider'},
    "GS Dodongo's Cavern East Side Room": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (2350, 1310),
        'type': 'spider'},
    "GS Dodongo's Cavern Scarecrow": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (2060, 1720),
        'type': 'spider'},
    "GS Dodongo's Cavern Vines Above Stairs": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (130, 520),
        'type': 'spider'},
    "GS Dodongo's Cavern Alcove Above Stairs": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (90, 740),
        'type': 'spider'},
    "GS Dodongo's Cavern Back Room": {
        'maps': ('Dodongos Cavern',),
        'coordinates': (1250, 2990),
        'type': 'spider'},
    "GS Jabu Jabu Water Switch Room": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1870, 2160),
        'type': 'spider'},
    "GS Jabu Jabu Lobby Basement Lower": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1480, 2170),
        'type': 'spider'},
    "GS Jabu Jabu Lobby Basement Upper": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1460, 2060),
        'type': 'spider'},
    "GS Jabu Jabu Near Boss": {
        'maps': ('Jabu Jabus Belly',),
        'coordinates': (1270, 1700),
        'type': 'spider'},
    "GS Forest Temple First Room": {
        'maps': ('Forest Temple',),
        'coordinates': (1850, 340),
        'type': 'spider'},
    "GS Forest Temple Lobby": {
        'maps': ('Forest Temple',),
        'coordinates': (1660, 1410),
        'type': 'spider'},
    "GS Forest Temple Outdoor West": {
        'maps': ('Forest Temple',),
        'coordinates': (920, 1130),
        'type': 'spider'},
    "GS Forest Temple Outdoor East": {
        'maps': ('Forest Temple',),
        'coordinates': (1690, 2370),
        'type': 'spider'},
    "GS Forest Temple Basement": {
        'maps': ('Forest Temple',),
        'coordinates': (2480, 360),
        'type': 'spider'},
    "GS Fire Temple Song of Time Room": {
        'maps': ('Fire Temple',),
        'coordinates': (2420, 2950),
        'type': 'spider'},
    "GS Fire Temple Basement": {
        'maps': ('Fire Temple',),
        'coordinates': (2130, 2610),
        'type': 'spider'},
    "GS Fire Temple Unmarked Bomb Wall": {
        'maps': ('Fire Temple',),
        'coordinates': (1640, 3470),
        'type': 'spider'},
    "GS Fire Temple East Tower Climb": {
        'maps': ('Fire Temple',),
        'coordinates': (1120, 3060),
        'type': 'spider'},
    "GS Fire Temple East Tower Top": {
        'maps': ('Fire Temple',),
        'coordinates': (840, 3090),
        'type': 'spider'},
    "GS Water Temple South Basement": {
        'maps': ('Water Temple',),
        'coordinates': (1590, 840),
        'type': 'spider'},
    "GS Water Temple Near Boss Key Chest": {
        'maps': ('Water Temple',),
        'coordinates': (1390, 2210),
        'type': 'spider'},
    "GS Water Temple Central Room": {
        'maps': ('Water Temple',),
        'coordinates': (1970, 1900),
        'type': 'spider'},
    "GS Water Temple Serpent River": {
        'maps': ('Water Temple',),
        'coordinates': (590, 1970),
        'type': 'spider'},
    "GS Water Temple Falling Platform Room": {
        'maps': ('Water Temple',),
        'coordinates': (930, 930),
        'type': 'spider'},
    "GS Spirit Temple Metal Fence": {
        'maps': ('Spirit Temple',),
        'coordinates': (1460, 670),
        'type': 'spider'},
    "GS Spirit Temple Bomb for Light Room": {
        'maps': ('Spirit Temple',),
        'coordinates': (1370, 360),
        'type': 'spider'},
    "GS Spirit Temple Boulder Room": {
        'maps': ('Spirit Temple',),
        'coordinates': (1440, 1320),
        'type': 'spider'},
    "GS Spirit Temple Hall to West Iron Knuckle": {
        'maps': ('Spirit Temple',),
        'coordinates': (2310, 1930),
        'type': 'spider'},
    "GS Spirit Temple Lobby": {
        'maps': ('Spirit Temple',),
        'coordinates': (1490, 2360),
        'type': 'spider'},
    "GS Shadow Temple Like Like Room": {
        'maps': ('Shadow Temple',),
        'coordinates': (670, 5950),
        'type': 'spider'},
    "GS Shadow Temple Crusher Room": {
        'maps': ('Shadow Temple',),
        'coordinates': (1720, 4980),
        'type': 'spider'},
    "GS Shadow Temple Single Giant Pot": {
        'maps': ('Shadow Temple',),
        'coordinates': (1590, 3590),
        'type': 'spider'},
    "GS Shadow Temple Near Ship": {
        'maps': ('Shadow Temple',),
        'coordinates': (1180, 3230),
        'type': 'spider'},
    "GS Shadow Temple Triple Giant Pot": {
        'maps': ('Shadow Temple',),
        'coordinates': (2360, 170),
        'type': 'spider'},
    "GS Well West Inner Room": {
        'maps': ('Bottom of the Well',),
        'coordinates': (180, 920),
        'type': 'spider'},
    "GS Well East Inner Room": {
        'maps': ('Bottom of the Well',),
        'coordinates': (210, 1090),
        'type': 'spider'},
    "GS Well Like Like Cage": {
        'maps': ('Bottom of the Well',),
        'coordinates': (400, 1520),
        'type': 'spider'},
    "GS Ice Cavern Spinning Scythe Room": {
        'maps': ('Ice Cavern',),
        'coordinates': (680, 1420),
        'type': 'spider'},
    "GS Ice Cavern Heart Piece Room": {
        'maps': ('Ice Cavern',),
        'coordinates': (970, 1720),
        'type': 'spider'},
    "GS Ice Cavern Push Block Room": {
        'maps': ('Ice Cavern',),
        'coordinates': (290, 1180),
        'type': 'spider'},
}
