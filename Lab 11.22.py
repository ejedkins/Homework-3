#Elijah Jedkins PSID: 1786452
sent = input()
text = sent.split(" ")
for i in text:
    freq = text.count(i)
    print(i, freq)