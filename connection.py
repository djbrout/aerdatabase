
import dataset
from sqlalchemy import create_engine
def con():
    connection = dataset.connect('postgresql://fowytuhxyrzbkg:A_YB7GxeAZcwBi33iOFCHrMosx@ec2-54-221-225-242.compute-1.amazonaws.com:5432/d452ub83ajvmic')
    diskengine = create_engine('postgresql://fowytuhxyrzbkg:A_YB7GxeAZcwBi33iOFCHrMosx@ec2-54-221-225-242.compute-1.amazonaws.com:5432/d452ub83ajvmic')
    return connection,diskengine
