from datetime import datetime

import pandas as pd

from application.db.people import get_employees
from application.salary import calculate_salary


def data():
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
    print(df)


if __name__ == "__main__":
    calculate_salary()
    get_employees()
    data()
    print(datetime.now().strftime("%Y-%m-%d"))