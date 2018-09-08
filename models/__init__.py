"""
Models representing the “database” of the IRC server, plus some abstractions.

`Actor`: stores and manages the connections of users and other servers
`ActorCollection`: used to broadcast messages to a collection of `Actor`s
`Channel`: an IRC channel. D'uh.
`Server`: another IRC server on the network.
`User`: all the data associated with a user connected to the IRC network.
"""
from typing import Union


from .error import Error
from .actor import Actor
from .actorcollection import ActorCollection
from .channel import Channel
from .server import Server
from .user import User


Target = Union[Actor, ActorCollection, Server]
