import streamlit as st
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Productive Buddy", page_icon="🤖", layout="centered")

st.title("🤖 AI Productive Buddy")
st.write("Your AI-powered assistant to boost focus, productivity, and learning!")

# Predefined questions
questions = {
    "Productivity & Time Management": [
        "Suggest a daily routine for better focus.",
        "Give me a 25-minute Pomodoro timer plan.",
        "Remind me to drink water every 2 hours.",
        "Summarize my to-do list into priorities."
    ],
    "Learning & Knowledge": [
        "Explain AI in simple words.",
        "Give me 3 quick facts about machine learning.",
        "Summarize this paragraph into key points."
    ],
    "Writing & Notes": [
        "Draft a short motivational note for today.",
        "Generate a quick LinkedIn post idea about productivity.",
        "Correct grammar in this sentence: I has a dream to be success."
    ],
    "Wellbeing": [
        "Suggest a 2-minute breathing exercise.",
        "Give me a quick motivational quote.",
        "List 3 simple ways to avoid procrastination."
    ],
    "Efficiency Boost": [
        "Break this big task into smaller steps: Finish my semester project.",
        "Suggest tools/apps for productivity.",
        "How do I stay consistent with my goals?"
    ]
}

# Dropdown for category
category = st.selectbox("📌 Choose a category", ["Type my own question"] + list(questions.keys()))

selected_question = None
if category != "Type my own question":
    selected_question = st.selectbox("💡 Pick a question", questions[category])

# User input
user_input = st.text_area("Or type your own question here:")

# Final question to answer
final_question = user_input if user_input.strip() else selected_question

# Function to get AI response
def get_ai_response(query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful productivity buddy."},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content.strip()

# Show answer
if st.button("🚀 Get Answer"):
    if final_question:
        st.subheader("🤖 Buddy's Answer:")
        with st.spinner("Thinking..."):
            st.write(get_ai_response(final_question))
    else:
        st.warning("Please select or type a question.")
