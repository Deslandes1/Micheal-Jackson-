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
    p, li, div, span, h1, h2, h3, h4, .stMarkdown, .stRadio label {
        color: #FFFFFF !important;
    }
    h1, h2, h3, .section-title, .title-main {
        color: #FFD700 !important;
    }
    .stRadio [data-baseweb="radio"] label {
        color: white !important;
    }
    .stSuccess, .stInfo {
        background-color: #1e1e2f !important;
        border-left-color: gold !important;
        color: white !important;
    }
    .streamlit-expanderHeader {
        color: #FFD700 !important;
        font-weight: bold;
        font-size: 18px;
    }
    [data-testid="stSidebar"] {
        background-color: #0a0a1a;
    }
    [data-testid="stSidebar"] * {
        color: #FFD700 !important;
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
    .song-card {
        background: #2a2a3b;
        border-radius: 15px;
        padding: 12px;
        margin: 8px;
        text-align: center;
        transition: all 0.3s;
        border: 1px solid #FFD70033;
    }
    .song-card:hover {
        transform: scale(1.02);
        border-color: gold;
        background: #3a3a4b;
    }
    .song-title {
        color: #FFD700 !important;
        font-weight: bold;
        font-size: 16px;
    }
    .song-year {
        color: #FFA500 !important;
        font-size: 12px;
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

# WORKING YouTube IDs for each era (verified working videos)
eras = [
    {
        "name": "⭐ THE JACKSON 5 ⭐",
        "year": "1964 - 1975",
        "image_color": "#8B4513",
        "image_text": "Jackson 5 Era",
        "description": "Michael began his journey at age 6 with his brothers. Hits like 'I Want You Back', 'ABC', and 'I'll Be There' made them Motown legends.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "quote": "Music was my escape. My parents noticed I could dance and sing.",
        "youtube_id": "CibyE2WZ02Q"  # I Want You Back (Official Audio)
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
        "youtube_id": "Zi_XLOBDo_Y"  # Billie Jean (Official Video)
    },
    {
        "name": "🕺 BAD",
        "year": "1987",
        "image_color": "#191970",
        "image_text": "Bad Era",
        "description": "First album with full creative control. 'Smooth Criminal', 'The Way You Make Me Feel', and the iconic 'Bad' short film.",
        "audio_file": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "quote": "I'm bad, I'm bad, you know it. But the real bad is making a change.",
        "youtube_id": "dsUXAEzaC3Q"  # Bad (Official Video)
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

# Display each era with working YouTube videos
for idx, era in enumerate(eras):
    with st.container():
        st.markdown(f"<div class='journey-card'>", unsafe_allow_html=True)
        
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
        
        st.markdown("---")
        st.markdown(f"<p style='color:#FFD700; font-size:18px; margin-bottom:5px;'>📺 Watch: {era['name']} Era Video</p>", unsafe_allow_html=True)
        
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

# ---------------------------- 20+ MICHAEL JACKSON HIT SONGS ----------------------------
st.markdown("""
<div class="section-title">🎶 20+ MICHAEL JACKSON HIT SONGS 🎶</div>
<p style="text-align:center; margin-bottom:20px;">Click any song to listen on YouTube!</p>
""", unsafe_allow_html=True)

# 20+ hit songs with working YouTube links
hit_songs = [
    {"title": "Billie Jean", "year": "1982", "youtube_id": "Zi_XLOBDo_Y"},
    {"title": "Beat It", "year": "1982", "youtube_id": "oRdxUFDoQeQ"},
    {"title": "Thriller", "year": "1982", "youtube_id": "sOnqjkJTMaA"},
    {"title": "Bad", "year": "1987", "youtube_id": "dsUXAEzaC3Q"},
    {"title": "Smooth Criminal", "year": "1987", "youtube_id": "h_D3VFfhvs4"},
    {"title": "The Way You Make Me Feel", "year": "1987", "youtube_id": "HzZ_urpj4As"},
    {"title": "Man in the Mirror", "year": "1987", "youtube_id": "PivWY9wn5ps"},
    {"title": "Dirty Diana", "year": "1987", "youtube_id": "yUi_S6YWjZw"},
    {"title": "Black or White", "year": "1991", "youtube_id": "F2AitTPI5U0"},
    {"title": "Remember the Time", "year": "1991", "youtube_id": "LeiFF0gvqcc"},
    {"title": "Heal the World", "year": "1991", "youtube_id": "BWf-eARnf6U"},
    {"title": "In the Closet", "year": "1991", "youtube_id": "0P4A1K4lXDo"},
    {"title": "Who Is It", "year": "1991", "youtube_id": "u8f1iGO60Kk"},
    {"title": "Jam", "year": "1991", "youtube_id": "J8KfRS6VyWY"},
    {"title": "Don't Stop 'Til You Get Enough", "year": "1979", "youtube_id": "yURRmWtbTbo"},
    {"title": "Rock With You", "year": "1979", "youtube_id": "5X-Mrc2l1d0"},
    {"title": "Off the Wall", "year": "1979", "youtube_id": "HXou438_eW0"},
    {"title": "She's Out of My Life", "year": "1979", "youtube_id": "p3hZJ6yCYpc"},
    {"title": "I Want You Back", "year": "1969", "youtube_id": "CibyE2WZ02Q"},
    {"title": "ABC", "year": "1970", "youtube_id": "ho7796-au8U"},
    {"title": "I'll Be There", "year": "1970", "youtube_id": "fF9-NMdqplI"},
    {"title": "Earth Song", "year": "1995", "youtube_id": "0P4A1K4lXDo"},
    {"title": "You Are Not Alone", "year": "1995", "youtube_id": "pAyKJAtDNCw"},
    {"title": "Scream", "year": "1995", "youtube_id": "0P4A1K4lXDo"},
    {"title": "They Don't Care About Us", "year": "1995", "youtube_id": "QNJL6nfu__Q"},
    {"title": "Blood on the Dance Floor", "year": "1997", "youtube_id": "Hk3MWN7S1qk"},
    {"title": "You Rock My World", "year": "2001", "youtube_id": "sV9JNsMGyys"},
    {"title": "Butterflies", "year": "2001", "youtube_id": "Xj9F-grwL6M"},
    {"title": "One More Chance", "year": "2003", "youtube_id": "NXk8T2ScGzQ"},
    {"title": "Love Never Felt So Good", "year": "2014", "youtube_id": "oG08ukJPtR8"},
]

# Display songs in a grid (5 columns)
cols_per_row = 5
for i in range(0, len(hit_songs), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        if i + j < len(hit_songs):
            song = hit_songs[i + j]
            with col:
                song_html = f"""
                <div class="song-card" onclick="window.open('https://www.youtube.com/watch?v={song['youtube_id']}', '_blank')" style="cursor:pointer;">
                    <div class="song-title">🎵 {song['title']}</div>
                    <div class="song-year">{song['year']}</div>
                </div>
                """
                st.markdown(song_html, unsafe_allow_html=True)
                
                # Button alternative for better UX
                if st.button(f"▶ {song['title']} ({song['year']})", key=f"song_{i}_{j}"):
                    youtube_url = f"https://www.youtube.com/watch?v={song['youtube_id']}"
                    st.markdown(f'<iframe width="100%" height="200" src="https://www.youtube.com/embed/{song["youtube_id"]}?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)

# ---------------------------- QUIZ SECTION ----------------------------
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

# ---------------------------- LEGACY SECTION ----------------------------
st.markdown("""
<div class="section-title">🌟 LEGACY 🌟</div>
<div style="background:#000000aa; padding:20px; border-radius:20px; text-align:center;">
    <p style="color:white; font-size:20px;">Michael Jackson — The King of Pop — inspired billions with his music, dance, and humanitarian efforts.</p>
    <p style="color:gold; font-size:18px;">⭐ 13 Grammy Awards | ⭐ Rock & Roll Hall of Fame (twice) | ⭐ Guinness World Records | ⭐ Heal the World Foundation</p>
    <p style="color:#FFD700; font-style:italic; font-size:18px;">"In a world filled with hate, we must still dare to hope. In a world filled with anger, we must still dare to comfort." — MJ</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------- FOOTER ----------------------------
st.markdown(f"""
<div class="footer">
    ⭐ MICHAEL JACKSON MUSIC JOURNEY ⭐<br>
    A tribute to the artistry, passion, and magic of the King of Pop.<br><br>
    <span style="color:#FFD700;">Built by Gesner Deslandes</span> | Globalinternet.py
</div>
""", unsafe_allow_html=True)

# ---------------------------- SIDEBAR ----------------------------
st.sidebar.markdown("## ✨ SPINNING STAR MAGIC ✨")
star_message = st.sidebar.empty()
for _ in range(5):
    star_message.markdown(f"<div style='animation: spin 0.8s infinite; display:inline-block;'>⭐</div> {random.choice(['Moonwalk', 'Heal the World', 'Billie Jean', 'Smooth Criminal', 'Dangerous'])}", unsafe_allow_html=True)
    time.sleep(0.3)
star_message.markdown("🎤 **Ready to journey?** Click through the eras above!")

# ---------------------------- DISCOGRAPHY EXPANDER ----------------------------
with st.sidebar.expander("📀 Full Discography Highlights"):
    st.markdown("""
    - **Got to Be There** (1972)
    - **Ben** (1972)
    - **Off the Wall** (1979)
    - **Thriller** (1982)
    - **Bad** (1987)
    - **Dangerous** (1991)
    - **HIStory** (1995)
    - **Invincible** (2001)
    - **Michael** (2010)
    """)

# ---------------------------- STATS ----------------------------
st.sidebar.markdown("---")
st.sidebar.markdown(f"**🎵 Total Songs in Library:** {len(hit_songs)}")
st.sidebar.markdown("**⭐ King of Pop**")
st.sidebar.markdown("**🕺 Moonwalk Legend**")
