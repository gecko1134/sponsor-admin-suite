[![Launch Admin Suite](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gecko1134-sponsor-admin-suite.streamlit.app)

---
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gecko1134-sponsor-admin-suite.streamlit.app)

**[Launch Admin Dashboard](https://gecko1134-sponsor-admin-suite.streamlit.app)**

---
# Sponsor Admin Suite

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)

This is a secure Sponsor Admin Dashboard built with Streamlit for managing:
- Sponsor onboarding
- User accounts
- Pricing tools
- Contract generation
- Analytics and logs
- Password reset token management

## 🚀 How to Deploy

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run locally:
```
streamlit run app.py
```

3. Or deploy on [Streamlit Cloud](https://streamlit.io/cloud)

## 🛠️ Admin Login

- **Username**: `admin`
- **Password**: `secure123`

These can be changed in `app.py`.

## 📂 Files

- `app.py`: Admin dashboard entry point
- `sponsor_admin_onboarding.py`: Add sponsors
- `sponsor_admin_user_manager.py`: Edit/delete sponsors
- `sponsor_admin_token_manager.py`: Manage reset tokens
- `sponsorship_pricing_app.py`: Run AI pricing
- `sponsorship_contract_app.py`: Generate contracts
- `fill_sponsorship_contract.py`: Populate contract template
- `sponsorship_agreement_template.docx`: Word template for contracts
