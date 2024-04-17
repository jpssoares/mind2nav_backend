import pywinctl as gw
import pyautogui

def get_chrome_window_title():
    window_titles = gw.getAllTitles()
    print(window_titles)
    for t in window_titles:
        names = t.split(" ")
        if 'Google' in names and 'Chrome' in names:
            index_a = names.index('Google')
            index_b = names.index('Chrome')
            if abs(index_a - index_b) == 1:
                return t 
    return None
def screenshot_current_chrome_window():

    window_title = get_chrome_window_title()
    print(window_title)
    if not window_title:
        print("No active Google Chrome window found.")
        return
    chrome_window = gw.getWindowsWithTitle(window_title)[0]
    print(chrome_window)
    chrome_window.activate()
    screenshot = pyautogui.screenshot(region=(chrome_window.left, chrome_window.top, chrome_window.width, chrome_window.height))
    screenshot.save("screenshot.png")

screenshot_current_chrome_window()
