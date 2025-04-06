import streamlit as st
from app.recommender import recommend

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("🔍 SHL Assessment Recommender")

query = st.text_area("Paste Job Description or Query 👇", height=150)

if st.button("Recommend Assessments"):
    if query.strip():
        results = recommend(query)
        st.markdown("### 🎯 Top Recommended Assessments")
        for i, res in enumerate(results, 1):
            st.markdown(f"**{i}. [{res['name']}]({res['url']})**")
            st.markdown(f"- **Remote Testing**: {res['remote_testing']}")
            st.markdown(f"- **Adaptive Support**: {res['adaptive_support']}")
            st.markdown(f"- **Test Type**: {res['test_type']}")
            st.markdown("---")
    else:
        st.warning("Please enter a query or job description.")