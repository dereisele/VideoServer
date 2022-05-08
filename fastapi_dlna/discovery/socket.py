import socket
import struct
import asyncio
import logging

from .protocol_server import MediaServerDiscover
from ..settings import Settings

log = logging.getLogger(__name__)


def build_sock(discovery_multicast_addr: str = "239.255.255.250", discover_port: int = 1900):
    log.info(f"Creating sock {discovery_multicast_addr}:{discover_port}")
    info = socket.getaddrinfo(discovery_multicast_addr, None)[0]
    sock = socket.socket(info[0], socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    group_bin = socket.inet_pton(info[0], info[4][0])
    sock.bind(('', discover_port))

    if info[0] == socket.AF_INET:  # IPv4
        group = group_bin + struct.pack('=I', socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, group)

    return sock


async def register_ssdp(settings: Settings):
    discover_server = MediaServerDiscover(settings)
    loop = asyncio.get_event_loop()

    sock = build_sock(settings.discovery_multicast_addr, settings.discovery_port)
    transport = await loop.create_datagram_endpoint(
        lambda: discover_server,
        sock=sock
    )
    return transport, discover_server
