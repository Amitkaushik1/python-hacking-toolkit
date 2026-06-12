# 🌐 Network Scanner

A fast multi-threaded network scanner built in Python using Scapy. It discovers all active devices on a network using ARP requests and displays their IP address, MAC address, and hostname.

---

## 📋 Features

- ARP-based network scanning
- Multi-threaded for fast results
- Displays IP, MAC address, and Hostname of all active devices
- Supports full CIDR notation (e.g. `192.168.1.0/24`)
- Lightweight with minimal dependencies

---

## 🛠️ Requirements

- Python 3.x
- `scapy` library
- Root/sudo privileges (required for ARP scanning)

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Amitkaushik1/python-hacking-toolkit.git
cd python-hacking-toolkit/Network_Scanner
```

**2. Install dependencies**
```bash
pip install scapy
```

---

## 🚀 Usage

```bash
sudo python3 network_scanner.py
```

You will be prompted to enter a network range:
```
Enter network ip address: 192.168.1.0/24
```

### Example Output

```
IP                    MAC                         Hostname
--------------------------------------------------------------------------------
192.168.1.1           aa:bb:cc:dd:ee:ff           router.local
192.168.1.5           11:22:33:44:55:66           desktop.local
192.168.1.10          77:88:99:aa:bb:cc           Unknown
```

---

## 📁 Project Structure

```
Network_Scanner/
│
├── network_scanner.py      # Main script
└── README.md               # Documentation
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized testing only**.  
Only use it on networks you own or have explicit permission to scan.  
The author is not responsible for any misuse.

---

## 📄 License

This project is open source and available under the [MIT License](../LICENSE).

---

## 👤 Author

Made with ❤️ on Kali Linux by **Amitkaushik1**  
GitHub: [Amitkaushik1](https://github.com/Amitkaushik1)  
Feel free to fork, star ⭐, and contribute!
