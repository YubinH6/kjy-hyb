import streamlit as st

st.set_page_config(page_title="개보점프 - 개인정보 보호 퀴즈", page_icon="🔒")

st.title("🔒 개보점프에 오신 걸 환영합니다!")
st.write("개인정보 보호에 대해 잘 알고 있는지 퀴즈로 알아보세요!")
st.write("맞히면 칭찬, 틀리면 해설이 나옵니다.\n")

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

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
    st.session_state.score = 0
    st.session_state.answered = False

if st.session_state.quiz_step < len(quiz_list):
    quiz = quiz_list[st.session_state.quiz_step]
    st.subheader(f"문제 {st.session_state.quiz_step + 1}: {quiz['question']}")

    col1, col2 = st.columns(2)
    if col1.button("⭕ O") and not st.session_state.answered:
        st.session_state.answered = True
        selected = "O"
    elif col2.button("❌ X") and not st.session_state.answered:
        st.session_state.answered = True
        selected = "X"
    else:
        selected = None

    if st.session_state.answered:
        if selected == quiz["answer"]:
            st.success("✅ 정답입니다! 아주 잘했어요! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"❌ 오답입니다. 정답은 '{quiz['answer']}'예요.")
            st.info(f"💡 해설: {quiz['explanation']}")

        if st.button("👉 다음 문제로 넘어가기"):
            st.session_state.quiz_step += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.write(f"📊 퀴즈 완료! 총 {len(quiz_list)}문제 중 {st.session_state.score}문제를 맞혔어요.")
    if st.session_state.score == len(quiz_list):
        st.balloons()
        st.success("🌟 완벽해요! 개인정보 보호 챔피언입니다!")
    elif st.session_state.score >= 2:
        st.info("👍 잘했어요! 조금 더 공부하면 완벽할 수 있어요.")
    else:
        st.warning("📚 괜찮아요, 지금부터 배우면 늦지 않았어요!")

    if st.button("🔁 처음부터 다시 풀기"):
        st.session_state.quiz_step = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
