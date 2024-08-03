
def day_to_string(data: str) -> str:
    """
    Convert the day to string
    """
    day_mapping = {
        '2': 'MO',
        '3': 'TU',
        '4': 'WE',
        '5': 'TH',
        '6': 'FR',
        '7': 'SA',
        '8': 'SU'
    }
    
    return day_mapping[data]