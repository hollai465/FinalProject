# -*- coding: utf-8 -*-
"""app0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17H0b2rVFyPhP_2BoztLHuCd-PPV-0l-I
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.colors
import textwrap
import matplotlib.font_manager as fm


tab1, tab2, tab5, tab3, tab4 = st.tabs(["Home", "Opinions by Playtime","Opinions by Favorite Activity" ,"Enviormental Concern Globally","Links/References"])

with tab1:
    st.header("Virtual Worlds; Real Problems")
    st.write("The research examines how immersive environmental video games can influence players' climate awareness and concern. By exploring the link between virtual experiences and real-world attitudes, it highlights the potential of games as powerful tools for climate communication and education.")
    st.write("As a case study, we chose to examine Animal Crossing: New Horizons (Nintendo 2020), a popular game that emphasizes interactions with the in-game enviornment. Players are incentivized to gather resources for use in crafting items or building amenities (like a general store) for the island. They are also prompted to collect bugs, fish, and fossils to donate to the museum, sell, or display. This environmental interaction is the focus of this study. ")
    st.write("Visit the different pages to view three different visualizations representing our findings, or if you're unfamiliar with the game you can watch the video below for a brief overview.")
    st.video("https://www.youtube.com/watch?v=8AkEFot5UF0") 

with tab2:
    df = pd.read_csv('gameData.csv')
    df = df[df['A1'] != "What is your nationality?"]

    conditions = [
        df['A1'].isin(['Vietnam', 'Japan', 'China','Philippines','Indonesia','Singapore','Myanmar']),
        df['A1'].isin(['Canada', 'USA'])
    ]

    choices = ['Asia', 'North America']

    df['A1_Region'] = np.select(conditions, choices, default='Other')

    for col in ["C1", "C2", "C3","C4", "C5", "C6","C7", "C8", "C9","C10", "C11", "C12","C13", "C14", "C15","D5"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df.fillna(0, inplace=True)

    for col in ["C7", "C8", "C9"]:
        df[col] = 6 - df[col]

    df[['C7', 'C8', 'C9']] = df[['C7', 'C8', 'C9']].clip(0, 5)

    st.header("Opinions of ACNH Players by Playtime")


    df['Resource Limits and Overpopulation'] = (df[['C1', 'C11']].sum(axis=1)) / 2
    df['Human Impact on the Environment'] = (df[['C3', 'C5', 'C15']].sum(axis=1)) / 3
    df['Natures Balance and Fragility'] = (df[['C8', 'C13']].sum(axis=1)) / 2
    df['Human Superiority vs. Ecocentrism'] = (df[['C2', 'C12', 'C7', 'C9']].sum(axis=1)) / 4
    df['Technological Optimism vs. Environmental Concern'] = (df[['C4', 'C14', 'C10', 'C6']].sum(axis=1)) / 4

    y_tick_labels = {
        'Resource Limits and Overpopulation': ["Resources are Plentiful", "Resources are Limited"],
        'Human Impact on the Environment': ["Humans Have Little Impact", "Humans Harm the Environment"],
        'Natures Balance and Fragility': ["Nature is Resilient", "Nature is Fragile"],
        'Human Superiority vs. Ecocentrism': ["Humans Should Dominate Nature", "Nature is Equal to Humans"],
        'Technological Optimism vs. Environmental Concern': ["Tech Will Save Us", "Environment in Danger"],
    }
    wrapped_y_tick_labels = {
        key: [textwrap.fill(label, width=15) for label in labels]
        for key, labels in y_tick_labels.items()
    }


    column_names = ['Resource Limits and Overpopulation',
                'Human Impact on the Environment',
                'Natures Balance and Fragility',
                'Human Superiority vs. Ecocentrism',
                'Technological Optimism vs. Environmental Concern']

   
    selected_y_column = st.selectbox(
        'Select the agreement statement to analyze:',
        column_names
    )
    df = df[df['D5'] != 7]

    reverse_mapping = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    df['D5_reversed'] = df['D5'].map(reverse_mapping)

    x = df['D5_reversed'].astype('category').cat.codes


    def update_plot(selected_y_column):
        y = df[selected_y_column]

        countries = df['A1_Region'].astype('category')
        country_labels = countries.cat.categories
        color_values = countries.cat.codes

        jitter_strength = 0.5
        x_jittered = x + np.random.uniform(-jitter_strength, jitter_strength, size=len(x))
        y_jittered = y + np.random.uniform(-jitter_strength, jitter_strength, size=len(y))

        plt.figure(figsize=(20, 12))

        cmap = matplotlib.colors.ListedColormap(sns.color_palette("colorblind", as_cmap=False))

        scatter = plt.scatter(x_jittered, y_jittered, c=color_values, cmap=cmap, alpha=0.8, s=150)

        handles = []
        for i, country in enumerate(country_labels):
            hex_color = matplotlib.colors.to_hex(cmap(i % len(cmap.colors)))  # Use the colorblind-safe palette
            handles.append(plt.Line2D([0], [0], marker='o', color='w',
                                    label=country,
                                    markerfacecolor=hex_color, markersize=6))
        font_properties = fm.FontProperties(weight='bold', size=20)
        plt.legend(
            handles=handles,
            title='Region',
            loc='upper right',
            framealpha=0.9,
            fontsize=20,                
            title_fontproperties=font_properties,  
            markerscale=2     
        )
        slope, intercept = np.polyfit(x_jittered, y_jittered, 1)
        line_x = np.linspace(x_jittered.min(), x_jittered.max(), 100)
        line_y = slope * line_x + intercept
        plt.plot(line_x, line_y, color='red', label='Best Fit Line')

        correlation_matrix = np.corrcoef(x_jittered, y_jittered)
        correlation_coefficient = correlation_matrix[0, 1]
        r_squared = correlation_coefficient ** 2

        if selected_y_column in wrapped_y_tick_labels:
            plt.yticks([1, 5], wrapped_y_tick_labels[selected_y_column], rotation=90,fontsize=20)
            for label in plt.gca().get_yticklabels():
                label.set_verticalalignment('center')

        plt.xticks([1, 6], ["Less than once a month", "Everyday"])
        plt.xticks(fontsize=20)
        


        plt.text(0.95, 0.05, f'R² = {r_squared:.2f}',
         transform=plt.gca().transAxes,
         fontsize=20,
         verticalalignment='bottom',
         horizontalalignment='right')
        
        plt.title(f'Fig 1. Opinion on: {selected_y_column} by Time Playing ACNH', fontweight='bold', fontsize=30, pad=60)
        plt.xlabel('Time Spent Playing ACNH', fontweight='bold',fontsize=20)
        plt.ylabel("Opinion", fontweight='bold',fontsize=20)


        plt.tight_layout()  

        st.pyplot(plt)


    update_plot(selected_y_column)
    st.write("Fig 1. analyzes players' opinions on various enviormental topics, mapped to the frequency they play New Horizons. Topics can be selected between, and the graph includes both a line of best fit and the R^2 correlation coefficient. The line of best fit shows the general trend of player opinions, while the correlation coefficient shows the degree of correlation between the data and the trend on a scale of 0-1, with 0 being weakly correlated and 1 being very strongly correlated.")


with tab3:
    st.header("ACNH Players Compared to Global Population")

    dfglobal = pd.read_csv("globalData.csv")
    dfglobal["Country"] = dfglobal["Country"].str.strip().str.upper()


    dfglobal = dfglobal.dropna(subset=["Weighted Mean", "Question Text (Short)", "Response", "Country"])

    agree_map = {
        "Big businesses performance": ["Very well", "Somewhat well"],
        "Countries working together": ["Yes - they should work together despite their disagreements"],
        "Country performance": ["Very well", "Somewhat well"],
        "Effects on big decisions": ["A lot"],
        "Extreme weather experience": ["Worse than usual"],
        "Protect and restore nature": ["A lot"],
        "Protection from extreme weather": ["More protection"],
        "Renewable energy transition": ["Very quickly", "Somewhat quickly"],
        "Rich countries helping poor": ["More help"],
        "Strengthening commitments": ["Strengthen"],
        "Teaching about climate change": ["More"],
        "Thinking about climate change": ["Daily", "Weekly"],
        "Worry compared to last year": ["More worried"],
        "Worry for next generation": ["Extremely", "Very","Somewhat"]
    }

    agree_rows = []
    for question, agree_responses in agree_map.items():
        subset = dfglobal[(dfglobal["Question Text (Short)"] == question) & (dfglobal["Response"].isin(agree_responses))]
        agree_rows.append(subset)

    df_agree = pd.concat(agree_rows)

    pivot_df = df_agree.pivot_table(
        index="Country",
        columns="Question Text (Short)",
        values="Weighted Mean",
        aggfunc="mean"  
    )

    pivot_df.columns.name = None
    pivot_df = pivot_df.sort_index()

    global_row = pivot_df.mean(axis=0)

    pivot_df.loc["GLOBAL"] = global_row

    df_game = pd.read_csv("gameData.csv")

    country_col_game = 'A1'  
    gender_col = 'A2'        
    agree_cols_game = [f'C{i}' for i in range(1, 16)] 

    df_game[country_col_game] = df_game[country_col_game].str.strip().str.upper()


    df_game[gender_col] = df_game[gender_col].str.strip().str.title()

    df_game[agree_cols_game] = df_game[agree_cols_game].apply(pd.to_numeric, errors='coerce').fillna(0)
    df_game[agree_cols_game] = df_game[agree_cols_game].apply(lambda x: (x >= 4).astype(int))

    country_agreement_game = df_game.groupby(country_col_game)[agree_cols_game].mean() * 100
    country_agreement_game = country_agreement_game.reset_index()
    country_agreement_game.columns = [f"Agree: {col}" if col != country_col_game else "Country" for col in country_agreement_game.columns]

    df_game['Country-Gender'] = df_game[country_col_game] + " - " + df_game[gender_col]


    country_gender_agreement = df_game.groupby('Country-Gender')[agree_cols_game].mean() * 100
    country_gender_agreement = country_gender_agreement.reset_index()
    country_gender_agreement.columns = [f"Agree: {col}" if col != 'Country-Gender' else "Country" for col in country_gender_agreement.columns]

    full_agreement_game = pd.concat([country_agreement_game, country_gender_agreement], ignore_index=True)

    full_agreement_game = full_agreement_game.sort_values(by="Country").reset_index(drop=True)

    global_overall = df_game[agree_cols_game].mean() * 100
    global_overall["Country"] = "GLOBAL"
    global_overall = global_overall.rename(lambda x: f"Agree: {x}" if x not in ["Country"] else x)

    global_male = df_game[df_game[gender_col] == "Male"][agree_cols_game].mean() * 100
    global_male["Country"] = "GLOBAL - Male"
    global_male = global_male.rename(lambda x: f"Agree: {x}" if x not in ["Country"] else x)

    global_female = df_game[df_game[gender_col] == "Female"][agree_cols_game].mean() * 100
    global_female["Country"] = "GLOBAL - Female"
    global_female = global_female.rename(lambda x: f"Agree: {x}" if x not in ["Country"] else x)

    global_rows = pd.DataFrame([global_overall, global_male, global_female])

    full_agreement_game = pd.concat([full_agreement_game, global_rows], ignore_index=True)

    full_agreement_game = full_agreement_game.sort_values(by="Country").reset_index(drop=True)



    final_merged = full_agreement_game.merge(pivot_df, how="inner", on="Country")

 
    final_merged_gendered = final_merged[final_merged["Country"].str.contains(" - ")]

    final_merged_non_gendered = final_merged[~final_merged["Country"].str.contains(" - ")]

    final_merged_combined = pd.concat([final_merged_non_gendered, final_merged_gendered], ignore_index=True)

    global_row = final_merged_combined[final_merged_combined["Country"] == "GLOBAL"]

    final_merged_combined = final_merged_combined[final_merged_combined["Country"] != "GLOBAL"]

    final_merged_combined = pd.concat([global_row, final_merged_combined], ignore_index=True)

    final_merged_combined = final_merged_combined.sort_values(by="Country").reset_index(drop=True)

    plot_data = final_merged_combined[["Country", "Strengthening commitments", "Agree: C15"]].copy()


    plot_data = plot_data.dropna(subset=["Strengthening commitments", "Agree: C15"], how='all')

    plot_data = plot_data[~plot_data["Country"].str.contains(" - ")]


    global_row_plot = plot_data[plot_data["Country"] == "GLOBAL"]

    plot_data = plot_data[plot_data["Country"] != "GLOBAL"]

    plot_data = pd.concat([global_row_plot, plot_data], ignore_index=True)

    x = np.arange(len(plot_data)) 
    width = 0.35  

    fig, ax = plt.subplots(figsize=(20, 12))  

    colors = sns.color_palette("colorblind")

    rects1 = ax.bar(x - width/2, plot_data["Strengthening commitments"], width, label="General Population", color=colors[0])
    rects2 = ax.bar(x + width/2, plot_data["Agree: C15"], width, label="ACNH Players", color=colors[1])


    plt.title('Fig 3. Percentage of Population Concerned for Environmental Future', fontweight='bold', fontsize=30, pad=60)
    plt.xlabel('Country', fontweight='bold',fontsize=20)
    plt.ylabel("Percentage", fontweight='bold',fontsize=20)

    plt.yticks(fontsize=20)

    ax.set_xticks(x)
    plt.xticks(rotation=45,fontsize=20)
    ax.set_xticklabels(plot_data["Country"], rotation=45)
    ax.legend()
    plt.legend(
            loc='upper right',
            framealpha=0.9,
            fontsize=20,                
            markerscale=2     
        )

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            if not np.isnan(height):
                ax.annotate(f'{height:.1f}%',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=15)

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    st.pyplot(fig)
    st.write("Fig 3. compares the percentage of select countries' population that are concerned about the enviornment. The percentages for each country are split between the general population and players of Animal Crossing: New Horizons.")
with tab4:
    st.header("Links and References")
    st.markdown("[Our Github](https://github.com/hollai465/FinalProject)")
    st.markdown("[Dataset 1: A multinational dataset of game players’ behaviors in a virtual world and environmental perceptions](https://www.scidb.cn/en/detail?dataSetId=cb5d36cce29f4e5695a586c9b85d04b6&dataSetType=journal)")
    st.markdown("[Dataset 2: The People's Climate Vote](https://peoplesclimate.vote/data-center)")
with tab5:
    st.header("Opinions of ACNH Players by Favorite Activity")
    def categorize_activity(value):
        value = value.lower() if isinstance(value, str) else ''
        if "fish" in value:
            return "fishing"
        elif "bug" in value:
            return "catching bugs"
        elif "villager" in value:
            return "interacting with villagers"
        elif "terraform" in value:
            return "terraforming"
        elif "plant" in value:
            return "planting trees/flowers"
        elif "collect" in value or "catalog" in value:
            return "collecting"
        elif "design" in value or "decor" in value:
            return "designing/decorating"
        else:
            return "other"

    df["D6_Category"] = df["D6"].apply(categorize_activity)

    avg_by_category = df.groupby('D6_Category')[selected_y_column].mean().sort_values()

    if "other" in avg_by_category.index:
        other_value = avg_by_category.pop("other")
        avg_by_category["other"] = other_value  
    
    selected_y_column_2 = st.selectbox(
        'Select the agreement statement to analyze:',
        column_names,
        key="selectbox_y_column_2"
    )

    def update_boxplot(selected_y_column):
        plt.figure(figsize=(20, 12))
        sns.boxplot(x='D6_Category', y=selected_y_column, data=df, palette=sns.color_palette("colorblind"))

        plt.xlabel('Favorite Activity Category\n', fontweight='bold',fontsize=20)
        plt.ylabel('Opinion', fontweight='bold',fontsize=20)
        plt.title(f'Fig 2. Opinion on: {selected_y_column} by Favorite ACNH Activity', fontweight='bold', fontsize=30, pad=60)


        plt.tight_layout()
        plt.xticks(rotation=45,fontsize=20)

        plt.yticks([1, 5], wrapped_y_tick_labels[selected_y_column], rotation=90,fontsize=20)
        for label in plt.gca().get_yticklabels():
            label.set_verticalalignment('center')

        st.pyplot(plt)


    update_boxplot(selected_y_column_2)
    st.write("Fig 2. analyzes the distribution of players' opinions on various enviormental topics, sorted by their favorite activity in the game. Fig 2. uses the same categories as fig 1, and these can be selected between in a similar way. Box plots were used to display the data, which shows the median and quartiles, as well as any outliers.")


    
