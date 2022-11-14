import pytz
import datetime

APP_TIMEZONE = pytz.timezone('America/Sao_Paulo')

def convert_date_time(dt: datetime.datetime):
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        # Aware
        return dt.replace(tzinfo=pytz.utc).astimezone(APP_TIMEZONE)
    # Naive
    return dt.astimezone(APP_TIMEZONE)