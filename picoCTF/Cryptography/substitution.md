# substitution0
### Author: Will Hong
> FLAG: picoCTF{5ub5717u710n_3v0lu710n_357bf9ff}

## Description
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message here.

## Solution
- They gave the substituion order in the start of the cipher text which made things easy. Just follow the code below
```
cipher= """ZGSOCXPQUYHMILERVTBWNAFJDK 

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}"""

val = ""
alpha = 'abcdefghijklmnopqrstuvwxyz'
calpha = "ZGSOCXPQUYHMILERVTBWNAFJDK"

for i in cipher:
    try: 
        index = calpha.index(i.upper())
        val = val + alpha[index]
    except:
        val = val+i
print(val)
```
- OUTPUT:
abcdefghijklmnopqrstuvwxyz 

hereupon legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. it was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. there were two round black spots near one extremity of the back, and a
long one near the other. the scales were exceedingly hard and glossy, with all the
appearance of burnished gold. the weight of the insect was very remarkable, and,
taking all things into consideration, i could hardly blame jupiter for his opinion
respecting it.

the flag is: picoctf{5ub5717u710n_3v0lu710n_357bf9ff}

