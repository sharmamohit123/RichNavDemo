
# importing modules
import urllib.request
import pandas as pd
import streamlit as st
from PIL import Image
import requests

st.header("Rich Nav Demo")
df = pd.read_csv('SampledDemoData.tsv', sep='\t', on_bad_lines = 'warn')
# df  = df[["DocumetUrl", "ImageUrl", "Title"]]
df = df.groupby("DocumetUrl")
# print(df.head(1000))
# df = df.iloc[:100000]
# df.to_csv('SampledDemoData.tsv', sep="\t", index=False)
# cnt=0
for name, group in df:
    st.subheader(name)
    imageList = []
    captionList = []
    for img in group["ImageUrl"]:
        # urllib.request.urlretrieve("www.bing.com"+img, "pic.png")
        image = Image.open(requests.get("http://www.bing.com"+img, stream=True).raw)
        imageList.append(image)
    for t in group["Title"]:
        captionList.append(t)
    st.image(imageList, width=100, caption=captionList)
    # cnt+=1
    # if(cnt==100): break
