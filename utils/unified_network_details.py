import socket
import uuid

def get_server_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "unknown"

def get_server_hostname():
    try:
        return socket.gethostname()
    except:
        return "unknown"

def get_server_mac():
    try:
        mac = uuid.getnode()
        mac_address = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -8, -8))
        return mac_address
    except:
        return "unknown"

def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')
    except:
        return "unknown"

def get_client_hostname(client_ip):
    try:
        return socket.gethostbyaddr(client_ip)[0]
    except:
        return "unknown"

# Client MAC cannot be retrieved in most web-based APIs due to security.
def get_network_details(request=None):
    client_ip = get_client_ip(request) if request else None
    client_hostname = get_client_hostname(client_ip) if client_ip and client_ip != "unknown" else None

    return {
        "server_ip": get_server_ip(),
        "server_hostname": get_server_hostname(),
        "server_mac": get_server_mac(),
        "client_ip": client_ip,
        "client_hostname": client_hostname,
        "client_mac": "unavailable"  # Only possible in local/LAN environments with custom clients
    }
