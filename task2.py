import string
punctuation = list(string.punctuation)
digits = list(string.digits)
alpha1 = list(string.ascii_lowercase)
alpha2 = list(string.ascii_uppercase)
characters = punctuation + digits + alpha1 + alpha2
import numpy as np
rand_num = np.random.randint(len(characters))
length = int(input("Specify the desired length of the password: "))
count = 0
result = []
while count < length:
    rand_num = np.random.randint(len(characters))
    result.append(characters[rand_num])
    count+=1
password = "".join(result)
print("Random generated password of length {} is {}".format(length, password))