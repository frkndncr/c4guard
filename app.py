from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import file_search_module
import os
import webbrowser  # Tarayıcıyı açmak için eklenmiştir
import requests
import psutil  # Sistemi kontrol etmek için psutil eklendi
import threading  # Tarayıcıyı sadece bir kere açmak için

C4Guard = Flask(__name__)

@C4Guard.route('/')
def index():
    return render_template('index.html')

# Sistem durumu kontrolü için endpoint
@C4Guard.route('/system-status', methods=['GET'])
def system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage('/').percent
    memory_usage = psutil.virtual_memory().percent

    return jsonify({
        'cpuUsage': cpu_usage,
        'diskUsage': disk_usage,
        'memoryUsage': memory_usage
    })

def analyze_file_with_virustotal(file):
    api_key = 'APİ_KEY'
    url = "https://www.virustotal.com/api/v3/files"

    with open(file, 'rb') as f:
        files = {'file': f}
        headers = {
            "accept": "application/json",
            "X-Apikey": api_key,
        }

        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            data = response.json()
            analysis_id = data['data']['id']

            analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
            analysis_response = requests.get(analysis_url, headers=headers)

            if analysis_response.status_code == 200:
                last_analysis_stats = analysis_response.json()['data']['attributes'].get('last_analysis_stats', {})
                malicious_count = last_analysis_stats.get('malicious', 0)
                harmless_count = last_analysis_stats.get('harmless', 0)

                status = "Tehlikeli" if malicious_count > 0 else "Tehlikesiz"
                item_url = analysis_response.json()['data']['links']['item']
                gui_link = f"https://www.virustotal.com/gui/file/{item_url.split('/')[-1]}"

                return {
                    'status': status,
                    'malicious_count': malicious_count,
                    'harmless_count': harmless_count,
                    'analysis_link': analysis_url,
                    'gui_link': gui_link
                }
            else:
                return {'error': 'Analiz alınamadı', 'status_code': analysis_response.status_code}
        else:
            return {'error': 'Dosya yüklenemedi', 'status_code': response.status_code}

@C4Guard.route('/search', methods=['POST'])
def search():
    file_name = request.form['filename']  # Burada 'filename' yerine 'query' kullanıyorsanız, kontrol edin
    root_directory = request.form['directory']
    
    found_files = file_search_module.search_files_by_name(root_directory, file_name)
    analysis_results = []
    
    if not found_files:
        analysis_results.append({
            'name': file_name,
            'size': 0,
            'result': 'Başarısız',
            'virustotalStatus': {
                'error': 'Dosya bulunamadı.',
                'status_code': 404
            }
        })
    else:
        for file in found_files:
            vt_analysis = analyze_file_with_virustotal(file)
            
            if 'error' not in vt_analysis:
                analysis_results.append({
                    'name': file,
                    'size': os.path.getsize(file) / 1024,
                    'result': 'Başarılı',
                    'virustotalStatus': {
                        'status': vt_analysis['status'],
                        'malicious_count': vt_analysis['malicious_count'],
                        'harmless_count': vt_analysis['harmless_count'],
                        'analysis_link': vt_analysis['analysis_link'],
                        'gui_link': vt_analysis['gui_link']
                    }
                })
            else:
                analysis_results.append({
                    'name': file,
                    'size': os.path.getsize(file) / 1024,
                    'result': 'Başarısız',
                    'virustotalStatus': {
                        'error': vt_analysis.get('error', 'Bilinmeyen hata'),
                        'status_code': vt_analysis.get('status_code', 500)
                    }
                })
    
    return jsonify({
        'searchedFiles': len(found_files),
        'results': analysis_results
    })

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    C4Guard.run(host='0.0.0.0', port=5000, debug=True)
