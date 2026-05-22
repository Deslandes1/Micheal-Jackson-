# michael_jackson_app.py
import streamlit as st
import base64
from PIL import Image, ImageDraw, ImageFont
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

# Custom CSS for animations, star effects, and strong white text
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
        color: #FFD700 !important;
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
        color: #FFFFFF !important;
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
    /* Strong white text for all content */
    p, li, div, span, h1, h2, h3, h4, .stMarkdown, .stRadio label {
        color: #FFFFFF !important;
    }
    /* Keep gold for titles and special elements */
    h1, h2, h3, .section-title, .title-main {
        color: #FFD700 !important;
    }
    /* Quiz options white */
    .stRadio [data-baseweb="radio"] label {
        color: white !important;
    }
    /* Success and info messages */
    .stSuccess, .stInfo {
        background-color: #1e1e2f !important;
        border-left-color: gold !important;
        color: white !important;
    }
    .stSuccess p, .stInfo p {
        color: white !important;
    }
    /* Expander header */
    .streamlit-expanderHeader {
        color: #FFD700 !important;
        font-weight: bold;
        font-size: 18px;
    }
    /* Sidebar text */
    [data-testid="stSidebar"] {
        background-color: #0a0a1a;
    }
    [data-testid="stSidebar"] * {
        color: #FFD700 !important;
    }
    /* Audio caption */
    .stAudio caption {
        color: white !important;
    }
    hr {
        border-color: gold !important;
    }
    .quote-text {
        color: #FFD700 !important;
        font-style: italic;
        font-size: 18px;
    }
    .era-name {
        color: #FFD700 !important;
        font-size: 28px;
        font-weight: bold;
    }
    .year-text {
        color: #FFA500 !important;
        font-size: 20px;
        font-weight: bold;
    }
    .desc-text {
        color: #FFFFFF !important;
        font-size: 16px;
        line-height: 1.5;
    }
    .legacy-text {
        color: white !important;
        font-size: 20px;
    }
    .legacy-stars {
        color: gold !important;
        font-size: 18px;
    }
    .creator-bar {
        background: linear-gradient(90deg, #00000088, #1a1a2e88, #00000088);
        padding: 12px 20px;
        border-radius: 40px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid gold;
        font-size: 14px;
    }
    .creator-bar span {
        color: #FFD700 !important;
        font-weight: bold;
    }
    .youtube-container {
        margin: 15px 0;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- CREATOR CREDITS (TOP) ----------------------------
st.markdown(f"""
<div class="creator-bar">
    <span>✨ Built by Gesner Deslandes</span> | 📞 (509)-47385663 | ✉️ deslandes78@gmail.com | <span>🌐 Globalinternet.py</span> ✨
</div>
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

# ---------------------------- DATA: ERA, IMAGE, TEXT, AUDIO, YOUTUBE ----------------------------
def get_image_base64(color, text):
    """Generate a simple colored image with text as base64 (placeholder)"""
    img = Image.new('RGB', (600, 400), color=color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (600 - text_width) // 2
    y = (400 - text_height) // 2
    draw.text((x, y), text, fill="white", font=font)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Define music journey eras with YouTube embed links
eras = [
    {
        "name": "⭐ THE JACKSON 5 ⭐",
        "year": "1964 - 1975",
        "image_color": "#8B4513",
        "image_text": "Jackson 5 Era",
        "description": "Michael began his journey at age 6 with his brothers. Hits like 'I Want You Back', 'ABC', and 'I'll Be There' made them Motown legends.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "quote": "Music was my escape. My parents noticed I could dance and sing.",
        "youtube_id": "s3Q80mk7o1Y"  # I Want You Back
    },
    {
        "name": "🎤 OFF THE WALL",
        "year": "1979",
        "image_color": "#2E8B57",
        "image_text": "Off The Wall",
        "description": "His first adult solo album with Quincy Jones. 'Don't Stop 'Til You Get Enough' and 'Rock With You' became disco-funk masterpieces.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "quote": "When I dance, I feel free. Off The Wall was my declaration.",
        "youtube_id": "yURRmWtbTbo"  # Don't Stop 'Til You Get Enough
    },
    {
        "name": "🌍 THRILLER",
        "year": "1982",
        "image_color": "#B22222",
        "image_text": "Thriller",
        "description": "The best-selling album of all time. 'Billie Jean', 'Beat It', 'Thriller' music video changed pop culture forever.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "quote": "I wanted to create an album where every song was a killer.",
        "youtube_id": "sOnqjkJTMaA"  # Billie Jean
    },
    {
        "name": "🕺 BAD",
        "year": "1987",
        "image_color": "#191970",
        "image_text": "Bad Era",
        "description": "First album with full creative control. 'Smooth Criminal', 'The Way You Make Me Feel', and the iconic 'Bad' short film.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "quote": "I'm bad, I'm bad, you know it. But the real bad is making a change.",
        "youtube_id": "dsUXAEzaC3Q"  # Bad
    },
    {
        "name": "⚡ DANGEROUS",
        "year": "1991",
        "image_color": "#556B2F",
        "image_text": "Dangerous",
        "description": "Incorporated New Jack Swing. 'Black or White', 'Remember the Time', 'Heal the World' - a message of unity.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
        "quote": "Heal the world, make it a better place for you and for me.",
        "youtube_id": "F2AitTPI5U0"  # Black or White
    },
    {
        "name": "👑 HIStory",
        "year": "1995",
        "image_color": "#4B0082",
        "image_text": "HIStory",
        "description": "Double album. 'Scream' duet with Janet, 'Earth Song', 'You Are Not Alone' - introspective and powerful.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
        "quote": "Tell me what has become of my life? But my legacy is HIStory.",
        "youtube_id": "0P4A1K4lXDo"  # Earth Song
    }
]

# Display each era as an interactive card with YouTube embed
for idx, era in enumerate(eras):
    with st.container():
        st.markdown(f"<div class='journey-card'>", unsafe_allow_html=True)
        
        # First row: Title, year, description, quote, audio (left side) + Image (right side)
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"<p class='era-name'>{era['name']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='year-text'>{era['year']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='desc-text'>{era['description']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='quote-text'>\"{era['quote']}\"</p>", unsafe_allow_html=True)
            st.markdown("🎧 **Listen to a sample track (Era vibe)**")
            st.audio(era["audio_file"], format="audio/mp3")
        
        with col2:
            img_b64 = get_image_base64(era["image_color"], era["image_text"])
            st.markdown(f'<img src="data:image/png;base64,{img_b64}" style="width:100%; border-radius:20px;">', unsafe_allow_html=True)
        
        # Second row: YouTube video embed (full width)
        st.markdown("---")
        st.markdown(f"<p style='color:#FFD700; font-size:18px; margin-bottom:5px;'>📺 Watch: {era['name']} Era Video</p>", unsafe_allow_html=True)
        
        # YouTube embed using iframe
        youtube_html = f"""
        <div class="youtube-container">
            <iframe 
                width="100%" 
                height="400" 
                src="https://www.youtube.com/embed/{era['youtube_id']}?autoplay=0&rel=0" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        </div>
        """
        st.markdown(youtube_html, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# Special interactive timeline quiz (fun extra) - with white text
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

# Legacy section - all white text
st.markdown("""
<div class="section-title">🌟 LEGACY 🌟</div>
<div style="background:#000000aa; padding:20px; border-radius:20px; text-align:center;">
    <p class="legacy-text">Michael Jackson — The King of Pop — inspired billions with his music, dance, and humanitarian efforts.</p>
    <p class="legacy-stars">⭐ 13 Grammy Awards | ⭐ Rock & Roll Hall of Fame (twice) | ⭐ Guinness World Records | ⭐ Heal the World Foundation</p>
    <p class="quote-text">"In a world filled with hate, we must still dare to hope. In a world filled with anger, we must still dare to comfort." — MJ</p>
</div>
""", unsafe_allow_html=True)

# Footer with white text and credits
st.markdown(f"""
<div class="footer">
    ⭐ MICHAEL JACKSON MUSIC JOURNEY ⭐<br>
    A tribute to the artistry, passion, and magic of the King of Pop.<br><br>
    <span style="color:#FFD700;">Built by Gesner Deslandes</span> | Globalinternet.py
</div>
""", unsafe_allow_html=True)

# Sidebar spinning star effects
st.sidebar.markdown("## ✨ SPINNING STAR MAGIC ✨")
star_message = st.sidebar.empty()
for _ in range(5):
    star_message.markdown(f"<div style='animation: spin 0.8s infinite; display:inline-block;'>⭐</div> {random.choice(['Moonwalk', 'Heal the World', 'Billie Jean', 'Smooth Criminal', 'Dangerous'])}", unsafe_allow_html=True)
    time.sleep(0.3)
star_message.markdown("🎤 **Ready to journey?** Click through the eras above!")

# Full discography mini list with white text
with st.expander("📀 Full Discography Highlights"):
    st.markdown("""
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
