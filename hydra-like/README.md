# Python Hydra-like tool

## Description
A basic python script based on the functionalities of hydra brute-force tool.

> [!WARNING]
>
> This is only for testing purpuses and for learning about legal hacking.
>
>Only do this in a safe, isolated environment (like a VM).

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick start](#quick-start)
3. [Usage](#usage)
    - [Install the SSH Server](#install-the-ssh-server)
    - [Use the brute force script](#use-the-brute-force-script)

## Prerequisites

- A test machine (VM recommended)
- `SSH Server` running on the test machine
- A test `user` for the ssh server
- `IP` address of the test machine

## Quick start

Clone this repository to your local machine and follow the README.md instructions.

Open your command line and type the following commands:

With SSH configured (if SSH Keys are provided to GitHub)
```
git clone git@github.com:MarcosChavez09/baby-tools-shop.git
```
Classic HTTPS (if no SSH Keys are provided to GitHub)
```
git clone https://github.com/MarcosChavez09/dso-python-exercices.git
```
After cloning the repository, navigate to `hydra_like` directory:

```
cd hydra_like
```

Create your virtual environment:

On macOS
```
    python3 -m venv .venv
```
On Linux
```
    python -m venv .venv
```

Activate your venv:
```
source .venv/bin/activate
```

> **_NOTE:_** To deactivate your venv, just type `deactivate` in the command line.

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

### Install the SSH Server

First, you need to have a test machine or VM with a SSH Server and a `user` for this server. 

If you have a based Linux VM, you can install the SSH Server with the following commands:

```
   sudo apt update
   sudo apt install openssh-server
```

Start the service:
```
sudo systemctl start ssh
```
Add a user and password:

```
  sudo adduser <test_user>
```
- Follow the prompts to set a password

> **_NOTE:_**
> Remember this password and add it to the `wordlist.txt`

Find your test machine or VM's IP address. If you are on a linux VM, type the following in the command line:

```
ifconfig
```
### Use the brute force script

Inputs:

| Input    | requirement | description |
| -------- | ------- | ------- |
| -s, --server       | mandatory    | Server IP or DNS name |
| -u, --username | mandatory | Username for SSH login|
| -w, --wordlist    | optional     | Path to the wordlist file for dictionary attack |
| --min| optional | Minimum length of the password (for brute force)|
| --max| optional | Maximum length of the password (for brute force)|
| -c, --charset | optional | Chartset for brute force |

Example: Brute force using a wordlist:

```
  python main.py -u <test_user> -s <ip_address> -w <path_to_wordlist_txt>
```
Example: Brute force passwords based on the specified charset and length:

```
python main.py -u <test_user> -s <ip_address> --min 3 --max 3 -c abc
```

> **_NOTE:_** Use a short password, max 3 characters in lenght. If you use a large charset or a big length range, brute-forcing can take a very long time! For testing, keep the charset and length small.
