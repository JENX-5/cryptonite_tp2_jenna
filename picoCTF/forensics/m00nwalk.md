# m00nwalk

## Description
Decode this message from the moon.

## Solution
- The given file was .wav file. The audio didn't sound like morse code and no other information about the file from exiftool.
- Hint 1 : How did pictures from the moon landing get sent back to Earth?
  After lots of research, because they kept talking about the hardware like antennas n stuff. Finally found SSTV- Slow scan television
  ![Screenshot from 2024-12-18 00-01-23](https://github.com/user-attachments/assets/bafe2d82-8d40-4e57-aa3f-67fd39c91d6d)
- FROM WIKI: Slow-scan television (SSTV) is a picture transmission method, used mainly by amateur radio operators, to transmit and receive static pictures via radio in monochrome or color.
- We have the audio so we need to convert it to the image, looked up online to find websites that do it. Couldn't find any. So type sstv to find packages.
![Screenshot from 2024-12-18 00-05-32](https://github.com/user-attachments/assets/dfb8da45-18f4-402d-87c9-43f9763f13ff)
- So qsstv can do it. After downloading start it
```bash
crypto@crypto:~/Downloads$ qsstv
```
- Gave some warningSlow-scan television (SSTV) is a picture transmission method, used mainly by amateur radio operators, to transmit and receive static pictures via radio in monochrome or color. s just ignore it. Go to the receiver side. There are bunch of modes as per the second hint CMU mascot its SCOTTY.
 ![Screenshot from 2024-12-18 00-08-57](https://github.com/user-attachments/assets/665351f4-28b5-4464-9ecd-c9e9eb26f874)

Doesn't seem like there is a way to import the audio, so played the audio and and the receiver simultaneously.


https://github.com/user-attachments/assets/e2135d0d-e443-4831-b01f-9ead7b7abdd6


![Screenshot from 2024-12-18 00-29-43](https://github.com/user-attachments/assets/deb9770e-8a3a-4006-ad03-6da9f7b4cbad)
- Got the flag.
> FLAG: picoCTF{beep_boop_im_in_space}
