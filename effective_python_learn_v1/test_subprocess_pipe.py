import os, sys, subprocess

def run_openssl(data):
    env = os.environ.copy()
    env['passwd'] = 'hello'
    proc = subprocess.Popen(
            ['openssl', 'enc', '-des3', '-pass', 'env:passwd'],
            env = env,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

def run_md5(data):
    proc = subprocess.Popen(
            ['md5'],
            stdin = data,
            stdout = subprocess.PIPE)
    return proc

## main body

if __name__ == '__main__':
    print(__name__)
    
    procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        procs.append(proc)

    for proc in procs:
        out, err = proc.communicate()
        print("pid = {}".format(proc.pid))
        print(out[-10 : ])
