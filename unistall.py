import subprocess
import sys

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])

if __name__ == "__main__":
    packages_to_uninstall = [
        'aiohappyeyeballs',
        'aiohttp',
        'beautifulsoup4',
        'Flask',
        'numpy',
        # Diğer kaldırmak istediğiniz paketleri buraya ekleyin
    ]
    
    for package in packages_to_uninstall:
        uninstall(package)
    
    print("Kaldırma işlemi tamamlandı.")
