import argparse
import html
import markovify
import json
import re


TAG_REGEX = re.compile(r'(<!--.*?-->|<[^>]*>)')


def write_post_corpus(posts, output):
    post_contents = '\n'.join([html.unescape(TAG_REGEX.sub('', p['history'][0]['content']).replace('#pin', '')) for p in posts])
    with open(output, 'w') as fp:
        for line in post_contents.split('\n'):
            line = line.strip()
            if line and len(line) > 0:
                if line[-1] not in '.!?':
                    line += '.'
                fp.write(line + '\n')


def main():
    parser = argparse.ArgumentParser(
        description='Builds a corpus from a JSON file of Piazza posts.')
    parser.add_argument('--posts', '-p', help='path to file with Piazza posts', required=True)
    parser.add_argument('--output', '-o', help='output corpus path', required=True)
    args = parser.parse_args()

    posts = json.load(open(args.posts, 'r'))
    write_post_corpus(posts, args.output)


if __name__ == '__main__':
    main()
