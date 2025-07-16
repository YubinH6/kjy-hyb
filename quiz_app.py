import streamlit as st

quiz_list = [
    {
        "question": "AI 교과서는 학생의 얼굴 인식 정보를 수집할 수 있다.",
        "answer": "O",
        "explanation": "일부 AI 시스템은 얼굴 인식 기능을 통해 출석 체크 등을 할 수 있습니다."
    },
    {
        "question": "이름, 주소, 전화번호는 개인정보가 아니다.",
        "answer": "X",
        "explanation": "이름, 주소, 전화번호 모두 개인정보에 해당합니다."
    },
    {
        "question": "친구의 개인정보를 허락 없이 단체 채팅방에 올려도 괜찮다.",
        "answer": "X",
        "explanation": "본인의 동의 없이 개인정보를 공유하는 것은 불법입니다."
    }
]

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

def check_answer(user_answer):
    correct_answer = quiz_list[st.session_state.current_question]["answer"]
    if user_answer == correct_answer:
        st.session_state.score += 1
        st.success("✅ 정답입니다! 아주 잘했어요! 🎉")
    else:
        st.error(f"❌ 오답입니다. 정답은 '{correct_answer}'입니다.")
        st.info(f"💡 해설: {quiz_list[st.session_state.current_question]['explanation']}")
    st.session_state.answered = True

st.title("🔒 개보점프 - 개인정보 보호 퀴즈")

if st.session_state.current_question < len(quiz_list):
    q = quiz_list[st.session_state.current_question]
    st.write(f"문제 {st.session_state.current_question + 1}: {q['question']}")

    if not st.session_state.answered:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("O"):
                check_answer("O")
        with col2:
            if st.button("X"):
                check_answer("X")
    else:
        if st.button("다음 문제"):
            st.session_state.current_question += 1
            st.session_state.answered = False
else:
    st.write(f"퀴즈 완료! 총 {len(quiz_list)}문제 중 {st.session_state.score}문제를 맞혔어요.")
    if st.session_state.score == len(quiz_list):
        st.success("🌟 완벽해요! 개인정보 보호 챔피언입니다!")
    elif st.session_state.score >= 2:
        st.info("👍 잘했어요! 조금 더 공부하면 완벽할 수 있어요.")
    else:
        st.warning("📚 괜찮아요, 지금부터 배우면 늦지 않았어요!")
