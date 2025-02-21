# jai maa saraswati

# STEP 1 Import the Important Library
import serpapi
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from serpapi import GoogleSearch

# STEP 4 Create a function for Search
def compare(med_name):
        params = {
        "engine": "google_shopping",
        "q": med_name,
        "api_key": "8975039bc628760153087b21fefb49e86b763d52e4287129ea8511627cf4b59c",
        "gl" : "in"
         }
        search = serpapi.GoogleSearch(params)
        results = search.get_dict()
        shopping_results = results['shopping_results']
        return shopping_results


# STEP 2 Create 2 columns for one picture and one for Title
c1,c2 = st.columns(2)
c1.image("e_pharmacy.png",width=200)
c2.header("E PHARMACY PRICE COMPARISON SYSTEM")

# STEP 3 Create a Sidebar
st.sidebar.title("ENTER NAME OF MEDICINE")
med_name = st.sidebar.text_input("Enter Name of Medicine 💊🧑‍⚕️")
number = st.sidebar.text_input("Enter The Number of Options Here 👌")
medicine_comp = []
med_price = []
# STEP 5 Create a sidebar buttom
if med_name is not None:
    # Step 1 in the STEP 5
    if st.sidebar.button("Price Compare"):
        shopping_results = compare(med_name)
        lowest_price = float((shopping_results[0].get('price'))[1:]) # STEP 2 in Step 5
        # Step 7 in Step 5
        st.sidebar.image(shopping_results[0].get('thumbnail'))
        print(lowest_price)
        for i in range(int(number)):
            # Step 8 in step 5
            medicine_comp.append(shopping_results[i].get('source'))
            med_price.append(float((shopping_results[i].get('price'))[1:]))
            # Step 4 in step 5
            current_price = float((shopping_results[i].get('price'))[1:])
            # Step 2 in STEP 5
            st.title(f"option{i+1}")
            c1,c2 = st.columns(2)
            c1.write("Company:")
            c2.write(shopping_results[i].get('source'))

            c1.write('title')
            c2.write(shopping_results[i].get('title'))

            c1.write("Price")
            c2.write(shopping_results[i].get('price'))

            url = shopping_results[i].get('product_link')
            c1.write("Buy Link")
            c2.write("[Link](%s)"%url)
            """_____________________________________________________________________"""
            # Step 5 in Step 5
            if (current_price < lowest_price):
                lowest_price = current_price
                lowest_price_index = i


        # Step 6 in Step 5 For Best Option
        lowest_price_index = i
        st.title("BEST OPTION")

        c1, c2 = st.columns(2)
        c1.write("Company:")
        c2.write(shopping_results[lowest_price_index].get('source'))

        c1.write("title:")
        c2.write(shopping_results[lowest_price_index].get('title'))

        c1.write("Price:")
        c2.write(shopping_results[lowest_price_index].get('price'))

        url = shopping_results[lowest_price_index].get('product_link')
        c1.write("Buy Link")
        c2.write("[Link](%s)" % url)


        """_____________________________________________________________________"""
        # STEP 9 in step 5 Bar Graph
        df=pd.DataFrame(med_price,medicine_comp)
        st.title("CHART COMPARISON")
        st.bar_chart(df)

        # STEP 10 in step 5 Pie Chart
        fig,ax=plt.subplots()
        ax.pie(med_price,labels=medicine_comp,shadow=True)
        ax.axis("equal")
        st.pyplot(fig)



