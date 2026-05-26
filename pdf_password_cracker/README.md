# 🔓 PDF Password Cracker

A fast multi-threaded Python tool to crack password-protected PDF files using wordlists or brute-force generation.

---

## 📋 Features

- Multi-threaded cracking for fast results
- Supports **wordlist attack** (custom password list)
- Supports **brute-force attack** (auto password generation)
- Customizable character set, min/max password length
- Progress bar using `tqdm`
- Adjustable number of parallel threads

---

## 🛠️ Requirements

- Python 3.x
- `pikepdf` library
- `tqdm` library

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Amitkaushik1/python-hacking-toolkit.git
cd python-hacking-toolkit/pdf_password_cracker
```

**2. Install dependencies**
```bash
pip install pikepdf tqdm
```

---

## 🚀 Usage

### Wordlist Attack
```bash
python3 crack_pdf.py file.pdf --wordlist passwords.txt
```

### Brute-Force Attack
```bash
python3 crack_pdf.py file.pdf --generate --min_length 1 --max_length 4
```

### Custom Charset + Threads
```bash
python3 crack_pdf.py file.pdf --generate --min_length 1 --max_length 3 --charset abc123 --max_workers 8
```

---

## ⚙️ Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `pdf_file` | Path to the PDF file | Required |
| `--wordlist` | Path to wordlist file | Optional |
| `--generate` | Enable brute-force generation | Optional |
| `--min_length` | Minimum password length | 1 |
| `--max_length` | Maximum password length | 3 |
| `--charset` | Characters to use for generation | a-z, A-Z, 0-9, symbols |
| `--max_workers` | Number of parallel threads | 4 |

---

### Example Output

```
Decrypting PDF: 100%|████████████| 1000/1000 [00:05<00:00]
[+] Password Found: MyPass123
PDF decrypted successfully with password: MyPass123
```

---

## 📁 Project Structure

```
pdf_password_cracker/
│
├── crack_pdf.py        # Main script
└── README.md           # Documentation
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized use only**.  
Only use it on PDF files you own or have explicit permission to test.  
The author is not responsible for any misuse.

---

## 📄 License

This project is open source and available under the [MIT License](../LICENSE).

---

## 👤 Author

Made with ❤️ on Kali Linux by **Amitkaushik1**  
GitHub: [Amitkaushik1](https://github.com/Amitkaushik1)  
Feel free to fork, star ⭐, and contribute!
