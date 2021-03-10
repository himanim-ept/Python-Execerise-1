#Write a Python program to match key values in two dictionaries.
#Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
#Expected output: key1: 1 is present in both x and y

dic1 = {'key1': 1, 'key2': 3, 'key3': 2}
dic2 = {'key1': 1, 'key2': 2}

for k in dic1:
    if k in dic2:
       if dic1[k]==dic2[k]: #compare the key and value
        print(k,"is present in both dic1 and dic2")