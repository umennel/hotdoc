#!/usr/bin/env python

import argparse
import sys

import jinja2
import markdown
from importlib.resources import open_text


def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    parser.add_argument('-t', '--template', type=argparse.FileType('r'),
                        default=open_text('mddoc', 'default.html'),
                        help='HTML Template.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensions = ['extra', 'attr_list', 'tables']
    content = markdown.markdown(md, extensions=extensions, output_format='html5')
    html = jinja2.Template(args.template.read()).render(content=content)
    args.out.write(html)


if __name__ == '__main__':
    sys.exit(main())
