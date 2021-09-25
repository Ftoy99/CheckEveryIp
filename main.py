import os

import asyncio


class HostChecker:

    def __init__(self, ip):
        ip_split = ip.split(".")
        self.A = int(ip_split[0])
        self.B = int(ip_split[1])
        self.C = int(ip_split[2])
        self.D = int(ip_split[3])

    def increment(self):
        self.D = self.D + 1
        if self.D == 256:
            self.D = 0
            self.C = self.C + 1

        if self.C == 256:
            self.C = 0
            self.B = self.B + 1

        if self.B == 256:
            self.B = 0
            self.A = self.A + 1

        if self.A == 256:
            return False
        else:
            return True

    def toString(self):
        return str(self.A) + "." + str(self.B) + "." + str(self.C) + "." + str(self.D)


    async def checkHostname(self):
        response = os.system("ping -n 1 " + self.toString() +" >nul 2>&1")

        # and then check the response...
        if response == 0:
            f = open('activeAddresses.txt', "a")
            f.write(self.toString()+"\n")
            print(self.toString()+"Responded")
        else:
            print("No Response from " + self.toString())


def main():
    a = HostChecker("82.102.57.157")
    while a.increment():
        asyncio.run(a.checkHostname())
        print(a.toString())


if __name__ == '__main__':
    main()
