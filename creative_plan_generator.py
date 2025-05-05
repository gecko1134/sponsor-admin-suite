import streamlit as st

def run():
    st.title("🎨 Creative Sponsor Plan Generator")

    budget = st.number_input("Enter Sponsor Budget ($)", value=3000, step=100)
    name = st.text_input("Sponsor or Business Name (optional)")

    st.markdown("---")

    if budget <= 1000:
        st.subheader("💡 Suggested Plan (Low Budget)")
        st.write(f"- In-kind donation: sponsor signage, supplies, or water bottles")
        st.write(f"- Fund registration for 1–2 youth athletes")
        st.write(f"- Name/logo on shared community banner or team warmups")
        st.write(f"- Listed as scholarship sponsor on website or thank-you wall")
    elif 1000 < budget <= 5000:
        st.subheader("💡 Suggested Plan (Mid-Tier Budget)")
        st.write(f"- Co-sponsor scoreboard or high-exposure banner")
        st.write(f"- Cover 4–6 athlete memberships or a full team’s fees")
        st.write(f"- Branded equipment or training gear (in-kind or branded)")
        st.write(f"- Monthly payment option: ${budget//12}/mo for 12 months")
        st.write(f"- Social media + digital listing as community partner")
    elif budget > 5000:
        st.subheader("💡 Suggested Plan (Premium Sponsor)")
        st.write(f"- Priority naming rights to high-traffic zone or field")
        st.write(f"- Full tournament or team jersey sponsorship")
        st.write(f"- Branded video board ad rotation or facility signage")
        st.write(f"- Add-on: athlete scholarship fund or regional travel support")
        st.write(f"- Option to spread over 2–3 years with benefits scaling annually")

    st.markdown("---")

    st.subheader("📝 Summary")
    summary = f"""
**Sponsor Budget:** ${budget:,.2f}  
**Sponsor Name:** {name or "N/A"}  
**Plan Type:** {"Low" if budget<=1000 else "Mid" if budget<=5000 else "Premium"}  
**Key Recommendation:** Diversify visibility with scholarships, signage, and payment options.
"""
    st.markdown(summary)
