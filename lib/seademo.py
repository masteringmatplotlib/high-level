import numpy as np
import pandas as pd


def get_data_set():
    rs = np.random.RandomState(4)
    pos = rs.randint(-1, 2, (20, 5)).cumsum(axis=1)
    pos -= pos[:, 0, np.newaxis]
    step = np.tile(range(5), 20)
    walk = np.repeat(range(20), 5)
    return pd.DataFrame(np.c_[pos.flat, step, walk],
                        columns=["position", "step", "walk"])
