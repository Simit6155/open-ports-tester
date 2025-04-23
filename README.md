# 🔌 Port Tester

A simple Python-based port testing tool that allows you to check the status of open or closed ports on a target IP address. Great for quick network diagnostics or cybersecurity experiments.

## 📦 Features

- Checks if a specific port on a target IP is open or closed.
- Lightweight and fast.
- Uses sockets and customizable timeout.
- Colored output with `colorama` for easy readability.

---

## 🧰 Requirements

This tool requires the following Python modules:

```txt
colorama
socket and time are built-in Python modules and do not require installation.

To install the required module, run:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Or install it manually:

bash
Kopyala
Düzenle
pip install colorama
🚀 Usage
bash
Kopyala
Düzenle
python port_tester.py
Then follow the prompts in the terminal to:

Enter the target IP or domain.

Enter the port number.

Get instant feedback on the port status.

🖥️ Example Output
bash
Kopyala
Düzenle
Enter target IP: 8.8.8.8
Enter port: 53
[✓] Port 53 is open on 8.8.8.8
or

bash
Kopyala
Düzenle
[✗] Port 80 is closed on 8.8.8.8
🛠️ Tech Stack
Python 3

socket for network communication

time for timeout handling

colorama for colored terminal output

📜 License
This project is licensed under the MIT License. Feel free to use and modify it as you like!

✨ Author
Developed by Simit
🔗 Instagram = https://www.instagram.com/Redsimit
📺 YouTube = https://www.youtube.com/@redsimitofficial
   
