from subprocess import Popen, PIPE, DEVNULL
from os import path
from time import sleep
from bin.keys import fqdn, repo
from argparse import ArgumentParser


def update(current_ip, method):
    print("°°° UPDATING IP °°°\n")

    # DNS
    if method == 'dns' or method == None:
        print("Updating record DNS ...\n")
        Popen(["noipy -n %s --provider noip > /dev/null" % fqdn], shell=True).wait()
        sleep(1)

    # GIT
    if method == 'git' or method == None:
        print("Creating webpage on Github.io ...\n")
        with open("resources/%s.github.io/index.html" % repo, "w+") as home:
            home.write(current_ip)
        Popen(['bash', 'bin/commit.sh']).wait()
        sleep(1)
    
    # TELEGRAM
    if method == 'telegram' or method == None:
        print('Posting on Telegram ...\n')
        Popen(['python3', 'bin/telegram.py', current_ip]).wait()
        sleep(1)

    # TOR
    if method == 'tor' or method == None:
        print("Creating webpage for TOR hidden service ...\n")
        with open("resources/tor_hidden_service/index.html", "w+") as home:
            home.write(current_ip)
        sleep(1)

    # BLOCKCHAIN
    if method == 'eth' or method == None:
        print("Creating and deploying contract in Ethereum Blockchain ...\n")
        Popen(['python3', 'bin/ethereum.py', current_ip]).wait()

if __name__ == '__main__':

    parser = ArgumentParser(description="Botmaster", epilog="Version 0.1")
    parser.add_argument('-m', '--method', help='how to check ip', action='store')
    args = parser.parse_args()

    p = Popen(['curl', '-s', 'ifconfig.me'], stdout=PIPE)
    current_ip = p.communicate()[0].decode()
    print(current_ip)

    try:
        with open('public-ip.txt', 'r') as ip_file:
            if ip_file.read() != current_ip:
                update(current_ip, args.method) 

    except FileNotFoundError:
        with open('public-ip.txt', 'w+') as ip_file:
            ip_file.write(current_ip)
        update(current_ip, args.method)
