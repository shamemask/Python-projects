import socket
import configparser

h_name = socket.gethostname()
IP_addres = str(socket.gethostbyname(h_name))
UDP_MAX_SIZE = 65535

def listen(host: str = IP_addres, port: int = 2999 ): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f'Listening at {host}:{port}')
    data_conn = (host,int(port))
    s.bind(data_conn)

    members = []
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)

        if addr not in members:
            members.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        msg_text = msg.decode('ascii')
        print(msg)
        if msg_text == '__join':
            print(f'Client {s} joined chat')
            continue

        message_template = '{}__{}'
        if msg_text == '__members':
            print(f'Client {addr} requested members')
            active_members = [f'client{m[1]}' for m in members if m != addr]
            members_msg = ';'.join(active_members)
            s.sendto(message_template.format('members', members_msg).encode('ascii'), addr)




if __name__ == '__main__':

    
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("server.config")  # читаем конфиг
    port = config["server-config"]["port"]
    print("Server host name is:" + h_name)
    print("Server IP Address is: " + IP_addres+":"+port)
    listen(port = port)