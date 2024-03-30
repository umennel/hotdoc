#!/usr/bin/env python

import argparse
import asyncio
import os
from pathlib import Path
import json
import jinja2
import yaml
from yaml.loader import SafeLoader
import pyppeteer

from .htmlutils import inline_css


def parse_context(file):
    _, ext = os.path.splitext(file.name)
    match ext.lower():
        case (".yml"|".yaml"):
            return yaml.load(file, Loader=SafeLoader)
        case ".json":
            return json.load(file)
        case _:
            raise NotImplementedError(f"unknown file format: {ext}")


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Make a complete, styled HTML document from a Markdown file.')
    parser.add_argument('-c', '--context', type=argparse.FileType('r'), action='append',
                        help='File which stores context. Supported file formats: YAML, JSON')
    parser.add_argument('-o', '--out', type=Path, required=True,
                        help='Output file name. Defaults to stdout.')
    parser.add_argument('-t', '--template', type=argparse.FileType('r'), required=True,
                        help='HTML Template.')
    parser.add_argument('--css', type=argparse.FileType('r'), action='append',
                        help='Apply CSS stylesheet')
    return parser.parse_args(args)


def render(template, context: dict):
    html = jinja2.Template(template).render(**context)
    return inline_css(html)


def main(args=None):
    args = parse_args(args)
    template = args.template.read()
    context = { k: v for f in args.context for k, v in parse_context(f).items() }
    html = render(template, context)
    

def write(html: str, output_path: Path):
    _, ext = os.path.splitext(output_path)
    match ext.lower():
        case (".htm"|".html"):
            with open(output_path, 'w') as f:
                f.write(html)
        case ".pdf":
            asyncio.run(html2pdf(html, output_path))
        case _:
            raise NotImplementedError(f"unknown file format: {ext}")

async def html2pdf(html, output_path: Path):
    browser = await pyppeteer.launch(headless=True, executablePath='/usr/bin/chromium-browser', args=["--no-sandbox"])
    page = await browser.newPage()

    await page.setContent(html)
    page_margins = {"left": "1cm", "right": "1cm", "top": "1cm", "bottom": "1cm"}
    await page.pdf({'path': output_path, 'format': 'A4', 'margin': page_margins, "printBackground": True})
    await browser.close()


if __name__ == '__main__':
    main()
