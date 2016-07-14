def get():
    import connection as c
    db,de = c.con()
    from IPython.display import display
    import pandas as pd
    import datetime as dt
    import warnings
    warnings.filterwarnings("ignore")
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.style.use('ggplot')
    matplotlib.rcParams['figure.figsize'] = (12.0, 5.0)
    import numpy as np
    import insertest as insert
    import logging as l
    l.getLogger("FFC").setLevel(l.ERROR)

    return c, db, de, display, pd, dt, plt, np, insert, l
