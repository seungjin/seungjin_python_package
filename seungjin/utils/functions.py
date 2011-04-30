
run_cmd = lambda c : subprocess.Popen(c.split(), stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=False).stdout.read()
