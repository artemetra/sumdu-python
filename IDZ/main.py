from fpdf import FPDF
from PIL import Image
from dataclasses import dataclass

# hrd skills
# soft ksils
# desmrprtion 
# languwrnfp

@dataclass
class CV_data:
    personal_info: dict 
    education: list[dict]
    work_experience: list[dict]
    languages: list
    hard_skills: list[str]
    soft_skills: list[str]
    

class CV(FPDF):
    image_x = 10  # X-координата верхнього лівого кута фото
    image_y = 10  # Y-координата верхнього лівого кута фото

    col_offset = 110 # відступ для другої колонки
    y_offset = 80 # вертикальний відступ
    
    typeface = "Times"
    head_size = 14
    main_size = 12
    
    def __init__(self):
        super().__init__()
        self.has_experience = False
        self.has_education = False
        self.has_description = False
        
    # def header(self):
    #     self.set_font(self.typeface, "B", self.head_size)
    #     self.cell(0, 10, "Curriculum Vitae", 0, 1, "C")

    def add_description(self, text):
        self.set_font(self.typeface, "I", self.main_size)
        self.cell(0, 10, text)

    # def footer(self):
    #     self.set_y(-15)
    #     self.set_font(self.typeface, "I", 8)
    #     self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_personal_info(self, name, email, address=None, phone=None):
        self.set_font(self.typeface, "B", self.head_size)
        self.cell(0, 10, f"{name}", 0, 1, "R")
        self.set_font(self.typeface, "", self.main_size)

        if address is not None:
            self.cell(0, 10, f"{address}", 0, 1, "R")
        if phone is not None:
            self.cell(0, 10, f"{phone}", 0, 1, "R")
        self.cell(0, 10, f"{email}", 0, 1, "R")
        self.ln(10)

    def add_education(self, degree, school, year):
        self.set_x(self.col_offset)
        # self.set_y(self.y_offset)
        # Education header        
        if not self.has_education:
            self.set_font(self.typeface, "B", self.head_size)
            self.cell(0, 10, "Education", 0, 1, "L")
            self.has_education = True
        
        self.set_font(self.typeface, "I", self.main_size)
        self.set_x(self.col_offset)
        self.cell(0, 10, degree, 0, 1, "L")
        self.set_font("")
        self.set_x(self.col_offset)
        self.cell(0, 10, f"{school}, {year}", 0, 1, "L")
        # self.set_x(self.col_offset)
        # self.cell(0, 10, f"Year: {year}", 0, 1, "L")

    def add_experience(self, position, company, year):
        self.set_y(self.y_offset)
        # Work Experience header
        if not self.has_experience:
            self.set_font(self.typeface, "B", self.head_size)
            self.cell(0, 10, "Work Experience", 0, 1, "L")
            self.has_experience = True
        self.set_font(self.typeface, "", self.main_size)
        self.cell(0, 10, f"Position: {position}", 0, 1, "L")
        self.cell(0, 10, f"Company: {company}", 0, 1, "L")
        self.cell(0, 10, f"Year: {year}", 0, 1, "L")
        self.ln(10)

    def add_image(self, image_path, width=50, height=50):
        self.image(image_path, self.image_x, self.image_y, width, height)


# Create instance of FPDF class
cv = CV()

# Add a page
cv.add_page()

# Add an image to the cv (replace 'path/to/image.jpg' with the actual image path)
cv.add_image("images/joe.png")

# Add personal information
cv.add_personal_info(
    "Joe Doe", "joe.doe@company.com", "123 Main St, Cityville", "555-1234"
)

# Add education details
cv.add_education("Bachelor of Science in Computer Science", "University of XYZ", "2016")
cv.add_education("PhD in Computer Science", "University of br", "2084")

# Add work experience
cv.add_experience("Software Engineer", "ABC Corporation", "2018-2022")

# Save the cv with name .pdf
cv.output("cv_with_image.pdf")
