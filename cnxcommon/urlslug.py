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
    if chapter_title and not section_title:
        """The chapter title is ONLY used for generating a complete section title,
        so just the chapter title is useless, please check for mistakes.
        """
        return (None, None)

    book_title = slugify(remove_html_tags(book_title))

    # allow generating a slug when only one argument is passed-in, essentially.
    if not section_title :
        return book_title

    section_title = slugify(remove_html_tags(section_title))
    if re.match(r"^\d", section_title):  # if section title starts with a digit
        pass  # we already know the chapter number
    else:  # prepend the chapter number to the section title
        chapter_title = remove_html_tags(chapter_title)
        # find chapter number in chapter title
        chapter_number = re.split(r"^([0-9\.]*)?(.*)$", chapter_title)[1]
        # update section title with the chapter number, only if found.
        section_title = f"{chapter_number}-{section_title}" if chapter_number else f"{section_title}"

    return (book_title, section_title)


def remove_html_tags(title):
    return re.sub(r"<.*?>", "", title)
