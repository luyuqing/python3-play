import datetime
import pytz
import tzlocal


dt = datetime.datetime(2020, 7, 8)
print(dt.timestamp())  # 1594159200.0
print(dt.tzinfo)  # None


dt1 = datetime.datetime(2020, 7, 8, tzinfo=datetime.timezone.utc)
print(dt1.tzinfo)  # UTC+00:00


dt2 = datetime.datetime(2020, 7, 8, tzinfo=datetime.timezone(datetime.timedelta(hours=-2)))
print(dt2)
print(dt2.tzinfo)  # UTC-02:00
print(dt2.astimezone(datetime.timezone.utc))  # 2020-07-08 02:00:00+00:00
print(dt2.astimezone(datetime.timezone(datetime.timedelta(hours=3))))  # 2020-07-08 05:00:00+03:00

utc = dt2.astimezone(datetime.timezone.utc)  # utc.tzinfo = UTC+00:00
utc.replace(tzinfo=None)  # utc.tzinfo = None


def _as_utc_without_tzinfo(timestamp: datetime.datetime) -> datetime.datetime:
    """
    Converts timezone-aware timestamp to UTC and strips the UTC tzinfo
    property.

    This is only useful when you have a timezone aware datetime object and need
    to use it with a database column that does NOT have a timezone.
    """
    utc = timestamp.astimezone(datetime.timezone.utc)
    return utc.replace(tzinfo=None)


dt3 = datetime.datetime(2020, 7, 8, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))  # dt3.tzinfo UTC+02:00
res = _as_utc_without_tzinfo(dt3)  # res.tzinfo None


print(tzlocal.get_localzone())  # Europe/Oslo


utc = pytz.utc
print(utc.zone)  # UTC
oslo = pytz.timezone('Europe/Oslo')
print(oslo)  # Europe/Oslo
print(isinstance(oslo, pytz.tzinfo.BaseTzInfo))  # True