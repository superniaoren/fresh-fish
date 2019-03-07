import os, sys, time, subprocess

def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

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

print('-' * 60)
start = time.time()
procs = []

for i in range(10):
    proc = run_sleep(i * 0.01)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time.time()
print("finish the proc list in %3.f secs" % (end - start))
