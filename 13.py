from ipaddress import ip_network
k=0
for i in range(17,32):
    n = ip_network(f'115.53.128.88/{i}',0)
    if n.num_addresses > 1000:
        print(n.network_address,i)
        k+=1
print(k)
