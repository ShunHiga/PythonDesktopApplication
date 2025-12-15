import pyperclip
import FreeSimpleGUI as sg

#文字列をコピー
pyperclip.copy("コピーaaしたい文言を入力しました")

#コピーした文字列を取得して画面に表示する
text = pyperclip.paste()
sg.popup(text, title="クリップボードから取得しました")