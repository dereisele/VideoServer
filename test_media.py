import asyncio
import socket
import struct

import xmltodict
from fastapi import FastAPI
from fastapi import responses

import base_xml
from discover import MediaServerDiscover

app = FastAPI()


def build_sock():
    info = socket.getaddrinfo(MediaServerDiscover.MULTICAST_ADDRESS, None)[0]
    sock = socket.socket(info[0], socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    group_bin = socket.inet_pton(info[0], info[4][0])
    sock.bind(('', 1900))

    if info[0] == socket.AF_INET:  # IPv4
        group = group_bin + struct.pack('=I', socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, group)

    return sock


async def register_ssdp():
    discover_server = MediaServerDiscover()
    loop = asyncio.get_event_loop()

    sock = build_sock()
    transport = await loop.create_datagram_endpoint(
        lambda: discover_server,
        sock=sock
    )
    return transport, discover_server


class XMLResponse(responses.Response):
    media_type = "text/xml"

    def render(self, content: dict) -> bytes:
        return xmltodict.unparse(content, pretty=True).encode("utf-8")


@app.get("/server.xml", response_class=XMLResponse)
def get_server():
    return base_xml.server


@app.get("/contentdirectory/contentdirectory.xml", response_class=XMLResponse)
def get_content_directory():
    return base_xml.contentdirectory


@app.get("/contentdirectory/control", response_class=XMLResponse)
def get_content_directory(ObjectId: int):
    print(ObjectId)
    return base_xml.contentdirectory


@app.post("/contentdirectory/control", response_class=XMLResponse)
def post_content_directory(control: str):
    print(control)
    return base_xml.contentdirectory


@app.on_event("startup")
async def on_startup() -> None:
    transport, discover_server = await register_ssdp()

    app.state.discover_server = discover_server


@app.on_event("shutdown")
async def on_shutdown() -> None:
    app.state.udp_transport.close()


def main():
    # Start the asyncio loop.
    loop = asyncio.get_event_loop()

    connect = register_ssdp()

    transport, protocol = loop.run_until_complete(connect)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    loop.close()


if __name__ == "__main__":
    pass
