import pytest

from unstructured.metrics.table.table_formats import SimpleTableCell


def test_simple_table_cell_parsing_from_table_transformer_when_expected_input():
    table_transformer_cell = {"row_nums": [3, 2, 1], "column_nums": [6, 7], "cell text": "text"}
    transformed_cell = SimpleTableCell.from_table_transformer_cell(table_transformer_cell)
    expected_cell = SimpleTableCell(x=6, y=1, w=2, h=3, content="text")
    assert expected_cell == transformed_cell


def test_simple_table_cell_parsing_from_table_transformer_when_missing_input():
    table_transformer_cell = {"row_nums": [], "column_nums": [], "cell text": "text"}
    with pytest.raises(ValueError):
        SimpleTableCell.from_table_transformer_cell(table_transformer_cell)
