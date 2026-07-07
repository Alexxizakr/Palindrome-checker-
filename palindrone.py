small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big  =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word=str(input("Enter a number or word:"))
ref=""
ref1=""
cutword=[]
for k in word:
    cutword.append(k)
for i in range(len(cutword)):
    if cutword[i] in big:
        for j in range(len(big)):
            if cutword[i]==big[j]:
                cutword[i]=small[j]
word=""
for l in cutword:
    word=word+l

for i in range(len(word)):
    if word[i] !=" ":
        ref=word[i]+ref
        ref1=ref1+word[i]
if ref1==ref:
    print("Palindrone")
if ref1!=ref:
    print("Not Palindrone")
