# 鼠标操作模块
import pyautogui
# 复制模块
import pyperclip
# 时间模块
import time
# 现实时间模块
import datetime


for i in range(3):
# 打开微信
    def openWeChat():
        pyautogui.hotkey("ctrl" , "alt" , "w")

    # 搜索微信联系人
    def chatname(name):
        pyautogui.hotkey("ctrl" , "f")
        pyperclip.copy(name)
        pyautogui.hotkey("ctrl" , "v")
        time.sleep(1)
        pyautogui.hotkey("return")


    # 发送内容
    def message(msg):
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl" , "v")
        pyautogui.hotkey("return")

    # 批量发内容
    """def message_in_bulk(name):
        openWeChat()
        for i in name:
            chatname(i)
            time.sleep(1)
            message("测试东西 不用回复")"""


    openWeChat()
    chatname("韦昱丞")
    message("sb")