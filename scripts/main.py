
import pandas as pd
import streamlit as st
import datetime


def proecess_data(data):

    # standardize to datetime
    data['founded_at'] = pd.to_datetime(data['founded_at'], errors='ignore')

    # # get founded year
    # data['founded_year'] = data['founded_at'].apply(lambda x: str(x).split("-")[0])
    #
    # # get company age
    # now = datetime.datetime.now().year
    # data['company_age'] = now - data['founded_year']

    return data


@st.cache
def load_data():

    data = pd.read_csv('./data/startup-investments-crunchbase.zip',
                       compression='zip', encoding='ISO-8859-2')
    data = proecess_data(data)

    return data


def main():

    data = load_data()
    st.table(data.dtypes)
    st.table(data[['permalink', 'founded_at']].sample(10))


if __name__ == '__main__':
    main()
