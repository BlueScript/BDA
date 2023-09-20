from xmlrpc.client import ServerProxy

filec = len(open("data.txt").read().split(" "))
count1 =0
count2 =0

if __name__ == '__main__':
    s = ServerProxy("http://192.168.108.205:8080")
    count1 = s.add(filec)

    a = ServerProxy("http://192.168.108.206:8080")
    count2 = a.add(count1)

    print(count1)

    print(count2)
    