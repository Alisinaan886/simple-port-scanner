Simple Python Port Scanner

A simple Python-based port scanner that detects open ports on a target system using socket programming.  
Includes automatic local IP detection and user-selectable target scanning.

 
 📌 Features
- Automatic local IP detection
- Choose to scan your own IP or any target IP
- Select custom port range
- Displays open ports in a clean format

 
 🚀 How to Run
1. Clone this repository or download the files.
2. Open terminal or PowerShell in the project folder.
3. Run:
   ```bash
   python portscanner.py
Follow the prompts:

Choose target IP (own IP or custom)

Enter starting and ending port

📖 Example Output
yaml
Copy
Edit
=== Simple Python Port Scanner ===
Your detected IP address is: 192.168.0.105
Do you want to scan your own IP? (y/n): y
Enter starting port: 1
Enter ending port: 100
[OPEN] Port 22
[OPEN] Port 80
[+] Scan Completed at: 2025-08-09 07:15:42
⚠ Disclaimer
This tool is for educational and authorized security testing only.
Do not scan systems you do not own or have explicit permission to test.
