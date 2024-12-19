# Custom encryption
> FLAG : picoCTF{custom_d2cr0pt6d_e4530597}

## Description
Can you get sense of this code file and write the function that will decode the given encrypted file content. Find the encrypted file here flag_info and code file might be good to analyze and get the flag. 

# Solution
- The code was given, it encrypted the flag twice, first with xor cipher then custom encryption.
- For xor cipher we don't need to make a decoder since encrypt/decrypt is the same thing. 
- The custom encryption wasn't using anything complex just multiplying ascii value of the character with key\*311. So to decrypt we have the out value just divide it by (key*311) to get the characters ascii value.
- I have attached the decoder I made.
```bash
crypto@crypto:~/pico$ /bin/python3 /home/crypto/decrypt.py
FLAG is: picoCTF{custom_d2cr0pt6d_e4530597}
```

