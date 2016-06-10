import datetime

from . import utils


class DateTime(datetime.datetime):
    """ DateTime is a subclass of standard datetime.datetime class
        with some additional methods.

    """
    def epoch(self):
        """ Return the seconds since epoch

        """
        return utils.to_timestamps(self, self.is_naive())

    def is_naive(self):
        """ Return a boolean to indicate the DateTime object is naive
            date time or Not

        """
        return self.tzinfo is None or self.tzinfo.utcoffset(self) is None

    def is_aware(self):
        """ Return a boolean to indicate the DateTime object is aware
            date time or Not

        """
        return (
            self.tzinfo is not None and
            self.tzinfo.utcoffset(self) is not None
        )
