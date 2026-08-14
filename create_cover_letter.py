from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import datetime
import os

def create_pdf():
    output_path = r"C:\Users\pfili\Downloads\Cover_Letter_Pietro_Filippo_Schgor.pdf"
    
    # Ensure the Downloads directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            rightMargin=inch, leftMargin=inch,
                            topMargin=inch, bottomMargin=inch)
    
    styles = getSampleStyleSheet()
    # Modify normal style to look like a standard letter
    normal_style = styles["Normal"]
    normal_style.fontName = "Times-Roman"
    normal_style.fontSize = 12
    normal_style.leading = 18
    normal_style.spaceAfter = 12
    normal_style.alignment = 4 # Justify
    
    # Create a custom style for the date
    date_style = ParagraphStyle(
        'DateStyle',
        parent=normal_style,
        spaceAfter=24,
        alignment=0 # Left
    )
    
    # Custom style for greeting
    greeting_style = ParagraphStyle(
        'GreetingStyle',
        parent=normal_style,
        spaceAfter=12,
        alignment=0 # Left
    )

    signoff_style = ParagraphStyle(
        'SignoffStyle',
        parent=normal_style,
        spaceAfter=0,
        alignment=0 # Left
    )

    Story = []
    
    # Date
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    Story.append(Paragraph(date_str, date_style))
    
    # Greeting
    Story.append(Paragraph("Dear Hiring Manager,", greeting_style))
    
    # Body
    body_paragraphs = [
        "I am writing to express my strong enthusiasm for the Data Scientist position at Bending Spoons. Bending Spoons stands out to me as the absolute best tech and data company to work for in Italy. It represents a true source of Italian pride in the global tech landscape, and I would be incredibly honored to bring my dedication and skills to your reality.",
        "Taking on this role feels like the natural continuation of an academic journey that I am extremely proud of and passionate about. I am currently completing my Master's degree in Mathematical Engineering with a specialization in Statistical Learning at Politecnico di Milano. My studies have given me a robust theoretical foundation, but I am particularly enthusiastic about the practical applications I have explored. I have a strong interest in classical regression methods, which I have applied thoroughly in my exams and hands-on projects. A key example is my work utilizing non-linear regression and functional data analysis in R to analyze the effects of ionizing radiations on microcirculation for the Istituto Nazionale dei Tumori.",
        "Alongside classical statistics, I have cultivated a deep expertise in Artificial Neural Networks and Deep Learning. This is heavily reflected in my ongoing thesis, which focuses on Cross-Modal Medical Image Synthesis for MRI and PET scans. For this project, I have been developing PyTorch-based frameworks using 3D GANs and transformers to synthesize expensive medical modalities from single baseline scans. My practical experience is further supported by my participation in Artificial Neural Networks Kaggle challenges, where I tackled time series classification via LSTMs and histological image classification via CNNs.",
        "I am eager to bring my analytical rigor and genuine enthusiasm to the Bending Spoons team. Thank you for considering my application. I look forward to the opportunity to discuss how my background and drive can contribute to your continued success."
    ]
    
    for p in body_paragraphs:
        Story.append(Paragraph(p, normal_style))
        
    # Sign off
    Story.append(Paragraph("Sincerely,", signoff_style))
    Story.append(Spacer(1, 0.4 * inch))
    Story.append(Paragraph("Pietro Filippo Schgor", signoff_style))
    
    doc.build(Story)
    print(f"Successfully generated PDF at: {output_path}")

if __name__ == "__main__":
    create_pdf()
