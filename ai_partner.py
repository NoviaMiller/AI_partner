import streamlit as st
import os
from openai import OpenAI
from streamlit import session_state
from datetime import datetime
import json


# =============================================================================
# ------------------------------ 【 func define 】 ------------------------------
# =============================================================================

def change_nick_name():
    st.session_state.nick_name = st.session_state.nick_name_temp
    st.session_state.nick_name_temp = ""
def change_character():
    st.session_state.character = st.session_state.character_temp
    st.session_state.character_temp = ""

def change_lang():
    if st.session_state.lang_toggle:
        st.session_state.lang = "zh"
    else:
        st.session_state.lang = "en"

def generate_current_session():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_current_session():
    # 1. save the old one
    if st.session_state.current_session:
        # a. save the basic info of the old one
        data_messages = {
            "messages": st.session_state.messages,
            "nick_name": st.session_state.nick_name,
            "character": st.session_state.character,
            "current_session": st.session_state.current_session
        }

        # b. save to a file (director judge)
        if not os.path.isdir("sessions"):
            os.makedirs("sessions")

        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(data_messages, f, ensure_ascii=False, indent=2)
# end



def load_history_files():
    file_list = []

    # exist sessions folder
    if os.path.isdir("sessions"):
        file_names = os.listdir("sessions")
        for file_name in file_names:
            if file_name.endswith(".json"):
                file_list.append(file_name[:-5])

    # s.t. sort the file list by the time
    file_list.sort(reverse=True)
    return file_list
# end

def load_session(filename):
    try:
        if os.path.exists(f"sessions/{filename}.json"):
            with open(f"sessions/{filename}.json", "r", encoding="utf-8") as f:
                file_list = json.load(f)
                return file_list
        else:
            print(f"{filename}.json does not exist")
        raise FileNotFoundError(f"{filename}.json does not exist")
    except Exception as e:
        st.error(f"load fail: {e}", icon="❌")
        return None
# end


def delete_session(filename):
    try:
        if os.path.exists(f"sessions/{filename}.json"):
            os.remove(f"sessions/{filename}.json")
            if filename == st.session_state.current_session:
                st.session_state.current_session = generate_current_session()
                st.session_state.messages = []
        else:
            raise FileNotFoundError(f"{filename}.json does not exist")
    except Exception as e:
        st.error(f"delete fail: {e}", icon="❌")
# end

# =============================================================================
# ------------------------------ 【 page config 】 ------------------------------
# =============================================================================

# Create a language dictionary
LANG_DICT = {
    "en": {
        "title": "AI Partner",
        "sidebar_header": "AI Partner Panel",
        "new_session": "Create a new session",
        "name_label": "Name",
        "name_placeholder": "input name",
        "char_label": "Character",
        "char_placeholder": "input character",
        "history": "History Files:",
        "current_session": "current session",
        "prompt": "Say something"
    },
    "zh": {
        "title": "AI 伙伴",
        "sidebar_header": "AI 控制面板",
        "new_session": "新建对话会话",
        "name_label": "角色名称",
        "name_placeholder": "请输入角色名称",
        "char_label": "角色性格",
        "char_placeholder": "请输入角色性格",
        "history": "历史记录:",
        "current_session": "当前会话",
        "prompt": "说点什么"
    }
}

# call the api by create a client
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# save the messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "cute cat"
if "character" not in st.session_state:
    st.session_state.character = """you are very friendly and like to eat fish"""
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_current_session()
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "lang_toggle" not in st.session_state:
    st.session_state.lang_toggle = False


# it is a page config
st.set_page_config(
    page_title=LANG_DICT[st.session_state.lang]["title"],
    page_icon="🦌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': f"### {LANG_DICT[st.session_state.lang]['title']}"
    }
)

# system prompt
system_prompt = """
    你叫 %s, 接下来请扮演这个角色和用户进行互动.
    规则:
        1. 每次只回一条消息
        2. 回复简短精炼, 就和微信聊天一样
        3. 在不伤害到用户的情况下, 尽可能符合角色
    请务必遵守以上规则来回答用户的问题
    --- 
    性格等补充:
    %s
"""


