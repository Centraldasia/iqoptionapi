import datetime
from iqoptionapi.ws.objects.timesync import TimeSync


def test_server_datetime_none():
    ts = TimeSync()
    ts.server_timestamp = None
    assert ts.server_datetime is None


def test_expiration_properties_none():
    ts = TimeSync()
    ts.server_timestamp = None
    assert ts.expiration_datetime is None
    assert ts.expiration_timestamp is None
