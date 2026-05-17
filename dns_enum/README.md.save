# 🔍 DNS Enumerator

A simple and effective DNS enumeration tool written in Python. It queries multiple DNS record types for a given domain and displays the results in a clean format.

---

## 📋 Features

- Queries the following DNS record types:
  - **A** — IPv4 address
  - **AAAA** — IPv6 address
  - **MX** — Mail exchange servers
  - **TXT** — Text records (SPF, DKIM, etc.)
  - **SOA** — Start of Authority
- Handles common DNS errors gracefully (NXDOMAIN, Timeout, NoAnswer, NoNameservers)
- Lightweight with minimal dependencies

---

## 🛠️ Requirements

- Python 3.x
- `dnspython` library

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Amitkaushik1/python-hacking-toolkit.git
cd dns-enumerator
```

**2. Install dependencies**
```bash
pip install dnspython
```

---

## 🚀 Usage

```bash
python dns_enum.py
```
or
```bash
python3 dns_enum.py
```

You will be prompted to enter a domain name:
```
Enter Domain Name: example.com
```

### Example Output

```
A record for example.com
93.184.216.34

MX record for example.com
10 mail.example.com.

TXT record for example.com
"v=spf1 -all"

SOA record for example.com
ns1.example.com. admin.example.com. 2024010101 3600 900 604800 300
```

---

## 📁 Project Structure

```
dns-enumerator/
│
├── dns_enum.py      # Main script
└── README.md        # Project documentation
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized testing only**.  
Do not use it on domains you do not own or have explicit permission to test.  
The author is not responsible for any misuse.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Made with ❤️ on Kali Linux  
Feel free to fork, star ⭐, and contribute!
