#!/usr/bin/env python3
"""
PDF to Markdown Converter for LME Options Trading Specifications
"""

import sys
import fitz  # PyMuPDF
import os
from pathlib import Path

def extract_text_from_pdf(pdf_path, output_md_path):
    """Extract text from PDF and save as Markdown"""
    try:
        doc = fitz.open(pdf_path)
        
        # Extract filename without extension for title
        filename = Path(pdf_path).stem
        
        # Create markdown content
        md_content = f"# {filename}\n\n"
        md_content += f"*Source: {os.path.basename(pdf_path)}*\n\n"
        md_content += "---\n\n"
        
        # Extract text from each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            
            # Add page separator
            if page_num > 0:
                md_content += f"\n\n---\n*Page {page_num + 1}*\n\n"
            
            # Clean up the text and add to markdown
            cleaned_text = text.strip()
            if cleaned_text:
                md_content += cleaned_text + "\n"
        
        # Write to markdown file
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✓ Converted: {pdf_path} -> {output_md_path}")
        print(f"  Pages: {len(doc)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error converting {pdf_path}: {str(e)}")
        return False

def main():
    """Main function to convert all PDFs in raw directory"""
    raw_dir = Path("raw")
    output_dir = Path("docs/specs")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all PDF files
    pdf_files = list(raw_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in raw/ directory")
        sys.exit(1)
    
    print(f"Found {len(pdf_files)} PDF files to convert:\n")
    
    success_count = 0
    for pdf_file in pdf_files:
        # Create output markdown filename
        md_filename = pdf_file.stem + ".md"
        output_path = output_dir / md_filename
        
        # Convert PDF to Markdown
        if extract_text_from_pdf(str(pdf_file), str(output_path)):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion complete: {success_count}/{len(pdf_files)} files converted successfully")
    
    if success_count == len(pdf_files):
        print("✓ All files converted successfully!")
    else:
        print(f"✗ {len(pdf_files) - success_count} files failed to convert")
        sys.exit(1)

if __name__ == "__main__":
    main()
