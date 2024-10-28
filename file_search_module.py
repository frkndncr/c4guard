import os
import zipfile
import tarfile
import shutil
import smtplib
from email.mime.text import MIMEText
import logging
import sqlite3
import psutil
import requests
import schedule
import time

# Logging setup
logging.basicConfig(filename='file_search.log', level=logging.INFO)

# Virustotal API Key (Güvenlik için dışarıdan alınmalı)
VIRUSTOTAL_API_KEY = os.getenv('2440f34c350a618b99ecaad71ce096871f7ac5b96a4128371160147951c92860')  # Çevresel değişken kullanımı
VIRUSTOTAL_API_URL = 'https://www.virustotal.com/api/v3/files'

# SQLite veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('files.db')
    return conn

# Function to search for files by name
def search_files_by_name(root_directory, file_name):
    found_files = []
    try:
        for dirpath, dirnames, filenames in os.walk(root_directory):
            for filename in filenames:
                if file_name in filename:
                    found_files.append(os.path.join(dirpath, filename))
                    log_file_search(os.path.join(dirpath, filename))
    except Exception as e:
        logging.error(f"Error searching files: {e}")
    return found_files

# Function to log file search
def log_file_search(file):
    logging.info(f"File found: {file}")

# Function to analyze file with VirusTotal
def analyze_file_with_virustotal(file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(VIRUSTOTAL_API_URL, 
                                     headers={'x-apikey': VIRUSTOTAL_API_KEY}, 
                                     files={'file': file})
        return response.json()
    except Exception as e:
        logging.error(f"Error analyzing file with VirusTotal: {e}")
        return None

# Function to filter files based on size and type
def filter_files(files, min_size=None, max_size=None, file_types=None, modified_after=None):
    filtered_files = []
    for file in files:
        try:
            file_size = os.path.getsize(file)
            file_mtime = os.path.getmtime(file)

            if min_size and file_size < min_size:
                continue
            if max_size and file_size > max_size:
                continue
            if file_types and not any(file.endswith(ft) for ft in file_types):
                continue
            if modified_after and file_mtime < modified_after:
                continue
            
            filtered_files.append(file)
        except Exception as e:
            logging.error(f"Error filtering file {file}: {e}")
    return filtered_files

# Function to extract compressed files
def extract_compressed_file(file, destination_path):
    try:
        if file.endswith('.zip'):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(destination_path)
        elif file.endswith('.tar'):
            with tarfile.open(file) as tar_ref:
                tar_ref.extractall(destination_path)
    except Exception as e:
        logging.error(f"Error extracting file {file}: {e}")

# Function to batch process files
def batch_process_files(files, action='delete', destination_path=None):
    for file in files:
        try:
            if action == 'delete':
                os.remove(file)
            elif action == 'copy' and destination_path:
                shutil.copy(file, destination_path)
            elif action == 'move' and destination_path:
                shutil.move(file, destination_path)
        except Exception as e:
            logging.error(f"Error processing file {file}: {e}")

# Function to send email notifications
def send_email_notification(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'  # Güncellemeyi unutmayın
    msg['To'] = 'recipient@example.com'  # Güncellemeyi unutmayın
    
    try:
        with smtplib.SMTP('smtp.example.com') as server:  # Güncellemeyi unutmayın
            server.starttls()  # Use TLS for security
            server.login('your_email@example.com', 'your_password')  # Güncellemeyi unutmayın
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
    except Exception as e:
        logging.error(f"Error sending email: {e}")

# Function to monitor system status
def monitor_system():
    try:
        disk_usage = psutil.disk_usage('/')
        memory_usage = psutil.virtual_memory()
        
        logging.info(f"Disk Usage: {disk_usage.percent}%")
        logging.info(f"Memory Usage: {memory_usage.percent}%")
    except Exception as e:
        logging.error(f"Error monitoring system: {e}")

# Function to create a SQLite database
def save_to_database(file):
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS files (filename TEXT)")
        c.execute("INSERT INTO files (filename) VALUES (?)", (file,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
    finally:
        conn.close()

# Function for scheduled tasks
def scheduled_task():
    # Define the task to run periodically
    logging.info("Scheduled task running.")