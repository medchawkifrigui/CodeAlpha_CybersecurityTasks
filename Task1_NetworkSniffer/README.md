# Task 1: Basic Network Sniffer

This task is part of my internship at **CodeAlpha**, focused on building a basic network packet sniffer using Python.

## 🎯 Objective

- Capture real-time network traffic.
- Analyze packet structure and contents.
- Understand how data flows through the network and learn basic protocols.
- Display relevant info like source/destination IPs, protocol, ports, and payloads.
- Log captured data for later analysis.

## 🛠 Tools & Libraries

- **Python 3**
- **Scapy**: For packet sniffing and analysis.
- **datetime**: For timestamp logging.

## 📁 Files

- `sniffer.py`: Main script that captures and logs network traffic.
- `sniffer_output.txt`: Automatically generated output file containing packet details (with timestamp).
- *(Optional)* `capture_example.txt`: Example capture output (can be renamed or removed).

## ⚙️ How It Works

1. Listens for IP packets using `scapy.sniff()`.
2. Filters packets containing IP/TCP/UDP layers.
3. Extracts:
   - Source & Destination IPs
   - Protocol (TCP/UDP)
   - Ports and payload (when applicable)
4. Displays the packet summary in the terminal.
5. Saves each result into `sniffer_output.txt` with timestamps.

## ▶️ How to Run

> ⚠️ Requires root privileges to sniff packets.

```bash
sudo python3 sniffer.py
