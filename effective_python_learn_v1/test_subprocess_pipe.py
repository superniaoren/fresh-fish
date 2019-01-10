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
            ['md5sum'],
            stdin = data,
            stdout = subprocess.PIPE)
    return proc

## main body

if __name__ == '__main__':
    print(__name__)
    
    ssl_procs = []
    md5_procs = []
    for _ in range(3):
        data = os.urandom(10)
        ssl_proc = run_openssl(data)
        ssl_procs.append(ssl_proc)
        # [zoo] here establish the connection
        md5_proc = run_md5(ssl_proc.stdout)
        md5_procs.append(md5_proc)

    for proc in ssl_procs:
        out, err = proc.communicate()
        print("pid = {}".format(proc.pid))
        print(out[-10 : ])
    for proc in md5_procs:
        out, err = proc.communicate()
        print(out.strip())
