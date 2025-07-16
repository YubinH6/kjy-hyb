import streamlit as st
import random

st.set_page_config(page_title="개보점프 심화탐구 퀴즈", page_icon="🔒")

st.title("🔒 개보점프 심화탐구")
st.write("개보점프 심화탐구 퀴즈에 오신 것을 환영합니다")
st.write("2025 STEAM융합수업의 아동 개인정보 보호, 물리 과학, 유엔아동권리협약을 재미있게 배워봐요!")
st.write("한 번 문제를 풀어볼까요?\n")

quiz_list = [
    # 1번 영역: 아동 개인정보 보호 개념
    {
        "type": "5지선다",
        "category": "아동 개인정보 보호",
        "question": "다음 중 아동의 사생활 보호에 어긋나는 행동은 무엇일까요?",
        "options": [
            "나의 정보 지우기 요청하기",
            "친구 이름을 인터넷에 올리기",
            "사진을 찍기 전 친구의 동의받기",
            "집 주소를 안 알리기",
            "정보 수집 동의서 꼼꼼하게 읽기"
        ],
        "answer": "친구 이름을 인터넷에 올리기",
        "explanation": None
    },
    {
        "type": "OX",
        "category": "아동 개인정보 보호",
        "question": "AI 교과서가 나의 학습 상태를 저장하는 것도 개인정보 수집이다.",
        "answer": "O",
        "explanation": None
    },
    {
        "type": "5지선다",
        "category": "아동 개인정보 보호",
        "question": "개인정보를 수집할 때 필요한 것은 무엇일까요?",
        "options": [
            "학습을 도와주기 위해",
            "친구와 비교하려고",
            "광고를 만들려고",
            "기억력이 나빠서",
            "그냥"
        ],
        "answer": "학습을 도와주기 위해",
        "explanation": None
    },
    # 2번 영역: 융합수업 내 물리 과학 개념
    {
        "type": "5지선다",
        "category": "물리 과학",
        "question": "자유전자는 어디에서 움직일까요?",
        "options": [
            "핵 안",
            "전선 밖",
            "물질의 내부",
            "바깥 공기",
            "세포 속"
        ],
        "answer": "물질의 내부",
        "explanation": None
    },
    {
        "type": "5지선다",
        "category": "물리 과학",
        "question": "도체란 자유 전자가 많아 전류가 잘 흐르는 물질이다. 다음 중 도체에 해당하는 것은 무엇일까요?",
        "options": [
            "나무",
            "유리",
            "철",
            "고무",
            "플라스틱"
        ],
        "answer": "철",
        "explanation": None
    },
    {
        "type": "5지선다",
        "category": "물리 과학",
        "question": "부도체란 자유 전자가 거의 없어 전류가 잘 흐르지 않는 물질이다. 다음 중 부도체에 해당하는 것은 무엇일까요?",
        "options": [
            "금",
            "구리",
            "은",
            "알루미늄",
            "고무"
        ],
        "answer": "고무",
        "explanation": None
    },
    {
        "type": "5지선다",
        "category": "물리 과학",
        "question": "반도체는 전기를 어떻게 흘릴까요?",
        "options": [
            "항상 흐르게 한다.",
            "절대로 안 흐르게 한다.",
            "일정 시간만 흐르게 한다.",
            "조건에 따라 흐르게도 하고 안 흐르게도 한다.",
            "전혀 관련없다."
        ],
        "answer": "조건에 따라 흐르게도 하고 안 흐르게도 한다.",
        "explanation": None
    },
    # 3번 영역: 유엔아동권리협약 관련 인권
    {
        "type": "OX",
        "category": "유엔아동권리협약",
        "question": "아동도 의견을 표현할 권리가 있다.",
        "answer": "O",
        "explanation": "유엔아동권리협약 제 12조에 따르면 아동은 자신에게 영향을 미치는 일에 대해 자유롭게 의견을 말할 권리가 있습니다."
    },
    {
        "type": "OX",
        "category": "유엔아동권리협약",
        "question": "유엔아동권리협약은 초등학생들에만 해당한다.",
        "answer": "X",
        "explanation": "유엔아동권리협약 제 1조에 따르면 아동이란, 18세 미만의 모든 사람을 의미합니다. 따라서 초등학생들만 해당되는 것이 아닙니다."
    },
    {
        "type": "5지선다",
        "category": "유엔아동권리협약",
        "question": "다음 중 아동의 권리에 해당하지 않는 것은 무엇일까요?",
        "options": [
            "차별받지 않을 권리",
            "의견을 말할 권리",
            "스스로 정보를 공유할 권리",
            "보호 받을 권리",
            "돈을 벌기 위한 노동 의무"
        ],
        "answer": "돈을 벌기 위한 노동 의무",
        "explanation": None
    }
]

