import hashlib
import sys

#Input into crack 3 strings: user, salt, and given hash value respectively
#Output will be the password in string form
def crack(user,salt,hash_val):
    i = 0
    flag = 1
    ps = "00000000"
    fpw1 = user + "," + ps + "," + salt
    while(hashlib.sha256(fpw1.encode()).hexdigest()!= hash_val or i > 100000000):
        fpw2 = user + "," + str(i) + "," + salt
        i = i + 1
        if(hashlib.sha256(fpw2.encode()).hexdigest()== hash_val):
            flag = 2
            break
        else:
            ps = "00000000"[:-len(str(i))] + str(i)
            fpw1 = user + "," + ps + "," + salt
    if flag == 1:
        return fpw1.split(",")[1]
    else:
        return fpw2.split(",")[1]