import platform
import subprocess
import os
import glob
import argparse

def system_info():
    system_details = (
        f"System: {platform.system()}\n"
        f"Node Name: {platform.node()}\n"
        f"Release: {platform.release()}\n"
        f"Version: {platform.version()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}\n"
        f"Python Version: {platform.python_version()}\n"
    )
    return system_details

def users():
    netuser = os.popen('net user').read()  
    return netuser

def network():
    ipconfig = os.popen('ipconfig').read()  
    arp = os.popen('arp -a').read()  
    network_details = f"{ipconfig}\n{arp}\n"
    return network_details

def envs():
    envs = os.popen('set').read()
    return envs

def installed_software():
    result = subprocess.check_output('wmic product get name, version', shell=True, text=True)
    return result

def services():
    task = os.popen('tasklist').read()
    return task

def search_config_files():
    config_dirs = [
        os.path.expanduser(r"~\AppData\Local"),  
        os.path.expanduser(r"~\AppData\Roaming"),  
        r"C:\ProgramData",  
        r"C:\Windows\System32",  
        r"C:\Windows\SysWow64"  
    ]
    
    config_extensions = ["*.ini", "*.config", "*.json", "*.xml", "*.yml", "*.yaml"]
    found_files = []
    
    for directory in config_dirs:
        for ext in config_extensions:
            files = glob.glob(os.path.join(directory, ext), recursive=True)
            found_files.extend(files)
    
    return found_files

def save_to_file(output_file, system_info, users_info, network_info, env_info, software_info, services_info, config_files):
    with open(output_file, 'w') as f:
        f.write("##################### System Info #####################\n")
        f.write(system_info + "\n")
        f.write("##################### Users #####################\n")
        f.write(users_info + "\n")
        f.write("##################### Network #####################\n")
        f.write(network_info + "\n")
        f.write("##################### Environment Variables #####################\n")
        f.write(env_info + "\n")
        f.write("##################### Services #####################\n")
        f.write(services_info + "\n")
        f.write("##################### Installed Software #####################\n")
        f.write(software_info + "\n")
        f.write("##################### Config Files #####################\n")
        if config_files:
            for file in config_files:
                f.write(f"{file}\n")
        else:
            f.write("No config files found.\n")

def parse_args():
    parser = argparse.ArgumentParser(description="Gere um arquivo com informações do sistema.")
    parser.add_argument('-o', '--output', type=str, help="Arquivo de saída", default="output.txt")
    return parser.parse_args()

def menu():
    options = {
        1: installed_software,
        2: users,
        3: system_info,
        4: network,
        5: envs,
        6: services,
        7: search_config_files,
        8: "output",
        0: "exit"
    }

    while True:
        print("\n  Choose an option :")
        print("1 - Installed Software")
        print("2 - System Users")
        print("3 - System Information")
        print("4 - Network Information")
        print("5 - Environment Variables")
        print("6 - Services")
        print("7 - Search Config Files")
        print("8 - Output File")
        print("0 - Exit")

        try:
            option = int(input(" Choose a number: "))

            if option in options:
                if options[option] == "exit":
                    print("Leaving...")
                    break
                elif options[option] == "output":
                    return True
                else:
                    result = options[option]() 
                    print(result)
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("Please, insert a valid number")

def main():
    args = parse_args()

    if menu():
        system = system_info()
        users_info = users()
        network_info = network()
        env_info = envs()
        software_info = installed_software()
        services_info = services()
        config_files = search_config_files()

        save_to_file(args.output, system, users_info, network_info, env_info, software_info, services_info, config_files)

        print(f"Informações salvas em: {args.output}")

if __name__ == "__main__":
    main()