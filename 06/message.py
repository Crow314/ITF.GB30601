class Message:
    _sender: str
    _recipient: str
    _body: str

    def __init__(self, sender: str, recipient: str, body: str) -> None:
        self._sender = sender
        self._recipient = recipient
        self._body = body

    @property
    def sender(self) -> str:
        return self._sender

    @property
    def recipient(self) -> str:
        return self._recipient

    @property
    def body(self) -> str:
        return self._body
