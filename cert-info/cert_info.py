import ssl, socket
from datetime import datetime

def get_cert(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
    return cert, cipher

def parse_and_print(cert, cipher):
    print("=== Certificate Details ===")
    print("Subject:", cert.get('subject'))
    print("Issuer:", cert.get('issuer'))
    print("Expiry:", cert.get('notAfter'))
    print("SANs:", cert.get('subjectAltName'))
    print("Cipher:", cipher)

    # Extra: days until expiry
    exp = cert.get('notAfter')
    if exp:
        exp_dt = datetime.strptime(exp, "%b %d %H:%M:%S %Y %Z")
        days = (exp_dt - datetime.utcnow()).days
        print("Days until expiry:", days)

if __name__ == "__main__":
    host = input("Enter hostname (e.g. google.com): ").strip()
    cert, cipher = get_cert(host)
    parse_and_print(cert, cipher)
