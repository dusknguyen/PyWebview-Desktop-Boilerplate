import threading
import socket
import os
import subprocess
from fastapi.staticfiles import StaticFiles
import webview
from server.main import server
import uvicorn

# Hàm tìm cổng trống ngẫu nhiên
def get_free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    _, port = s.getsockname()
    s.close()
    return port

PORT = get_free_port()  # Lấy cổng trống ngẫu nhiên

# Chạy FastAPI trên thread riêng
def start_server():
    uvicorn.run(server, host="127.0.0.1", port=PORT)

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()

    # Khởi động webview để mở React SPA
    webview.create_window("Python + React SPA", f"http://127.0.0.1:{PORT}")
    webview.start()
