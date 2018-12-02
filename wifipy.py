import pywifi
import time

const = pywifi.const

profile = pywifi.Profile()
profile.ssid = 'freebox_hilkens'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = ''

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

name = iface.name()

iface.scan()

time.sleep(5)

iface.scan_results()

iface.network_profiles()


pywifi.profile.Profile

print(name)