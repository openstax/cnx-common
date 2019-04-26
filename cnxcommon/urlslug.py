# -*- coding: utf-8 -*-
import re

from slugify import slugify


def generate_slug(book_title, section_title="", chapter_title=""):
    """Given a book title, a section title, and a chapter title
    generates slugs for the book title and the section title.

    GIVEN just the book title
    book_title = "1.1 The Science of Biology"
    RETURNS
     "1-1-the-science-of-biology"

    GIVEN
    book_title = "College Physics"
    section_title = "1.1 The Science of Biology"
    RETURNS a tuple
     ("college-physics", "1-1-the-science-of-biology")

     GIVEN
     book_title = "College Physics"
     chapter_title = "1 Introduction: The Nature of Science and Physics"
     section_title = "Problems &amp; Exercises"
     RETURNS a tuple
     ("college-physics", "1-problems-and-exercises")

     NOTE that the chapter title is only used to determine the chapter number
     in case it is missing from the section title like for "Introduction" sections.
    """
    book_title_slug = slugify(remove_html_tags(book_title))
    if not section_title:
        return book_title_slug

    section_title_slug = slugify(remove_html_tags(section_title))

    if re.match(r"^\d", section_title):  # if section title starts with a digit
        pass  # we already know the chapter number
    else:  # prepend the chapter number to the section title
        chapter_title = remove_html_tags(chapter_title)
        chapter_number = re.split(r"^([0-9\.]*)?(.*)$", chapter_title)[1]
        section_title_slug = f"{chapter_number}-{section_title}"

    return (book_title_slug, section_title_slug)


def remove_html_tags(title):
    return re.sub(r"<.*?>", "", title)
