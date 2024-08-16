import streamlit as st
from extract import extract_text_and_images
from summarize import summarize_text
from PIL import Image

def main():
    st.title("PDF Text and Image Extraction with Summarization")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save the uploaded PDF
        with open("uploaded.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("## Extracted Text and Images")
        
        # Extract text and images
        text, images = extract_text_and_images("uploaded.pdf")
        
        # Display the extracted text
        st.subheader("Extracted Text")
        st.text_area("Text from PDF:", text, height=300)
        
        # Perform and display text summarization
        st.subheader("Summarized Text")
        summary = summarize_text(text)
        st.text_area("Summary:", summary, height=150)
        
        # Display the extracted images
        st.subheader("Extracted Images")
        if images:
            for image_path in images:
                img = Image.open(image_path)
                st.image(img, caption=image_path, use_column_width=True)
        else:
            st.write("No images found in the PDF.")

if __name__ == "__main__":
    main()
