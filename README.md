## Rar-Fu
Python script to crack RAR file with dictionary attack.

## Preview
![image](https://raw.githubusercontent.com/sumit-buddy/Rar-Fu/main/rar-fu.gif)

## Install
```
git clone https://github.com/sumit-buddy/Rar-Fu.git

cd Rar-Fu

pip3 install -r requirements.txt
```

> You need to install `unrar` package before running the script otherwise it will not work.
You can install `unrar` using below commands. Run this commands as root user.

### Termux android
```pkg install unrar```

### Google Cloud Shell 
```apt-get install unrar-free```

### Debian Linux
```apt-get install unrar```
or
```apt-get install unrar-free```

### Fedora Core Linux
```yum install unrar```

### Arch Linux
```pacman -S unrar```

### OpenBSD
```pkg_add –v –r unrar```

### Suse10 
```yast2 –i unrar```

### Suse11
```zipper install unrar```

## Running Script
```
python3 rar-fu.py
```
