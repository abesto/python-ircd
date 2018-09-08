from typing import List

from commands.base import Command
from include.message import Message as M, Message
from models.actorcollection import ActorCollection


class QuitCommand(Command):
    required_parameter_count = 0
    command = "QUIT"
    user_registration_command = True

    def from_user(self, message="leaving", *_):
        ret = []
        for channel in self.user.channels:
            channel.part(self.user)
            ret.append(
                M(
                    ActorCollection(channel.users),
                    "PART",
                    str(channel),
                    message,
                    prefix=str(self.user),
                )
            )
        self.user.delete()
        self.actor.disconnect()
        return ret + [M(self.actor, "ERROR")]

    def from_server(self, *args) -> List[Message]:
        raise Exception("IRC: Server Protocol (RFC2813) is not (yet?) implemented")
