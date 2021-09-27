import os
import pandas as pd
import time


def get_most_recent_file(path, fname, ext, ignore=''):
    """
    Get most recent file in path with specific file name and extension
    :param path: directory
    :param fname: name or partial name of file
    :param ext: file extension
    :param ignore: ignore substring
    :return: file path
    """
    files = [os.path.join(path, f) for f in os.listdir(path) if (ignore not in f.lower()
                                                                 and ext in f.lower()
                                                                 and fname in f.lower())]

    dates = [os.path.getctime(os.path.join(path, f)) for f in files]

    dict_files = dict(zip(dates, files))

    return dict_files[max(dict_files)]


if __name__ == "__main__":

    path = os.environ.get(PATH)

    trades = pd.read_excel(get_most_recent_file(path=path,
                                                fname="estrutura de tabelas",
                                                ext=".xlsm",
                                                ignore="$"),
                           ['Trades Onshore', "Trades Offshore"])

    for trade in trades:
        print(trade)

    time.sleep(1)