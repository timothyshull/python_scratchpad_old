import os
import shutil


def merge_tree(src, dest):
    src = src.rstrip('/')
    dest = dest.rstrip('/')
    src_len = len(src) + 1  # to account for trailing /
    for (current_dir, current_subs, current_files) in os.walk(src):

        if current_dir != src:
            dir_fragment = current_dir[src_len:].rstrip('/')
            dest_dir = '{0}/{1}'.format(dest, dir_fragment)
        else:
            dest_dir = dest

        if not os.path.isdir(dest_dir):
            try:
                os.makedirs(dest_dir)
            except EnvironmentError:
                print('Unable to create the directory {0}.'.format(dest_dir))

        for f in current_files:
            src_file = '{0}/{1}'.format(current_dir, f)
            dest_file = '{0}/{1}'.format(dest_dir, f)

            if not os.path.exists(dest_file):
                try:
                    shutil.copy2(src_file, dest_file)
                except (TypeError, ValueError, EnvironmentError) as e:
                    print('Unable to copy {0} to {1}: {2}'.format(src_file, dest_file, e.message))


if __name__ == '__main__':
    merge_tree('/Users/test_user/Documents/Java', '/Users/test_user/Documents/tmp')
