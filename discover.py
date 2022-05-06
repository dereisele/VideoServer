from asyncio import transports
from enum import Enum
import platform

import ssdp

__version_info__ = (0, 0, 1)
__version__ = '.'.join(map(str, __version_info__))
__service_name__ = 'Test'


class Header(str, Enum):
    NT = 'nt'  # Notification Type
    NTS = 'nts'  # Notification Sub Type
    ST = 'st'  # Search Target
    USN = 'usn'  # Unique Service Name
    MX = 'mx'  # Maximum wait time
    EXT = 'ext'  # Extension acknowledge flag
    SERVER = 'server'
    CACHE_CONTROL = 'cache-control'
    LOCATION = 'location'  # Device description xml url


class Messages(str, Enum):
    ALIVE = 'ssdp:alive'
    BYE = 'ssdp:byebye'
    ALL = 'ssdp:all'


class MediaServerDiscover(ssdp.SimpleServiceDiscoveryProtocol):
    USN_MS = "uuid:2fac1234-31f8-11b4-a222-08002b34c003::urn:schemas-upnp-org:device:MediaServer:1"
    SERVER_ID = f'{platform.system()},{platform.release()},UPnP/1.0,{__service_name__},{__version__}'

    def __init__(self):
        self.transport = None

    def connection_made(self, transport: transports.DatagramTransport) -> None:
        self.transport = transport

    def response_received(self, response, addr):
        """Handle an incoming response."""
        print(
            "received response: {} {} {}".format(
                response.status_code, response.reason, response.version
            )
        )

        for header in response.headers:
            print("header: {}".format(header))

        print()

    def request_received(self, request, addr):
        """Handle an incoming request and respond to it."""
        # print(
        #     "received request: {} {} {}".format(
        #         request.method, request.uri, request.version
        #     )
        # )

        # for header in request.headers:
            #print("header: {}".format(header))

        # print()

        # Build response and send it.
        #print("Sending a response back to {}:{}".format(*addr))
        ssdp_response = ssdp.SSDPResponse(
            200,
            "OK",
            headers={
                "Cache-Control": "max-age=30",
                "Location": "http://192.168.100.185:8080/server.xml",
                "Server": "Python UPnP/1.0 SSDP",
                "ST": "urn:schemas-upnp-org:device:MediaServer:1",
                "USN": self.USN_MS,
                "EXT": "",
            },
        )
        self.transport.sendto(bytes(ssdp_response) + b"\r\n" + b"\r\n", addr)

    def send_notify(self, transport):
        alive = ssdp.SSDPRequest("NOTIFY", headers={
            "Cache-Control": "max-age=30",
            "Location": "http://192.168.100.185:8080/server.xml",
            "Server": "Python UPnP/1.0 SSDP",
            "NTS": "ssdp:alive",
            "NT": "urn:schemas-upnp-org:device:MediaServer:1",
            "USN": self.USN_MS
        })
        transport.sendto(bytes(alive) + b"\r\n" + b"\r\n", (MediaServerDiscover.MULTICAST_ADDRESS, 1900))

    def register_devices(self, ssdp_server):
        ssdp_server.register_local(self._unique_device_name, 'upnp:rootdevice')
        ssdp_server.register_local(self._unique_device_name, self._device_type, f'{self._urlbase}/desc.xml')
        ssdp_server.register_local(self._unique_device_name, self._service_type)

    def register_local(self, unique_device_name, search_target, location=''):
        usn = f'{unique_device_name}::{search_target}'

        # TODO: from https://dangfan.me/en/posts/upnp-intro
        # Cache-control: The integer following max-age= specifies the number of seconds the advertisement is valid,
        # which indicates that the device need to resend this notification before expiration....TODO so need to resend?!
        device = {Header.USN: usn,
                  Header.ST: search_target,
                  Header.EXT: '',  # Required by spec...confirms message was understood
                  Header.CACHE_CONTROL: 'max-age=1800',  # 1800 = 30 minutes
                  Header.SERVER: self.SERVER_ID}
        if location:
            device[Header.LOCATION] = location

        self._devices_local[usn] = device
        self._send_alive(usn)
