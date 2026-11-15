import pandas
import re
NAME = re.compile(r"[A-Za-z_]+")

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    if not NAME.fullmatch(new_column) or not role:
        return pandas.DataFrame([])

    new_df = df.copy(deep=True)

    try:
        column = new_df.eval(role)
    except pandas.errors.UndefinedVariableError as e:
        print(e)
        return pandas.DataFrame([])
    except TypeError as e:
        print(e)
        return pandas.DataFrame([])
    except SyntaxError as e:
        print(e)
        return pandas.DataFrame([])

    new_df[new_column.strip()] = column
    return new_df

