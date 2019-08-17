#!/usr/bin/python3.6
import gi
import os
import getpass
import keyboard
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2

#Defining variables
dir = os.path.dirname(os.path.abspath(__file__))
usr = getpass.getuser()
window = Gtk.Window()
headbar = Gtk.HeaderBar()
webview = WebKit2.WebView()
window.set_title("Velvet Browser")
scrolled_window = Gtk.ScrolledWindow()
entry = Gtk.Entry()
headbar.set_custom_title(entry)

#Back/Forward buttons

def on_go_back(self):
    webview.go_back()

def on_go_forward(self):
    webview.go_forward()

go_back_button = Gtk.Button()
go_back_arrow = Gtk.Image.new_from_icon_name("go-previous", Gtk.IconSize.SMALL_TOOLBAR)
go_back_button.add(go_back_arrow)
go_back_button.connect("clicked", on_go_back)

go_forward_button = Gtk.Button()
go_forward_arrow = Gtk.Image.new_from_icon_name("go-next", Gtk.IconSize.SMALL_TOOLBAR)
go_forward_button.add(go_forward_arrow)
go_forward_button.connect("clicked", on_go_forward)



def on_reload(self):
        webview.reload()

def on_history(self):
        webview.load_uri(f"file:///{dir}/history.html")

def on_destroy(window):
    Gtk.main_quit()

def on_enter(entry):
    url = webview.get_uri()
    entry_uri = entry.get_text()
    print(url)
    webview.load_uri(f"https://{entry_uri}")
    with open(f"{dir}/history.html", 'a') as history:
                history.write("* <a href=\"" + url + "\">" + url + "</a><br>")
    if (entry_uri == "about:history"):
        webview.load_uri(f"file:///{dir}/history.html")
        return

entry.connect("activate", on_enter)

history_button = Gtk.Button()
history_icon = Gtk.Image.new_from_icon_name("weather-fog", Gtk.IconSize.SMALL_TOOLBAR)
history_button.add(history_icon)
history_button.connect("clicked", on_history)

reload_button = Gtk.Button()
reload_icon = Gtk.Image.new_from_icon_name("object-rotate-left", Gtk.IconSize.SMALL_TOOLBAR)
reload_button.add(reload_icon)
reload_button.connect("clicked", on_reload)

#Buttons
headbar.pack_start(go_back_button)
headbar.pack_start(go_forward_button)
headbar.pack_start(reload_button)
headbar.pack_start(history_button)
#window
scrolled_window.add(webview)
headbar.set_show_close_button(True)
window.set_titlebar(headbar)
window.set_default_size(1000,600)
window.add(scrolled_window)
#webview

webview.load_uri("https://www.duckduckgo.com")
#window
window.connect("destroy", on_destroy)
window.show_all()
Gtk.main()
