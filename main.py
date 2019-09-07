#!/usr/bin/python3.6
import gi
import os
import getpass
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2

class Velvet():
      
        def __init__(self):
                #Defining variables
                self.window = Gtk.Window()
                self.headbar = Gtk.HeaderBar()
                self.webview = WebKit2.WebView()
                self.window.set_title("Velvet Browser")
                self.scrolled_window = Gtk.ScrolledWindow()
                self.directory = os.path.dirname(os.path.abspath(__file__))
                self.url = self.webview.get_uri()
                self.entry = Gtk.Entry()
                self.headbar.set_custom_title(self.entry)
                self.go_back_button = Gtk.Button()
                self.go_back_arrow = Gtk.Image.new_from_file("go_back.png")
                self.go_back_button.add(self.go_back_arrow)
                self.go_back_button.connect("clicked", self.on_go_back)
                self.go_forward_button = Gtk.Button()
                self.go_forward_arrow = Gtk.Image.new_from_file("go_forward.png")
                self.go_forward_button.add(self.go_forward_arrow)
                self.go_forward_button.connect("clicked", self.on_go_forward)
                self.entry.connect("activate", self.on_enter)
                self.entry.set_size_request(500,50)

                

                self.reload_button = Gtk.Button()
                self.reload_icon = Gtk.Image.new_from_file("on_reload.png")
                self.reload_button.add(self.reload_icon)
                self.reload_button.connect("clicked", self.on_reload)

                #Buttons
                self.headbar.pack_start(self.go_back_button)
                self.headbar.pack_start(self.go_forward_button)
                self.headbar.pack_start(self.reload_button)
 
                #window
                self.scrolled_window.add(self.webview)
                self.headbar.set_show_close_button(True)
                self.window.set_titlebar(self.headbar)
                self.window.set_default_size(1000,600)
                self.window.add(self.scrolled_window)
                #webview

                self.webview.load_uri("https://duckduckgo.com")
                url = self.webview.get_uri()
                self.entry.set_text(url)
                #window
                self.window.connect("destroy", self.on_destroy)
                self.window.show_all()
                Gtk.main()
        
        #Back/Forward buttons
        def on_history(self, webview):
                directory = os.path.dirname(os.path.abspath(__file__))
                self.webview.load_uri(f"file:///{directory}/history.html")

        def on_go_back(self, webview):
                self.webview.go_back()
                url = self.webview.get_uri()
                self.entry.set_text(url)

        def on_go_forward(self, webview):
                self.webview.go_forward()
                url = self.webview.get_uri()
                self.entry.set_text(url)

        def on_reload(self, webview):
                self.webview.reload()
                url = self.webview.get_uri()
                self.entry.set_text(url)

        def on_destroy(self, window):
                Gtk.main_quit()

        def on_enter(self, entry):
                entry_uri = self.entry.get_text()
                url = self.webview.get_uri()
                directory = os.path.dirname(os.path.abspath(__file__))
                print(url)
                with open(f"{directory}/history.html", 'a') as history:
                        history.write("* <a href=\"" + url + "\">" + url + "</a><br>")
                if entry_uri.startswith('http://') or entry_uri.startswith('https://'):
                        self.webview.load_uri(entry_uri)
                elif (entry_uri == "about:history"):
                        self.webview.load_uri(f"file:///{directory}/history.html")
                        return
                else:
                        entry_uri = f'https://{entry_uri}'
                        self.entry.set_text(entry_uri)
                        self.webview.load_uri(entry_uri)


run = Velvet()