import re
from datetime import datetime
import pytz

def is_iso_8601(date_string):
    iso_8601_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.\d+)?(Z|[+-][01][0-9]:[0-5][0-9])?$'
    match = re.match(iso_8601_regex, date_string)
    if not match:
        return False
    try:
        datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def time_format(data, **kwargs):
    """
    Format time to ISO 8601
    current_format = '%d-%m-%Y %H:%M:%S'
    """
    current_format = '%d-%m-%Y %H:%M:%S'
    timezone_str = kwargs.get('timezone', 'Asia/Ho_Chi_Minh')
    timezone = pytz.timezone(timezone_str)
    
    res = None
    
    # print('Data before format:', data)
        
    if isinstance(data, str):
        if is_iso_8601(data):
            res = data
        else:
            try:
                # Chuyển đổi chuỗi thành đối tượng datetime
                date_obj = datetime.strptime(data, current_format)
                date_obj = timezone.localize(date_obj)

                # Chuyển đổi đối tượng datetime thành định dạng ISO 8601 với múi giờ
                res = date_obj.isoformat()
            except ValueError:
                print("Invalid date format.")
    
    elif isinstance(data, datetime):
        if data.tzinfo is None:
            date_obj = timezone.localize(data)
        else:
            date_obj = data.astimezone(timezone)
        
        # Chuyển đổi đối tượng datetime thành định dạng ISO 8601 với múi giờ
        res = date_obj.isoformat()
        
    # print('Data after format:', res)
    
    return res

def time_format_until(data, **kwargs):
    """
    Format time to YYYYMMDDTHHMMSSZ
    """
    iso_date = time_format(data, **kwargs)
    
    if iso_date:
        try:
            # Parse the ISO 8601 date string to a datetime object
            # Convert to UTC if necessary
            if iso_date.endswith('Z'):
                dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
            else:
                dt = datetime.fromisoformat(iso_date)
                dt = dt.astimezone(pytz.UTC)
            
            # Format the datetime object to the desired format
            formatted_date = dt.strftime("%Y%m%dT%H%M%SZ")
            return formatted_date
        
        except ValueError as e:
            print(f"Error parsing ISO 8601 date: {e}")
            return None
    else:
        return None