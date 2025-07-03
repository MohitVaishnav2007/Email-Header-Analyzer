import re
import ipaddress

#Defining function to load email header (from text or file)
def load_email_header():
  print("Choose input method:")
  print("1. Paste email header")
  print("2. Load from file (header.txt)")
  choice = input("Enter your choice (1/2): ")

  if choice == "1":
    print("Paste the header below (end with an empty line):")
    lines = []
    while True:
      line = input()
      if line.strip() == "":
        break
      lines.append(line)
    return '\n'.join(lines)
  
  elif choice == '2':
    try:
      with open("header.txt","r") as file:
        return file.read()
    except FileNotFoundError:
      print("File not found. Make sure header.txt exists.")
      return ""
    
  else:
    print("Invalid choice")
    return ""
  
#Function to extract important fields from header
def analyze_header(header_text):
  print("\n----- Analyzing Header -----")
  

#Extracting FROM, TO, SUBJECT
  from_match = re.search(r'From: (.+)',header_text)
  to_match = re.search(r'To: (.+)',header_text)
  subject_match = re.search(r'Subject: (.+)',header_text)

  if from_match:
    print("From:", from_match.group(1))
  if to_match:
    print("To:", to_match.group(1))
  if subject_match:
    print("Subject:", subject_match.group(1))
    

#To extract all IP address which are common in Received headers
  ips = re.findall(r'\d+\.\d+\.\d+\.\d+', header_text)
  valid_ips = []
  for ip in ips:
    try:
      ipaddress.ip_address(ip)
      valid_ips.append(ip)
    except ValueError:
      continue

  print("\nFound IP Addresses:")
  for ip in valid_ips:
    print(" -", ip)



#Script to check for suspicious keywords
  suspicious_keywords = ["phish","spoof","fraud","scam","malware","ransom"]
  header_lower = header_text.lower()
  detected_keywords = [kw for kw in suspicious_keywords if kw in header_lower]

  print("\nSuspicious Keywords Found:")
  if detected_keywords:
    for kw in detected_keywords:
      print(" -",kw)
  else:
    print("None detected")


#Script for simple risk scoring
  risk_score = len(valid_ips) + len(detected_keywords) * 5
  print("\nRisk Score", risk_score)
  if risk_score >= 10:
    print("High Risk Email! Possible Spam/Phishing.")
  else:
    print("Low Risk Email.")



#Main function to run the program
def main():
  header = load_email_header()
  if header:
    analyze_header(header)

if __name__ == "__main__":
  main()

