from sys import stdin
import argparse
from email import policy
from email.parser import BytesParser
from nltk.tokenize import sent_tokenize
from langdetect import detect
import langdetect


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--language', help='Video file name.', default='czech')
    args = parser.parse_args()
    return args


def main(args):
    for file_name in stdin.readlines():
        with open(file_name.strip(), 'rb') as f:
            message = BytesParser(policy=policy.default).parse(f)
        text = message.get_body(preferencelist=('plain')).get_content()
        text = text
        sentences = sent_tokenize(text)
        for sent in sentences:
            try:
                if detect(sent) == 'cs' and not '/' in sent and '>' not in sent:
                    print(' '.join(sent.split()))
            except langdetect.lang_detect_exception.LangDetectException:
                pass


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
