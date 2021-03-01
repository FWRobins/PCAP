import subprocess

host = "8.8.8.8"
numberOfPings = "4"


ping = subprocess.Popen(
    ["ping", "-n", numberOfPings, host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
out = str(out)[1:].replace(r"\r\n", "\n")
##for i in out:
##    print(out)
print(out)

