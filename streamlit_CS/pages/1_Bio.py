import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Li Mei"
PROGRAM = "CS"
INTRO = (
    "HI Everyone  "
    "Night owls sleep less than 4 hours"
    "or more than 9 hours, nothing inbetween, Test"
)
FUN_FACTS = [
    "I love Nights",
    "I’m learning to work with Data",
    "I want to build computing Systems",
]
PHOTO_PATH = "your_photo.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
