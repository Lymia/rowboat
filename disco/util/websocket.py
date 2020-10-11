from __future__ import absolute_import

import websocket
import six

from holster.emitter import Emitter

from disco.util.logging import LoggingClass


class Websocket(LoggingClass, websocket.WebSocketApp):
    """
    A utility class which wraps the functionality of :class:`websocket.WebSocketApp`
    changing its behavior to better conform with standard style across disco.

    The major difference comes with the move from callback functions, to all
    events being piped into a single emitter.
    """
    def __init__(self, *args, **kwargs):
        LoggingClass.__init__(self)
        websocket.WebSocketApp.__init__(self, *args, **kwargs)

        self.emitter = Emitter()

        # Hack to get events to emit
        for var in six.iterkeys(self.__dict__):
            if not var.startswith('on_'):
                continue

            setattr(self, var, var)
            
        self.on_close = self._callback_on_close

    def _get_close_args(self, data):
        if data and len(data) >= 2:
            code = 256 * six.byte2int(data[0:1]) + six.byte2int(data[1:2])
            reason = data[2:].decode('utf-8')
            return [code, reason]
        return [None, None]

    def on_close(self, a, b, c):
        self._callback("on_close", a, b, c)
    def _callback(self, callback, *args):
        if not callback:
            return

        self.emitter.emit(callback, *args)
