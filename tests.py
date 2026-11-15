import unittest
from pandas.testing import assert_frame_equal

from test_virtual_column import *


class AddVirtualColumnUnitTest(unittest.TestCase):
    # Given tests

    def test_sum_of_two_columns(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one+label_two", "label_three")
        assert_frame_equal(df_result, df_expected)


    def test_multiplication_of_two_columns(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one * label_two", "label_three")
        assert_frame_equal(df_result, df_expected)


    def test_subtraction_of_two_columns(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 1, 0]] * 2, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one - label_two", "label_three")
        assert_frame_equal(df_result, df_expected)

    def test_empty_result_when_invalid_labels(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label_one + label_two", "label3")
        self.assertTrue(df_result.empty)

    def test_empty_result_when_invalid_rules(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label&one + label_two", "label_three")
        self.assertTrue(df_result.empty)

    def test_empty_result_when_invalid_rules2(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_result = add_virtual_column(df, "label_five + label_two", "label_three")
        self.assertTrue(df_result.empty)

    def test_when_extra_spaces_in_rules(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one + label_two ", "label_three")
        assert_frame_equal(df_result, df_expected)

    def test_when_extra_spaces_in_rules2(self):
        df = pd.DataFrame([[1, 1]] * 2, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "  label_one + label_two ", "label_three")
        assert_frame_equal(df_result, df_expected)

    # My tests

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

    def test_addition_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 2, 3]] * 3, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one+label_two", "label_three")
        assert_frame_equal(df_result, df_expected)

    def test_multiplication_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 2, 2]] * 3, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one*label_two", "label_three")
        assert_frame_equal(df_result, df_expected)

    def test_subtraction_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 2, -1]] * 3, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_one-label_two", "label_three")
        assert_frame_equal(df_result, df_expected)

    def test_square_rule(self):
        df = pd.DataFrame([[1, 2]] * 3, columns=["label_one", "label_two"])
        df_expected = pd.DataFrame([[1, 2, 4]] * 3, columns=["label_one", "label_two", "label_three"])
        df_result = add_virtual_column(df, "label_two*label_two", "label_three")
        assert_frame_equal(df_result, df_expected)

