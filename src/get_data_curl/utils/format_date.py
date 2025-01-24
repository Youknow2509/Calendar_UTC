
from datetime import datetime

def date_format(data: str) -> str:
    """
    Convert a date string from 'DD/MM/YYYY' to 'DD-MM-YYYY'.
    
    Args:
        data (str): A date string in the format 'DD/MM/YYYY'.
    
    Returns:
        str: The formatted date string in the format 'DD-MM-YYYY'.
    """
    # Parse the date string to a datetime object
    date_obj = datetime.strptime(data, '%d/%m/%Y')
    
    # Format the datetime object to the desired format
    formatted_date = date_obj.strftime('%d-%m-%Y')
    
    return formatted_date


def format_date(day, h, m):
    """
        Format date
            day: Ngay (ex: 06/01/2025) - format DD/MM/YYYY
            h: Gio (ex: 7.0) - format X.X
            m: Phut (ex: 0.0) - format Y.Y
        Output: DD-MM-YYYY HH:MM:SS
            Ex: 06-01-2025 07:00:00
    """
    
    day_formated = date_format(day)
    time_formated = time_format(h, m)
    
    return day_formated + ' ' + time_formated
    
def time_format(h, m):
    """
        Format time
            h: Gio (ex: 7.0) - format X.X
            m: Phut (ex: 0.0) - format Y.Y
        Output: HH:MM:SS
            Ex: 07:00:00
    """
    
    h = int(h)
    m = int(m)
    
    h = str(h)
    m = str(m)
    
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
        
    return h + ':' + m + ':00'
    