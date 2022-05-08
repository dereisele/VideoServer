import logging

import xmltodict
from fastapi import APIRouter
from fastapi import responses

from fastapi_dlna.discovery import base_xml

router = APIRouter()
log = logging.getLogger(__name__)


class XMLResponse(responses.Response):
    media_type = "text/xml"

    def render(self, content: dict) -> bytes:
        return xmltodict.unparse(content, pretty=True).encode("utf-8")


@router.get("/server.xml", response_class=XMLResponse)
def get_server():
    return base_xml.server


@router.get("/contentdirectory/contentdirectory.xml", response_class=XMLResponse)
def get_content_directory():
    return base_xml.contentdirectory


@router.get("/contentdirectory/control", response_class=XMLResponse)
def get_content_directory(ObjectId: int):
    log.debug(ObjectId)
    return base_xml.contentdirectory


@router.post("/contentdirectory/control", response_class=XMLResponse)
def post_content_directory(control: str):
    log.debug(control)
    return base_xml.contentdirectory
