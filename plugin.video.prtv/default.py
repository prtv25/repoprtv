# -*- coding: utf-8 -*-
import xbmcplugin, xbmcgui, sys, requests

url = "https://pastebin.com/raw/F92vXYgR"  # URL principal da lista

def listar():
    r = requests.get(url)
    linhas = r.text.splitlines()
    for linha in linhas:
        if linha.strip():
            nome, link = linha.split(",")
            li = xbmcgui.ListItem(label=nome)
            li.setInfo("video", {"title": nome})
            xbmcplugin.addDirectoryItem(int(sys.argv[1]), link, li, False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    listar()
