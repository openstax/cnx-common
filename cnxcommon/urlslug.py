# -*- coding: utf-8 -*-
import re

from unidecode import unidecode


def generate_slug(title):
    """Given a book/page title,
    generates a URL slug.

    GIVEN "1.1 The Science of Biology"
    RETURNS  "1-1-the-science-of-biology"
    """
    section_number = extract_section_number(title)
    title = split_parts(title)[1].strip().lower()

    title = re.sub(r"<.*?>", "", title)  # remove html tags
    import html  # PY3
    # unescape html chars like '&amp;' becomes '&'
    title = html.unescape(title)

    title = unidecode(title)  # replace unicode chars with ascii equivalents

    title = re.sub(r'[^a-z0-9 ]', ' ', title)  # remove special characters
    title = re.sub(r' +', '-', title)  # spaces to dashes
    title = title.strip("-")  # remove trailing dashes

    slug = f"{section_number}-{title}" if section_number else f"{title}"
    return slug


def extract_section_number(complete_title):
    section_number = split_parts(complete_title)[0]
    # use dash instead of '.'
    section_number = re.sub(r'\.', '-', section_number)

    return section_number


def split_parts(complete_title):
    from copy import copy
    title = copy(complete_title)
    matches = re.findall(r'^([0-9\.]*)?(.*)$', title)

    section_number = matches[0][0]
    title = matches[0][1]

    return [section_number, title]
