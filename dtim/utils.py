import datetime
import sys

EPOCH_DT = datetime.datetime(1970, 1, 1)

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY33 = sys.version_info[0:2] >= (3, 3)


def to_timestamps(dt, is_naive):
    if PY33:
        if is_naive:
            from datetime import timezone
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    elif PY3:
        epoch = EPOCH_DT
        if not is_naive:
            from datetime import timezone
            epoch = epoch.replace(tzinfo=timezone.utc)
        return (dt - epoch) / datetime.timedelta(seconds=1)
    elif PY2:
        if not is_naive:
            dt = dt.replace(tzinfo=None) - dt.utcoffset()
        return (dt - EPOCH_DT).total_seconds()
    else:
        raise NotImplementedError
