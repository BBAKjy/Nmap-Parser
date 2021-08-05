f = open("portscan.txt", "r")

scanList = f.readlines()

#print(scanList)

ips = []
ports = []

for i in range(len(scanList)):
    if "Nmap scan report " in scanList[i]:

        res = ""

        if "host down" in scanList[i]:
            print(scanList[i][:-1])
            continue

        if "(" in scanList[i]:
            res = scanList[i][scanList[i].find("(")+1:-2]

        else:
            res = scanList[i][scanList[i].find("for ")+4:-1]

        for j in range(i + 1, 99999):

            if j == 21489 or "Nmap scan report" in scanList[j] or "Discovered" in scanList[j]:
                break

            #print(i, j)
            if "/tcp" in scanList[j]:
                print(' '.join((res + "\t" + scanList[j]).split()))