## Esercitazione
### Esercizio 1
ip a
ssh utente@ip
sudo systemctl | grep ssh
sudo systemctl enable ssh
sudo apt install openssh-server
script bash:
```
#!/bin/bash
sudo sytemctl enable ssh
sudo systemctl start ssh
echo “bind-address = 127.0.0.1” | sudo tee -a /etc/mysql/my.cnf
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables-save
sudo iptables-restore <<EOT configurazione EOT
```
sudo iptables -nvL (regole firewall)
sudo netstat -tulnp (porte aperte)
il database è visibile a tutti e andrebbe messo in [localhost](http://localhost) (mariadb bind interface)
accettare le connessioni establish e mettere la regola di default a DROP
sudo iptables -A INPUT -m state —state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -p tcp —dport 22 -j ACCEPT
sudo iptables-save (la stampa)
sudo iptables-restore <<EOT configurazione EOT
tee  /iptables.conf <<EOT configurazione EOT
sudo iptables-restore -f /iptables.conf

### Esercizio 2

login con utente root nei log

sudo cat /etc/shadow | grep root
sudo cat /etc/shadow (senza asterisco)
```
sudo passwd -l root
```

### Esercizio 3
nei log pippo è loggato come root ma non ha diritti

sudo su pippo
history
rimuoviamo pippo dai sudoers
sudo visudo
sudo cat /etc/sudoers.d/pippo
```
sudo rm /etc/sudoers.d/pippo
```
potrebbe anche trovarsi in un gruppo
