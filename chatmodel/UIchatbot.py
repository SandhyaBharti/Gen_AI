import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Personal Chat",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

PERSONALITIES = {
    "funny":     {"label": "😂 Funny",     "system": "You are a hilarious and witty AI. Make every reply funny with puns and jokes, but still be helpful.", "accent": "#f5a623", "bg": "rgba(245,166,35,0.12)",  "glow": "rgba(245,166,35,0.3)"},
    "angry":     {"label": "😤 Angry",     "system": "You are an irritable, hot-headed AI. You respond with barely-concealed frustration and impatience, but still answer.", "accent": "#e53935", "bg": "rgba(229,57,53,0.12)",   "glow": "rgba(229,57,53,0.3)"},
    "sarcastic": {"label": "🙄 Sarcastic", "system": "You are a deeply sarcastic AI. Layer every response with dry wit and eye-rolling sarcasm, but still answer.", "accent": "#ab47bc", "bg": "rgba(171,71,188,0.12)", "glow": "rgba(171,71,188,0.3)"},
    "sad":       {"label": "😢 Sad",       "system": "You are a melancholic, sad AI. You respond with a heavy heart and gentle sighs, but still try to help.", "accent": "#42a5f5", "bg": "rgba(66,165,245,0.12)",  "glow": "rgba(66,165,245,0.3)"},
    "romantic":  {"label": "💕 Romantic",  "system": "You are a deeply romantic AI. You speak with warmth, poetic flair and tender affection in every reply.", "accent": "#ec407a", "bg": "rgba(236,64,122,0.12)",  "glow": "rgba(236,64,122,0.3)"},
}

if "persona" not in st.session_state:
    st.session_state.persona = None
if "messages" not in st.session_state:
    st.session_state.messages = []


def inject_css(accent="#7c3aed", bg="rgba(124,58,237,0.12)", glow="rgba(124,58,237,0.3)"):
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [data-testid="stApp"] {{
    min-height: 100vh;
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0d0d1a 0%, #12102b 50%, #0d0d1a 100%);
    background-size: 200% 200%;
    animation: bgPulse 20s ease infinite;
}}
@keyframes bgPulse {{
    0%,100% {{ background-position: 0% 50%; }}
    50%      {{ background-position: 100% 50%; }}
}}

#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] {{ display:none !important; visibility:hidden !important; }}

.main .block-container {{
    max-width: 760px;
    padding: 2rem 1.25rem 7rem;
    margin: 0 auto;
}}

.pg-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.9rem; font-weight: 700;
    color: #fff; text-align: center;
    letter-spacing: -0.5px; margin-bottom: 0.15rem;
}}
.pg-sub {{
    text-align: center;
    color: rgba(255,255,255,0.38);
    font-size: 0.82rem; margin-bottom: 1.5rem;
}}

.persona-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    background: {bg}; border: 1px solid {accent};
    border-radius: 20px; padding: 0.3rem 0.9rem;
    font-size: 0.78rem; color: rgba(255,255,255,0.8);
    margin-bottom: 1rem; box-shadow: 0 0 14px {glow};
}}

.msg-wrap {{ display:flex; margin-bottom:0.9rem; animation: fadeUp 0.25s ease both; }}
@keyframes fadeUp {{ from{{opacity:0;transform:translateY(8px)}} to{{opacity:1;transform:translateY(0)}} }}
.msg-wrap.user {{ justify-content:flex-end; }}
.msg-wrap.bot  {{ justify-content:flex-start; }}

.bubble {{
    max-width: 72%; padding: 0.75rem 1rem;
    border-radius: 18px; font-size: 0.88rem; line-height: 1.6;
    backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    word-break: break-word;
}}
.bubble.user {{
    background: {bg}; border-color: {accent};
    color: #f0f0ff; border-bottom-right-radius: 4px;
    box-shadow: 0 4px 20px {glow};
}}
.bubble.bot {{
    background: rgba(255,255,255,0.07);
    color: rgba(255,255,255,0.85);
    border-bottom-left-radius: 4px;
}}

