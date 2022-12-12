from __future__ import annotations
import json
from json import JSONEncoder, JSONDecoder


class Member:
    members: dict[str, Member]

    _idm: str
    _name: str
    _state: int

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

    def __init__(self, idm: str, name: str):
        self._idm = idm
        self._name = name
        self._state = 0  # out state

    @property
    def idm(self) -> str:
        return self._idm

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> int:
        return self._state

    @state.setter
    def state(self, state: int):
        if state in {0, 1}:
            self._state = state
        else:
            raise ValueError


class MembersJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Member):
            return {'idm': Member.idm, 'name': Member.name, 'state': Member.state}
        else:
            return super(MembersJSONEncoder, self).default(o)
