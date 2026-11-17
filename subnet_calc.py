import sys
import ipaddress

def calculate_subnet(cidr_str):
    try:
        network = ipaddress.ip_network(cidr_str, strict=False)
        print("="*50)
        print(f"📊 Subnet Analysis for: {cidr_str}")
        print("="*50)
        print(f"Network ID:         {network.network_address}")
        print(f"Broadcast ID:       {network.broadcast_address}")
        print(f"Subnet Mask:        {network.netmask}")
        print(f"Wildcard Mask:      {network.hostmask}")
        print(f"CIDR Prefix:        /{network.prefixlen}")
        hosts = list(network.hosts())
        if hosts:
            print(f"Usable Host Range:  {hosts[0]} - {hosts[-1]}")
            print(f"Total Usable Hosts: {len(hosts)}")
        else:
            print("Total Usable Hosts: 0 (Point-to-point /31 or /32 host)")
        print("="*50)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.100/26"
    calculate_subnet(target)
