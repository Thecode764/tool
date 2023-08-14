import os
import sys
print("SELECT TOOL")
print("1(make folders")
print("2(delete folders")
print("3(Install Apps")
print("4(Tmux") 
print("5(get system info")
print("6(get system name")
print("7(Create File with vscode")
print("8(Install Windows Powershell")
print("9(Install Zsh and Oh My Zsh")
print("10(Install Katoolin")
tool = input("Select tool number:")
if tool == "1":
    folder = input("Enter Folder Name:")
    os.mkdir(folder)
if tool == "2":
    rmdirfolder = input("Enter Folder Name:")
    os.rmdir(rmdirfolder)
if tool == "3":
    installapp = input("Enter Command For Install:")
    os.system(installapp)
if tool == "4":
    os.system("tmux")
if tool == "5":
    print(os.uname())
if tool == "6":
    print(sys.platform)
if tool == "7":
    print("Set programing languages")
    print("1(python")
    print("2(ruby")
    print("3(perl")
    print("4(java")
    print("5(php")
    print("6(C#")
    print("7(Dart")
    print("8(js")
    print("9(C++")
    print("10(html")
    print("11(css")
    print("12(json")
    program = input("Enter Number For programing:")
    if program == "1":
        os.system("code main.py")
    if program == "2":
        os.system("code main.ruby")
    if program == "3":
        os.system("code main.perl")
    if program == "4":
        os.system("code index.java")
    if program == "5":
        os.system("code index.php")
    if program == "6":
        os.system("code main.cs")
    if program == "7":
        os.system("code index.dart")
    if program == "8":
        os.system("code idnex.js")
    if program == "9":
        os.system("code main.cpp")
    if program == "10":
        os.system("code index.html")
    if program == "11":
        os.system("code style.css")
    if program == "12":
        os.system("code main.json")
if tool == "8":
    os.system("sudo snap install powershell --classic")
    os.system("powershell")
if tool == "9":
    os.system("sudo apt-get install zsh")
    os.system("wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh")
if tool == "10":
    os.system("sudo python2 katoolin.py")
