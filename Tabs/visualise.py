"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
'''from sklearn.metrics import plot_confusion_matrix'''
from sklearn import tree
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise Skin Ailment Demographics")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (14, 8))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)


    if st.checkbox("Show Sample Results"):
        fig = plt.figure(figsize = (14, 8))
        safe = (df['Disease_Severity'] == 1).sum()
        okay = (df['Disease_Severity'] == 2).sum()
        care = (df['Disease_Severity'] == 3).sum()
        prone = (df['Disease_Severity'] == 4).sum()
        danger = (df['Disease_Severity'] == 5).sum()
        
        data = [safe,okay,care,prone,danger]
        labels = ['Safe', 'Okay', 'Care', 'Prone','Danger']
        colors = sns.color_palette('pastel')[0:5]
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        st.pyplot()

    '''if st.checkbox("Plot confusion matrix"):
        model, score = train_model(X, y)
        plt.figure(figsize = (10, 6))
        plot_confusion_matrix(model, X, y, values_format='d')
        st.pyplot()'''

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(X, y)
        # Export decision tree in dot format and store in 'dot_data' variable.
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['1', '2', '3', '4','5']
        )
        # Plot the decision tree using the 'graphviz_chart' function of the 'streamlit' module.
        st.graphviz_chart(dot_data)

