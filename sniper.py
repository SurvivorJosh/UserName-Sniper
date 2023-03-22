
try:
    import requests, threading, os, sys, time, asyncio, string, random, logging
    from requests.adapters import HTTPAdapter
    from getpass import getpass
    from colorama import Fore
    from pystyle import Colorate, Colors, Center, Write, System
    
except:
    os.system('pip install asyncio')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install pystyle')
    
logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;196m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;196m] \033[0m%(message)s\033[0m",
    datefmt="%H:%M:%S"
)

token = input("[>] Token: ")
password = input("[>] PassWord: ")
usrname = input("[>] Username With Tag: ")
System.Clear()
os.system("mode 90,30")
class Sniper:
    def __init__(self):
        self.headers = {"Authorization": token}
        self.spitter = usrname.split("#")
        self.discrim = self.spitter[1]
        self.user = self.spitter[0]
        self.json = {"username": self.user, "discriminator": self.discrim, "password": password}
        self.des = str(self.user) + str(self.discrim)
        self.session = requests.Session()
        self.session.mount("", HTTPAdapter(max_retries=1))
        
        self.not_sniped = True
        
        self.heads = [
        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },

        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
        },

        {
            "Content-Type": "application/json",
             "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
]

    def getheaders(self):
        headers = random.choice(self.heads)
        
        return headers
    
    
            
            
    def sniper(self):
        time.sleep(1.7)
        url = f"https://discord.com/api/v9/users/@me"
        
        res = self.session.patch(url=url, json=self.json, timeout=5, headers = self.headers)
        try:
            if res.status_code == 404:
                logging.info(f"ERROR SNIPING USER | {res.status_code}")
                
                
            elif res.status_code == 200:
                logging.info(f"USERNAME {self.des} SNIPED | {res.status_code}")
                self.not_sniped = False
                
                
            elif res.status_code == 429:
                logging.info(f"RATELIMITED : You sent way too many requests suffering from ratelimits")
                b = res.json()
                time.sleep(0.7)
                self.sniper()
                
            else:
                logging.info(f"Status code : {res.status_code} - still taken")
                
        except:
            logging.info(f"Response from user sniper: {res.status_code}")
            
            
    def start(self):
        print(Colorate.Vertical(Colors.red_to_white, Center.XCenter("""
        
╦ ╦╔═╗╔═╗╦═╗╔╗╔╔═╗╔╦╗╔═╗
║ ║╚═╗║╣ ╠╦╝║║║╠═╣║║║║╣ 
╚═╝╚═╝╚═╝╩╚═╝╚╝╩ ╩╩ ╩╚═╝
   ╔═╗╔╗╔╦╔═╗╔═╗╦═╗        
   ╚═╗║║║║╠═╝║╣ ╠╦╝        
   ╚═╝╝╚╝╩╩  ╚═╝╩╚═   
        
        """)))
        while self.not_sniped:
            self.sniper()
         
        
        
        
        
if __name__ == "__main__":
    Sniper().start()
