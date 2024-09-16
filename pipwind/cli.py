import argparse
import sys
from pipwin_alternative.installer import get_wheel_links, download_and_install_wheel

def install_package(package_name):
    wheels = get_wheel_links(package_name)
    if wheels:
        download_and_install_wheel(wheels[0])
    else:
        print(f"No compatible wheel found for {package_name}")
        sys.exit(1)

def install_from_requirements(file_path):
    try:
        with open(file_path, 'r') as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            for package in packages:
                print(f"Installing {package}...")
                install_package(package)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Pipwin alternative using PyPI wheels.")
    parser.add_argument('command', choices=['install'], help='Command to execute')
    parser.add_argument('package', nargs='?', help="The name of the package to install")
    parser.add_argument('-r', '--requirement', help='Install from the given requirements file')

    args = parser.parse_args()

    if args.command == 'install':
        if args.requirement:
            install_from_requirements(args.requirement)
        elif args.package:
            install_package(args.package)
        else:
            print("Please specify a package or use the -r option to install from a requirements file.")
            sys.exit(1)

if __name__ == "__main__":
    main()
