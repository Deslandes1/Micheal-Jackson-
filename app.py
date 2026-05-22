# michael_jackson_app.py
import streamlit as st
import base64
from PIL import Image, ImageDraw, ImageFont
import io
import random
import time
import tempfile
import os

# ---------------------------- CONFIG ----------------------------
st.set_page_config(
    page_title="Michael Jackson Music Journey",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
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
    .era-card {
        background: linear-gradient(145deg, #1e1e2f, #2a2a3b);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .song-card {
        background: linear-gradient(135deg, #16213e, #1a1a2e);
        border-radius: 20px;
        padding: 20px;
        margin: 25px 0;
        border: 1px solid #FFD70033;
        transition: transform 0.3s;
    }
    .song-card:hover {
        transform: scale(1.01);
        border-color: gold;
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
    p, li, div, span, h1, h2, h3, h4, .stMarkdown, .stRadio label {
        color: #FFFFFF !important;
    }
    h1, h2, h3, .section-title, .title-main {
        color: #FFD700 !important;
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
    .quote-text {
        color: #FFD700 !important;
        font-style: italic;
        font-size: 18px;
    }
    .song-title {
        color: #FFD700 !important;
        font-size: 24px;
        font-weight: bold;
    }
    .song-year {
        color: #FFA500 !important;
        font-size: 18px;
    }
    .song-desc {
        color: #FFFFFF !important;
        font-size: 16px;
        line-height: 1.5;
        margin: 15px 0;
    }
    .mj-image {
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        width: 100%;
        object-fit: cover;
    }
    hr {
        border-color: gold;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- TEXT-TO-SPEECH FUNCTION (using gTTS) ----------------------------
def text_to_speech_audio(text, idx):
    """Convert text to speech using gTTS (Google Text-to-Speech) - female voice"""
    try:
        from gtts import gTTS
        import os
        
        # Create a unique filename
        filename = f"temp_audio_{idx}.mp3"
        
        # Generate speech
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        
        # Read the audio file
        with open(filename, "rb") as f:
            audio_bytes = f.read()
        
        # Clean up temp file
        try:
            os.remove(filename)
        except:
            pass
            
        return audio_bytes
    except Exception as e:
        return None

# ---------------------------- CREATOR CREDITS ----------------------------
st.markdown(f"""
<div class="creator-bar">
    <span>✨ Built by Gesner Deslandes</span> | 📞 (509)-47385663 | ✉️ deslandes78@gmail.com | <span>🌐 Globalinternet.py</span> ✨
</div>
""", unsafe_allow_html=True)

# ---------------------------- TITLE SECTION ----------------------------
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

# ---------------------------- JACKSON 5 ERA SECTION ----------------------------
st.markdown(f"""
<div class="era-card">
    <div style="display: flex; gap: 30px; flex-wrap: wrap;">
        <div style="flex: 1;">
            <p class='era-name'>⭐ THE JACKSON 5 ⭐</p>
            <p class='year-text'>1964 - 1975</p>
            <p class='desc-text'>Michael began his journey at age 6 with his brothers. Hits like 'I Want You Back', 'ABC', and 'I'll Be There' made them Motown legends.</p>
            <p class='quote-text'>"Music was my escape. My parents noticed I could dance and sing."</p>
            <p>🎧 <strong>Listen to a sample track (Era vibe)</strong></p>
        </div>
        <div style="flex: 0.5; min-width: 200px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Jackson_5_1972.jpg/400px-Jackson_5_1972.jpg" style="width:100%; border-radius:20px; box-shadow:0 5px 15px rgba(0,0,0,0.3);">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Jackson 5 era audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------- 35+ MICHAEL JACKSON SONGS WITH AI VOICE & IMAGES ----------------------------
st.markdown("""
<div class="section-title">🎶 MICHAEL JACKSON COMPLETE MUSIC COLLECTION 🎶</div>
<p style="text-align:center; margin-bottom:20px;">🎤 Each song has AI Female voice description + Michael Jackson image + YouTube video 🎤</p>
<hr>
""", unsafe_allow_html=True)

# 35+ songs with descriptions, images, and YouTube links
songs = [
    {"title": "Billie Jean", "year": "1982", "youtube_id": "Zi_XLOBDo_Y", "description": "Billie Jean is one of Michael Jackson's most iconic songs. Released in 1982 on the Thriller album, it tells the story of a woman who claims the singer is the father of her child. The song features a legendary bassline and Michael's signature vocal style. The music video broke racial barriers on MTV.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Michael_Jackson_-_Billie_Jean.png/220px-Michael_Jackson_-_Billie_Jean.png"},
    {"title": "Beat It", "year": "1982", "youtube_id": "oRdxUFDoQeQ", "description": "Beat It is a rock-infused anthem from the Thriller album. Featuring a guitar solo by Eddie Van Halen, the song promotes non-violence and conflict resolution. The iconic music video featured real gang members as extras and showcased Michael's incredible dance moves.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Michael_Jackson_-_Beat_It.png/220px-Michael_Jackson_-_Beat_It.png"},
    {"title": "Thriller", "year": "1982", "youtube_id": "sOnqjkJTMaA", "description": "Thriller is the title track and masterpiece of Michael's career. The 14-minute music video, directed by John Landis, features horror-themed choreography, zombies, and a famous voiceover by Vincent Price. It revolutionized the music video format forever.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Michael_Jackson_-_Thriller.png/220px-Michael_Jackson_-_Thriller.png"},
    {"title": "Bad", "year": "1987", "youtube_id": "dsUXAEzaC3Q", "description": "Bad is the title track from Michael's seventh studio album. The song is about being tough and confident. The music video, directed by Martin Scorsese, features elaborate choreography in a subway station setting.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Michael_Jackson_-_Bad.png/220px-Michael_Jackson_-_Bad.png"},
    {"title": "Smooth Criminal", "year": "1987", "youtube_id": "h_D3VFfhvs4", "description": "Smooth Criminal features Michael's famous anti-gravity lean move. The song tells the story of a woman named Annie who has been attacked. The music video is set in a 1930s-style nightclub with incredible choreography.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Smooth_Criminal_cover.png/220px-Smooth_Criminal_cover.png"},
    {"title": "The Way You Make Me Feel", "year": "1987", "youtube_id": "HzZ_urpj4As", "description": "This upbeat love song showcases Michael's romantic side. The music video features Michael pursuing a beautiful woman through city streets, ending with a joyful dance sequence. It became one of his most beloved hits.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b3/Michael_Jackson_-_The_Way_You_Make_Me_Feel.png/220px-Michael_Jackson_-_The_Way_You_Make_Me_Feel.png"},
    {"title": "Man in the Mirror", "year": "1987", "youtube_id": "PivWY9wn5ps", "description": "Man in the Mirror is a powerful ballad about self-reflection and making a change in the world. The song features a gospel choir and became one of Michael's most inspirational anthems about social change.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Michael_Jackson_-_Man_in_the_Mirror.png/220px-Michael_Jackson_-_Man_in_the_Mirror.png"},
    {"title": "Dirty Diana", "year": "1987", "youtube_id": "yUi_S6YWjZw", "description": "Dirty Diana is a rock-driven song about groupies and the dark side of fame. Featuring heavy guitar riffs, it shows Michael's edgier side and became his fifth number-one single from the Bad album.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Dirty_Diana.png/220px-Dirty_Diana.png"},
    {"title": "Black or White", "year": "1991", "youtube_id": "F2AitTPI5U0", "description": "Black or White promotes racial unity and equality. The groundbreaking music video featured 'morphing' technology and ended with Michael's famous dance sequence. The song's message is timeless and powerful.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Michael_Jackson_-_Black_or_White.png/220px-Michael_Jackson_-_Black_or_White.png"},
    {"title": "Remember the Time", "year": "1991", "youtube_id": "LeiFF0gvqcc", "description": "This song features an epic ancient Egyptian-themed music video starring Eddie Murphy and Iman. The track has a sensual R&B feel and showcases Michael's smooth vocals and incredible dance moves.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Michael_Jackson_-_Remember_the_Time.png/220px-Michael_Jackson_-_Remember_the_Time.png"},
    {"title": "Heal the World", "year": "1991", "youtube_id": "BWf-eARnf6U", "description": "Heal the World is a humanitarian ballad dedicated to making the world a better place for children. Michael established the Heal the World Foundation to support children in need around the globe.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Heal_the_World_-_Michael_Jackson.png/220px-Heal_the_World_-_Michael_Jackson.png"},
    {"title": "Don't Stop 'Til You Get Enough", "year": "1979", "youtube_id": "yURRmWtbTbo", "description": "This disco-funk classic was Michael's first solo single as an adult. The song features his signature falsetto and celebratory lyrics. It won a Grammy Award and launched the Off the Wall era.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/Michael_Jackson_-_Don%27t_Stop_%27Til_You_Get_Enough.png/220px-Michael_Jackson_-_Don%27t_Stop_%27Til_You_Get_Enough.png"},
    {"title": "Rock With You", "year": "1979", "youtube_id": "5X-Mrc2l1d0", "description": "Rock With You is a smooth, romantic disco ballad. It became the second single from Off the Wall and showcases Michael's incredible vocal range and charismatic delivery.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Michael_Jackson_-_Rock_with_You.png/220px-Michael_Jackson_-_Rock_with_You.png"},
    {"title": "I Want You Back", "year": "1969", "youtube_id": "CibyE2WZ02Q", "description": "The Jackson 5's debut single that launched young Michael Jackson to stardom. At just 11 years old, Michael's powerful vocals amazed the world. The song became a Motown classic.", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Jackson_5_1971.JPG/400px-Jackson_5_1971.JPG"},
    {"title": "ABC", "year": "1970", "youtube_id": "ho7796-au8U", "description": "ABC was the Jackson 5's second number-one hit. The upbeat, playful song shows the young Michael's incredible charisma and talent, becoming a Motown classic loved by generations.", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Jackson_5_1972.jpg/400px-Jackson_5_1972.jpg"},
    {"title": "Earth Song", "year": "1995", "youtube_id": "0P4A1K4lXDo", "description": "Earth Song is a powerful environmental anthem. Michael's passionate performance and the dramatic music video highlight issues of deforestation, pollution, and animal cruelty. It became a massive global hit.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Earth_Song_cover.png/220px-Earth_Song_cover.png"},
    {"title": "You Are Not Alone", "year": "1995", "youtube_id": "pAyKJAtDNCw", "description": "This emotional ballad holds the Guinness World Record for first song to debut at number one on the Billboard Hot 100. The song offers comfort to those feeling lonely or isolated.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/You_Are_Not_Alone_MJ.jpg/220px-You_Are_Not_Alone_MJ.jpg"},
    {"title": "They Don't Care About Us", "year": "1995", "youtube_id": "QNJL6nfu__Q", "description": "A powerful protest song addressing social injustice, racism, and police brutality. The song features powerful drumming from Brazil and two controversial but impactful music videos.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/They_Don%27t_Care_About_Us.png/220px-They_Don%27t_Care_About_Us.png"},
    {"title": "Blood on the Dance Floor", "year": "1997", "youtube_id": "Hk3MWN7S1qk", "description": "This song combines elements of new jack swing and industrial dance. It tells a dark story of seduction and betrayal, with one of Michael's most energetic dance performances.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Michael_Jackson_-_Blood_on_the_Dance_Floor.png/220px-Michael_Jackson_-_Blood_on_the_Dance_Floor.png"},
    {"title": "You Rock My World", "year": "2001", "youtube_id": "sV9JNsMGyys", "description": "The lead single from Invincible album, featuring Chris Tucker. The song returns to Michael's classic funk and R&B sound with an elaborate 13-minute music video.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/You_Rock_My_World_cover.png/220px-You_Rock_My_World_cover.png"},
    {"title": "Wanna Be Startin' Somethin'", "year": "1982", "youtube_id": "3VU8jNp4XqQ", "description": "This high-energy track features African-inspired rhythms and the famous 'Mama-se, mama-sa, ma-ma-ko-ssa' chant. It became a cornerstone of the Thriller album.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Wanna_Be_Startin%27_Somethin%27.jpg/220px-Wanna_Be_Startin%27_Somethin%27.jpg"},
    {"title": "Human Nature", "year": "1982", "youtube_id": "B4jBnPp7H-w", "description": "A beautiful, introspective ballad about human emotions and connection. The song's gentle melody and Michael's tender vocals made it a timeless classic from Thriller.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9c/Human_Nature_cover.png/220px-Human_Nature_cover.png"},
    {"title": "Liberian Girl", "year": "1987", "youtube_id": "FXPdIuNtSfA", "description": "This song honors African beauty and culture. The music video features numerous celebrity cameos and showcases Michael's appreciation for African heritage.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/07/Liberian_Girl.png/220px-Liberian_Girl.png"},
    {"title": "Off the Wall", "year": "1979", "youtube_id": "HXou438_eW0", "description": "The title track from Michael's breakthrough solo album. The song celebrates living life freely and dancing without worries, setting the tone for his incredible career.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Michael_Jackson_-_Off_the_Wall.png/220px-Michael_Jackson_-_Off_the_Wall.png"},
    {"title": "I'll Be There", "year": "1970", "youtube_id": "fF9-NMdqplI", "description": "A heartfelt ballad by the Jackson 5 showing young Michael's emotional depth. The song became one of the group's biggest hits and remains a classic love song.", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Jackson_5_1972.jpg/400px-Jackson_5_1972.jpg"},
    {"title": "P.Y.T. (Pretty Young Thing)", "year": "1982", "youtube_id": "R6X1_7U2V5k", "description": "An upbeat, fun song about young love. The track features energetic production and became a fan favorite from the Thriller album.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/PYT_MJ.png/220px-PYT_MJ.png"},
    {"title": "Leave Me Alone", "year": "1987", "youtube_id": "Uqdmnoz5rns", "description": "A song about Michael's frustration with media scrutiny. The innovative music video uses stop-motion animation and won a Grammy for Best Short Form Music Video.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Leave_Me_Alone.jpg/220px-Leave_Me_Alone.jpg"},
    {"title": "Who Is It", "year": "1991", "youtube_id": "u8f1iGO60Kk", "description": "A mysterious song about betrayal and hidden identity. The track features complex production and an orchestral arrangement, showing Michael's artistic growth.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Who_Is_It_cover.png/220px-Who_Is_It_cover.png"},
    {"title": "Jam", "year": "1991", "youtube_id": "J8KfRS6VyWY", "description": "This song features a collaboration with heavyweights like Michael Jordan and Heavy D. The track has a powerful beat and addresses social pressures.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Jam_-_Michael_Jackson.png/220px-Jam_-_Michael_Jackson.png"},
    {"title": "In the Closet", "year": "1991", "youtube_id": "0P4A1K4lXDo", "description": "A sensual track featuring a duet with Princess Stephanie of Monaco. The song explores themes of love and privacy with an exotic musical arrangement.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/09/In_the_Closet_cover.png/220px-In_the_Closet_cover.png"},
    {"title": "She's Out of My Life", "year": "1979", "youtube_id": "p3hZJ6yCYpc", "description": "An emotional ballad where Michael reportedly cried during recording. The song showcases his vulnerable side and became a top 10 hit.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/She%27s_Out_of_My_Life.png/220px-She%27s_Out_of_My_Life.png"},
    {"title": "Butterflies", "year": "2001", "youtube_id": "Xj9F-grwL6M", "description": "A smooth R&B track that samples music from the 1970s. Michael's delicate vocals and the romantic lyrics made it a late-career fan favorite.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Butterflies_MJ.jpg/220px-Butterflies_MJ.jpg"},
    {"title": "One More Chance", "year": "2003", "youtube_id": "NXk8T2ScGzQ", "description": "Michael's last single released during his lifetime. The song is a pop ballad about lost love and the hope for reconciliation.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/8/83/One_More_Chance_MJ.png/220px-One_More_Chance_MJ.png"},
    {"title": "Love Never Felt So Good", "year": "2014", "youtube_id": "oG08ukJPtR8", "description": "A posthumous duet featuring Justin Timberlake. Originally written in 1983, this upbeat song shows Michael's timeless appeal and joyful energy.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Love_Never_Felt_So_Good.png/220px-Love_Never_Felt_So_Good.png"},
    {"title": "Scream", "year": "1995", "youtube_id": "0P4A1K4lXDo", "description": "A duet with Michael's sister Janet Jackson. The song addresses media harassment and features futuristic production and an award-winning music video.", "image": "https://upload.wikimedia.org/wikipedia/en/thumb/1/15/ScreamMJ.png/220px-ScreamMJ.png"},
]

# Display each song with AI voice and image
for idx, song in enumerate(songs):
    with st.container():
        st.markdown(f"<div class='song-card'>", unsafe_allow_html=True)
        
        # Two columns: Left side (AI voice + text), Right side (Image)
        col1, col2 = st.columns([1, 0.6])
        
        with col1:
            st.markdown(f"<p class='song-title'>🎵 {song['title']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='song-year'>📅 {song['year']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='song-desc'>{song['description']}</p>", unsafe_allow_html=True)
            
            # AI Voice button and audio player
            audio_bytes = text_to_speech_audio(song['description'], idx)
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3")
                st.caption("🎤 AI Female Voice - Click play to hear the song description")
            else:
                st.info("🔊 Click the YouTube video below to listen to the song!")
        
        with col2:
            # Display Michael Jackson image
            st.markdown(f"""
            <img src="{song['image']}" class="mj-image" style="width:100%; border-radius:20px; height:auto; min-height:250px; object-fit:cover;">
            """, unsafe_allow_html=True)
        
        # YouTube video player (full width)
        st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
        st.markdown(f"**📺 Watch: {song['title']} Music Video**")
        st.video(f"https://www.youtube.com/watch?v={song['youtube_id']}")
        
        st.markdown("</div>", unsafe_allow_html=True)

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
star_message.markdown("🎤 **Ready to journey?** Explore all 35 songs above!")

# ---------------------------- STATS ----------------------------
st.sidebar.markdown("---")
st.sidebar.markdown(f"**🎵 Total Songs:** {len(songs)}")
st.sidebar.markdown("**🎤 AI Voice Descriptions**")
st.sidebar.markdown("**📸 Michael Jackson Images**")
st.sidebar.markdown("**🎬 Embedded YouTube Videos**")
st.sidebar.markdown("**⭐ King of Pop Legacy**")