.avatar {{
    width:28px; height:28px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:0.7rem; font-weight:600; flex-shrink:0;
    border: 1px solid rgba(255,255,255,0.18);
}}
.avatar.user {{ background:{accent}66; color:#fff; margin-left:7px; }}
.avatar.bot  {{ background:rgba(255,255,255,0.1); color:rgba(255,255,255,0.7); margin-right:7px; }}

.typing {{ display:flex; align-items:center; gap:5px; padding:0.35rem 0; }}
.typing span {{
    width:7px; height:7px; border-radius:50%;
    background:{accent}; display:inline-block;
    animation:bounce 1.1s infinite ease-in-out;
}}
.typing span:nth-child(2) {{ animation-delay:0.18s; }}
.typing span:nth-child(3) {{ animation-delay:0.36s; }}
@keyframes bounce {{ 0%,60%,100%{{transform:translateY(0)}} 30%{{transform:translateY(-6px)}} }}

[data-testid="stChatInput"] {{
    background: rgba(255,255,255,0.06) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid {accent}66 !important;
    border-radius: 16px !important;
    box-shadow: 0 0 18px {glow} !important;
}}
[data-testid="stChatInput"] textarea {{
    color: rgba(255,255,255,0.9) !important;
    background: transparent !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
}}
[data-testid="stChatInput"] textarea::placeholder {{ color:rgba(255,255,255,0.3) !important; }}
[data-testid="stChatInput"] button {{
    background: {accent} !important;
    border-radius: 10px !important; color: #fff !important;
}}

[data-testid="stButton"] > button {{
    background: rgba(255,255,255,0.06) !important;
    color: rgba(255,255,255,0.55) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 10px !important; font-size: 0.76rem !important;
    backdrop-filter: blur(8px); transition: all 0.2s;
}}
[data-testid="stButton"] > button:hover {{
    background: rgba(255,255,255,0.12) !important;
    color: #fff !important; border-color: {accent} !important;
}}

.empty-hint {{
    text-align:center; color:rgba(255,255,255,0.22);
    font-size:0.82rem; margin-top:3rem; font-style:italic;
}}
</style>
""", unsafe_allow_html=True)


# ── inject CSS ────────────────────────────────────────────────────────────────
p = st.session_state.persona
if p and p in PERSONALITIES:
    inject_css(PERSONALITIES[p]["accent"], PERSONALITIES[p]["bg"], PERSONALITIES[p]["glow"])
else:
    inject_css()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="pg-title">🎭 Persona Chat</div>', unsafe_allow_html=True)
st.markdown('<div class="pg-sub">Pick a personality — then start talking</div>', unsafe_allow_html=True)

# ── Personality selector ──────────────────────────────────────────────────────
cols = st.columns(5)
persona_keys = list(PERSONALITIES.keys())

for i, col in enumerate(cols):
    key = persona_keys[i]
    info = PERSONALITIES[key]
    is_active = (st.session_state.persona == key)
    with col:
        btn_type = "primary" if is_active else "secondary"
        if st.button(info["label"], key=f"btn_{key}",
                     use_container_width=True, type=btn_type):
            if st.session_state.persona != key:
                st.session_state.persona = key
                st.session_state.messages = [
                    SystemMessage(content=PERSONALITIES[key]["system"])
                ]
                st.rerun()

# ── No persona selected ───────────────────────────────────────────────────────
if not p:
    st.markdown('<div class="empty-hint">⬆ Choose a personality above to start</div>',
                unsafe_allow_html=True)
    st.stop()

# ── Active badge + clear ──────────────────────────────────────────────────────
acc = PERSONALITIES[p]["accent"]
badge = PERSONALITIES[p]["label"]

col_l, col_r = st.columns([5, 1])
with col_l:
    st.markdown(
        f'<div class="persona-badge" style="margin-top:1rem;">'
        f'<span style="color:{acc}">●</span> {badge} mode</div>',
        unsafe_allow_html=True
    )
with col_r:
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    if st.button("Clear", key="clear_btn"):
        st.session_state.messages = [
            SystemMessage(content=PERSONALITIES[p]["system"])
        ]
        st.rerun()

# ── Chat history ──────────────────────────────────────────────────────────────
history = [m for m in st.session_state.messages if not isinstance(m, SystemMessage)]

if not history:
    emoji = PERSONALITIES[p]["label"].split()[0]
    name  = PERSONALITIES[p]["label"].split()[1].lower()
    st.markdown(f'<div class="empty-hint">{emoji} Your {name} AI is waiting…</div>',
                unsafe_allow_html=True)

for msg in history:
    if isinstance(msg, HumanMessage):
        st.markdown(f"""
        <div class="msg-wrap user">
            <div class="bubble user">{msg.content}</div>
            <div class="avatar user">YOU</div>
        </div>""", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"""
        <div class="msg-wrap bot">
            <div class="avatar bot">AI</div>
            <div class="bubble bot">{msg.content}</div>
        </div>""", unsafe_allow_html=True)

# ── Chat input ────────────────────────────────────────────────────────────────
name = PERSONALITIES[p]["label"].split()[1].lower()
if prompt := st.chat_input(f"Message your {name} AI…"):
    st.session_state.messages.append(HumanMessage(content=prompt))

    st.markdown(f"""
    <div class="msg-wrap user">
        <div class="bubble user">{prompt}</div>
        <div class="avatar user">YOU</div>
    </div>""", unsafe_allow_html=True)

    typing_ph = st.empty()
    typing_ph.markdown(f"""
    <div class="msg-wrap bot">
        <div class="avatar bot">AI</div>
        <div class="bubble bot">
            <div class="typing"><span></span><span></span><span></span></div>
        </div>
    </div>""", unsafe_allow_html=True)

    model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=300)
    res = model.invoke(st.session_state.messages)
    reply = res.content
    st.session_state.messages.append(AIMessage(content=reply))

    typing_ph.markdown(f"""
    <div class="msg-wrap bot">
        <div class="avatar bot">AI</div>
        <div class="bubble bot">{reply}</div>
    </div>""", unsafe_allow_html=True)