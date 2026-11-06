
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="I'm Sorry",
    page_icon="💗",
    layout="centered"
)

# CSS Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #190b25, #42152f, #190b25);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    color: #ffb6d9;
    text-shadow: 0 0 15px #ff4d94, 0 0 35px #ff4d94;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #ff4d94; }
    to { text-shadow: 0 0 30px white, 0 0 50px #ff4d94; }
}

.message {
    text-align: center;
    font-size: 19px;
    color: #ffe3f0;
    line-height: 1.8;
}

.heart {
    text-align: center;
    font-size: 75px;
    animation: beat 1s infinite;
}

@keyframes beat {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# Floating hearts
components.html("""
<div style="position:fixed; bottom:0; left:0; width:100%;
height:100%; pointer-events:none; overflow:hidden; z-index:0;">
<style>
.floating {
 position:absolute;
 bottom:-50px;
 color:#ff80b5;
 animation: floatUp 8s linear infinite;
 opacity:0.7;
}
@keyframes floatUp {
 0% {transform:translateY(0) rotate(0deg); opacity:0;}
 20% {opacity:0.8;}
 100% {transform:translateY(-100vh) rotate(360deg); opacity:0;}
}
</style>
<div class="floating" style="left:10%; animation-delay:0s;">♥</div>
<div class="floating" style="left:30%; animation-delay:2s;">♥</div>
<div class="floating" style="left:50%; animation-delay:4s;">♥</div>
<div class="floating" style="left:70%; animation-delay:1s;">♥</div>
<div class="floating" style="left:90%; animation-delay:3s;">♥</div>
</div>
""", height=0)

# Main heading
st.markdown('<div class="heart">♡</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">I AM SORRY</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Personal name
name = st.text_input(
    "Who am I saying sorry to?",
    placeholder="Enter your special person's name..."
)

if name:

    st.markdown(
        f"<h2 style='text-align:center;color:#ffb6d9;'>"
        f"Hey {name}...</h2>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="message">
        I know that sometimes words are not enough.<br>
        But today, I just want to tell you something.<br><br>

        I never wanted to hurt you.<br>
        I never wanted to make you feel bad.<br><br>

        Maybe I made mistakes, maybe I could have handled
        things better...<br><br>

        But I genuinely feel sorry.<br>
        You are important to me, and I don't want a small
        misunderstanding to ruin something beautiful.<br><br>

        I cannot change what happened,<br>
        but I can promise to try to do better.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Song upload
    st.markdown(
        "<h3 style='text-align:center;color:#ffb6d9;'>"
        "A Song For You</h3>",
        unsafe_allow_html=True
    )

    song = st.file_uploader(
        "Upload your special song (MP3/WAV)",
        type=["mp3", "wav"]
    )

    if song:
        st.audio(song, format=song.type)

    st.markdown("<br>", unsafe_allow_html=True)

    # Forgiveness button
    if "forgiven" not in st.session_state:
        st.session_state.forgiven = False

    if st.button("Can You Forgive Me? 💗", use_container_width=True):

        st.session_state.forgiven = True

    if st.session_state.forgiven:

        st.balloons()

        st.markdown("""
        <div style="
            text-align:center;
            background:rgba(255,255,255,0.08);
            padding:25px;
            border-radius:20px;
            border:1px solid #ff80b5;
        ">
            <h1 style="color:#ffb6d9;">Thank You!</h1>
            <h2 style="color:white;">You mean a lot to me.</h2>
            <div style="font-size:65px;">💗</div>
            <p style="color:#ffe3f0;font-size:19px;">
                No matter what, I will always cherish you.
            </p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <p style="text-align:center;color:#ffb6d9;font-size:18px;">
        Someone is waiting to say something from the heart...
    </p>
    """, unsafe_allow_html=True)

st.markdown("""
<hr>
<p style="text-align:center;color:#dba6c3;">
Made with love and a little regret.
</p>
""", unsafe_allow_html=True)
