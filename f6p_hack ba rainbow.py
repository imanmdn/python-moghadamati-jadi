import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    inp = open(input_file_name)
    outp = open(output_file_name , 'w')

    lines = inp.readlines()

    for line in lines:
        line = line.split(',')
        name = line[0]
        pssw = line[1]
        if pssw[-1] == '\n':
            pssw = pssw[:-1]
        pssw = pssw.lower()
        
        
        for password in range(1000 , 9999 + 1):
            hash_i = hashlib.sha256(str(password).encode()).hexdigest()
            if hash_i == pssw:
                outp.write(name)
                outp.write(',')
                outp.write(str(password))
                outp.write('\n')

    outp.close()
    inp.close()