TOTAL_QUESTIONS = 10
POINTS_PER_QUESTION = 10

# 세션 상태 초기화
if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = random.sample(range(len(quiz_list)), TOTAL_QUESTIONS)
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None

def show_encouragement(score):
    percent = (score / (TOTAL_QUESTIONS * POINTS_PER_QUESTION)) * 100
    if percent == 100:
        return "🌟 완벽해요! 당신은 아동 인권과 과학 지식 모두를 잘 알고 있어요. 진짜 멋져요!"
    elif 90 <= percent < 100:
        return "👏 훌륭해요! 아주 깊이 있는 이해를 보여줬어요. 거의 완벽에 가까워요. 조금만 더 힘내요!"
    elif 70 <= percent < 90:
        return "👍 잘했어요! 중요한 개념을 잘 알고 있어요. 부족한 부분은 다시 복습하면 금방 좋아져요!"
    elif 50 <= percent < 70:
        return "🙂 괜찮아요. 아직 부족한 부분이 있지만, 노력하는 과정 자체가 훌륭해요. 앞으로가 더 기대돼요!"
    elif 30 <= percent < 50:
        return "😅 조금 아쉬워요. 틀린 문제를 다시 복습하면 분명 더 나아질 수 있어요. 지금이 시작이에요!"
    elif 10 <= percent < 30:
        return "🌱 아직 연습이 필요해요. 걱정 말고 하나하나 다시 해보면 누구든지 잘할 수 있어요."
    else:
        return "📖 괜찮아요. 모든 시작은 작은 실수에서부터예요. 틀려도 괜찮아요. 함께 다시 배워봐요!"

def reset_quiz():
    st.session_state.quiz_order = random.sample(range(len(quiz_list)), TOTAL_QUESTIONS)
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None

def show_question(idx):
    quiz = quiz_list[idx]
    st.subheader(f"문제 {st.session_state.current + 1} / {TOTAL_QUESTIONS}")
    st.write(f"**{quiz['question']}**")

    selected = st.session_state.selected

    if quiz["type"] == "OX":
        col1, col2 = st.columns(2)
        if col1.button("⭕ O") and not st.session_state.answered:
            st.session_state.selected = "O"
            st.session_state.answered = True
        if col2.button("❌ X") and not st.session_state.answered:
            st.session_state.selected = "X"
            st.session_state.answered = True

    else: 
        cols = st.columns(5)
        for i, option in enumerate(quiz["options"]):
            if cols[i].button(option) and not st.session_state.answered:
                st.session_state.selected = option
                st.session_state.answered = True

    if st.session_state.answered and selected is not None:
        if selected == quiz["answer"]:
            st.success("✅ 정답입니다! 아주 잘했어요! 🎉")
            if not getattr(st.session_state, "scored_for_current", False):
                st.session_state.score += POINTS_PER_QUESTION
                st.session_state.scored_for_current = True
        else:
            st.error(f"❌ 오답입니다. 정답은 '{quiz['answer']}'입니다.")
            if quiz["category"] == "유엔아동권리협약" and quiz["explanation"]:
                st.info(f"💡 해설: {quiz['explanation']}")

        if st.button("👉 다음 문제로 넘어가기"):
            st.session_state.current += 1
            st.session_state.answered = False
            st.session_state.selected = None
            st.session_state.scored_for_current = False

if st.session_state.current < TOTAL_QUESTIONS:
    show_question(st.session_state.quiz_order[st.session_state.current])
else:
    st.header("🎉 퀴즈 완료!")
    st.write("수고하셨습니다.")
    st.write(f"총 점수: {st.session_state.score} / {TOTAL_QUESTIONS * POINTS_PER_QUESTION}점")
    st.markdown(f"### {show_encouragement(st.session_state.score)}")

    if st.button("🔁 처음부터 다시 풀기"):
        reset_quiz()
