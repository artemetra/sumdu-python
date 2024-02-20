from fpdf import FPDF
from PIL import Image
from dataclasses import dataclass

# hrd skills
# soft ksils
# desmrprtion
# languwrnfp


@dataclass
class CVData:
    personal_info: dict
    education: list[dict]
    work_experience: list[dict]
    languages: list
    hard_skills: list[str]
    soft_skills: list[str]
    image_path: str


class CVRenderer(FPDF):
    image_x = 10  # X-координата верхнього лівого кута фото
    image_y = 10  # Y-координата верхнього лівого кута фото

    col_offset = 110  # відступ для другої колонки
    y_offset = 80  # вертикальний відступ

    typeface = "Times"
    head_size = 14
    main_size = 12

    def __init__(self):
        super().__init__()

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

    def add_personal_info(self, info: dict):
        self.set_font(self.typeface, "B", self.head_size)
        self.cell(0, 10, f"{info['name']}", 0, 1, "R")
        self.set_font(self.typeface, "", self.main_size)

        if info["address"] is not None:
            self.cell(0, 10, f"{info['address']}", 0, 1, "R")
        if info["phone"] is not None:
            self.cell(0, 10, f"{info['phone']}", 0, 1, "R")
        self.cell(0, 10, f"{info['email']}", 0, 1, "R")
        self.ln(10)

    def add_education(self, edus: list[dict]):
        self.set_x(self.col_offset)
        # self.set_y(self.y_offset)
        # Education header
        self.set_font(self.typeface, "B", self.head_size)
        self.cell(0, 10, "Education", 0, 1, "L")
        for edu in edus:
            self.set_font(self.typeface, "I", self.main_size)
            self.set_x(self.col_offset)
            # self.set_y(self.y_offset)
            self.cell(0, 10, edu["degree"], 0, 1, "L")
            self.set_font("")
            self.set_x(self.col_offset)
            # self.set_y(self.y_offset)
            self.cell(0, 10, f"""{edu["school"]}, {edu["year"]}""", 0, 1, "L")
            # self.set_x(self.col_offset)
            # self.cell(0, 10, f"Year: {year}", 0, 1, "L")

    def add_experience(self, exps: list[dict]):
        # self.set_y(self.y_offset)
        # Work Experience header
        self.set_font(self.typeface, "B", self.head_size)
        self.cell(0, 10, "Work Experience", 0, 1, "L")
        for exp in exps:
            self.set_font(self.typeface, "", self.main_size)
            if exp.get("position"):
                self.cell(0, 10, f"Position: {exp['position']}", 0, 1, "L")
            if exp.get("company"):
                self.cell(0, 10, f"Company: {exp['company']}", 0, 1, "L")
            if exp.get("year"):
                self.cell(0, 10, f"Year: {exp['year']}", 0, 1, "L")
            self.ln(10)

    def add_image(self, image_path, width=50, height=50):
        self.image(image_path, self.image_x, self.image_y, width, height)

    def add_languages(self, languages: list):
        pass

    def add_hard_skills(self, hskills: list):
        pass

    def add_soft_skills(self, sskills: list):
        pass

    def render_data(self, data: CVData):
        self.add_page()
        self.add_image(data.image_path)
        self.add_personal_info(data.personal_info)
        self.add_education(data.education)
        self.add_experience(data.work_experience)


# # Create instance of FPDF class
# data = CVData()

# # Add an image to the data (replace 'path/to/image.jpg' with the actual image path)
# data.add_image("images/joe.png")

# # Add personal information
# data.add_personal_info(
#     "Joe Doe", "joe.doe@company.com", "123 Main St, Cityville", "555-1234"
# )

# # Add education details
# data.add_education(
#     "Bachelor of Science in Computer Science", "University of XYZ", "2016"
# )
# data.add_education("PhD in Computer Science", "University of br", "2084")

# # Add work experience
# data.add_experience("Software Engineer", "ABC Corporation", "2018-2022")
# data.add_experience("Software Engineer 2", "BCD Corporation", "2019-2023")


def create_cv_data() -> CVData:
    cv_data = CVData(
        personal_info={},
        education=[],
        work_experience=[],
        languages=[],
        hard_skills=[],
        soft_skills=[],
        image_path=""
    )

    print("CV Creator")
    for field in ["name", "address", "email", "phone"]:
        cv_data.personal_info[field] = input(f"Enter your {field}: ")

    while True:
        print("Add an education entry:")
        degree = input("Degree: ")
        school = input("School: ")
        year = input("Year: ")
        cv_data.education.append({"degree": degree, "school": school, "year": year})

        add_more = input("Add another education entry? (y/n): ")
        if add_more.lower() != "y":
            break

    while True:
        print("Add a work experience entry:")
        position = input("Position: ")
        company = input("Company: ")
        year = input("Year: ")
        cv_data.work_experience.append(
            {"position": position, "company": company, "year": year}
        )

        add_more = input("Add another work experience entry? (y/n): ")
        if add_more.lower() != "y":
            break

    while True:
        language = input("Enter a language: ")
        cv_data.languages.append(language)

        add_more = input("Add another language? (y/n): ")
        if add_more.lower() != "y":
            break

    while True:
        hard_skill = input("Enter a hard skill: ")
        cv_data.hard_skills.append(hard_skill)

        add_more = input("Add another hard skill? (y/n): ")
        if add_more.lower() != "y":
            break

    while True:
        soft_skill = input("Enter a soft skill: ")
        cv_data.soft_skills.append(soft_skill)

        add_more = input("Add another soft skill? (y/n): ")
        if add_more.lower() != "y":
            break

    cv_data.image_path = input("Enter image path: ")

    return cv_data

if __name__ == "__main__":
    cv_data = create_cv_data()

    renderer = CVRenderer()
    renderer.render_data(cv_data)
    renderer.output(f"{cv_data.personal_info['name']} CV.pdf")
