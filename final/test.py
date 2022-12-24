import unittest
from unittest import mock
from unittest.mock import patch

from in_out_state import InState, OutState
from member import Member


class MemberTest(unittest.TestCase):
    def setUp(self):
        self.idm = '0123456789012345'
        self.name = 'test_name'
        self.member = Member(self.idm, self.name)

    @patch('member.notify_in_out')
    def test_pass_gate_enter(self, mock_obj: mock.Mock):
        self.member._state = OutState()
        self.member.pass_gate()

        mock_obj.assert_called_once_with(self.name + 'が入室しました')
        self.assertIsInstance(self.member.state, InState)

    @patch('member.notify_in_out')
    def test_pass_gate_exit(self, mock_obj: mock.Mock):
        self.member._state = InState()
        self.member.pass_gate()

        mock_obj.assert_called_once_with(self.name + 'が退出しました')
        self.assertIsInstance(self.member.state, OutState)
