from subprocess import Popen, PIPE, DEVNULL
from os import path
from time import sleep

def update(current_ip):
    print("°°° UPDATING IP ON ALL SITES °°°\n")

    # DDNS
    print("Updating record DNS ...\n")
    Popen(["noipy -n localhoneypot.ddns.net --provider noip > /dev/null"], shell=True).wait()
    sleep(1)

    # GIT
    print("Creating webpage on Github.io ...\n")
    with open("resources/localhoneypot.github.io/index.html", "w+") as home:
        home.write(current_ip)
    Popen(['bash', 'bin/commit.sh']).wait()
    sleep(1)
    
    # TELEGRAM
    print('Posting on Telegram ...\n')
    Popen(['python3', 'bin/telegram.py', current_ip]).wait()
    sleep(1)

    # TOR
    print("Creating webpage for TOR hidden service ...\n")
    with open("resources/tor_hidden_service/index.html", "w+") as home:
        home.write(current_ip)
    sleep(1)

    # BLOCKCHAIN
    print("Creating and deploying contract in Ethereum Blockchain ...\n")
    Popen(['python3', 'bin/ethereum.py', current_ip]).wait()

if __name__ == '__main__':
    p = Popen(['curl', '-s', 'ifconfig.me'], stdout=PIPE)
    current_ip = p.communicate()[0].decode()
    print(current_ip)

    try:
        with open('public-ip.txt', 'r') as ip_file:
            if ip_file.read() != current_ip:
                update(current_ip) 

    except FileNotFoundError:
        with open('public-ip.txt', 'w+') as ip_file:
            ip_file.write(current_ip)
        update(current_ip)
