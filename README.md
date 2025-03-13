# GenAI-based ATS Tracker

GenAI-based ATS Tracker is an AI-powered Applicant Tracking System designed to streamline the recruitment process by leveraging Generative AI technologies.

## Features

- **Resume Parsing**: Extracts and analyzes key information from resumes.
- **Job Description Matching**: Compares resumes against job descriptions to assess candidate fit.
- **User-Friendly Interface**: Simplifies the recruitment workflow with an intuitive design.

## Technologies Used

- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS  
- **AI Integration**: OpenAI's GPT models for natural language processing  
- **Deployment**: Hosted on Render at [GenAI ATS Tracker](https://genai-based-ats-tracker-1.onrender.com)  

## Installation

To run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akshat12375/GenAi-based-ATS-Tracker.git
   cd GenAi-based-ATS-Tracker
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. **Access the Application**: Navigate to [GenAI ATS Tracker](https://genai-based-ats-tracker-1.onrender.com) or your local instance.
2. **Upload Resume**: Use the provided interface to upload a resume in PDF format.
3. **Input Job Description**: Enter the job description text in the designated field.
4. **Analyze**: Click the "Analyze" button to receive insights on the resume's alignment with the job description.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/akshat12375/GenAi-based-ATS-Tracker/issues).
