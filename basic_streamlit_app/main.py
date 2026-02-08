# I start with loading the packages that I need for this Project
import streamlit as st #Streamlit is the one used most frequently
import pandas as pd #Pandas is used for loading and analyzing the data
import pydeck as pdk #Pydeck is a package I have used in a previous data science class to get maps and overlay information over other graphics

st.title("Drunk by Country")
st.write("This seeks to analyze alcohol consumption by country. Perhaps we will garner a clearer picture of what countries booze the most!")

st.subheader("Exploring Our Dataset")

df = pd.read_csv("data/drinks.csv")

#This part is my form of data manipulation. I wanted to see geographic region correlations, so I needed to create a new column that assigns a region to each country
#In order to do this, I created a dictionary (country_to_region) that assigns each country a region
country_to_region = {
    "Afghanistan": "Asia",
    "Albania": "Europe",
    "Algeria": "Africa",
    "Andorra": "Europe",
    "Angola": "Africa",
    "Antigua & Barbuda": "North America",
    "Argentina": "South America",
    "Armenia": "Asia",
    "Australia": "Oceania",
    "Austria": "Europe",
    "Azerbaijan": "Asia",
    "Bahamas": "North America",
    "Bahrain": "Asia",
    "Bangladesh": "Asia",
    "Barbados": "North America",
    "Belarus": "Europe",
    "Belgium": "Europe",
    "Belize": "North America",
    "Benin": "Africa",
    "Bhutan": "Asia",
    "Bolivia": "South America",
    "Bosnia-Herzegovina": "Europe",
    "Botswana": "Africa",
    "Brazil": "South America",
    "Brunei": "Asia",
    "Bulgaria": "Europe",
    "Burkina Faso": "Africa",
    "Burundi": "Africa",
    "Cote d'Ivoire": "Africa",
    "Cabo Verde": "Africa",
    "Cambodia": "Asia",
    "Cameroon": "Africa",
    "Canada": "North America",
    "Central African Republic": "Africa",
    "Chad": "Africa",
    "Chile": "South America",
    "China": "Asia",
    "Colombia": "South America",
    "Comoros": "Africa",
    "Congo": "Africa",
    "Cook Islands": "Oceania",
    "Costa Rica": "North America",
    "Croatia": "Europe",
    "Cuba": "North America",
    "Cyprus": "Europe",
    "Czech Republic": "Europe",
    "North Korea": "Asia",
    "DR Congo": "Africa",
    "Denmark": "Europe",
    "Djibouti": "Africa",
    "Dominica": "North America",
    "Dominican Republic": "North America",
    "Ecuador": "South America",
    "Egypt": "Africa",
    "El Salvador": "North America",
    "Equatorial Guinea": "Africa",
    "Eritrea": "Africa",
    "Estonia": "Europe",
    "Ethiopia": "Africa",
    "Fiji": "Oceania",
    "Finland": "Europe",
    "France": "Europe",
    "Gabon": "Africa",
    "Gambia": "Africa",
    "Georgia": "Asia",
    "Germany": "Europe",
    "Ghana": "Africa",
    "Greece": "Europe",
    "Grenada": "North America",
    "Guatemala": "North America",
    "Guinea": "Africa",
    "Guinea-Bissau": "Africa",
    "Guyana": "South America",
    "Haiti": "North America",
    "Honduras": "North America",
    "Hungary": "Europe",
    "Iceland": "Europe",
    "India": "Asia",
    "Indonesia": "Asia",
    "Iran": "Asia",
    "Iraq": "Asia",
    "Ireland": "Europe",
    "Israel": "Asia",
    "Italy": "Europe",
    "Jamaica": "North America",
    "Japan": "Asia",
    "Jordan": "Asia",
    "Kazakhstan": "Asia",
    "Kenya": "Africa",
    "Kiribati": "Oceania",
    "Kuwait": "Asia",
    "Kyrgyzstan": "Asia",
    "Laos": "Asia",
    "Latvia": "Europe",
    "Lebanon": "Asia",
    "Lesotho": "Africa",
    "Liberia": "Africa",
    "Libya": "Africa",
    "Lithuania": "Europe",
    "Luxembourg": "Europe",
    "Madagascar": "Africa",
    "Malawi": "Africa",
    "Malaysia": "Asia",
    "Maldives": "Asia",
    "Mali": "Africa",
    "Malta": "Europe",
    "Marshall Islands": "Oceania",
    "Mauritania": "Africa",
    "Mauritius": "Africa",
    "Mexico": "North America",
    "Micronesia": "Oceania",
    "Monaco": "Europe",
    "Mongolia": "Asia",
    "Montenegro": "Europe",
    "Morocco": "Africa",
    "Mozambique": "Africa",
    "Myanmar": "Asia",
    "Namibia": "Africa",
    "Nauru": "Oceania",
    "Nepal": "Asia",
    "Netherlands": "Europe",
    "New Zealand": "Oceania",
    "Nicaragua": "North America",
    "Niger": "Africa",
    "Nigeria": "Africa",
    "Nauru": "Oceania",
    "Norway": "Europe",
    "Oman": "Asia",
    "Pakistan": "Asia",
    "Palau": "Oceania",
    "Panama": "North America",
    "Papua New Guinea": "Oceania",
    "Paraguay": "South America",
    "Peru": "South America",
    "Philippines": "Asia",
    "Poland": "Europe",
    "Portugal": "Europe",
    "Qatar": "Asia",
    "South Korea": "Asia",
    "Moldova": "Europe",
    "Romania": "Europe",
    "Russian Federation": "Europe",
    "Rwanda": "Africa",
    "St. Kitts & Nevis": "North America",
    "St. Lucia": "North America",
    "St. Vincent & the Grenadines": "North America",
    "Samoa": "Oceania",
    "San Marino": "Europe",
    "Sao Tome & Principe": "Africa",
    "Saudi Arabia": "Asia",
    "Senegal": "Africa",
    "Serbia": "Europe",
    "Seychelles": "Africa",
    "Sierra Leone": "Africa",
    "Singapore": "Asia",
    "Slovakia": "Europe",
    "Slovenia": "Europe",
    "Solomon Islands": "Oceania",
    "Somalia": "Africa",
    "South Africa": "Africa",
    "Spain": "Europe",
    "Sri Lanka": "Asia",
    "Sudan": "Africa",
    "Suriname": "South America",
    "Swaziland": "Africa",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "Syria": "Asia",
    "Tajikistan": "Asia",
    "Thailand": "Asia",
    "Macedonia": "Europe",
    "Timor-Leste": "Asia",
    "Togo": "Africa",
    "Tonga": "Oceania",
    "Trinidad & Tobago": "North America",
    "Tunisia": "Africa",
    "Turkey": "Europe",
    "Turkmenistan": "Asia",
    "Tuvalu": "Oceania",
    "Uganda": "Africa",
    "Ukraine": "Europe",
    "United Arab Emirates": "Asia",
    "United Kingdom": "Europe",
    "Tanzania": "Africa",
    "USA": "North America",
    "Uruguay": "South America",
    "Uzbekistan": "Asia",
    "Vanuatu": "Oceania",
    "Venezuela": "South America",
    "Vietnam": "Asia",
    "Yemen": "Asia",
    "Zambia": "Africa",
    "Zimbabwe": "Africa"
}

