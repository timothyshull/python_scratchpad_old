import os


def get_files_recursively(root):
    all_files = []
    for (thisdir, subshere, fileshere) in os.walk(root):
        for fname in fileshere:
            all_files.append(os.path.join(thisdir, fname))
    return all_files


if __name__ == '__main__':
    dir_to_use = os.getcwd()
    af = get_files_recursively(dir_to_use)
    af = ['{0}/{1}'.format(dir_to_use.rstrip('/'), os.path.basename(elem)) for elem in af]
    print(',\n'.join(af))
