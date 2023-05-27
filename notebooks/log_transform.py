import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def log_transform(x):
# Apply a log transformation to the "LoanAmount" column
 x = np.log(x)
 return x


