from utils.pdf_generator import PDFGenerator

generator = PDFGenerator()

pdf_path = generator.generate(
    topic="Test Research Report",
    markdown="# Test Report\n\nThis is a test PDF.",
    output_path="reports/test_report.pdf",
)

print(f"PDF created at: {pdf_path}")