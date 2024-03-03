import ctypes
from ctypes import wintypes


class WLAN_AVAILABLE_NETWORK(ctypes.Structure):
    _fields_ = [
        ("strProfileName", wintypes.WCHAR * 256),
        ("dot11Ssid", ctypes.c_ubyte * 32),
        ("dot11BssType", wintypes.DWORD),
        ("uNumberOfBssids", wintypes.DWORD),
        ("bNetworkConnectable", wintypes.BOOL),
        ("wlanNotConnectableReason", wintypes.DWORD),
        ("uNumberOfPhyTypes", wintypes.DWORD * 8),
        ("bMorePhyTypes", wintypes.BOOL),
        ("dot11PhyTypes", wintypes.DWORD * 8),
        ("bFullyAutomatic", wintypes.BOOL),
        ("bProfileConnectable", wintypes.BOOL),
        ("wlanConnectionMode", wintypes.DWORD),
        ("dwNumberOfBssids", wintypes.DWORD),
        ("bNetworkConnectable", wintypes.BOOL),
        ("wlanNotConnectableReason", wintypes.DWORD),
        ("uNumberOfPhyTypes", wintypes.DWORD * 8),
        ("bMorePhyTypes", wintypes.BOOL),
        ("dot11PhyTypes", wintypes.DWORD * 8),
        ("bFullyAutomatic", wintypes.BOOL),
        ("bProfileConnectable", wintypes.BOOL),
        ("wlanConnectionMode", wintypes.DWORD),
        ("dwNumberOfBssids", wintypes.DWORD),
        ("dot11BssPhyType", wintypes.DWORD),
    ]


class WLAN_INTERFACE_INFO_LIST(ctypes.Structure):
    _fields_ = [
        ("dwIndex", wintypes.DWORD),
        ("strInterfaceDescription", wintypes.WCHAR * 256),
        ("isState", wintypes.DWORD),
    ]


class WLAN_INTERFACE_INFO(ctypes.Structure):
    _fields_ = [
        ("InterfaceGuid", ctypes.c_byte * 16),
        ("strInterfaceDescription", wintypes.WCHAR * 256),
        ("isState", wintypes.DWORD),
    ]


wlanapi = ctypes.windll.wlanapi


def get_interface_info_list():
    interface_list = WLAN_INTERFACE_INFO_LIST()
    if wlanapi.WlanEnumInterfaces(None, None, ctypes.byref(interface_list)) != 0:
        raise Exception("Error in WlanEnumInterfaces")

    interface_info_list = (WLAN_INTERFACE_INFO * interface_list.dwNumberOfItems)()
    ctypes.memmove(ctypes.byref(interface_info_list), interface_list.InterfaceInfo, ctypes.sizeof(interface_info_list))

    return interface_info_list


def scan_wifi_networks():
    interface_info_list = get_interface_info_list()

    print("Dostępne sieci WiFi:")

    for interface_info in interface_info_list:
        interface_handle = wintypes.HANDLE()
        if wlanapi.WlanOpenHandle(1, None, ctypes.byref(interface_info.dwIndex), ctypes.byref(interface_handle)) != 0:
            raise Exception("Error in WlanOpenHandle")

        available_network_list = ctypes.POINTER(WLAN_AVAILABLE_NETWORK)()
        if wlanapi.WlanGetAvailableNetworkList(interface_handle, ctypes.byref(interface_info.InterfaceGuid),
                                               0, None, ctypes.byref(available_network_list)) != 0:
            raise Exception("Error in WlanGetAvailableNetworkList")

        for i in range(available_network_list.contents.dwNumberOfItems):
            network = available_network_list.contents.Network[i]
            ssid = bytes(network.dot11Ssid[:network.dot11SsidLength]).decode("utf-8")
            bssid = ":".join(f"{byte:02X}" for byte in network.dot11Bssid)
            signal_strength = network.wlanSignalQuality
            print(f"SSID: {ssid}, BSSID: {bssid}, Siła sygnału: {signal_strength}%")


if __name__ == "__main__":
    scan_wifi_networks()
