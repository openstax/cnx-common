# -*- coding: utf-8 -*-
import re

from slugify import slugify


def generate_slug(title):
    """Given a book/page title,
    generates a URL slug.

    GIVEN "1.1 The Science of Biology"
    RETURNS  "1-1-the-science-of-biology"
    """
    title = re.sub(r"<.*?>", "", title)  # remove html tags
    return slugify(title)
