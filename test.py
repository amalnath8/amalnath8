# File Selection Drop Down
from contextlib import nullcontext
from logging import NOTSET
from altair.vegalite.v4.api import value
import streamlit as st
import os
from typing import Dict
# importing pandas as pd
import pandas as pd
import numpy as np


# FinalNames = 1

# @st.cache(allow_output_mutation=True)
# def get_static_store() -> Dict:
#     """This dictionary is initialized once and can be used to store the files uploaded"""
#     return {}

# def file_selector(folder_path):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

# def main():
#     fileslist = get_static_store()
#     folderPath = st.text_input('Enter folder path:')
#     if folderPath:    
#         filename = file_selector(folderPath)
#         if not filename in fileslist.values():
#             fileslist[filename] = filename
#     else:
#         fileslist.clear()  # Hack to clear list if the user clears the cache and reloads the page
#         st.info("Select one or more files.")

#     if st.button("Clear file list"):
#         fileslist.clear()

#     finalNames = list(fileslist.keys())

#     if st.checkbox("Show file list?", True):
#         st.write(list(fileslist.keys()))
#     return finalNames

# finalNames=main()

# st.write(finalNames[0])
# df = pd.read_csv (finalNames[0])
# st.dataframe(df)
dataframe = pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    dataframe = pd.read_csv(uploaded_file)
    dataframe.index = np.arange(1,len(dataframe)+1)
    st.write(dataframe)
user_input = st.text_input("Enter index",value="")

if user_input=="" :
     st.write("please enter Daily sales report in csv")
else :
    st.write(user_input)
    li= user_input.split(",")
    length = len(li)
    for i in range(length):
        li[i]= int(li[i])-1

    dr=dataframe.iloc[li]
    di=dr['Invoice ID']
    x = di.to_string(header=False,
                    index=False).split('\n')
    vals = [','.join(ele.split()) for ele in x]

    # initializing delim 
    delim = ","
    
    # using map to convert each element to string 
    temp = list(map(str, vals))
    
    # join() used to join with delimiter
    res = delim.join(temp)
    
    # printing result 
    print("Invoices for card: " + str(res))

    st.write(res)

   