import nmap

# Inicializa el escáner
scanner = nmap.PortScanner()

# Define el host a escanear y las opciones
target_host = "http://localhost:8080/"  # Cambia a tu objetivo
scan_options = "--script vuln"  # Escaneo con scripts de vulnerabilidades

print(f"Escaneando {target_host} con opciones: {scan_options}")
scanner.scan(hosts=target_host, arguments=scan_options)

# Iterar sobre los resultados y mostrar posibles vulnerabilidades
for host in scanner.all_hosts():
    print(f"Resultados para: {host}")
    if 'tcp' in scanner[host]:
        for port, info in scanner[host]['tcp'].items():
            print(f"  Puerto {port}: {info['state']}")
            if 'script' in info:
                print(f"    Scripts ejecutados: {info['script']}")
