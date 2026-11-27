import flet as ft
from flet_webview import WebView


def ttit(page: ft.Page):
    page.add(WebView(url="https://ttit-journal.duckdns.org/", expand=True))


ft.run(ttit)
