from dataclasses import dataclass
import pandas as pd
from copy import copy

from pandas.core.frame import DataFrame


def merge_data(pXdataFrame:DataFrame, pYdataFrame:DataFrame, pHow:str, pOn:str)->DataFrame(): 
    result = pd.DataFrame()
    result = pd.merge(pXdataFrame, pYdataFrame, pHow, pOn)
    return result

def concat_data(pXdataFrame, pYdataFrame):
    result = pd.concat([pXdataFrame, pYdataFrame])
    result.reset_index(drop = True, inplace=True)

    return result

def remove_columns(pDataFrame, pRemoveList):
    result = copy(pDataFrame)
    for column in pRemoveList:
        del(result[column])
    return result

def missing_value(pDataFrame:DataFrame, pColList:list):
    del(pDataFrame[pColList])
    pDataFrame.dropna(inplace=True)
