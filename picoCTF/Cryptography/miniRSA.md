# miniRSA

## Description
Let's decrypt this: ciphertext? Something seems a bit small.

## Solution
- In the cipher text, we have public key n and e given along with the cipher text. e=3 which is small and reduces security.
- So I looked up RSA algorithm, we have n but it's really large so finding p and q would be difficult to get the value of d.
- Anyway while searching I found a git repo RsaCtfTool, downloaded it and just gave the cipher text with n and e and got the flag.
![Screenshot from 2024-12-20 01-17-19](https://github.com/user-attachments/assets/0176412e-2ced-4f84-901c-d1b61d1d0681)
![Screenshot from 2024-12-20 01-17-37](https://github.com/user-attachments/assets/fa71b149-b6e4-4004-9d71-6016423d3779)
> FLAG : picoCTF{n33d_a_lArg3r_e_d0cd6eae}

- Note: Since there was really nothing to do in this challenge because I used an external tool. You can also try to do it with a different approach since n e c rsa is common in CTF challenges.
  We know c = (M\**e) % n and M = (c\**d) % n. Now we don't have d but since e = 3 finding the cuberoot of a number wont take too long.
  So M\**e = tn + c (t is any integer). M = cuberoot(tn+c). To find M we need to iterate throught different values of t till we get the true cube root.  
  
