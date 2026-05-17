# 🔍 Subdomain Finder

A fast multi-threaded subdomain enumeration tool written in Python. It uses a wordlist to discover active subdomains of a target domain.

---

## 📋 Features

- Multi-threaded scanning (fast results)
- Uses a custom wordlist (`subdomains.txt`)
- Saves discovered subdomains to `discovered_subdomain.txt`
- Lightweight with minimal dependencies

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/python-hacking-toolkit.git
cd python-hacking-toolkit/subdomain_finder
```

**2. Install dependencies**
```bash
pip install requests
```

**3. Add a wordlist**

You need a `subdomains.txt` file in the same folder. Example:
```
www
mail
ftp
admin
test
dev
api
blog
shop
```

> 💡 You can download a big wordlist from [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt)

---

## 🚀 Usage

```bash
python subdomain_finder.py
```
or
```bash
python3 subdomain_finder.py
```

You will be prompted to enter a domain:
```
Enter domain name: example.com
```

### Example Output

```
[+] discovered Subdomains: http://www.example.com
[+] discovered Subdomains: http://mail.example.com
[+] discovered Subdomains: http://api.example.com
```

Results are also saved in `discovered_subdomain.txt`

---

## 📁 Project Structure

```
subdomain_finder/
│
├── subdomain_finder.py       # Main script
├── subdomains.txt            # Wordlist (add your own)
├── discovered_subdomain.txt  # Output file (auto generated)
└── README.md                 # Documentation
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
