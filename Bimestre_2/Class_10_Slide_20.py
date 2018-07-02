import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)

def get_remote_machine_info():
    remote_host = 'www.ita.br'
    print("ITA IP address: %s" % socket.gethostbyname(remote_host))

if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info()