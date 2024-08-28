# Customized-QuestionBank
This project automates question bank management with LaTeX for formatting and Python for options and answers in separate question sets folders. Excel tracks question names, and JSON stores answers. Variables in questions enable randomized paper generation.

# Key Features:

1. **Question Formatting**: LaTeX is used to format the questions, ensuring that they are presented clearly and professionally, especially when dealing with mathematical content or graphs.
2. **Question Creation and Removal**: Python scripts handle the dynamic creation and removal of questions. Variables within the questions can be automatically adjusted, allowing the same template to generate multiple distinct questions.
3. **Question Bank Management**: An Excel sheet is used for adding and managing questions. Each question's metadata, such as difficulty level, topic, and correct answers, is stored systematically.
4. **Answer Storage**: Answers to the questions are stored in a JSON file, allowing for easy retrieval and update of information, and ensuring the system remains scalable.
5. **Automated Question Paper Generation**: The system can generate question papers by selecting a set of questions from the question bank and automatically changing the variables within them. This ensures that each generated paper is unique, making it suitable for repeated use in different contexts.

**Technology Stack**:
- LaTeX: For question formatting and creating PDF documents.
- Python: For handling the logic of question creation, variable adjustment, and question paper generation.
- Excel: For easy management and input of questions.
- JSON: For storing and managing answers and other metadata.
