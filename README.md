🚨 Email Header Analyzer Tool 

This is a beginner-friendly Python project built by Mohit Vaishnav.

This tool analyzes email headers to help detect phishing, spam, and suspicious emails.
It extracts important fields like From, To, Subject, finds IP addresses, and detects risky keywords.
Ideal for Cybersecurity Learners & Ethical Hackers starting their projects.


---

🔹 Key Features

Extracts From, To, Subject from header

Detects IP addresses in "Received" lines

Scans for suspicious words: phish, spoof, fraud, etc.

Calculates a simple Risk Score

Lightweight & Easy to Use



---

🔧 Technologies Used

Python 3.x

Built-in Libraries: re and ipaddress



---

🔹 How to Run (Steps)

1. Prepare Header

Either paste header manually or

Save header in header.txt in the same folder


2. Run the Tool

python email_header_analyzer.py

3. Follow Prompts

Choose option to paste header or load from file

View the detailed analysis report (Risk Score, Keywords, IPs)



---

🔹 Folder Structure

email-header-analyzer/
|├📄 email_header_analyzer.py
|└📄 header.txt  # (Optional, for loading header)


---

🌟 Author

Mohit Vaishnav
Cybersecurity & Python Enthusiast


---

🚀 Future Plans

Add GUI (Tkinter / PySimpleGUI)

Save analysis reports automatically

Integrate with AI for deeper detection



---