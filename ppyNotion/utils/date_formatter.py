'''
Include function to convert between ISO 8601 string and datetime class
'''
from datetime import datetime, timedelta


def iso8601_to_datetime(iso: str) -> datetime:
    '''
    from format yyyy-mm-ddThh:mm:ss.msm
    note without trailing 'Z'
    '''
    # haha, kidding I will replace it btw.
    iso = iso.replace('Z', '')
    return datetime.fromisoformat(iso)


def datetime_to_iso8601(
    datetime_object: datetime,
    offset_hour: float,
    add_offset: bool = False
) -> str:
    '''
    convert datetime to ISO8601 format

        Parameters:
            dt (datetime) : the datetime that want convert
            offset_hour (float) : just like time zone. will follow the string
                if offset is -07:30 -> offset_hour = -7.5
            add_offset (bool) : add offset to the datetime if `True`, not add otherwise
        Returns:
            string that be ISO8601 

    '''
    hours = int(abs(offset_hour))
    minutes = 0 if float(offset_hour).is_integer() else 30
    sign = -1 if offset_hour < 0 else 1
    offset_datetime = add_offset*sign*timedelta(hours=hours, minutes=minutes)

    time_zone = str('+' if sign > 0 else '-')
    time_zone += str(hours).zfill(2) + ':' + str(minutes).zfill(2)
    iso_format = (datetime_object + offset_datetime).isoformat()

    return iso_format + time_zone
