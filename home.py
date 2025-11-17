import streamlit as st

# Page config
st.set_page_config(page_title="Shape Drawer", layout="centered")

# Title
st.title("🎨 Shape Drawing Controller")
st.write("Click a button to draw a shape")

# Create 4 columns for buttons
col1, col2 = st.columns(2)

with col1:
    # Triangle button (blue)
    if st.button("Blue", use_container_width=True, type="primary"):
        st.success("Turning Blue!!")
        # Add your Raspberry Pi code here
        # draw_triangle()
        
    # Circle button (green)  
    if st.button("Green", use_container_width=True, type="secondary"):
        st.success("Turning Green!!")
        # Add your Raspberry Pi code here
        # draw_circle()

with col2:
    # Square button (red)
    if st.button("Yellow", use_container_width=True, type="primary"):
        st.success("Turning Yellow!!")
        # Add your Raspberry Pi code here
        # draw_square()
        
    # Line button (yellow)
    if st.button("Red", use_container_width=True, type="secondary"):
        st.success("Turning Red!!")
        # Add your Raspberry Pi code here
        # draw_line()

# Status display
st.divider()
st.write("**Status:** Ready to draw")

# Instructions
with st.expander("Turn"):
    st.write("Hello")
