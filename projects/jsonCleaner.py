import socket

socketLayer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketLayer.connect(('mbvans.com', 443))
cmd = 'GET https://www.mbvans.com/en/special-offers/jcr:content.filter-offer-json.html\r\n\r\n'.encode()
socketLayer.send(cmd)

while True:
    data = socketLayer.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
socketLayer.close()