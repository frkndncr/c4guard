from setuptools import setup, find_packages

setup(
    name='proje_adı',  # Proje adınızı buraya yazın
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiohappyeyeballs==2.4.3',
        'aiohttp==3.10.8',
        'beautifulsoup4==4.8.0',
        'Flask==3.0.3',
        'numpy==1.26.4',
        # Diğer bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'proje_adı = app:main',  # app.py dosyanızda bulunan ana fonksiyonu belirtin
        ],
    },
    python_requires='>=3.6',  # Gereken Python sürümü
)
