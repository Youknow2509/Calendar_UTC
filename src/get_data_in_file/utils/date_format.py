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

