import fitz  # PyMuPDF

def extract_text_and_images(pdf_file):
    # Open the PDF file
    doc = fitz.open(pdf_file)
    
    text = ""
    images = []
    
    # Loop through the pages
    for page_number in range(len(doc)):
        page = doc[page_number]
        
        # Extract text
        text += page.get_text()
        
        # Extract images
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"image_page{page_number+1}_{img_index}.{image_ext}"
            
            # Save the image
            with open(image_name, "wb") as image_file:
                image_file.write(image_bytes)
            
            images.append(image_name)
    
    return text, images
