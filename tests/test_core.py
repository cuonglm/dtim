import datetime

import pytz

from .context import dtim


def test_dtim():
    dt = dtim.DateTime.now()
    assert isinstance(dt, datetime.datetime)


def test_epoch():
    dt = dtim.DateTime.now()
    assert isinstance(dt.epoch(), float)


def test_is_naive():
    d = dtim.DateTime(1970, 1, 1)

    assert d.is_naive()


def test_is_aware():
    d = dtim.DateTime(1970, 1, 1, tzinfo=pytz.utc)

    assert d.is_aware()
