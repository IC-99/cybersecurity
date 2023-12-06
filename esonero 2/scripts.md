### Comandi utili
```
### SSH ###
ssh utente@ip -p port
sudo systemctl | grep ssh
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```
### Configura sudo affinchè un utente possa eseguire solo un comando specifico (e.s: cat sul file shadow, nmap)
```
#!/bin/bash
sudo chown root:root /usr/bin/nmap
sudo chmod 700 /usr/bin/nmap
sudo visudo
# pippo  ALL=(ALL:ALL) /usr/bin/cat /etc/shadow
# pippo  ALL=(ALL:ALL) /usr/bin/nmap
```
### Configura sudo affinchè un utente possa eseguire solo un comando specifico ma senza un parametro (e.s: si puo eseguire nmap ma non nmap -p, )
```
#!/bin/bash
sudo visudo
# pippo  ALL=(ALL:ALL) /usr/bin/nmap [0-9]*.[0-9]*.[0-9]*.[0-9]*
```
### Cercare tutti gli eseguibili con SUID
```
#!/bin/bash
sudo find / -type f -perm /4000
```
### Cercare tutti gli eseguibili con GUID
```
#!/bin/bash
sudo find / -type f -perm /2000
```
### Creare uno unit file di Systemd per permettere una shell aperta a tutti sulla rete (netcat in modalità listen con il processo /bin/bash) e provare a connettersi dalla propria macchina usando netcat
[link](https://github.com/IC-99/cybersecurity/blob/main/esonero%202/unit%C3%A0.txt)
### Installare e configurare un modulo PAM per richiedere caratteristiche minime alla password (min 8 caratteri, maiuscole, minuscole e simboli)

### Imposta una password a GRUB così da non permettere l'avvio del sistema operativo con parametri del kernel non standard

### Rendi la cartella /var/log leggibile solo da root
```
#!/bin/bash
sudo chmod 700 /var/log
```
### Configura un utente per poter fare cat dei logs ma non essere amministratore (va configurato sudoers in modo opportuno)
```
#!/bin/bash
sudo visudo
# pippo  ALL=(ALL:ALL) /usr/bin/cat /var/log/*
```
### Trova tutti i processi che hanno un file descriptor aperto dentro la cartella /var/log (il comando lsof tornerà comodo)

### Usa docker per effettuare un privilege escalation

### Cercare se esiste un qualche file all'interno della home di un utente che sia scrivibile da tutti gli utenti
```
#!/bin/bash
find /home/nomeutente -type f -perm -o+w -exec ls -la {} \;
# chmod 644 /percorso/del/file
```
### Cercare se esiste una cartella all'interno della home di un utente che sia scrivibile da tutti gli utenti
```
#!/bin/bash
find /home/nomeutente -type d -perm -o+w -exec ls -lad {} \;
# chmod 755 /percorso/della/cartella
```
### Creare un utente con la password che scade ogni giorno
```
#!/bin/bash
sudo useradd pippo
sudo chage -M 1 pippo
```
### Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22)
```
#!/bin/bash
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

sudo iptables -A INPUT -i lo -j ACCEPT
```
### Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) dall'IP 1.2.3.4 e ad un webserver da qualunque IP (TCP port 80 e 443)
```
#!/bin/bash
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

sudo iptables -A INPUT -p tcp --dport 22 -s 1.2.3.4 -j ACCEPT

sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

sudo iptables -A INPUT -i lo -j ACCEPT
```
### Imposta Iptables affinchè sia bloccato tutto il traffico Internet sulla macchina (gli utenti non possono navigare) ma sia funzionante il webserver (TCP port 80 e 443)
```
#!/bin/bash
sudo iptables -F
sudo iptables -X

sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP

sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 443 -j ACCEPT

sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

----------------------------------------------------------------
sudo sh -c "iptables-save > /etc/iptables.rules"

# Assicurati che le regole siano caricate all'avvio del sistema
sudo iptables-save | sudo tee /etc/network/iptables.up.rules
sudo systemctl enable netfilter-persistent
sudo systemctl start netfilter-persistent
----------------------------------------------------------------
```
### Imposta Iptables affinchè sia permesso l'accesso alla macchina solo via SSH (TCP port 22) e ad un webserver (TCP port 80 e 443)
```
#!/bin/bash
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

sudo iptables -A INPUT -i lo -j ACCEPT
```
