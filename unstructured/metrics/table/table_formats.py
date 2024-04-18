from dataclasses import dataclass


@dataclass
class SimpleTableCell:
    x: int
    y: int
    w: int
    h: int
    content: str = ""

    def to_dict(self):
        return {"x": self.x, "y": self.y, "w": self.w, "h": self.h, "content": self.content}

    @classmethod
    def from_table_transformer_cell(cls, tatr_table_cell: dict[str, list[int] | str]):
        """
        Args:
            tatr_table_cell (dict):
                Cell in a format returned by Table Transformer model, for example:
                    {
                        "row_nums": [1,2,3],
                        "column_nums": [2],
                        "cell text": "Text inside cell"
                    }
        """

        row_nums = tatr_table_cell.get("row_nums", [])
        column_nums = tatr_table_cell.get("column_nums", [])

        if not row_nums:
            raise ValueError(f'Cell {tatr_table_cell} has missing values under "row_nums" key')
        if not column_nums:
            raise ValueError(f'Cell {tatr_table_cell} has missing values under "column_nums" key')

        x = sorted(column_nums)[0]
        y = sorted(row_nums)[0]

        width = len(column_nums)
        height = len(row_nums)

        return cls(x=x, y=y, w=width, h=height, content=tatr_table_cell.get("cell text", ""))