# Then, I added this new column to the dataset
df['Region'] = df['country'].map(country_to_region)

# I saved the new dataset as new_drinks
df.to_csv("data/new_drinks.csv", index=False)

#In addition to analyzing general regions, I was especially keen to create a map visualization
#I had the idea to overlay points based on teh general size of the amount of drinking, so one could see what countries drink the most alcohol
#However, I knew that in order to properly place the points, I needed the latitidue and longitude to be a new column in the dataset

#Therefore, I created a dictionary for the country coordinates
# *** Here I would like to acknowledge my use of AI. In order to speed along the process of finding the coordinates for each country, I asked AI to give me the coordinates for each country in the list.
# *** I double checked the coordinates to ensure it gave me correct information
country_coords = {
    "Afghanistan": [67.709953, 33.93911],
    "Albania": [20.1683, 41.1533],
    "Algeria": [1.6596, 28.0339],
    "Andorra": [1.5218, 42.5063],
    "Angola": [17.8739, -11.2027],
    "Antigua & Barbuda": [61.8175, 17.0747],
    "Argentina": [-63.6167, -38.4161],
    "Armenia": [45.0382, 40.0691],
    "Australia": [133.7751, -25.2744],
    "Austria": [14.5501, 47.5162],
    "Azerbaijan": [47.5769, 40.1431],
    "Bahamas": [-77.3963, 25.0343],
    "Bahrain": [50.5577, 26.0667],
    "Bangladesh": [90.3563, 23.685],
    "Barbados": [-59.5432, 13.1939],
    "Belarus": [27.9534, 53.7098],
    "Belgium": [4.4699, 50.5039],
    "Belize": [-88.4976, 17.1899],
    "Benin": [5.6037, 6.335],
    "Bhutan": [90.4336, 27.5142],
    "Bolivia": [-63.5887, -16.2902],
    "Bosnia-Herzegovina": [17.6791, 43.9159],
    "Botswana": [24.6849, -22.3285],
    "Brazil": [-51.9253, -14.235],
    "Brunei": [114.7277, 4.5353],
    "Bulgaria": [25.4858, 42.7339],
    "Burkina Faso": [1.5616, 12.2383],
    "Burundi": [29.9189, 3.3731],
    "Cote d'Ivoire": [5.5471, 7.54],
    "Cabo Verde": [23.0418, 16.5388],
    "Cambodia": [104.991, 12.5657],
    "Cameroon": [12.3547, 7.3697],
    "Canada": [106.3468, 56.1204],
    "Central African Republic": [20.9394, 6.6111],
    "Chad": [18.7322, 15.4542],
    "Chile": [-71.543, 35.6751],
    "China": [104.1954, 35.8617],
    "Colombia": [-74.2973, 4.5709],
    "Comoros": [43.3333, 11.6455],
    "Congo": [21.7587, 4.0383],
    "Cook Islands": [159.7777, 21.2367],
    "Costa Rica": [83.7534, 9.7489],
    "Croatia": [15.2, 45.1],
    "Cuba": [-77.7812, 21.5218],
    "Cyprus": [33.4299, 35.1264],
    "Czech Republic": [15.473, 49.8175],
    "North Korea": [127.5101, 40.3399],
    "DR Congo": [21.7587, 4.0383],
    "Denmark": [9.5018, 56.2639],
    "Djibouti": [42.5903, 11.8251],
    "Dominica": [61.371, 15.415],
    "Dominican Republic": [70.1627, 18.7357],
    "Ecuador": [78.1834, 1.8312],
    "Egypt": [30.8025, 26.8206],
    "El Salvador": [88.8965, 13.7942],
    "Equatorial Guinea": [10.2679, 1.6508],
    "Eritrea": [39.7823, 15.1794],
    "Estonia": [25.0136, 58.5953],
    "Ethiopia": [40.4897, 9.145],
    "Fiji": [178.065, 17.7134],
    "Finland": [25.7482, 61.9241],
    "France": [2.2137, 46.2276],
    "Gabon": [11.6094, 0.8037],
    "Gambia": [15.3101, 13.4432],
    "Georgia": [82.9071, 32.1574],
    "Germany": [10.4515, 51.1657],
    "Ghana": [1.02, 7.95],
    "Greece": [21.8243, 39.0742],
    "Grenada": [61.679, 12.1165],
    "Guatemala": [90.2308, 15.7835],
    "Guinea": [9.6966, 9.9456],
    "Guinea-Bissau": [15.1804, 11.8037],
    "Guyana": [58.9302, 4.8604],
    "Haiti": [72.2852, 18.9712],
    "Honduras": [86.2419, 15.2],
    "Hungary": [19.5033, 47.1625],
    "Iceland": [19.0208, 64.9631],
    "India": [78.9629, 20.5937],
    "Indonesia": [113.9213, 0.7893],
    "Iran": [53.688, 32.4279],
    "Iraq": [43.6793, 33.2232],
    "Ireland": [7.3055, 53.7798],
    "Israel": [34.8516, 31.0461],
    "Italy": [12.5674, 41.8719],
    "Jamaica": [77.2975, 18.1096],
    "Japan": [138.2529, 36.2048],
    "Jordan": [36.2384, 30.5852],
    "Kazakhstan": [66.9237, 48.0196],
    "Kenya": [37.9062, 0.0236],
    "Kiribati": [172.983, 1.4421],
    "Kuwait": [47.4818, 29.3117],
    "Kyrgyzstan": [74.7661, 41.2044],
    "Laos": [102.4955, 19.8563],
    "Latvia": [24.6032, 56.8796],
    "Lebanon": [35.8623, 33.8547],
    "Lesotho": [28.2336, 29.61],
    "Liberia": [9.4295, 6.4281],
    "Libya": [17.2283, 26.3351],
    "Lithuania": [28.8813, 55.1694],
    "Luxembourg": [6.1296, 49.8153],
    "Madagascar": [46.8691, 18.7669],
    "Malawi": [34.3015, 13.2543],
    "Malaysia": [101.9758, 4.2105],
    "Maldives": [73.2207, 3.2028],
    "Mali": [3.9962, 17.5707],
    "Malta": [14.3754, 35.9375],
    "Marshall Islands": [171.1845, 7.1315],
    "Mauritania": [10.9408, 21.0079],
    "Mauritius": [57.5522, 20.3484],
    "Mexico": [102.5528, 23.6345],
    "Micronesia": [150.5508, 7.4256],
    "Monaco": [7.4246, 43.7384],
    "Mongolia": [103.8467, 46.8625],
    "Montenegro": [19.3744, 42.7087],
    "Morocco": [7.0926, 31.7917],
    "Mozambique": [35.5296, 18.6657],
    "Myanmar": [95.956, 21.9162],
    "Namibia": [18.4904, -22.9576],
    "Nauru": [166.9315, 0.5228],
    "Nepal": [84.124, 28.3949],
    "Netherlands": [5.2913, 52.1326],
    "New Zealand": [174.886, 40.9006],
    "Nicaragua": [85.2072, 12.8654],
    "Niger": [8.0817, 17.6078],
    "Nigeria": [8.6753, 9.082],
    "North Korea": [127.5101, 40.3399],
    "Oman": [55.9754, 21.7435],
    "Pakistan": [69.3451, 30.3753],
    "Palau": [134.5825, 7.515],
    "Panama": [80.7821, 8.538],
    "Papua New Guinea": [143.96, 6.31],
    "Paraguay": [-58.4438, -23.4425],
    "Peru": [-75.02, 9.19],
    "Philippines": [121.774, 12.8797],
    "Poland": [19.1451, 51.9194],
    "Portugal": [8.2245, 39.3999],
    "Qatar": [51.1839, 25.3548],
    "South Korea": [127.7669, 35.9078],
    "Moldova": [28.3699, 47.4116],
    "Romania": [24.9668, 45.9432],
    "Russian Federation": [37.6151, 55.7559],
    "Rwanda": [29.8739, -1.9403],
    "St. Kitts & Nevis": [62.783, 17.3578],
    "St. Lucia": [60.9789, 13.9094],
    "St. Vincent & the Grenadines": [61.2872, 12.9843],
    "Samoa": [172.1046, 13.759],
    "San Marino": [12.4468, 43.9352],
    "Sao Tome & Principe": [6.6131, 0.1864],
    "Saudi Arabia": [45.0792, 23.8859],
    "Senegal": [14.4524, 14.4974],
    "Serbia": [21.0059, 44.0165],
    "Seychelles": [55.492, 4.6796],
    "Sierra Leone": [11.7799, 8.4606],
    "Singapore": [103.8198, 1.3521],
    "Slovakia": [19.699, 48.669],
    "Slovenia": [14.9955, 46.1512],
    "Solomon Islands": [160.1562, 9.6457],
    "Somalia": [46.1996, 5.1521],
    "South Africa": [22.9375, 30.5595],
    "Spain": [3.7492, 40.4637],
    "Sri Lanka": [80.7718, 7.8731],
    "Sudan": [30.2176, 12.8628],
    "Suriname": [56.0278, 3.9193],
    "Swaziland": [31.4659, -26.5225],
    "Sweden": [18.6435, 60.1282],
    "Switzerland": [8.2275, 46.8182],
    "Syria": [38.9968, 34.8021],
    "Tajikistan": [71.2761, 38.861],
    "Thailand": [100.9925, 15.87],
    "Macedonia": [21.7453, 41.6086],
    "Timor-Leste": [125.7275, 8.8742],
    "Togo": [0.8248, 8.6195],
    "Tonga": [175.1982, 21.179],
    "Trinidad & Tobago": [61.2225, 10.6918],
    "Tunisia": [9.5375, 33.8869],
    "Turkey": [35.2433, 38.9637],
    "Turkmenistan": [59.5563, 38.9697],
    "Tuvalu": [177.6493, 7.1095],
    "Uganda": [32.2903, 1.3733],
    "Ukraine": [31.1656, 48.3794],
    "United Arab Emirates": [53.8478, 23.4241],
    "United Kingdom": [3.436, 55.3781],
    "Tanzania": [34.8888, 6.369],
    "USA": [-106.5348, 38.7946],
    "Uruguay": [55.7658, 32.5228],
    "Uzbekistan": [64.5853, 41.3775],
    "Vanuatu": [166.9592, 15.3767],
    "Venezuela": [66.5897, 6.4238],
    "Vietnam": [108.2772, 14.0583],
    "Yemen": [48.5164, 15.5527],
    "Zambia": [27.8493, -13.1339],
    "Zimbabwe": [29.1549, 19.0154],
}

