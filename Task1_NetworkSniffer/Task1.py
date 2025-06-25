from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

# Fichier de sortie
output_file = "sniffer_output.txt"

def log_to_file(text):
    with open(output_file, "a") as f:
        f.write(text + "\n")

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto_num = packet[IP].proto

        proto = {
            6: "TCP",
            17: "UDP"
        }.get(proto_num, str(proto_num))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        header = f"[{timestamp}] {ip_src} -> {ip_dst} | Protocol: {proto}"
        print(header)
        log_to_file(header)

        details = ""
        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            payload = bytes(packet[TCP].payload)
            details = f"    TCP Ports: {sport} → {dport}\n    Payload: {payload}"
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            payload = bytes(packet[UDP].payload)
            details = f"    UDP Ports: {sport} → {dport}\n    Payload: {payload}"

        if details:
            print(details)
            log_to_file(details)

        separator = "-" * 60
        print(separator)
        log_to_file(separator)

def main():
    print("Sniffer démarré... Résultats enregistrés dans sniffer_output.txt")
    try:
        # Modifier le nombre de paquets selon besoin
        sniff(filter="ip", prn=packet_callback, store=0, count=20)
    except KeyboardInterrupt:
        print("\nSniffer arrêté.")

if __name__ == "__main__":
    main()
