import sys


# Print iterations progress
def print_progress_line(iteration, prefix='', bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    # format_str = "{0:." + str(decimals) + "f}"
    # percents = format_str.format(100 * (iteration / float(total)))

    # bar_length = global_display.columns
    filled_length = int(round(bar_length * iteration / float(total)))
    # sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix))
    global_display.display('\r{0} |{1}{2}|'.format(prefix, '#' * filled_length, '-' * (bar_length - filled_length)))
    if iteration == total:
        global_display.display.write('\n')
        # sys.stdout.flush()


def print_progress():
    bar_length = global_display.columns
    i = 0
    while True:
        print_progress_line(i, prefix='Running:', bar_length=50)
        if i == 100:
            i = 0
        else:
            i += 1
