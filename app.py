from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch required details
    full_name = "Tharani"
    username = os.getenv("USER", "codespace")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Fetch 'top' output
    top_output = subprocess.getoutput("top -b -n 1")
    
    # Prepare HTML
    html_content = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
