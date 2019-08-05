from datetime import datetime

import pytz

vn_timezone = pytz.timezone('Asia/Bangkok')


def current_time_rfc3339_str():
    time = datetime.utcnow()
    return datetime_format_rfc3339(time)


def datetime_format_rfc3339(date):
    t_with_timezone = date.replace(tzinfo=pytz.UTC)
    return t_with_timezone.isoformat()
