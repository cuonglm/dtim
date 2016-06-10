import datetime

from .context import dtim

from dtim.utils import to_timestamps


def test_utils():
    dt = datetime.datetime.now()
    assert isinstance(to_timestamps(dt, is_naive=True), float)
