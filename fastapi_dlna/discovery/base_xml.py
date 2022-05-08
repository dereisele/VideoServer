BASE_URL = "http://192.168.100.185:8080/"
#BASE_URL = "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/"

server = {
    "root": {
        "@xmlns": "urn:schemas-upnp-org:device-1-0",
        "@xmlns:dlna": "urn:schemas-dlna-org:device-1-0",
        "specVersion": {
            "major": 1,
            "minor": 0
        },
        "device": {
            "dlna:X_DLNACAP": None,
            "dlna:X_DLNADOC": [
                {
                    "@xmlns:dlna": "urn:schemas-dlna-org:device-1-0",
                    "#text": "DMS-1.50"
                },
                {
                    "@xmlns:dlna": "urn:schemas-dlna-org:device-1-0",
                    "#text": "M-DMS-1.50"
                }
            ],
            "deviceType": "urn:schemas-upnp-org:device:MediaServer:1",
            "friendlyName": "Test",
            "manufacturer": "Test",
            "manufacturerURL": "https://github.com/jellyfin/jellyfin",
            "modelDescription": "UPnP/AV 1.0 Compliant Media Server",
            "modelName": "Test",
            "modelNumber": "01",
            "modelURL": "https://github.com/jellyfin/jellyfin",
            "serialNumber": "2fac123431f811b4a22208002b34c003",
            "UPC": "",
            "UDN": "uuid:2fac123431f811b4a22208002b34c003",
            "iconList": {
                "icon": [
                    {
                        "mimetype": "image/png",
                        "width": "240",
                        "height": "240",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo240.png"
                    },
                    {
                        "mimetype": "image/jpeg",
                        "width": "240",
                        "height": "240",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo240.jpg"
                    },
                    {
                        "mimetype": "image/png",
                        "width": "120",
                        "height": "120",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo120.png"
                    },
                    {
                        "mimetype": "image/jpeg",
                        "width": "120",
                        "height": "120",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo120.jpg"
                    },
                    {
                        "mimetype": "image/png",
                        "width": "48",
                        "height": "48",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo48.png"
                    },
                    {
                        "mimetype": "image/jpeg",
                        "width": "48",
                        "height": "48",
                        "depth": "24",
                        "url": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/icons/logo48.jpg"
                    }
                ]
            },
            "presentationURL": "http://192.168.100.10:8096/web/index.html",
            "serviceList": {
                "service": [
                    {
                        "serviceType": "urn:schemas-upnp-org:service:ContentDirectory:1",
                        "serviceId": "urn:upnp-org:serviceId:ContentDirectory",
                        "SCPDURL": f"{BASE_URL}contentdirectory/contentdirectory.xml",
                        "controlURL": f"{BASE_URL}contentdirectory/control",
                        "eventSubURL": f"{BASE_URL}contentdirectory/events"
                    },
                    {
                        "serviceType": "urn:schemas-upnp-org:service:ConnectionManager:1",
                        "serviceId": "urn:upnp-org:serviceId:ConnectionManager",
                        "SCPDURL": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/connectionmanager/connectionmanager.xml",
                        "controlURL": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/connectionmanager/control",
                        "eventSubURL": "http://192.168.100.10:8096/dlna/9a5f415c23524fb7b8757843cbd2e6de/connectionmanager/events"
                    }
                ]
            }
        }
    }
}

