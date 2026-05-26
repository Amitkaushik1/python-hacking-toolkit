import pikepdf
from tqdm import tqdm
import itertools
import string
from concurrent.futures import ThreadPoolExecutor
import argparse

def generate_password(chars, min_length, max_length):
    for length in range(min_length, max_length+1):
        for password in itertools.product(chars, repeat=length):
            yield''.join(password)

def load_passwords(wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            yield line.strip()

def try_passwords(pdf_file, password):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print('[+] Password Found:', password)
            return password
    except pikepdf._core.PasswordError:
        return None
    
def decrypt_pdf(pdf_file, passwords, total_passwords, max_workers):
    with tqdm(total_passwords, desc="Decrypting PDF", unit='password') as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            furure_to_password = {executor.submit(try_passwords, pdf_file, pwd): pwd for pwd in passwords}

            for future in tqdm(furure_to_password, total=total_passwords):
                password = furure_to_password[future]
                if future.result():
                    return future.result()
                pbar.update(1)
    print("Unable to decrypt PDF. Password not found in the wordlist.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt a password-protected PDF file.")
    parser.add_argument('pdf_file', help='Path to the password-protected PDF file.')
    parser.add_argument('--wordlist', help='Path to the password list file.')
    parser.add_argument('--generate', action='store_true', help='Generate passwords on the fly')
    parser.add_argument('--min_length', type=int, help='Minimum length of passwords to generate', default=1)
    parser.add_argument('--max_length', type=int, help='Maximum length of password to generate', default=3)
    parser.add_argument('--charset', type=str, help='Characters to use for password generation', default=string.ascii_letters + string.digits + string.punctuation)
    parser.add_argument('--max_workers', type=int, help='Maximum number of parallel threads', default=4)

    args = parser.parse_args()

    if args.generate:
        passwords = generate_password(args.charset, args.min_length, args.max_length)
        total_passwords = sum(1 for _ in generate_password(args.charset, args.min_length, args.max_length))
    elif args.wordlist:
        passwords = load_passwords(args.wordlist)
        total_passwords = sum(1 for _ in load_passwords(args.wordlist))
    else:
        print('Either --wordlist must be providedd or --generate must be specified')
        exit(1)
    decrypted_password = decrypt_pdf(args.pdf_file, passwords, total_passwords, args.max_workers)
    if decrypted_password:
        print('PDF decrypted successfully with password:', decrypted_password)
    else:
        print('Unable to decrypt PDF. Password not found')
    
