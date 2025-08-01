import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
df = pd.read_csv('zomato.csv')
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]
df['Country Name'] = df['Country Code'].apply(country_name)
df["Cuisines"] = df.loc[:, "Cuisines"].apply(lambda x: str(x).split(",")[0])
# filtros
st.sidebar.title('Filtros')
country_name2 = st.sidebar.multiselect(
    'Selecione os países:',
    options=df.loc[:, 'Country Name'].dropna().unique().tolist(),
    default=df.loc[:, 'Country Name'].dropna().unique().tolist()    
)
linha2 = df['Country Name'].isin(country_name2)
df = df.loc[linha2, :]


# layout no streamlit

st.title('🍽️Cuisines')