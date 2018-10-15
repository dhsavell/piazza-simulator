import argparse
import markovify
import json


def main():
    parser = argparse.ArgumentParser(description='Generate sentences from a Markov model')
    parser.add_argument('--model', '-m', help='file path of Markov chain model', required=True)
    parser.add_argument('--length', '-l', help='max output character length', type=int, default=140)
    args = parser.parse_args()

    model = markovify.Text.from_json(open(args.model, 'r').read())
    print(model.make_short_sentence(args.length))


if __name__ == '__main__':
    main()
