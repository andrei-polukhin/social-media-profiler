# -*- coding: utf-8 -*-

import unittest
from app.backend.analyzing.substring_match.find_similarity_ratio import find_similarity_ratio


class TestSimilarityRatio(unittest.TestCase):
    def test_assure_similarity(self):
        real_similarity = find_similarity_ratio(
            "Institute of Mathematics trains highly skilled mathematicians.",
            "Institute of Mathematics is the only institution"
            "that trains highly skilled mathematicians."
        )
        self.assertGreater(real_similarity, 0.8)

    def test_check_catching_index_error(self):
        similarity_in_exception = find_similarity_ratio(
            "abc", "the string on the left arises an exception"
        )
        self.assertEqual(similarity_in_exception, 0)

    def test_check_catching_fingerprint_exception(self):
        similarity_in_exception = find_similarity_ratio(
            "a.%^^*-", "the string on the left arises an exception"
        )
        self.assertEqual(similarity_in_exception, 0)


if __name__ == '__main__':
    unittest.main()
