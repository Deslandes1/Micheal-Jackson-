# michael_jackson_app.py
import streamlit as st
import random
import time
import os
import base64

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
    hr {
        border-color: gold;
    }
    .stAudio {
        margin: 10px 0;
    }
    .ai-voice-label {
        color: #FFD700 !important;
        font-size: 14px;
        margin-top: 5px;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------- TEXT-TO-SPEECH FUNCTION ----------------------------
@st.cache_data(ttl=3600)
def text_to_speech_audio(text, song_title):
    """Convert text to speech using gTTS with caching"""
    try:
        from gtts import gTTS
        
        # Create a safe filename
        safe_title = song_title.replace(" ", "_").replace("'", "").replace("(", "").replace(")", "")
        filename = f"temp_audio_{safe_title}.mp3"
        
        # Generate speech
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        
        # Read the audio file
        with open(filename, "rb") as f:
            audio_bytes = f.read()
        
        # Clean up
        try:
            os.remove(filename)
        except:
            pass
            
        return audio_bytes
    except Exception as e:
        st.error(f"Audio generation error for {song_title}: {str(e)}")
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
    <p class='era-name'>⭐ THE JACKSON 5 ⭐</p>
    <p class='year-text'>1964 - 1975</p>
    <p class='desc-text'>Michael began his journey at age 6 with his brothers. Hits like 'I Want You Back', 'ABC', and 'I'll Be There' made them Motown legends.</p>
    <p class='quote-text'>"Music was my escape. My parents noticed I could dance and sing."</p>
    <p>🎧 <strong>Listen to a sample track (Era vibe)</strong></p>
</div>
""", unsafe_allow_html=True)

# Jackson 5 era audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------- MICHAEL JACKSON SONGS WITH AI VOICE ----------------------------
st.markdown("""
<div class="section-title">🎶 MICHAEL JACKSON COMPLETE MUSIC COLLECTION 🎶</div>
<p style="text-align:center; margin-bottom:20px;">🎤 Each song includes AI Female Voice reading the description + Music Video 🎤</p>
<hr>
""", unsafe_allow_html=True)

# Songs with full descriptions for AI voice
songs = [
    {"title": "Billie Jean", "year": "1982", "youtube_id": "Zi_XLOBDo_Y", "description": "Billie Jean is one of Michael Jackson's most iconic songs. Released in 1982 on the Thriller album, it tells the story of a woman who claims the singer is the father of her child. The song features a legendary bassline and Michael's signature vocal style. The music video broke racial barriers on MTV and became a global phenomenon."},
    
    {"title": "Thriller", "year": "1982", "youtube_id": "sOnqjkJTMaA", "description": "Thriller is the title track and masterpiece of Michael's career. Released in 1982, the 14-minute music video was directed by John Landis and features horror-themed choreography, zombies, and a famous voiceover by Vincent Price. It revolutionized the music video format forever and remains the best-selling album of all time."},
    
    {"title": "Bad", "year": "1987", "youtube_id": "dsUXAEzaC3Q", "description": "Bad is the title track from Michael's seventh studio album released in 1987. The song is about being tough and confident. The music video, directed by Martin Scorsese, features elaborate choreography in a subway station setting and cost over two million dollars to produce."},
    
    {"title": "Smooth Criminal", "year": "1987", "youtube_id": "h_D3VFfhvs4", "description": "Smooth Criminal features Michael's famous anti-gravity lean move that defies physics. The song tells the story of a woman named Annie who has been attacked. The music video is set in a 1930s-style nightclub called Club 30s with incredible choreography and Michael in a white suit."},
    
    {"title": "The Way You Make Me Feel", "year": "1987", "youtube_id": "HzZ_urpj4As", "description": "This upbeat love song showcases Michael's romantic side. Released in 1987, the music video features Michael pursuing a beautiful woman through city streets, ending with a joyful dance sequence. It became one of his most beloved hits and reached number one on the Billboard Hot 100."},
    
    {"title": "Man in the Mirror", "year": "1987", "youtube_id": "PivWY9wn5ps", "description": "Man in the Mirror is a powerful ballad about self-reflection and making a change in the world. Released in 1987, the song features a gospel choir and became one of Michael's most inspirational anthems about social change and personal responsibility."},
    
    {"title": "Dirty Diana", "year": "1987", "youtube_id": "yUi_S6YWjZw", "description": "Dirty Diana is a rock-driven song about groupies and the dark side of fame. Released in 1987, it features heavy guitar riffs and shows Michael's edgier side. It became his fifth number-one single from the Bad album."},
    
    {"title": "Black or White", "year": "1991", "youtube_id": "F2AitTPI5U0", "description": "Black or White promotes racial unity and equality. Released in 1991, the groundbreaking music video featured revolutionary 'morphing' technology where faces blend into each other and ended with Michael's famous dance sequence. The song's message is timeless and powerful."},
    
    {"title": "Remember the Time", "year": "1991", "youtube_id": "LeiFF0gvqcc", "description": "This song features an epic ancient Egyptian-themed music video starring Eddie Murphy and supermodel Iman. Released in 1991, the track has a sensual R&B feel and showcases Michael's smooth vocals and incredible dance moves in a palace setting."},
    
    {"title": "Heal the World", "year": "1991", "youtube_id": "BWf-eARnf6U", "description": "Heal the World is a humanitarian ballad dedicated to making the world a better place for children. Released in 1991, Michael established the Heal the World Foundation to support children in need around the globe. The song features children singing with Michael."},
    
    {"title": "Don't Stop 'Til You Get Enough", "year": "1979", "youtube_id": "yURRmWtbTbo", "description": "This disco-funk classic was Michael's first solo single as an adult. Released in 1979, the song features his signature falsetto and celebratory lyrics. It won a Grammy Award and launched the Off the Wall era, establishing Michael as a solo superstar."},
    
    {"title": "Rock With You", "year": "1979", "youtube_id": "5X-Mrc2l1d0", "description": "Rock With You is a smooth, romantic disco ballad. Released in 1979, it became the second single from Off the Wall and showcases Michael's incredible vocal range and charismatic delivery. The song spent four weeks at number one."},
    
    {"title": "Earth Song", "year": "1995", "youtube_id": "0P4A1K4lXDo", "description": "Earth Song is a powerful environmental anthem released in 1995. Michael's passionate performance and the dramatic music video highlight urgent issues of deforestation, pollution, war, and animal cruelty. It became a massive global hit, especially in Europe."},
    
    {"title": "You Are Not Alone", "year": "1995", "youtube_id": "pAyKJAtDNCw", "description": "This emotional ballad holds the Guinness World Record for first song to debut at number one on the Billboard Hot 100. Released in 1995, the song offers comfort to those feeling lonely or isolated and features Michael partially naked in a spiritual setting."},
    
    {"title": "They Don't Care About Us", "year": "1995", "youtube_id": "QNJL6nfu__Q", "description": "A powerful protest song addressing social injustice, racism, and police brutality. Released in 1995, the song features powerful drumming from Brazil and two controversial but impactful music videos that show the harsh realities of poverty and oppression."},
    
    {"title": "Blood on the Dance Floor", "year": "1997", "youtube_id": "Hk3MWN7S1qk", "description": "This song combines elements of new jack swing and industrial dance. Released in 1997, it tells a dark story of seduction and betrayal, with one of Michael's most energetic dance performances. The music video features Michael in a club setting."},
    
    {"title": "You Rock My World", "year": "2001", "youtube_id": "sV9JNsMGyys", "description": "The lead single from Invincible album, featuring actor Chris Tucker. Released in 2001, the song returns to Michael's classic funk and R&B sound with an elaborate 13-minute music video that includes a cameo by Marlon Brando."},
    
    {"title": "Wanna Be Startin' Somethin'", "year": "1982", "youtube_id": "3VU8jNp4XqQ", "description": "This high-energy track features African-inspired rhythms and the famous 'Mama-se, mama-sa, ma-ma-ko-ssa' chant. Released in 1982 on Thriller, it became a cornerstone of the album and a fan favorite live performance."},
    
    {"title": "Human Nature", "year": "1982", "youtube_id": "B4jBnPp7H-w", "description": "A beautiful, introspective ballad about human emotions and connection. Released in 1982 on Thriller, the song's gentle melody and Michael's tender vocals made it a timeless classic. It was written by keyboardist Steve Porcaro of Toto."},
    
    {"title": "Liberian Girl", "year": "1987", "youtube_id": "FXPdIuNtSfA", "description": "This song honors African beauty and culture. Released in 1987 on Bad, the music video features numerous celebrity cameos including Steven Spielberg, Whoopi Goldberg, and Eddie Murphy, all waiting for Michael to arrive on set."}
]

# Display each song with AI voice
for idx, song in enumerate(songs):
    with st.container():
        st.markdown(f"<div class='song-card'>", unsafe_allow_html=True)
        
        # Song Title and Year
        st.markdown(f"<p class='song-title'>🎵 {song['title']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='song-year'>📅 {song['year']}</p>", unsafe_allow_html=True)
        
        # Song Description
        st.markdown(f"<p class='song-desc'>{song['description']}</p>", unsafe_allow_html=True)
        
        # AI Female Voice Audio
        st.markdown("🎤 **AI Female Voice Description**")
        audio_bytes = text_to_speech_audio(song['description'], song['title'])
        if audio_bytes:
            st.audio(audio_bytes, format="audio/mp3")
            st.caption("✨ AI Female Voice - Click play to hear the song description read aloud ✨")
        else:
            st.warning("⚠️ Audio generation failed - please check gTTS installation")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # YouTube Music Video
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
star_message.markdown("🎤 **Ready to journey?** Explore all songs above!")

# ---------------------------- STATS ----------------------------
st.sidebar.markdown("---")
st.sidebar.markdown(f"**🎵 Total Songs:** {len(songs)}")
st.sidebar.markdown("**🎤 AI Female Voice for EVERY song**")
st.sidebar.markdown("**🎬 All YouTube Videos Working**")
st.sidebar.markdown("**⭐ King of Pop Legacy**")
