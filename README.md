
Getting started (on new servers) with username notes and preference configration across various software. Last update Sept-2-19.

1. Linux Servers . 
- Clone this repo.  
 - copy vimrc and bashrc from repo to ~   
- Install below packages in ~/bin (if no sudo access) . 
```
# utilities
sudo apt-get install vim
sudo apt-get install tree

# tools
sudo apt-get install git
sudo apt-get install wget
sudo apt-get install curl
sudo apt-get install net-tools # arp, ifconfig, netstat
sudo apt-get install apache2
sudo apt-get install openssh-server

# Language support
sudo apt-get install gcc
sudo apt-get install default-jre
# maven
sudo apt-get ruby-full

# databases
sudo apt-get install postgresql postgresql-contrib
```

- Install below vim plugins . 

```
NERD tree
```

- Networking config . 
Block distracting websites with /etc/hosts. Add entry with 127.0.0.1 example_website.com . 

- Add server's public key to github . 
 Follow steps, [https://wiki.paparazziuav.org/wiki/Github_manual_for_Ubuntu](https://wiki.paparazziuav.org/wiki/Github_manual_for_Ubuntu) . 
 Note: https url will still ask for password, set 
 ```
 git remote set-url origin git@github.com:name/repo
 ```


2. Mac . 
- Follow all ubuntu steps . 
- Install below packages . 
  1. iTerm2 . 
    - Import profiles and settings from exported profile com.googlecode.iterm2.plist in this repo . 
    - Add password to password Manager
    
  2. HapticKey

3. Windows Software List . 
- Install below software
  1. Putty

4. Other software settings configure
- vscode 

5. Python packages below
```
export PIPVERSION='sudo pip3'
PIPVERSION install numpy
PIPVERSION install Pillow
```
