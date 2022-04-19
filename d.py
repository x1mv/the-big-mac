
import urllib.request

mac = urllib.request.urlopen("https://x1mv.github.io/")
byte = mac.read()

decoded = byte.decode("utf8")
mac.close()

print(decoded[4:-5], "<-- Now that i think of it, holy shit thats a fucking expensive burger dude")



