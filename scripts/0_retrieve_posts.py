import argparse
import json

from piazza_api import Piazza


def write_all_posts(network, dest_filename):
    posts = [post for post in network.iter_all_posts()]
    with open(dest_filename, 'w') as fp:
        json.dump(posts, fp)


def main():
    parser = argparse.ArgumentParser(description='Retrieve Piazza posts and answers in JSON format.')
    parser.add_argument('--networkid', '-n', help='piazza network ID', required=True)
    parser.add_argument('--output', '-o', help='output filename', required=True)
    args = parser.parse_args()

    piazza = Piazza()
    print('Login to Piazza:')
    piazza.user_login()

    network = piazza.network(args.networkid)
    write_all_posts(network, args.output)


if __name__ == '__main__':
    main()