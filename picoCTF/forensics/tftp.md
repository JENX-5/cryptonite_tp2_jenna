# Trivial Flag Transfer Protocol

## Description
Figure out how they moved the flag.

## Solution
- The file downloaded is .pcapng, used wireshark to open it.
- Sometimes the flag is hidden in one of the data packets. So I tried for tftp contains "picoCTF" but didn't find anything.
- I noticed the first packet had a file: instructions.txt
![Screenshot from 2024-12-18 23-28-17](https://github.com/user-attachments/assets/95dc52e7-e1b4-4504-87b6-06ec2546bf39)
- So I tried exporting this object, but they were more files transferred using tftp.
![Screenshot from 2024-12-18 23-49-29](https://github.com/user-attachments/assets/5b2c8739-1a21-4b39-b9ac-667d9d8d548e)
- The files plan and instructions.txt were encoded so I ignored them for now. I looked into program and it was actually just steghide(package)
![Screenshot from 2024-12-18 23-57-57](https://github.com/user-attachments/assets/429f1aa3-5717-4e65-b5ed-efaaaf6b0c29)
- Already have it installed, so now we know we need to use steghide to extract the info from the pictures given but we don't have a passphrase.
- I assume it's it the encoded data, it's not in base64, so we need to go through different types of encryption. Tried Caesar then ROT13 which gave the text but didn't  have spaces so added spaces to be able to read it better.
![Screenshot from 2024-12-19 00-02-20](https://github.com/user-attachments/assets/5918fed7-7fea-4962-be8d-e7d600e2fda7)
![Screenshot from 2024-12-19 00-03-25](https://github.com/user-attachments/assets/f8cf5dbf-cd3a-439e-bef3-449e06a3f6e9)
- Instructions file didn't have much but plan file had the passphrase DUEDILIGENCE. They mention they hid it with this.
- Tried to extract data from pic1, it failed and got really confused. But then remembered we have 3 images and got the flag for picture3.
![image](https://github.com/user-attachments/assets/91a02c95-9a64-4481-9002-78a232a4e2ce)

> FLAG: picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

- 