# Similar to how I created my region column, I added the coordinates dictionary to my dataset
df['coordinates'] = df['country'].map(country_coords)

# However, I needed the columns for latitude and longitude to be separate, so I had to create individual columns
df['longitude'] = df['coordinates'].apply(lambda x: x[0] if isinstance(x, list) else None)
df['latitude'] = df['coordinates'].apply(lambda x: x[1] if isinstance(x, list) else None)

# I no longer needed the original coordinates column, so I dropped it
df.drop(columns=['coordinates'], inplace=True)

# I did this just to check to make sure it was printing properly
print(df[['country', 'latitude', 'longitude']].head())

# Now moving into the actual visualizations
# I created tabs so that each tab could have different information and visualizations
tab1, tab2, tab3, tab4 = st.tabs(["Data", "Maps", "Graphs", "Summary Statistics"])

# Beginning with Tab 1
# Tab 1 shows the data set so that the audience can see exactly what data is being manipulated and analyzed
with tab1:
    st.subheader("Here's our Data!")
    st.write("This tab shows us our raw data. Using this data, we will create maps, graphs, and charts that can give us insight into the level of alcohol consumption throughout the world.")
    st.dataframe(df)

# Tab 2 is the visualization I think is the most interesting: the map
# I wanted to create a visualization that showed drinking around the world based on amount
with tab2:
    st.write("This tab shows us a map visualization. The larger the circle, the greater the level of alcohol consumption. Zoom in or out and play around with the map to get a better idea of alcohol consumption throughout the world.")
    # I began getting errors here, so I had to make sure my latitude and longitude were numeric 
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df['total_litres_of_pure_alcohol'] = pd.to_numeric(df['total_litres_of_pure_alcohol'], errors='coerce')
    
    # Originally, I had wanted to use a specific map from mapbox, so I needed a token access key
    # This was my token access key; however, it was very complicated and not appearing properly
    # As you will see below, I ended up not utilizing my token, but instead using just a preloaded 'light' theme
    mapbox_style_url = 'mapbox://styles/mapbox/street-v11?access_token=pk.eyJ1IjoiYXNoYnl3aGl0YWtlciIsImEiOiJjbWw5czRnZW0wNjFzM2hwbzhoemJ6aG9pIn0.kmZEpUq0OV5xqWjqNX5C_g'

    # Here is where I began to work with layering my map
    # I had previously learned this technique in R in a previous data science class. 
    # I had to rely partially on the internet to adapt what I knew to VS code 
    layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[longitude, latitude]',
    get_radius='total_litres_of_pure_alcohol * 30000',  # Here I had to play around with the size that would show up properly 
    get_fill_color='[255, 0, 0, 160]',  # I had to look up what fill colors were common, and this red sequence appeared for me and worked better than other color sequences
    pickable=True,
    )
    view_state = pdk.ViewState(
    latitude=df['latitude'].mean(),
    longitude=df['longitude'].mean(),
    zoom=1,
    pitch=0,
    ) 
    deck_map = pdk.Deck(
    map_style='light', # I mentioned this previously when discussing my map key 
    layers=[layer],
    initial_view_state=view_state,
    )
    st.pydeck_chart(deck_map)

