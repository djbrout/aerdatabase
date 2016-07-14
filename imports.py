import warnings
warnings.filterwarnings("ignore")

def get():
    import connection as c
    db,de = c.con()
    from IPython.display import display
    import pandas as pd
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.style.use('ggplot')
    matplotlib.rcParams['figure.figsize'] = (8.0, 6.0)
    import numpy as np
    from IPython.core.display import HTML
    import urllib2
    HTML(urllib2.urlopen('http://bit.ly/1Bf5Hft').read())
    import insertest as insert

    return c, db, de, display, pd, dt, plt, np, insert
