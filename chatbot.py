import streamlit as st
import openai
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# --------------- API Key Configuration ---------------
# Set your OpenAI API key here
openai.api_key = "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"

# --------------- File Path for Storing Data ---------------
DATA_FILE = "candidate_data.csv"

# --------------- Function to Save Candidate Info ---------------
def save_candidate_data(data):
    """Save candidate information to a CSV file."""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
    else:
        df = pd.DataFrame(columns=data.keys())
    
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# --------------- Function to Generate Technical Questions ---------------
def generate_questions(tech_stack):
    """Generate 5 technical questions based on the candidate's tech stack."""
    prompt = f"Generate 5 technical interview questions to assess proficiency in the following tech stack: {tech_stack}. Ensure diversity in the questions and cover practical concepts."
    
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response['choices'][0]['text'].strip().split('\n')
    except Exception as e:
        return [f"Error generating questions: {str(e)}"]

# --------------- Chatbot UI Setup ---------------
st.set_page_config(page_title="TalentScout - Hiring Assistant", page_icon="🤖", layout="wide")

# --------------- Chatbot Title and Introduction ---------------
st.title("🤖 Hiring Assistant Chatbot - TalentScout")
st.markdown(
    """
    Welcome to TalentScout! I am here to assist you in the initial screening process.
    Please provide the required details, and I will generate relevant technical questions to evaluate your skills.
    """
)

# --------------- Candidate Information Collection ---------------
with st.form("candidate_form"):
    st.subheader("📝 Candidate Information")
    name = st.text_input("Full Name", placeholder="Enter your full name...")
    email = st.text_input("Email Address", placeholder="Enter your email...")
    phone = st.text_input("Phone Number", placeholder="Enter your phone number...")
    experience = st.slider("Years of Experience", 0, 20, 1)
    position = st.text_input("Desired Position(s)", placeholder="Enter desired positions...")
    location = st.text_input("Current Location", placeholder="Enter your current location...")
    tech_stack = st.text_area("Tech Stack", placeholder="List technologies, frameworks, and tools (e.g., Python, Django, SQL)...")

    submit_button = st.form_submit_button("Submit Information")

# --------------- Handling Form Submission ---------------
if submit_button:
    if not all([name, email, phone, position, tech_stack]):
        st.error("⚠️ Please fill in all required fields.")
    else:
        # Prepare candidate data
        candidate_data = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Experience": experience,
            "Position": position,
            "Location": location,
            "Tech Stack": tech_stack
        }

        # Save candidate data
        save_candidate_data(candidate_data)
        st.success(f"✅ Thank you, {name}! Your information has been recorded successfully.")
        
        # Generate technical questions
        st.info("🎯 Generating technical questions based on your tech stack...")
        questions = generate_questions(tech_stack)

        if questions:
            st.subheader("🔍 Technical Questions:")
            for i, question in enumerate(questions, 1):
                st.write(f"{i}. {question}")
        else:
            st.error("❌ Unable to generate questions at this time. Please try again later.")
        
        # Closing message
        st.markdown(
            """
            ### 📩 Next Steps:
            1. Our team will review your responses.
            2. We will contact you for the next phase if you meet the criteria.
            3. Thank you for applying through TalentScout!
            """
        )

# --------------- Fallback Mechanism for Unexpected Inputs ---------------
def handle_unexpected_input(user_input):
    """Provide fallback response for unexpected user inputs."""
    fallback_responses = [
        "🤔 I'm not sure I understood that. Could you please rephrase?",
        "🙌 Let's stay focused on gathering your information. How can I help?",
        "❗ If you’re facing issues, please provide the requested details again."
    ]
    return fallback_responses[0]

# --------------- Graceful Exit Mechanism ---------------
def end_conversation():
    """End the conversation with a thank-you message."""
    st.write("🎉 Thank you for using TalentScout! We appreciate your time. Goodbye! 👋")


import pandas as pd

# Function to save candidate data to a CSV file
def save_to_csv(data):
    file_name = "candidate_data.csv"

    # Convert dictionary to DataFrame
    df = pd.DataFrame(data, index=[0])

    # Append to CSV, create new if it doesn't exist
    try:
        df.to_csv(file_name, mode="a", header=not pd.read_csv(file_name).empty, index=False)
    except FileNotFoundError:
        df.to_csv(file_name, mode="w", index=False)

def send_email_confirmation(name, email):
    """Send confirmation email to the candidate."""
    sender_email = "your-email@gmail.com"  # Your email address
    sender_password = "your-app-password"  # App password or email password
    subject = "Application Received - TalentScout"

    # Email content template
    body = f"""
    Dear {name},

    Thank you for applying to TalentScout. We have successfully received your application.
    Our team is currently reviewing your profile. If your qualifications match our requirements, 
    we will contact you shortly to discuss the next steps.

    Please feel free to reach out if you have any questions.

    Best Regards,  
    TalentScout Recruitment Team
    """

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print(f"✅ Confirmation email successfully sent to {email}.")
    except Exception as e:
        print(f"⚠️ Error sending email: {e}")

        send_email_confirmation(name, email)


import pandas as pd

def get_questions(position, tech_stack):
    """Fetch relevant technical questions based on position and skills."""
    try:
        # Load questions from CSV
        df = pd.read_csv("questions.csv")
        questions = []

        for skill in tech_stack.split(","):
            skill = skill.strip().lower()
            
            # Filter questions matching the position and skill
            position_questions = df[
                (df["position"].str.lower() == position.lower()) &
                (df["skill"].str.lower() == skill)
            ]["question"].tolist()

            if position_questions:
                questions.extend(position_questions)

        return questions[:5]  # Return a maximum of 5 questions
    except Exception as e:
        print(f"⚠️ Error loading questions: {e}")
        return []
# Generate and display relevant questions
questions = get_questions(position, tech_stack)
if questions:
    st.subheader("📚 Suggested Technical Questions:")
    for i, question in enumerate(questions, start=1):
        st.write(f"{i}. {question}")
else:
    st.warning("No relevant questions found for the selected position and tech stack.")



