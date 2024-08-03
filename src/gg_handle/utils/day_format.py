def day_format(data):
    """
    Format days to RFC 5545
    """
    # Mapping of days to their respective codes
    day_mapping = {
        'monday': 'MO',
        'tuesday': 'TU',
        'wednesday': 'WE',
        'thursday': 'TH',
        'friday': 'FR',
        'saturday': 'SA',
        'sunday': 'SU',
        'mon': 'MO',
        'tue': 'TU',
        'wed': 'WE',
        'thu': 'TH',
        'fri': 'FR',
        'sat': 'SA',
        'sun': 'SU',
        'mo': 'MO',
        'tu': 'TU',
        'we': 'WE',
        'th': 'TH',
        'fr': 'FR',
        'sa': 'SA',
        'su': 'SU',
        2: 'MO',
        3: 'TU',
        4: 'WE',
        5: 'TH',
        6: 'FR',
        7: 'SA',
        8: 'SU'
    }

    # Initialize an empty list for results
    result = []

    # Normalize the input to lowercase for consistent matching
    def normalize_day(day):
        return day.strip().lower()

    # Process input based on its type
    if isinstance(data, str):
        # If input is a string, split by comma and handle each part
        days = data.split(',')
        for day in days:
            normalized_day = normalize_day(day)
            if normalized_day in day_mapping:
                result.append(day_mapping[normalized_day])
    elif isinstance(data, list):
        # If input is a list, process each element
        for item in data:
            # Check if the item is a string or integer
            normalized_item = normalize_day(item) if isinstance(item, str) else item
            if normalized_item in day_mapping:
                result.append(day_mapping[normalized_item])
    elif isinstance(data, int):
        # If input is an integer, use the mapping directly
        if 1 <= data <= 7:
            result.append(day_mapping[data])
    elif isinstance(data, (tuple, set)):
        # If input is a tuple or set, process each element
        for item in data:
            # Check if the item is a string or integer
            normalized_item = normalize_day(item) if isinstance(item, str) else item
            if normalized_item in day_mapping:
                result.append(day_mapping[normalized_item])
    else:
        # If input type is not handled, raise an error
        raise ValueError("Unsupported input type")

    # Join the result list with commas
    return ','.join(result)
