from subprocess import Popen

# update auth certificate information
Popen(['python3', 'check-ip.py']).wait()

# run ovenvpn daemon to connect to c2 server
Popen(['openvpn', '--config', 'resources/cert.ovpn', '--daemon'])

# run pentbox
Popen(['python3', 'resources/honeypot/run_local_honeypot.py']).wait()

