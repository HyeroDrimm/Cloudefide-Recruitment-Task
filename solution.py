import pandas
import re
NAME = re.compile(r"[A-Za-z_]+")

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    if not NAME.fullmatch(new_column) or not role:
        return pandas.DataFrame([])

    new_df = df.copy(deep=True)

    # I used eval as a simple solution, even though it is not safe with code injection because project specs did not
    # mention what it will be used for. There are other ways to parse equation that are safe but require more implementation time
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

