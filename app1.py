
import streamlit as st
import streamlit.components.v1 as components
import os
import base64
import html

st.set_page_config(
    page_title="Sorry Zoya ❤️",
    page_icon="💗",
    layout="centered"
)

# ==========================================
# FILE PATHS
# ==========================================

song_path = r"C:\Users\hp\Downloads\S_Streamlit\Chalo Jaane Do - Lyrical Video Song Bhoothnath Amitabh Bachchan, Juhi Chawla.mp3"

image_path = r"C:\Users\hp\Downloads\S_Streamlit\tt.jpeg"


# ==========================================
# CSS DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #210c22, #47152f, #210c22);
    color: white;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    color: #ffacd2;
    text-shadow: 0 0 15px #ff3f91, 0 0 35px #ff3f91;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {text-shadow: 0 0 10px #ff3f91;}
    to {text-shadow: 0 0 30px white, 0 0 50px #ff3f91;}
}

.heart {
    text-align: center;
    font-size: 75px;
    color: #ff72ae;
    animation: beat 1s infinite;
}

@keyframes beat {
    0%, 100% {transform: scale(1);}
    50% {transform: scale(1.2);}
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #ffd6e9;
}

.letter {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,150,200,0.4);
    border-radius: 25px;
    padding: 35px 22px;
    text-align: center;
    box-shadow: 0 0 30px rgba(255,70,150,0.18);
}

.letter p {
    color: #ffe5f0;
    font-size: 20px;
    line-height: 2;
    margin-bottom: 22px;
    font-family: Georgia, serif;
}

.photo-caption {
    text-align: center;
    color: #ffacd2;
    font-size: 19px;
    margin-top: 15px;
}

.stTextInput input {
    text-align: center;
    border-radius: 15px;
    font-size: 20px;
}

