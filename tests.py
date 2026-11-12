import unittest
from pandas.testing import assert_frame_equal

from test_virtual_column import *


def given_tests():
    test_sum_of_two_columns()
    test_multiplication_of_two_columns()
    test_subtraction_of_two_columns()
    test_empty_result_when_invalid_labels()
    test_empty_result_when_invalid_rules()
    test_when_extra_spaces_in_rules()


class AddVirtualColumnUnitTest(unittest.TestCase):

    def test_empty_label(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label_one + label_two", "")
        self.assertTrue(df_result.empty)

    def test_empty_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "", "label_three")
        self.assertTrue(df_result.empty)

    def test_empty_df(self):
        df = pd.DataFrame()
        df_result = add_virtual_column(df, "label_one + label_two", "")
        self.assertTrue(df_result.empty)

    def test_incomplete_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label_two-", "label_three")
        self.assertTrue(df_result.empty)

    def test_incompatible_types(self):
        df = pd.DataFrame([[1, "str"]] * 3, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label_one + label_two", "label_three")
        self.assertTrue(df_result.empty)

    def test_complicated_equation(self):
        df = pd.DataFrame([[0, 2]] * 3, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[0, 2, 4.0]] * 3, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "sin(label_one) + label_two**2", "label_three")
        assert_frame_equal(df_result, df_expected)

