from __future__ import annotations
import json
from json import JSONEncoder

import requests

from final.in_out_state import InOutState
from in_out_state import InOutContext, OutState


def notify_in_out(txt: str):
    url = 'https://hooks.slack.com/services/******'
    requests.post(url, data=json.dumps({"text": txt}))


class Member(InOutContext):
    members: dict[str, Member]

    _idm: str
    _name: str
    _state: InOutState

    @classmethod
    def load_members(cls, workdir: str):
        members = {}

        with open(workdir + 'members.json', 'r') as f:
            j_members = json.load(f)

            for j_member in j_members:
                members[j_member.idm] = cls(j_member.idm, j_member.name)

        cls.members = members

    @classmethod
    def store_members(cls, workdir: str):
        with open(workdir + 'members.json', 'w') as fw:
            json.dump(cls.members, fw, cls=MembersJSONEncoder, indent=2, ensure_ascii=False)

    @classmethod
    def is_exist(cls, idm: str):
        return idm in cls.members

    def __init__(self, idm: str, name: str):
        self._idm = idm
        self._name = name
        self._state = OutState.get_instance()

    def pass_gate(self):
        notify_in_out(self.state.pass_gate(self, self.name))

    def set_state(self, state: InOutState):
        self._state = state

    @property
    def idm(self) -> str:
        return self._idm

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> InOutState:
        return self._state


class MembersJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Member):
            return {'idm': Member.idm, 'name': Member.name, 'state': Member.state}
        else:
            return super(MembersJSONEncoder, self).default(o)
