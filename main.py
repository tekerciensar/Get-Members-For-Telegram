import os
os.system("clear")
class ModulDenetleme:
    def indir(self, modul):
        os.system(f"pip install {modul}")
        os.system("clear")

    def kontrol(self, modul):
        try:
            __import__(modul)
        except ImportError:
            self.indir(modul)

    def __init__(self):
        gerekli_moduller = ["telethon","rich"]
        for gerekli_modul in gerekli_moduller:
            self.kontrol(gerekli_modul)
ModulDenetleme()

import time
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest
from rich.console import Console
from rich.panel import Panel
console = Console()
os.system("clear")
logo=Panel("""
[bold yellow]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

[bold purple]____  ______ _      ______  _____   _    ___     ________
|  _ \|  ____| |    |  ____|/ ____| | |  | \ \   / /  ____|
| |_) | |__  | |    | |__  | (___   | |  | |\ \_/ /| |__
|  _ <|  __| | |    |  __|  \___ \  | |  | | \   / |  __|
| |_) | |____| |____| |____ ____) | | |__| |  | |  | |____
|____/|______|______|______|_____/   \____/   |_|  |______|

[bold yellow]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

           [bold green]        < [bold purple]Üye Çekme Tool [bold green]>
            [bold green]    < [bold purple]@Tyrafi @TyrafiPython [bold green]>""",style="bold purple",border_style="bold blue")

console.print(logo)

info = Panel("[bold yellow]Sadece Gruptan Gruba Üye Çekebilirsiniz Telegram: [bold red]@Tyrafi",border_style="bold blue")

console.print(info)

import webbrowser

kullanim = ""
uyari = Panel("[bold red] Lütfen Kullandığınız Platformu Giriniz :\n\n1 - Python Ide\n2 - Termux",border_style="bold blue")
try:
    uyarii = int(console.input(uyari))
except:
    info = Panel("[bold red] Lütfen Yalnızca Değer Giriniz ",border_style="bold blue")
    console.print(info)
if uyarii == 1:
    kullanim+="ide"
elif uyarii == 2:
    kullanim+="termux"
else:
    console.print(Panel("[bold red] Lütfen Geçerli Bir Sayı Giriniz",border_style="bold blue"))
    exit()
if kullanim == "ide":
    webbrowser.open("https://t.me/TyrafiPython")
elif kullanim == "termux":
    os.system("termux-open-url https://t.me/TyrafiPython")
else:
    exit()
os.system("clear")
console.print(logo)
console.print(info)
input1 = Panel("[bold red]Telegram Api ID' Nizi Giriniz: ",border_style="bold blue")
input2 = Panel("[bold red]Telegram Api HASH'ınızı Giriniz: ",border_style="bold blue")
input3 = Panel("[bold red]Telegram Telefon Numaranızı Giriniz: ",border_style="bold blue")
try:
    api_id = int(console.input(input1))
except:
    info = Panel("[bold red] Lütfen Yalnızca Değer Giriniz ",border_style="bold blue")
    console.print(info)
    exit()
api_hash = console.input(input2)
phone_number = console.input(input3)
os.system("clear")
console.print(logo)
with console.status("Araç Kuruluyor Lütfen Bekleyin..",spinner="point"):
    time.sleep(1)

try:
    client = TelegramClient('scraper', api_id, api_hash)
    client.start(phone_number)
    info1 = Panel("[bold red]Telegram Hesabınıza Giriş Yapıldı ",border_style="bold blue")
    console.print(info1)
except:
    info1 = Panel("[bold red]Telegram Hesabınıza Giriş Yapılmadı Lütfen Aracı Tekrar Başlatıp Deneyin!",border_style="bold blue")
    console.print(info1)
    exit()
os.system("clear")
console.print(logo)
console.print(info)
info2 = Panel("[bold red] Gireceğiniz Grup Adlarının Başında '@' Olmamalıdır",border_style="bold blue")
console.print(info2)
input1 = Panel("[bold red]Üyeleri Çekmek İstediğiniz Grup Adını Giriniz: ",border_style="bold blue")
input2 = Panel("[bold red]Üyeleri Yerleştirmek İstediğiniz Grup Adını Giriniz: ",border_style="bold blue")
from_group_name = console.input(input1)
to_group_name = console.input(input2)
from_group = client.get_entity(from_group_name)
to_group = client.get_entity(to_group_name)

members = []
for member in client.iter_participants(from_group):
    members.append(member)
os.system("clear")
console.print(logo)
console.print(info)
time.sleep(0.8)
console.print(Panel("[bold red]Üyeler Bulundu",border_style="bold blue"))
time.sleep(1)
console.print(Panel("[bold red]Gruba Ekleniyor",border_style="bold blue"))
for member in members:
    try:
        client(InviteToChannelRequest(to_group,[member]))
        info3 = Panel(f"[bold red]{member.username} Grubunuza Eklendi",border_style="bold blue")
        console.print(info3)
    except PeerFloodError:
        info6 = Panel("[bold red]Telegram Hesabınız Maksimum Davet Etme Sınırına Ulaştı Engellenmemek İçin Programı 1 Saat Boyunca Açmayınız",border_style="bold blue")
        exit()
    except Exception as hata:
        infoo = Panel(f"[bold red]Kullanıcı {member.username} Gruba Eklenirken {hata} Adlı Sorun Oluştu",border_style="bold blue")
        console.print(infoo)
        
client.disconnect()
