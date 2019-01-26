'''
Hint item lists
'''


__all__ = 'HINTITEMS', 'HintTracker'


HINTITEMS = {
    'Magic Meter', 'Double Defense', 'Slingshot', 'Boomerang', 'Bow',
    'Bomb Bag', 'Progressive Hookshot', 'Progressive Strength Upgrade',
    'Progressive Scale', 'Hammer', 'Iron Boots', 'Hover Boots', 'Kokiri Sword',
    'Biggoron Sword', 'Deku Shield', 'Hylian Shield', 'Mirror Shield',
    'Farores Wind', 'Nayrus Love', 'Dins Fire', 'Fire Arrows', 'Light Arrows',
    'Lens of Truth', 'Ocarina', 'Goron Tunic', 'Zora Tunic', 'Epona',
    'Zeldas Lullaby', 'Eponas Song', 'Sarias Song', 'Suns Song',
    'Song of Time', 'Song of Storms', 'Minuet of Forest', 'Bolero of Fire',
    'Serenade of Water', 'Requiem of Spirit', 'Nocturne of Shadow',
    'Prelude of Light', 'Bottle', 'Bottle with Letter', 'Bottle with Big Poe',
    'Stone of Agony', 'Gerudo Membership Card', 'Progressive Wallet',
    'Heart Container', 'Rupees (200)', 'Weird Egg',
    'Pocket Egg', 'BossKey', 'SmallKey', 'Gold Skulltula Token'}


class HintTracker(dict):
    '''
    Hint storage
    '''

    def __init__(self, data: dict):
        '''
        Args:
            data: hint data
        '''

        super().__init__(data)
    
    def store(self) -> None:
        '''
        Store hint data.
        '''

        return self

    def load(self) -> list:
        '''
        Load hint data.

        Args:
            list: loaded data
        '''

        pass
