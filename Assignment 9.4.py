# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mail = dict()

for line in handle:
    line = line.rstrip()
    line = line.split()
    if len(line)<2 or line[0] != 'From':
        continue
    mail[line[1]] = mail.get(line[1], 0) + 1

bigk = None
bigv = None

for k in mail:
    if bigv is None:
        bigv = mail[k]
        bigk = k

    if mail[k] > bigv:
        bigv = mail[k]
        bigk = k

print(bigk, bigv)
