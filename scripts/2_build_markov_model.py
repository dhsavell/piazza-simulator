import argparse
import markovify


def main():
    parser = argparse.ArgumentParser(description='generate a markov chain model from a corpus of text')
    parser.add_argument('--corpus', '-c', help='corpus file path', required=True)
    parser.add_argument('--output', '-o', help='output model path', required=True)
    args = parser.parse_args()

    with open(args.corpus, 'r') as fp:
        corpus = fp.read()

    model = markovify.Text(corpus)

    with open(args.output, 'w') as fp:
        fp.write(model.to_json())


if __name__ == '__main__':
    main()