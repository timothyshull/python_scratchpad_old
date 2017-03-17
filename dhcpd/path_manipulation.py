import os
import sys
import argparse

GLOBAL_DEFAULT_DIR = '/Users/test_user/Documents'


def main():
    global GLOBAL_DEFAULT_DIR
    # print(sys.argv)
    parser = argparse.ArgumentParser(description='Gets the directory to use.')
    parser.add_argument('--directory_to_use')
    parser.add_argument('--another_argument')
    # if not len(sys.argv) >= 2:
    #     dir_to_use = GLOBAL_DEFAULT_DIR
    # else:
    #     dir_to_use = sys.argv[1]
    input_args = vars(parser.parse_args(sys.argv[1:]))
    if input_args.get('directory_to_use'):
        dir_to_use = input_args.get('directory_to_use')
    else:
        dir_to_use = GLOBAL_DEFAULT_DIR
    print(dir_to_use)
    print(os.path.dirname(dir_to_use))
    print(os.path.basename(dir_to_use))
    print(os.path.join(dir_to_use, 'fake_file.txt'))
    print(os.path.dirname(argparse.__file__))


if __name__ == '__main__':
    main()
