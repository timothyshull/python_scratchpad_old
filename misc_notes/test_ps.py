import os


def exit_if_duplicate_process():
    curr_pid = str(os.getpid())
    curr_file = os.path.basename(__file__)

    pids = [pid for pid in os.listdir('/proc') if (pid.isdigit() and pid.strip() != curr_pid)]

    proc_cmdlines = []
    for pid in pids:
        try:
            proc_cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if curr_file in proc_cmd:
                proc_cmdlines.append(proc_cmd)
        except IOError:
            continue

    if proc_cmdlines:
        exit(0)
