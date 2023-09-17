import requests
import sys

def enumerate_subdomains(domain):
  """Enumerates subdomains of a given domain.

  Args:
    domain: The domain to enumerate subdomains for.

  Returns:
    A list of subdomains.
  """

  subdomains = []
  with open("subdomains.txt", "r") as f:
    for line in f:
      subdomain = line.strip()
      subdomain_url = f"http://{subdomain}.{domain}"

      print(f"Attempting to connect to {subdomain_url}....")
      try:
        requests.get(subdomain_url)
        subdomains.append(subdomain_url)
        print("...success.")
        #Write the successful connection a text file
        with open("success.domain.txt", "a") as out_f:
          out_f.write(f"{subdomain_url}\n")
      except requests.ConnectionError:
          print("...failed.")

  return subdomains

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python subdomain_enum.py <domain>")
    sys.exit(1)

  domain = sys.argv[1]
  subdomains = enumerate_subdomains(domain)

  if subdomains:
    print("Valid domains:")
    for subdomain in subdomains:
      print(subdomain)
  else:
    print("No valid domains found.")
