# michael_jackson_app.py
import streamlit as st
import base64
from PIL import Image
import io
import random
import time

# ---------------------------- CONFIG ----------------------------
st.set_page_config(
    page_title="Michael Jackson Music Journey",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations, star effects, and overall styling
st.markdown("""
<style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes shine {
        0% { text-shadow: 0 0 5px gold, 0 0 10px gold; }
        50% { text-shadow: 0 0 20px yellow, 0 0 30px orange; }
        100% { text-shadow: 0 0 5px gold, 0 0 10px gold; }
    }
    .star-spin {
        display: inline-block;
        animation: spin 2s linear infinite;
        font-size: 48px;
        margin: 0 10px;
    }
    .title-main {
        text-align: center;
        font-size: 70px;
        font-weight: bold;
        background: linear-gradient(135deg, #FFD700, #FFA500, #FF4500);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: shine 1.5s ease-in-out infinite;
        letter-spacing: 5px;
    }
    .star-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .journey-card {
        background: linear-gradient(145deg, #1e1e2f, #2a2a3b);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        transition: transform 0.3s;
    }
    .journey-card:hover {
        transform: scale(1.01);
    }
    .section-title {
        color: #FFD700;
        font-size: 32px;
        border-left: 6px solid gold;
        padding-left: 20px;
        margin: 30px 0 20px 0;
    }
    .audio-player {
        margin-top: 15px;
        background: #00000066;
        border-radius: 30px;
        padding: 10px;
    }
    .footer {
        text-align: center;
        padding: 30px;
        color: #aaa;
        font-size: 14px;
    }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(120deg, #0f0c29, #302b63, #24243e);
    }
    .stImage {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- TITLE WITH SPINNING STARS ----------------------------
st.markdown("""
<div class="star-container">
    <span class="star-spin">⭐</span>
    <span class="star-spin">✨</span>
    <span class="star-spin">🌟</span>
</div>
<div class="title-main">MICHAEL JACKSON</div>
<div class="star-container">
    <span class="star-spin">🎤</span>
    <span class="star-spin">🎵</span>
    <span class="star-spin">🕺</span>
</div>
<h3 style="text-align:center; color:#FFD700;">✨ MUSIC JOURNEY ✨</h3>
<hr style="border:1px solid gold; width:60%;">
""", unsafe_allow_html=True)

# ---------------------------- DATA: ERA, IMAGE, TEXT, AUDIO ----------------------------
# Using local base64 images for demo (since we can't host actual images, we generate colored placeholders with emoji)
# But to make it visually appealing, we use a mix of base64 data URIs (simulated images) 
# For real deployment, you would replace with actual image URLs or uploaded files.

def get_image_base64(color, text):
    """Generate a simple colored image with text as base64 (placeholder)"""
    img = Image.new('RGB', (600, 400), color=color)
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((150, 180), text, fill="white", font=font)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Define music journey eras
eras = [
    {
        "name": "⭐ THE JACKSON 5 ⭐",
        "year": "1964 - 1975",
        "image_color": "#8B4513",
        "image_text": "Jackson 5 Era",
        "description": "Michael began his journey at age 6 with his brothers. Hits like 'I Want You Back', 'ABC', and 'I'll Be There' made them Motown legends.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",  # royalty-free example
        "quote": "Music was my escape. My parents noticed I could dance and sing."
    },
    {
        "name": "🎤 OFF THE WALL",
        "year": "1979",
        "image_color": "#2E8B57",
        "image_text": "Off The Wall",
        "description": "His first adult solo album with Quincy Jones. 'Don't Stop 'Til You Get Enough' and 'Rock With You' became disco-funk masterpieces.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "quote": "When I dance, I feel free. Off The Wall was my declaration."
    },
    {
        "name": "🌍 THRILLER",
        "year": "1982",
        "image_color": "#B22222",
        "image_text": "Thriller",
        "description": "The best-selling album of all time. 'Billie Jean', 'Beat It', 'Thriller' music video changed pop culture forever.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "quote": "I wanted to create an album where every song was a killer."
    },
    {
        "name": "🕺 BAD",
        "year": "1987",
        "image_color": "#191970",
        "image_text": "Bad Era",
        "description": "First album with full creative control. 'Smooth Criminal', 'The Way You Make Me Feel', and the iconic 'Bad' short film.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "quote": "I'm bad, I'm bad, you know it. But the real bad is making a change."
    },
    {
        "name": "⚡ DANGEROUS",
        "year": "1991",
        "image_color": "#556B2F",
        "image_text": "Dangerous",
        "description": "Incorporated New Jack Swing. 'Black or White', 'Remember the Time', 'Heal the World' - a message of unity.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
        "quote": "Heal the world, make it a better place for you and for me."
    },
    {
        "name": "👑 HIStory",
        "year": "1995",
        "image_color": "#4B0082",
        "image_text": "HIStory",
        "description": "Double album. 'Scream' duet with Janet, 'Earth Song', 'You Are Not Alone' - introspective and powerful.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
        "quote": "Tell me what has become of my life? But my legacy is HIStory."
    }
]

# Display each era as an interactive card
for idx, era in enumerate(eras):
    with st.container():
        st.markdown(f"<div class='journey-card'>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Generate image from base64 or use real image if you have URLs
            img_b64 = get_image_base64(era["image_color"], era["image_text"])
            st.markdown(f'<img src="data:image/png;base64,{img_b64}" style="width:100%; border-radius:20px;">', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"### {era['name']}")
            st.markdown(f"**{era['year']}**")
            st.markdown(f"*{era['description']}*")
            st.markdown(f"> *\"{era['quote']}\"*")
            
            # Audio player
            st.markdown("🎧 **Listen to a sample track (Era vibe)**")
            audio_bytes = None
            # For demonstration, we embed audio HTML (since Streamlit's audio supports URLs)
            st.audio(era["audio_file"], format="audio/mp3")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# Special interactive timeline quiz (fun extra)
st.markdown("""
<div class="section-title">🎵 JOURNEY TIMELINE QUIZ 🎵</div>
""", unsafe_allow_html=True)

quiz_q = st.radio(
    "Which Michael Jackson album features 'Billie Jean' and 'Thriller'?",
    ("Off The Wall", "Thriller", "Bad", "Dangerous"),
    index=1,
    horizontal=True
)
if quiz_q == "Thriller":
    st.success("✅ Correct! 'Thriller' (1982) is the best-selling album of all time! 🎉")
else:
    st.info("💡 Hint: The album with the iconic red jacket and zombie dance.")

# Add a tribute section
st.markdown("""
<div class="section-title">🌟 LEGACY 🌟</div>
<div style="background:#000000aa; padding:20px; border-radius:20px; text-align:center;">
    <p style="font-size:20px;">Michael Jackson — The King of Pop — inspired billions with his music, dance, and humanitarian efforts.</p>
    <p>⭐ 13 Grammy Awards | ⭐ Rock & Roll Hall of Fame (twice) | ⭐ Guinness World Records | ⭐ Heal the World Foundation</p>
    <p>🎤 <i>"In a world filled with hate, we must still dare to hope. In a world filled with anger, we must still dare to comfort."</i> — MJ</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    ⭐ MICHAEL JACKSON MUSIC JOURNEY ⭐<br>
    A tribute to the artistry, passion, and magic of the King of Pop.
</div>
""", unsafe_allow_html=True)

# Optional: spinning star effects with random messages on sidebar
st.sidebar.markdown("## ✨ SPINNING STAR MAGIC ✨")
star_message = st.sidebar.empty()
for _ in range(5):
    star_message.markdown(f"<div style='animation: spin 0.8s infinite; display:inline-block;'>⭐</div> {random.choice(['Moonwalk', 'Heal the World', 'Billie Jean', 'Smooth Criminal', 'Dangerous'])}", unsafe_allow_html=True)
    time.sleep(0.3)
star_message.markdown("🎤 **Ready to journey?** Click through the eras above!")

# Extra: full discography mini list
with st.expander("📀 Full Discography Highlights"):
    st.write("""
    - **Got to Be There** (1972)
    - **Ben** (1972)
    - **Off the Wall** (1979)
    - **Thriller** (1982)
    - **Bad** (1987)
    - **Dangerous** (1991)
    - **HIStory: Past, Present and Future, Book I** (1995)
    - **Invincible** (2001)
    - **Michael** (2010) - posthumous
    """)
