# -*- coding: utf-8 -*-
"""
# Copyright (c) 2019, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
"""
import re

import pytest

from cnxcommon.urlslug import generate_slug

class TestSlugGenerator:
    def test_it_removes_html_tags(self):
        title = "<span class=\"os-number\"></span><span>sometext</span>"
        expected = "sometext"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_removes_special_chars(self):
        title = "@#$*(&sometext!!!"

        expected = "sometext"
        actual = generate_slug(title)

        assert re.match(r'^\W+$', actual) is None
        assert expected == actual

    def test_it_replaces_special_chars_btwn_text_with_dashes(self):
        title = "@#$*(&some!!!text!!!"

        expected = "some-text"
        actual = generate_slug(title)

        assert re.match(r'^\W+$', actual) is None
        assert expected == actual

    def test_it_replaces_spaces_with_dashes(self):
        title = "some text and     a    bunch      of     spaces    "
        expected = "some-text-and-a-bunch-of-spaces"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_makes_all_lowercase(self):
        title = "SomeTEXT"
        expected = "sometext"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_replaces_unicode_chars_w_their_ascii_equivalent(self):
        title = "podręcznikfizykadlaszkółwyższych"
        expected = "podrecznikfizykadlaszkolwyzszych"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_can_identify_chapter_and_section_numbers(self):
        title = "12.4 sometext"
        expected = "12-4-sometext"
        actual = generate_slug(title)

        assert expected == actual

    def test_with_only_chapter_number_not_section(self):
        title = "1 introduction"
        expected = "1-introduction"
        actual = generate_slug(title)

        assert expected == actual

    def test_using_generate_slug(self):
        title = "12.4 sometext"
        expected = "12-4-sometext"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_removes_trailing_slashes(self):
        title = "-12.4 some-text--"
        expected = "12-4-some-text"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_removes_html_encoded_chars(self):
        title = "12.4 sometext&amp;moretext"
        expected = "12-4-sometext-moretext"
        actual = generate_slug(title)

        assert expected == actual

    def test_it_can_identify_chapter_num_when_not_in_section_title(self):
        """If the chapter number isn't present in the section title,
        it can find it in the chapter title instead.
        """
        book_title = "college-physics"
        chapter_title = "1 Introduction: The Nature of Science and Physics"
        section_title = "problems-and-exercises"
        expected = "1-problems-and-exercises"
        actual = generate_slug(book_title, chapter_title=chapter_title, section_title=section_title)

        assert expected == actual[1]

    def test_when_chapter_number_not_present_in_section_nor_chapter_titles(self):
        """What happens when (or if) a chapter number is not present in the chapter
        title nor the section title.
        """
        book_title = "college-physics"
        chapter_title = "Introduction: The Nature of Science and Physics"
        section_title = "problems-and-exercises"
        expected = "problems-and-exercises"
        actual = generate_slug(
            book_title, chapter_title=chapter_title, section_title=section_title)

        assert expected == actual[1]

    def test_slug_generator_integration_test(self):
        """Integration-level test using the Acceptance Criteria described in:
        https://github.com/openstax/cnx/issues/348
        """
        books = [
            (
                'College Physics',
                '<span class="os-number">12.4</span><span class="os-divider"> </span><span class="os-text">Viscosity and Laminar Flow; Poiseuille\'s Law< /span >',
                '<span class="os-number">12</span><span class="os-divider"> </span><span class="os-text">Fluid Dynamics and Its Biological and Medical Applications</span>',
            ), (
                'College Physics',
                '<span class="os-text">Problems &amp; Exercises</span>',
                '<span class="os-number">1</span><span class="os-divider"> </span><span class="os-text">Introduction: The Nature of Science and Physics</span>',
            ), (
                'Biology 2e',
                '<span class="os-number">1.1</span><span class="os-divider"> </span><span class="os-text">The Science of Biology</span>',
                '<span class="os-number">1</span><span class="os-divider"> </span><span class="os-text">The Study of Life</span>',
            ), (
                'Biology 2e',
                '<span class="os-text">Preface</span>',
            ),
        ]

        expectations = [
            ('college-physics', '12-4-viscosity-and-laminar-flow-poiseuille-s-law'),
            ('college-physics', '1-problems-exercises'),
            ('biology-2e', '1-1-the-science-of-biology'),
            ('biology-2e', 'preface')
        ]

        for index, book in enumerate(books):
            assert expectations[index] == generate_slug(*book)
