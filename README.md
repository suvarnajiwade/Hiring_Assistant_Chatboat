# Hiring_Assistant_Chatboat
Hiring Assistant Chatbot – Project Documentation
1. Project Overview
The Hiring Assistant Chatbot is designed to streamline the recruitment process for a fictional agency, TalentScout. It gathers candidate information,
generates technical questions based on the candidate’s tech stack, and maintains context throughout interactions.
 The chatbot uses a pre-trained LLM model (such as GPT-3/4) to craft relevant technical questions dynamically, ensuring an engaging and personalized experience for candidates.


3. Installation Instructions
Follow these steps to set up and run the application locally:
1. Clone the repository: `git clone https://github.com/your-repo-link.git`
2. Navigate to the project directory: `cd hiring_assistant_chatbot`
3. Create a virtual environment: `python -m venv hiring_assistant_env`
4. Activate the virtual environment:
   - On Windows: `hiring_assistant_env\Scripts\activate`
   - On Mac/Linux: `source hiring_assistant_env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `streamlit run chatbot.py`


4. Usage Guide
1. Launch the application by running `streamlit run chatbot.py`.
2. Fill in candidate details such as name, position, and tech stack.
3. The chatbot generates relevant technical questions for the candidate.
4. After completion, the responses are recorded for further review.
4. Technical Details
Libraries Used:
- Python 3.10
- Flask
- Streamlit
- OpenAI API
- Pandas
- LangChain

Model Details:
- Pre-trained model: GPT-3/4
Architectural Decisions:
- Used Flask backend to handle API requests.
- Integrated Streamlit for an interactive frontend.
- CSV file used for dynamic question generation.


5. Prompt Design
The prompts were carefully designed to ensure relevant technical questions are generated based on the candidate's selected position and skillset.
The prompt templates were created with a balance of open-ended and specific questions to evaluate the candidate’s proficiency effectively.
7. Challenges & Solutions
Challenge 1: Exceeding API quota limits
Solution: Implemented API key rotation and monitored usage more effectively.

Challenge 2: Error loading and tokenizing CSV files
Solution: Verified CSV file structure, corrected formatting issues, and improved error handling.

Challenge 3: Issues with dynamic prompt generation
Solution: Refined prompt templates and ensur
