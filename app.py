from dotenv import load_dotenv
import base64
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(file):
    if file:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an experienced software developer with having expertise in full stack development,data science,machine learning,
devops,cyber security analyze the candidate's profile with the job description provided and provide how can the person improve their skill to become fit for the job
provide the result in a step wise detailed format.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'Please upload a resume'})
    
    file = request.files['resume']
    job_description = request.form.get('job_description')
    action_type = request.form.get('action_type')

    if not file:
        return jsonify({'error': 'Please upload a resume'})

    try:
        pdf_content = input_pdf_setup(file)
        
        if action_type == 'tell_about_resume':
            response = get_gemini_response(input_prompt1, pdf_content, job_description)
        elif action_type == 'improve_skills':
            response = get_gemini_response(input_prompt2, pdf_content, job_description)
        elif action_type == 'percentage_match':
            response = get_gemini_response(input_prompt3, pdf_content, job_description)
        else:
            return jsonify({'error': 'Invalid action type'})

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()




