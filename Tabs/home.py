"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Dermatological Risk Predictor")

    # Add image to the home page
    st.image("./images/home.png", width=1000)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Skin diseases can be attributed to a myriad of factors, encompassing genetics, environmental influences, lifestyle choices, hormonal changes, and various other elements. Understanding the statistical relevance of these factors provides valuable insights into the complex nature of skin conditions.

1. **Genetics (Inherited Factors):**
   Genetic predisposition plays a significant role in the development of skin diseases. Statistical studies indicate that individuals with a family history of certain skin conditions are more likely to experience similar issues. For instance, a study published in the Journal of Investigative Dermatology found a strong genetic basis for conditions like psoriasis and eczema, with heritability estimates ranging from 60% to 90%.

2. **Environmental Factors:**
   Statistical analyses consistently highlight the impact of environmental factors on skin health. Research shows a correlation between air pollution and various skin diseases. A study published in the Journal of Investigative Dermatology revealed a positive association between exposure to air pollution and the development of skin aging signs, such as pigment spots and wrinkles.

3. **Lifestyle Choices:**
   Unhealthy lifestyle choices, including smoking, excessive alcohol consumption, and poor dietary habits, have been linked to skin diseases. Statistical evidence supports these associations. For example, a study in the Journal of Dermatology Science found that smokers had a higher prevalence of acne compared to non-smokers, demonstrating a clear relationship between lifestyle choices and skin health.

4. **Hormonal Changes:**
   Hormonal fluctuations, often occurring during puberty, pregnancy, or menopause, can influence skin conditions. Statistical analyses reveal a higher prevalence of acne during puberty, primarily due to increased androgen levels. Hormonal changes can also contribute to conditions like melasma, as evidenced by studies showing a higher incidence in pregnant women.

5. **Stress Levels:**
   High-stress levels have been consistently linked to exacerbation of various skin conditions. Research published in the Journal of the European Academy of Dermatology and Venereology demonstrated a significant association between stress and the severity of psoriasis. Statistical models revealed a positive correlation, emphasizing the importance of managing stress for skin health.

6. **Immune System Health:**
   The immune system plays a crucial role in skin health, and immune-related disorders can manifest as skin diseases. Statistical studies, such as those published in the Journal of the American Academy of Dermatology, highlight the association between autoimmune disorders like lupus and an increased risk of skin manifestations.

7. **Allergies:**
   Statistical data supports the connection between allergies and skin conditions. For instance, a study in the Journal of the European Academy of Dermatology and Venereology found a higher prevalence of atopic dermatitis in individuals with allergic rhinitis. Allergic reactions can manifest as eczema or urticaria, emphasizing the statistical correlation between allergy and skin diseases.

8. **Excessive Sun Exposure:**
   Statistical analyses consistently link excessive sun exposure to skin diseases, including skin cancer, premature aging, and sunburn. Studies published in JAMA Dermatology reveal a clear association between cumulative sun exposure and the risk of developing melanoma, underscoring the importance of sun protection for skin health.

In conclusion, statistical understanding of the factors influencing skin diseases provides a robust foundation for preventive strategies and targeted interventions. By comprehensively analyzing data, researchers and healthcare professionals can identify trends, risk factors, and potential avenues for personalized approaches to skin health. This statistical insight is instrumental in advancing dermatological research, guiding public health initiatives, and improving patient outcomes.      </p>
    """, unsafe_allow_html=True)