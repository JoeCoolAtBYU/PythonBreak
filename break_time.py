import webbrowser
import time

count = 0
while (count < 5):
  time.sleep(1)
  webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
  count = count + 1