# Tab 3 I wanted to look at some simply graphs showing different amounts of alcohol consumptions in different regions
# This tab is what the previous data manipulation, creating my region column, was used for 
with tab3:
    st.write("This tab shows us interactive graphs. You can either choose to compare all regions or choose a specific region and see the differences in type of alcohol consumption.")
    # Upon going through my data, I could not find any NA variables but they were appearing in my visualization, so I dropped NA variables just to be sure.
    df = df.dropna(subset=['Region', 'wine_servings', 'beer_servings', 'spirit_servings'])
    df['Region'] = df['Region'].astype(str)
    # I wanted to be able to compare individual regions by type of alcohol and compare all regions by total alcohol
    # In my drop down menu, I made it an option to look at 'Compare all Regions' or the unique regions 
    region_options = ['Compare All Regions'] + sorted(df['Region'].unique())
    selected_option = st.selectbox("Select a Region or Compare All", options=region_options)
    
    # I then made an if else statement for if the Compare All was chosen or not
    if selected_option == 'Compare All Regions':
        # If compare all is chosen, then it compares each region by total litres of pure alcohol
        agg_df = df.groupby('Region')['total_litres_of_pure_alcohol'].sum().reset_index()
        st.title("Total Alcohol Consumption by Region")
        st.bar_chart(agg_df.set_index('Region'))
    # If an individual region is chosen, then the chart compares the different types of alcohol within that region
    else:
        region_df = df[df['Region'] == selected_option]
        servings_data = {
        'Wine': region_df['wine_servings'].sum(),
        'Beer': region_df['beer_servings'].sum(),
        'Spirit': region_df['spirit_servings'].sum()
        }
        st.title(f"Drink Servings in {selected_option}")
        st.bar_chart(pd.DataFrame(servings_data, index=[0]).T)
    
    # From my chart it was CLEAR that Europe was way ahead of any other region in alcohol consumption, so I decided to create a graph that compared the countries of Europe 
    st.write("Clearly, Europe is head and shoulders above any other region, so let's take a deeper look to see what countries among this region are drinking the most!")
    europe_df = df[df['Region'] == 'Europe']
    europe_df = europe_df.dropna(subset=['total_litres_of_pure_alcohol'])
    europe_df = europe_df.sort_values(by='total_litres_of_pure_alcohol', ascending=False)
    st.title("Alcohol Consumption in European Countries")
    st.bar_chart(europe_df.set_index('country')['total_litres_of_pure_alcohol'])

# Finally, with Tab 4, I thought I would show a quick summary statistics page that could yield some interesting results
with tab4:
    st.write("This section offers us summary statistics.")
    st.write(df.describe())
