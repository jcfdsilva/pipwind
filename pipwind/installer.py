import os
import sys
import platform
import subprocess
import urllib.request
import requests
from bs4 import BeautifulSoup

def get_python_version_tag():
    """Get the Python version in the format used by wheels, e.g., cp39 for Python 3.9."""
    version = sys.version_info
    return f"cp{version.major}{version.minor}"

def get_platform_tag():
    """Get the platform tag for Windows (win32 or win_amd64)."""
    if platform.system() == 'Windows':
        arch = platform.architecture()[0]
        return 'win_amd64' if arch == '64bit' else 'win32'
    else:
        raise NotImplementedError("This tool currently only supports Windows.")

def get_wheel_links(package_name):
    python_version = get_python_version_tag()
    platform_tag = get_platform_tag()
    
    url = f"https://pypi.org/simple/{package_name}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Failed to retrieve package information: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    wheel_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('.whl') and python_version in href and platform_tag in href:
            wheel_links.append(href)
    return wheel_links

def download_and_install_wheel(url):
    wheel_filename = url.split('/')[-1]
    print(f"Downloading {wheel_filename}...")
    urllib.request.urlretrieve(url, wheel_filename)
    print(f"Installing {wheel_filename}...")
    subprocess.run(["pip", "install", wheel_filename])
    os.remove(wheel_filename)  # Clean up downloaded wheel file
    print(f"Installation of {wheel_filename} completed.")
