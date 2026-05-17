import dns.resolver

target_domain = input('Enter Domain Name: ')
records_type = ['A', 'AAAA', 'MX', 'TXT', 'SOA']

resolver = dns.resolver.Resolver()

for record_type in records_type:
    try:
       answer = resolver.resolve(target_domain, record_type)
       print(f'{record_type} record for {target_domain}')
       for data in answer:
         print(data)

    except dns.resolver.NXDOMAIN:
        print(f'Error: {target_domain} domain does not exist.')
        break

    except dns.resolver.NoAnswer:
        continue
    except dns.resolver.Timeout:
        print(f'Error: Dns query time out for: {target_domain}')
        break
    except dns.resolver.NoNameservers:
        print(f'Error: no nameserver found for: {target_domain}')
        break
