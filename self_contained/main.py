import argparse
import markovify
import pkgutil
import json


def main():
    parser = argparse.ArgumentParser(description='Generate sentences from a Markov model')
    parser.add_argument('--length', '-l', help='max output character length', type=int, default=140)
    args = parser.parse_args()

    model = markovify.Text.from_json(pkgutil.get_data('self_contained', 'model.json').decode('utf-8'))
    print(model.make_short_sentence(args.length))


if __name__ == '__main__':
    main()
