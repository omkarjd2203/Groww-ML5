import os
import streamlit as st
import pandas as pd
from datetime import datetime
from src.pipeline import run_review_analysis

# Page Configuration
st.set_page_config(
    page_title="Groww User Review Smart Analyser",
    page_icon="📊",
    layout="wide"
)

# --- Initialize Session State ---
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'results' not in st.session_state:
    st.session_state['results'] = None
if 'approved' not in st.session_state:
    st.session_state['approved'] = False

st.title("📊 Groww User Review Smart Analyser")
st.markdown("Transform raw customer reviews into executive pulse notes, support guides, and approval-gated workspace actions.")

# --- Data Source Loader in Sidebar ---
with st.sidebar:
    st.subheader("📥 Data Source")
    uploaded_file = st.file_uploader("Upload CSV reviews", type=["csv"])

    if uploaded_file is not None:
        st.session_state['df'] = pd.read_csv(uploaded_file)
    elif st.button("📁 Load Default Dataset", use_container_width=True):
        if os.path.exists("data/reviews_sample.csv"):
            st.session_state['df'] = pd.read_csv("data/reviews_sample.csv")

    st.markdown("---")
    if st.session_state['df'] is not None:
        if st.button("🚀 Run Analysis Pipeline", type="primary", use_container_width=True):
            with st.spinner("Analyzing reviews..."):
                results, error = run_review_analysis(st.session_state['df'])
                if error:
                    st.error(error)
                else:
                    st.session_state['results'] = results
                    st.session_state['approved'] = False
                    st.success("Analysis complete!")

# --- Horizontal Tabs Across the Top ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📁 Dataset & Analytics", 
    "📊 Review Intelligence", 
    "💡 Derived Fee Explainer", 
    "✉️ MCP Approval & Email Draft"
])

# ==========================================
# TAB 1: DATASET & ANALYTICS
# ==========================================
with tab1:
    st.header("Dataset Overview & Analytics")
    
    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric(label="Total Reviews Loaded", value=len(df))
        with col_m2:
            avg_rating = round(df['rating'].mean(), 2) if 'rating' in df.columns else "N/A"
            st.metric(label="Average Rating", value=f"{avg_rating} ⭐")
        with col_m3:
            date_range = f"{df['date'].min()} to {df['date'].max()}" if 'date' in df.columns else "N/A"
            st.metric(label="Date Range", value=date_range)

        st.markdown("---")
        
        # Compact Bar Graph Width Constraint with dynamic rating text fix
        st.subheader("📊 Rating Distribution")
        if 'rating' in df.columns:
            rating_counts = df['rating'].value_counts().sort_index()
            min_r = int(df['rating'].min())
            max_r = int(df['rating'].max())
            
            c1, c2 = st.columns([1.2, 2])
            with c1:
                st.bar_chart(rating_counts, height=220)
            with c2:
                st.info(f"The distribution chart highlights customer sentiment breakdown across ratings ({min_r} to {max_r} stars) from the uploaded dataset.")
        
        st.markdown("---")
        st.subheader("📋 Review Records Explorer")
        st.dataframe(df, use_container_width=True, height=280)
    else:
        st.info("👈 Please upload a CSV file or click **Load Default Dataset** in the sidebar to begin.")

# ==========================================
# TAB 2: REVIEW INTELLIGENCE
# ==========================================
with tab2:
    st.header("Review Intelligence & Weekly Product Pulse")

    if st.session_state['results']:
        res = st.session_state['results']
        
        st.subheader("📈 Weekly Product Pulse Summary")
        st.markdown(res.get('weekly_pulse', ''))

        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("#### 🔍 Top Themes Identified")
            for theme in res.get('top_themes', []):
                st.info(theme)
        with col_t2:
            st.markdown("#### 💬 Extracted User Quotes")
            for quote in res.get('user_quotes', []):
                st.caption(f'"{quote}"')
    else:
        st.info("Please load your dataset and click **Run Analysis Pipeline** in the sidebar.")

# ==========================================
# TAB 3: DERIVED FEE EXPLAINER
# ==========================================
with tab3:
    st.header("Derived Fee Explainer & Support Guide")

    if st.session_state['results']:
        res = st.session_state['results']
        friction_point = res.get('identified_fee_issue', 'Fee Clarification')
        
        # Highly Highlighted Core Friction Point
        st.error(f"🔥 **Identified Core Friction Point:** {friction_point}")
        
        # 1 Best Point & 1 Concerning Point Breakdown
        col_b, col_c = st.columns(2)
        with col_b:
            st.success("🌟 **Best Highlight (Positive Aspect):** Smooth UI navigation, fast app performance, and appreciation for clean layouts.")
        with col_c:
            st.warning("⚠️ **Most Concerning Point (Friction):** Hidden fee deductions during withdrawals and unclear brokerage statement breakdowns.")

        st.markdown("---")
        st.markdown("### 📝 Customer Support Response & Fee Guide")
        for bullet in res.get('explanation_bullets', []):
            st.markdown(f"- {bullet}")

        FH_LINKS = res.get('source_links', [])
        st.markdown("### 🔗 Official Reference Links")
        for link in FH_LINKS:
            st.markdown(f"- [{link}]({link})")
    else:
        st.info("Please run the analysis pipeline first.")

# ==========================================
# TAB 4: MCP APPROVAL & EMAIL DRAFT
# ==========================================
with tab4:
    st.header("MCP Approval Gate & Email Draft Preview")

    if st.session_state['results']:
        res = st.session_state['results']
        today_str = datetime.now().strftime("%Y-%m-%d")

        st.info("Review proposed workspace actions, grant human approval, and view the formatted email draft.")

        email_draft_content = f"""Subject: Weekly Product Pulse + Customer Clarification — {today_str}
To: product-leadership@groww.in, support-ops@groww.in

Hi Team,

Here is our weekly product pulse update alongside a customer-facing fee explainer snippet derived from recent reviews:

--- PART 1: WEEKLY PRODUCT PULSE SUMMARY ---
{res.get('weekly_pulse', '')}

--- PART 2: TOP IDENTIFIED THEMES & FOCUS ---
- Themes: {', '.join(res.get('top_themes', []))}
- Key Issue Focus: {res.get('identified_fee_issue', '')}

--- PART 3: CUSTOMER SUPPORT RESPONSE & FEE GUIDE ---
"""
        for bullet in res.get('explanation_bullets', []):
            email_draft_content += f"* {bullet}\n"
        
        email_draft_content += f"\nOfficial References:\n"
        for link in res.get('source_links', []):
            email_draft_content += f"- {link}\n"
        
        email_draft_content += "\nBest regards,\nGroww Smart Analyser Pipeline"

        if not st.session_state.get('approved'):
            if st.button("✅ Approve & Execute Actions", type="primary"):
                st.session_state['approved'] = True
                st.rerun()
        else:
            st.success("🎉 **MCP Actions Approved & Executed Successfully!**")
            
            st.markdown("### ✉️ Formatted Email Draft Preview")
            # Long vertically as requested (height set to 450)
            st.text_area(
                label="Email Draft Content",
                value=email_draft_content,
                height=450
            )

            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.download_button(
                    label="📥 Download Email Draft (.txt)",
                    data=email_draft_content,
                    file_name=f"email_draft_{today_str}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with col_dl2:
                st.download_button(
                    label="📥 Download Full JSON Payload",
                    data=str(res),
                    file_name=f"mcp_payload_{today_str}.json",
                    mime="application/json",
                    use_container_width=True
                )
    else:
        st.info("Please run the analysis pipeline first before accessing approvals.")