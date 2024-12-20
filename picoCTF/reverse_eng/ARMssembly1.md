# ARMssembly 1

## Description
For what argument does this program print `win` with variables 85, 6 and 3? File: chall_1.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution
- Solved ARMssembly 0 before this. Here we need to find the argument we need to give.
w0 contains the value of the argument we give. Then function jumps to func.
![Screenshot from 2024-12-21 00-39-28](https://github.com/user-attachments/assets/d64debb5-7a76-4068-b387-f441da32d6bb)
- Look at comments (; ). I have kept our argument as x.
- The initial part of the function is just storing values in the stack. Then it uses on w1=85 and w0 = 6 , lsl- Logical shif left. So 85<<6 = 5440. For sdiv which is signed division 5440/3 = 1813(ans in int) and this is stored in w0
![Screenshot from 2024-12-21 00-39-51](https://github.com/user-attachments/assets/2243543e-f72d-497e-95a2-871c5355b547)
- In the end of func, w0 has the value 1813 - x where x is our given argument.
- To print "You win" it needs to enter .LC0 for that the value of w0 should be 0
![image](https://github.com/user-attachments/assets/ae3ac89f-8422-4e31-a9fa-e4752a1b8364)
![Screenshot from 2024-12-21 00-40-45](https://github.com/user-attachments/assets/1869dfdd-a291-41a6-86e8-edb70eba62b2)

- This is possible only if w0 = 1813 -x =0 .So x= 1813.
- In hex 1813 is 0x715.
![Screenshot from 2024-12-21 00-41-21](https://github.com/user-attachments/assets/38220efc-ef9d-4c7e-a223-de6483c5beca)



  

> FLAG: picoCTF{00000715}
