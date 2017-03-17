import os
import glob


def get_most_recently_modified(file_list):
    assert (len(file_list))
    file_list = [elem for elem in file_list if os.path.isfile(elem)]
    file_list.sort(key=os.path.getmtime, reverse=True)
    return file_list[0]

if __name__ == '__main__':
    cdir = os.path.dirname(os.path.abspath(__file__))
    all_files = glob.glob('{0}/*'.format(cdir))
    recent_mod = get_most_recently_modified(all_files)
    print(recent_mod)
