import os, sys, subprocess

proc = subprocess.Popen(
        ['echo', 'greetings from the child process.'],
        stdout = subprocess.PIPE)

out, err = proc.communicate()
print(out.decode('utf-8'))
print("subprocess.pid: {}".format(proc.pid))

proc = subprocess.Popen(
        ['sleep', '0.3'], )
counter = 0
while proc.poll() is None:
    print('working ... pid = {}'.format(proc.pid))
    ## TODO
    counter += 1
    if counter > 10:
        print('exit the loop')
        break

print('Exit status ', proc.poll())
