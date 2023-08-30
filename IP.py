from ipaddress import IPv4Address
import re
import inflect
p = inflect.engine()
ip = []
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check(Ip):

    if(re.search(regex, Ip)):
        print("Valid Ip address")
        return True
    else:
        print("Invalid Ip address")
        return False
for i in range(10):   #task1
    ipadd = input(f"Enter IP address {i+1} : ")
    is_ip=check(ipadd)   #task2
    while (is_ip==False):
        ipadd = input(f"Pls enter {i+1} IP again : ")
        is_ip=check(ipadd)
    ip.append(ipadd)
print(ip[0])
ip_bin=[] # task 3
ip_hex=[]
ip_oct=[]
for i in range(10):
    ip_add = ip[i].split(".")
    ip_bin.append('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_add[0]),int(ip_add[1]),int(ip_add[2]),int(ip_add[3])))
for i in range(10):
    ip_add = ip[i].split(".")
    ip_hex.append('{0:02X}.{1:02X}.{2:02X}.{3:02X}'.format(int(ip_add[0]),int(ip_add[1]),int(ip_add[2]),int(ip_add[3])))
for i in range(10):
    ip_add = ip[i].split(".")
    ip_oct.append('{0:03o}.{1:03o}.{2:03o}.{3:03o}'.format(int(ip_add[0]),int(ip_add[1]),int(ip_add[2]),int(ip_add[3])))
print(ip_oct)
ip_dec = ip # task 4
fp = open(r"D:/Computer Science/Python Course/Python CISCO/IP.txt", 'w') #task 5
for deci,bina,octa,hexa in zip(ip_dec,ip_bin,ip_oct,ip_hex):
    print(deci,bina,octa,hexa)
    L = deci + " " + bina + " " + octa + " " + hexa + "\n"
    fp.write(L)
fp = open(r"D:/Computer Science/Python Course/Python CISCO/IP.txt", 'r') #task 6
for line in range(10):
    print(f"The {p.ordinal(line+1)} IP address in Decimal, Binary, Octal and hexadecimal format is {fp.readline()}");
        