contentdirectory = {
        "scpd": {
            "@xmlns": "urn:schemas-upnp-org:service-1-0",
            "specVersion": {
                "major": "1",
                "minor": "0"
            },
            "actionList": {
                "action": [
                    {
                        "name": "GetSearchCapabilities",
                        "argumentList": {
                            "argument": {
                                "name": "SearchCaps",
                                "direction": "out",
                                "relatedStateVariable": "SearchCapabilities"
                            }
                        }
                    },
                    {
                        "name": "GetSortCapabilities",
                        "argumentList": {
                            "argument": {
                                "name": "SortCaps",
                                "direction": "out",
                                "relatedStateVariable": "SortCapabilities"
                            }
                        }
                    },
                    {
                        "name": "GetSystemUpdateID",
                        "argumentList": {
                            "argument": {
                                "name": "Id",
                                "direction": "out",
                                "relatedStateVariable": "SystemUpdateID"
                            }
                        }
                    },
                    {
                        "name": "Browse",
                        "argumentList": {
                            "argument": [
                                {
                                    "name": "ObjectID",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_ObjectID"
                                },
                                {
                                    "name": "BrowseFlag",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_BrowseFlag"
                                },
                                {
                                    "name": "Filter",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Filter"
                                },
                                {
                                    "name": "StartingIndex",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Index"
                                },
                                {
                                    "name": "RequestedCount",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "SortCriteria",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_SortCriteria"
                                },
                                {
                                    "name": "Result",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Result"
                                },
                                {
                                    "name": "NumberReturned",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "TotalMatches",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "UpdateID",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_UpdateID"
                                }
                            ]
                        }
                    },
                    {
                        "name": "Search",
                        "argumentList": {
                            "argument": [
                                {
                                    "name": "ContainerID",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_ObjectID"
                                },
                                {
                                    "name": "SearchCriteria",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_SearchCriteria"
                                },
                                {
                                    "name": "Filter",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Filter"
                                },
                                {
                                    "name": "StartingIndex",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Index"
                                },
                                {
                                    "name": "RequestedCount",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "SortCriteria",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_SortCriteria"
                                },
                                {
                                    "name": "Result",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Result"
                                },
                                {
                                    "name": "NumberReturned",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "TotalMatches",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "UpdateID",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_UpdateID"
                                }
                            ]
                        }
                    },
                    {
                        "name": "X_GetFeatureList",
                        "argumentList": {
                            "argument": {
                                "name": "FeatureList",
                                "direction": "out",
                                "relatedStateVariable": "A_ARG_TYPE_Featurelist"
                            }
                        }
                    },
                    {
                        "name": "X_SetBookmark",
                        "argumentList": {
                            "argument": [
                                {
                                    "name": "CategoryType",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_CategoryType"
                                },
                                {
                                    "name": "RID",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_RID"
                                },
                                {
                                    "name": "ObjectID",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_ObjectID"
                                },
                                {
                                    "name": "PosSecond",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_PosSec"
                                }
                            ]
                        }
                    },
                    {
                        "name": "X_BrowseByLetter",
                        "argumentList": {
                            "argument": [
                                {
                                    "name": "ObjectID",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_ObjectID"
                                },
                                {
                                    "name": "BrowseFlag",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_BrowseFlag"
                                },
                                {
                                    "name": "Filter",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Filter"
                                },
                                {
                                    "name": "StartingLetter",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_BrowseLetter"
                                },
                                {
                                    "name": "RequestedCount",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "SortCriteria",
                                    "direction": "in",
                                    "relatedStateVariable": "A_ARG_TYPE_SortCriteria"
                                },
                                {
                                    "name": "Result",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Result"
                                },
                                {
                                    "name": "NumberReturned",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "TotalMatches",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Count"
                                },
                                {
                                    "name": "UpdateID",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_UpdateID"
                                },
                                {
                                    "name": "StartingIndex",
                                    "direction": "out",
                                    "relatedStateVariable": "A_ARG_TYPE_Index"
                                }
                            ]
                        }
                    }
                ]
            },
            "serviceStateTable": {
                "stateVariable": [
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_Filter",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_SortCriteria",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_Index",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_Count",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_UpdateID",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "SearchCapabilities",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "SortCapabilities",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "yes",
                        "name": "SystemUpdateID",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_SearchCriteria",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_Result",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_ObjectID",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_BrowseFlag",
                        "dataType": "string",
                        "allowedValueList": {
                            "allowedValue": [
                                "BrowseMetadata",
                                "BrowseDirectChildren"
                            ]
                        }
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_BrowseLetter",
                        "dataType": "string"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_CategoryType",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_RID",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_PosSec",
                        "dataType": "ui4"
                    },
                    {
                        "@sendEvents": "no",
                        "name": "A_ARG_TYPE_Featurelist",
                        "dataType": "string"
                    }
                ]
            }
        }
    }
