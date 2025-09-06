import random
import streamlit as st

# Predefined responses
responses = {
    "lazy": [
        "Start with just 5 minutes of work, momentum will follow.",
        "Break tasks into tiny steps – the smaller, the easier to begin."
    ],
    "distracted": [
        "Put your phone away for 20 minutes and focus.",
        "Write down the distraction, promise yourself you’ll check later."
    ],
    "tired": [
        "Drink some water, stretch, and reset your mind.",
        "Take a 10-minute break, then jump back in with energy."
    ],
    "overwhelmed": [
        "Write your tasks down, then pick just ONE to do first.",
        "Small steps lead to big wins – focus on the next step only."
    ],
    "unmotivated": [
        "Remember why you started – your goals are waiting for you.",
        "Motivation comes after action, not before. Start small."
    ]
}

def ai_buddy(feeling):
    feeling = feeling.lower()
    for key in responses:
        if key in feeling:
            return random.choice(responses[key])
    return "Stay consistent, even tiny progress counts today!"

# Streamlit UI
st.set_page_config(page_title="AI Productivity Buddy", page_icon="🤖")
st.title("🤖 AI Productivity Buddy")
st.write("Tell me how you feel, and I’ll give you a quick tip!")

user_input = st.text_input("How are you feeling right now?")

if st.button("Get Tip"):
    tip = ai_buddy(user_input)
    st.success(tip)