# =============================================================================
# ------------------------------ 【 main of the page 】 ------------------------------
# =============================================================================



st.logo("🦌", size="large")


# side_bar
with st.sidebar:
    st.markdown("""
        <style>
        /* This targets the text label of the toggle */
        div[data-testid="stWidgetLabel"] p {
            font-size: 12px ; /* Change this number to your liking */
            color: #FAFAFA;             /* Optional: change color */
        }
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 0.8], gap="small")
    with col1:
        st.subheader(LANG_DICT[st.session_state.lang]["sidebar_header"])
    with col2:
        st.toggle("English/中文", key="lang_toggle", on_change=change_lang)

    # create a new session
    if st.button(LANG_DICT[st.session_state.lang]["new_session"], type="primary", icon="♋️", width="stretch"):
        # 1. save the old one
        save_current_session()



        # 2. create a new one
        if st.session_state.messages: # not empty
            st.session_state.messages = []
            st.session_state.current_session = generate_current_session()
            save_current_session()
    # new session button end


    # load history files
    st.write(LANG_DICT[st.session_state.lang]["history"])
    file_list = load_history_files()
    # show history files
    for file_name in file_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(file_name, icon="📄", width="stretch", key=f"load_{file_name}", type="primary" if file_name == st.session_state.current_session else "secondary"):
                # load the session
                session = load_session(file_name)
                if session:
                    st.session_state.messages = session["messages"]
                    st.session_state.nick_name = session["nick_name"]
                    st.session_state.character = session["character"]
                    st.session_state.current_session = session["current_session"]
                st.rerun()
        with col2:
            if st.button("", icon="❌", width="stretch", key=f"delete_{file_name}"):
                # delete the session
                delete_session(file_name)
                st.rerun()





    st.divider()
    col1, col2 = st.columns([1, 3])  # Adjust ratios as needed

    with col1:
        # Use <br> for a tight line break instead of a new st.write()
        labels = f"{LANG_DICT[st.session_state.lang]['name_label']}<br>{LANG_DICT[st.session_state.lang]['char_label']}"
        st.markdown(f"<p style='color: gray; font-size: 0.8rem; line-height: 2.2;'>{labels}</p>",
                    unsafe_allow_html=True)

    with col2:
        # Match the line height so the text aligns perfectly with the labels
        values = f"{st.session_state.nick_name}<br>{st.session_state.character}"
        st.markdown(f"<p style='line-height: 2.2;'>{values}</p>", unsafe_allow_html=True)

    # about ai partner
    st.text_input(LANG_DICT[st.session_state.lang]["name_label"],
                  placeholder=LANG_DICT[st.session_state.lang]["name_placeholder"],
                  key="nick_name_temp",
                  on_change=change_nick_name)
    st.text_area(LANG_DICT[st.session_state.lang]["char_label"],
                  placeholder=LANG_DICT[st.session_state.lang]["char_placeholder"],
                  key="character_temp",
                  on_change=change_character)


# title
st.title(LANG_DICT[st.session_state.lang]["title"])




# history content
st.write(f"{LANG_DICT[st.session_state.lang]["current_session"]}: {st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"], avatar=message["avatar"]).write(message["content"])


# chat
prompt = st.chat_input(LANG_DICT[st.session_state.lang]["prompt"])
if prompt:
    # show user prompt
    st.chat_message("user", avatar="🐭").write(prompt)
    # save the messages in session state
    st.session_state.messages.append({"role": "user", "avatar": "🐭", "content": prompt})


    # print(st.session_state.nick_name)
    # print(st.session_state.character)
    # info from ai partner
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.character)},
            *st.session_state.messages
        ],
        stream=True
    )

    # empty as response_container
    response_container = st.empty()

    # show ai partner response
    full_response = "";

    for chunk in response:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
        # renew the info in response_container
        response_container.chat_message("assistant", avatar="🐈‍⬛").write(full_response)

    # save the messages in session state
    st.session_state.messages.append({"role": "assistant", "avatar": "🐈‍⬛", "content": full_response})

    # global save
    save_current_session()
