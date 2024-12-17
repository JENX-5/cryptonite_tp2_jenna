# tunn3l v1s10n

## Description
We found this file. Recover the flag.

## Solution
- I'm assuming the file is corrupted since they asked to recover it. Let's get the information about the file using exiftool
![Screenshot from 2024-12-17 16-27-08](https://github.com/user-attachments/assets/13af5592-4060-42e7-ba47-2f2c29fb213c)

-  When I tried opening the file it didn't display anything but did say the header size was wrong.
![Screenshot from 2024-12-17 16-58-40](https://github.com/user-attachments/assets/3e81d6cd-cb11-42b9-8bac-73d0206ef770)

- So looked up how to create a BMP ( bitmap data file). Referred the following video [BMP FILE MaKING](https://www.youtube.com/watch?v=kRTZJHMQVd4).
- The header bytes were indeed wrong, instead  of 28 bytes it had large byte value 53434 bytes(hex - D0BA)
![Screenshot from 2024-12-17 16-54-27](https://github.com/user-attachments/assets/0a7c8eca-e776-4345-9258-36070ab55e27)
- After changing it to 28 00 00 00. I opened the file again and this time it displayed.
![Screenshot from 2024-12-17 18-20-18](https://github.com/user-attachments/assets/9f47ecf6-5bf2-4644-a252-21db7d2656e9)
- Ok so we didn't get the flag but the file is 2.3MB and the data offset given is 53434 bytes. This basically refers to till where the image data will be found.
  In the video I referred to it was 36 bytes and this file was 53434 bytes implies there more to this image then shown. Out of the 28 byte header, the first 4 bytes is the width and next 4 is the height.
  Changed the width and after few tries,kept getting distorted image.
  ![Screenshot from 2024-12-17 17-01-06](https://github.com/user-attachments/assets/b7851075-92fa-4d4c-a75e-f4cda1e0b442)
- Then next changed the height , the given height is 306 which is really small, so increased it to 800. Keep in mind the value should be hexadecimal and entered in endian format.
    ![image](https://github.com/user-attachments/assets/9ec8bee1-3613-498a-98b2-64c58b090d12)
- This gave me the image.
![Screenshot from 2024-12-17 18-30-27](https://github.com/user-attachments/assets/34ccff48-193f-47c1-a852-e06fc438773a)
- In the top right is the flag, but it is cut off, so extended the height to 900.
![image](https://github.com/user-attachments/assets/4e566baf-2beb-412f-bbc7-efbf19fd4d11)
- Now the flag is seen. The picture colors were still off, so I changed the offset to 36 bytes too.
![image](https://github.com/user-attachments/assets/34efcdc3-fbcf-4878-a73c-607cd33c472f)

> FLAG: picoCTF{qu1t3_a_v13w_2020}

  
