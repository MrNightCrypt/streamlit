# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:48:36 2021

@author: acer
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App in 10 Year

Shown are the stock *closing prices* and *volumes* of Google, Apple and Amazon!
""")

###For Google
st.write("""
## GOOGLE
        """)
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period ='1d', start = '2011-9-15', end = '2021-9-15')

st.write("""
#### Closing Price
""")
st.bar_chart(tickerDf.Close)

st.write("""
#### Volume Price
""")
st.bar_chart(tickerDf.Volume)

st.write("""
====================================================================================
""")
###For Apple
st.write("""
## APPLE
        """)
tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period ='1d', start = '2011-9-15', end = '2021-9-15')

st.write("""
#### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
#### Volume Price
""")
st.line_chart(tickerDf.Volume)


st.write("""
====================================================================================
""")
###For Amazon
st.write("""
## AMAZON
        """)
tickerSymbol = 'AMZN'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period ='1d', start = '2011-9-15', end = '2021-9-15')

st.write("""
#### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
#### Volume Price
""")
st.line_chart(tickerDf.Volume)
