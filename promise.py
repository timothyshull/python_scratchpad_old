class TypeError(Exception):
    pass


from constants import *


class RangeError():
    pass


class Promise():
    @classmethod
    def RangeError(self):
        return RangeError()


# above here are temp defs
def make_self_resolution_error():
    return TypeError(CIRCULAR_RESOLUTION_ERROR)


def reflect_handler():
    return Promise.PromiseInspection(self._target())


def api_rejection(msg):
    return Promise.reject(TypeError(msg))


UNDEFINED_BINDING = {}

import

assert
import util

get_domain = None

# TODO: should not be necessary
if util.is_node:
    def get_domain():
        ret = process.domain
        if not ret:
            ret = None
        return ret
else:
    def get_domain():
        return None

test = Promise.RangeError()