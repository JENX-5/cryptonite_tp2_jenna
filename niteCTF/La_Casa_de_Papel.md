# La Casa de Papel
### Author: Wixter_07

## Description:
Word on the street is Bob's about to make a big withdrawal. Too bad you're the one holding his ID. 
Can you charm Alice into making the transfer before she catches on?

## Solution
- Looking at the code we notice it encrypts data using md5 which is irreversible and we don't even have the key. 
- Bruteforcing won't work but we don't have to because if we look carefully.
<img width="477" alt="{7CDAECB9-6639-4A3C-AFE6-FA5C18BA968A}" src="https://github.com/user-attachments/assets/d0be4408-a2dc-4063-917a-d71e784e141e" />

- In the practice_convo() func, it encodes the data we give for us using the secret key, and the condition checks the encoded value.
- So we need the user to be Bob, so giving Bob to practice convo we'll give the md5 encoded value with the key, then we just need to decode using base64 so that it matches with hash.
  base64.b64decode(<encrypted_value>), you'll get b'b4e0a802428cb35f69c0e952d96172d6'.
- Give this value as hmac and you'll get the secret, then give it as vault password for the flag.
```bash
crypto@crypto:~$ ncat --ssl la-casa-de-papel.chals.nitectf2024.live 1337
 _             ____                      _        ____                  _
| |    __ _   / ___|__ _ ___  __ _    __| | ___  |  _ \ __ _ _ __   ___| |
| |   / _` | | |   / _` / __|/ _` |  / _` |/ _ \ | |_) / _` | '_ \ / _ \ |
| |__| (_| | | |__| (_| \__ \ (_| | | (_| |  __/ |  __/ (_| | |_) |  __/ |
|_____\__,_|  \____\__,_|___/\__,_|  \__,_|\___| |_|   \__,_| .__/ \___|_|
                                                            |_|


1. Practice Convo
2. Let's Fool Alice!
3. Crack the Vault
4. Exit
Choose an option: 1
Send a message: Bob
Here is your encrypted message: YjRlMGE4MDI0MjhjYjM1ZjY5YzBlOTUyZDk2MTcyZDY=

1. Practice Convo
2. Let's Fool Alice!
3. Crack the Vault
4. Exit
Choose an option: 2

Bot: Okay, let's see if you're the real deal. What's your name?
Your name: Bob

Bot: Please provide your HMAC
Your HMAC: b4e0a802428cb35f69c0e952d96172d6

Alice: Oh hey Bob! Here is the vault code you wanted:
G0t_Th3_G0ld_B3rl1nale

1. Practice Convo
2. Let's Fool Alice!
3. Crack the Vault
4. Exit
Choose an option: 3

Vault Person: Enter password
Password: G0t_Th3_G0ld_B3rl1nale

Vault Unlocked! The flag is: nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
```
> FLAG:  nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
