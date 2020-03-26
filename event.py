class Event(object):
    def __init__(self, send_to, message):
        self._send_to = send_to
        self._message = message

    def get_message(self):
        return self._message

    def get_send_to(self):
        return self._send_to

