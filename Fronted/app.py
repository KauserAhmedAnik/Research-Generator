
"""
app.py

Main Streamlit application.
"""

import streamlit as st

from api import (
    generate_report,
    get_reports,
    delete_report,
    download_report,
)


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Multi-Agent Research & Report Writer",
    page_icon="📚",
    layout="wide",
)


# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("📚 Research Writer")

st.sidebar.markdown(
    """
Generate professional research reports using
multiple AI agents powered by CrewAI.
"""
)

st.sidebar.divider()

if st.sidebar.button("Refresh History"):
    st.rerun()


# ==========================================================
# Main Title
# ==========================================================

st.title("📚 Multi-Agent Research & Report Writer")

st.write(
    "Generate professional research reports "
    "using multiple AI agents."
)


# ==========================================================
# Topic Input
# ==========================================================

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Artificial Intelligence in Healthcare",
)


# ==========================================================
# Generate Button
# ==========================================================

if st.button(
    "Generate Report",
    type="primary",
):

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        with st.spinner(
            "Research agents are working..."
        ):

            try:

                report = generate_report(topic)

                st.success(
                    "Report generated successfully."
                )

                st.subheader("Generated Report")

                st.markdown(report["report"])

                # --------------------------------------------------
                # PDF Download
                # --------------------------------------------------

                try:

                    pdf_data = download_report(
                        report["id"]
                    )

                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_data,
                        file_name=f"research_report_{report['id']}.pdf",
                        mime="application/pdf",
                    )

                except Exception as download_error:

                    st.warning(
                        f"PDF download unavailable: {download_error}"
                    )

            except Exception as e:

                st.error(str(e))


# ==========================================================
# Report History
# ==========================================================

st.divider()

st.header("Generated Reports")

try:

    reports = get_reports()

    if len(reports) == 0:

        st.info("No reports generated yet.")

    else:

        for report in reports:

            with st.expander(
                report["topic"]
            ):

                st.write(
                    f"Status : {report['status']}"
                )

                st.write(
                    f"Generation Time : "
                    f"{report['generation_time']} sec"
                )

                st.markdown(
                    report["report"]
                )

                # --------------------------------------------------
                # Download PDF from History
                # --------------------------------------------------

                try:

                    pdf_data = download_report(
                        report["id"]
                    )

                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_data,
                        file_name=f"research_report_{report['id']}.pdf",
                        mime="application/pdf",
                        key=f"download_{report['id']}",
                    )

                except Exception as download_error:

                    st.warning(
                        f"PDF download unavailable: {download_error}"
                    )

                # --------------------------------------------------
                # Delete
                # --------------------------------------------------

                if st.button(
                    "Delete",
                    key=f"delete_{report['id']}",
                ):

                    try:

                        delete_report(
                            report["id"]
                        )

                        st.success(
                            "Report deleted."
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"Delete failed: {e}"
                        )

except Exception:

    st.info(
        "Backend is not running."
    )

