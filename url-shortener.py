import pyshorteners

link = input("Your Link : ")
shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)
print(x)