import nmap

scanner = nmap.PortScanner()

# Solicita la IP de red al usuario
ip = input('Ingrese la dirección IP base (ej. 192.168.1.0/24): ')

# Realiza el escaneo de hosts
print(f'Iniciando escaneo de la red {ip}...')
scanner.scan(hosts=ip, arguments='-sn')  # -sn realiza un ping scan (no escanea puertos)

# Cuenta los hosts que están activos
hosts_activos = scanner.all_hosts()

#Numero  de hot encontrados
print(f'Hosts activos encontrados: {len(hosts_activos)}')

# Muestra los hosts activos
if hosts_activos:
    print('\nLista de dispositivos conectados:')
    for host in hosts_activos:
        print(f'Host: {host} ({scanner[host].hostname()})')
else:
    print('No se encontraron dispositivos conectados en la red.')
