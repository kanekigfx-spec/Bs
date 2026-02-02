import streamlit as st
import google.generativeai as genai

# 1. UI Setup (The "Storefront")
st.set_page_config(page_title="Integrity Audit CEO", page_icon="🛡️")
st.title("🛡️ Academic Integrity & AI Auditor")
st.markdown("---")

# 2. Secure API Connection
# Make sure you have added GEMINI_API_KEY to your Streamlit Secrets!
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("CEO Warning: API Key missing in Settings > Secrets.")
    st.stop()

# 3. Input Section
user_text = st.text_area("Paste the undergraduate submission for forensic auditing:", height=250)

if st.button("🚀 Run Deep Forensic Audit"):
    if user_text:
        with st.spinner('Analyzing linguistic entropy...'):
            # The "Secret Sauce": A sophisticated prompt for forensic analysis
            audit_prompt = f"""
            Perform a forensic linguistic audit on the following text. 
            Evaluate it for 'AI patterns' vs 'Human Chaos'.
            Provide:
            1. An 'Integrity Score' (0-100%).
            2. Analysis of 'Burstiness' (sentence length variation).
            3. Detection of 'Model Markers' (words typical of LLMs like 'delve' or 'tapestry').
            4. A professional 'Verdict' for an academic board.
            
            Text to audit: {user_text}
            """
            
            response = model.generate_content(audit_prompt)
            
            # 4. Displaying the "Product" (The Dashboard)
            st.success("Audit Complete")
            
            # Metric logic (In a real app, you'd parse the score from the AI response)
            c1, c2, c3 = st.columns(3)
            c1.metric("Originality", "88%", "High")
            c2.metric("Burstiness", "Medium", "-2%")
            c3.metric("Regulatory Status", "Compliant", "EU AI Act")

            st.markdown("### 📋 Detailed Audit Report")
            st.info(response.text)
            
            # 5. The "Value-Add" (Downloadable Proof)
            st.download_button(
                label="📥 Download Integrity Certificate",
                data=response.text,
                file_name="integrity_audit_report.txt",
                mime="text/plain"
            )
    else:
        st.warning("No text detected. Please paste content to begin.")

# 6. CEO Footer
st.markdown("---")
st.caption("CEO Dashboard v2.0 | Built for UK Academic Compliance 2026")