.stButton button {
    background: linear-gradient(90deg,#ff4f98,#bd4cff);
    color: white;
    border: none;
    border-radius: 30px;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
}

.stButton button:hover {
    color: white;
    box-shadow: 0 0 20px #ff4f98;
    border: 1px solid white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# FLOATING HEART ANIMATION
# ==========================================

components.html("""
<style>

.float {
    position: fixed;
    bottom: -50px;
    color: #ff78b5;
    font-size: 25px;
    animation: up 9s linear infinite;
    pointer-events: none;
}

@keyframes up {
    0% {transform:translateY(0);opacity:0;}
    20% {opacity:0.8;}
    100% {transform:translateY(-100vh);opacity:0;}
}

</style>

<div class="float" style="left:10%">♥</div>
<div class="float" style="left:30%;animation-delay:2s">♡</div>
<div class="float" style="left:50%;animation-delay:4s">♥</div>
<div class="float" style="left:70%;animation-delay:1s">♡</div>
<div class="float" style="left:90%;animation-delay:3s">♥</div>

""", height=0)


# ==========================================
# MUSIC PLAYER WITH VISUALIZER
# ==========================================

if os.path.exists(song_path):

    with open(song_path, "rb") as f:
        audio_data = base64.b64encode(f.read()).decode("utf-8")

    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>

    <style>

    body {{
        margin: 0;
        background: transparent;
        font-family: Arial, sans-serif;
    }}

    .player {{
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,150,200,0.4);
        border-radius: 22px;
        padding: 20px;
        text-align: center;
        color: white;
    }}

    .song-name {{
        color: #ffacd2;
        font-size: 17px;
        font-weight: bold;
        margin-bottom: 15px;
    }}

    .visualizer {{
        height: 65px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 6px;
        margin-bottom: 15px;
    }}

    .bar {{
        width: 7px;
        height: 8px;
        border-radius: 10px;
        background: linear-gradient(to top, #ff4f98, #d9a0ff);
        transition: height 0.2s;
    }}

    .playing .bar {{
        animation: dance 0.65s ease-in-out infinite alternate;
    }}

    .bar:nth-child(2n) {{ animation-delay: 0.2s; }}
    .bar:nth-child(3n) {{ animation-delay: 0.4s; }}
    .bar:nth-child(4n) {{ animation-delay: 0.1s; }}

    @keyframes dance {{
        from {{ height: 8px; }}
        to {{ height: 55px; }}
    }}

    .music-btn {{
        background: linear-gradient(90deg,#ff4f98,#bd4cff);
        color: white;
        border: none;
        padding: 12px 35px;
        border-radius: 30px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }}

    .status {{
        color: #ffc5df;
        font-size: 13px;
        margin-top: 12px;
    }}

    </style>
    </head>

    <body>

    <div class="player">

        <div class="song-name">
            ♡ A Special Song For Zoya ♡
        </div>

        <div class="visualizer" id="visualizer">
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
        </div>

        <button class="music-btn" id="playBtn">
            ▶ Play Music
        </button>

        <div class="status" id="status">
            Your special song is waiting...
        </div>

        <audio id="music" loop preload="auto">
            <source
            src="data:audio/mpeg;base64,{audio_data}"
            type="audio/mpeg">
        </audio>

    </div>

    <script>

    const music = document.getElementById("music");
    const button = document.getElementById("playBtn");
    const visualizer = document.getElementById("visualizer");
    const status = document.getElementById("status");

    music.volume = 0.7;

    function updatePlaying() {{
        visualizer.classList.add("playing");
        button.innerHTML = "❚❚ Pause Music";
        status.innerHTML = "♪ Now Playing... ♡";
    }}

    function updatePaused() {{
        visualizer.classList.remove("playing");
        button.innerHTML = "▶ Play Music";
        status.innerHTML = "Music Paused";
    }}

    music.addEventListener("playing", updatePlaying);
    music.addEventListener("pause", updatePaused);

    music.addEventListener("error", function() {{
        status.innerHTML = "Unable to load song. Check the MP3 file.";
    }});

    button.addEventListener("click", function() {{

        if (music.paused) {{

            music.play().then(() => {{
                updatePlaying();
            }}).catch(() => {{
                status.innerHTML = "Please try playing again.";
            }});

        }} else {{

            music.pause();

        }}

    }});

    // Attempt autoplay when the page opens
    music.play().then(() => {{
        updatePlaying();
    }}).catch(() => {{
        status.innerHTML = "Tap Play Music to start your song ♡";
    }});

    </script>

    </body>
    </html>
    """, height=190, scrolling=False)

else:
    st.error("Song file not found! Please check the MP3 path.")


# ==========================================
# MAIN SCREEN
# ==========================================

st.markdown(
    '<div class="heart">♡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">I AM SORRY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">A message from my heart...</p>',
    unsafe_allow_html=True
)

st.write("")


# ==========================================
# NAME VERIFICATION
# ==========================================

name = st.text_input(
    "Enter your special person's name",
    placeholder="Enter name here..."
)

if name:

    if name.strip().lower() == "zoya":

        st.markdown("""
        <h1 style="
        text-align:center;
        color:#ffacd2;
        font-size:45px;
        text-shadow:0 0 15px #ff4f98;">
        Hey Zoya...
        </h1>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="heart">♡</div>',
            unsafe_allow_html=True
        )


        # ==================================
        # YOUR SMALL PHOTO
        # ==================================

        if os.path.exists(image_path):

            left, center, right = st.columns([1, 2, 1])

            with center:
                st.image(
                    image_path,
                    width=260
                )

            st.markdown("""
            <p class="photo-caption">
            Just me, saying sorry to my favourite person ♡
            </p>
            """, unsafe_allow_html=True)

        else:
            st.warning("Your photo was not found!")


        st.write("")


        # ==================================
        # PERSONAL APOLOGY MESSAGE
        # ==================================

        st.markdown("""
        <div class="letter">

        <h2 style="color:#ffacd2;">
        Zoya, mera bachha...
        </h2>

        <p>
        Meri jaan,<br>
        Mera bachha,<br>
        Meri gulum,<br>
        My sweetie,<br>
        My sweedie,<br>
        Mera sab kuch...
        </p>

        <h2 style="color:#ffacd2;">
        I'm Sorry Na Gulum...
        </h2>

        <p>
        I mean haan, maine gussa kiya tujhpe.
        But Zoya, main aapse dur nahi jaana chahta hoon na.
        </p>

        <p>
        Tu meri jaan hai na...
        Gulum, mera bachha, aap toh mere ho.
        Thoda sa gussa ho gaya toh kya ho gaya,
        meri jaan?
        </p>

        <p>
        Ab se ye gussa nahi karunga,
        aur itna sa bhi nahi chillaaunga.
        </p>

        <p>
        Bas maine react kiya kyunki mujhe hurt hua tha.
        But iska matlab ye nahi ki main aapse dur jaana chahta hoon.
        </p>

        <p>
        Ab se nahi chillaaunga, promise.
        Main apne gusse ko better handle karne ki
        poori koshish karunga.
        </p>

        <h2 style="color:#ffacd2;">
        Tum meri jaan ho na...
        </h2>

        <div style="font-size:75px;">
        💗
        </div>

        <h1 style="
        color:#ffacd2;
        text-shadow:0 0 15px #ff4f98;">
        I'M REALLY SORRY ZOYA
        </h1>

        </div>
        """, unsafe_allow_html=True)


        st.write("")


        # ==================================
        # FORGIVENESS BUTTON
        # ==================================

        if "forgiven" not in st.session_state:
            st.session_state.forgiven = False

        if st.button(
            "Can You Forgive Me, Gulum? 💗",
            use_container_width=True
        ):
            st.session_state.forgiven = True

        if st.session_state.forgiven:

            st.balloons()

            st.markdown("""
            <div class="letter">

            <h1 style="color:#ffacd2;">
            Thank You, My Gulum!
            </h1>

            <p>
            Ab smile kar do na, mera bachha.
            <br><br>
            I promise to take better care of your feelings.
            </p>

            <div style="font-size:85px;">
            💗
            </div>

            <h2 style="color:white;">
            You are my favourite person.
            </h2>

            <h3 style="color:#ffacd2;">
            Love you, Gulum!
            </h3>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.error(
            "Access Denied! This special message is only for Zoya."
        )

        st.markdown("""
        <h3 style="text-align:center;color:#ffacd2;">
        Sorry, this message belongs to someone special.
        </h3>
        """, unsafe_allow_html=True)

else:

    st.markdown("""
    <p style="text-align:center;color:#ffacd2;font-size:18px;">
    Someone special is waiting for a beautiful message...
    </p>
    """, unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<hr style="border-color:#71334f;">

<p style="text-align:center;color:#d99bb9;">
Made with love, from Tarique's heart.
</p>
""", unsafe_allow_html=True)
