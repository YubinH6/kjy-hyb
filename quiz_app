# 개보점프 - 개인정보 보호 퀴즈 프로그램

def print_intro():
    print("🔒 개보점프에 오신 걸 환영합니다!")
    print("개인정보 보호에 대해 잘 알고 있는지 퀴즈로 알아보세요!")
    print("맞히면 칭찬, 틀리면 해설이 나옵니다.\n")

def ask_question(q_num, question, correct_answer, explanation):
    print(f"문제 {q_num}: {question}")
    user_answer = input("👉 O 또는 X로 답해주세요: ").strip().upper()

    if user_answer == correct_answer:
        print("✅ 정답입니다! 아주 잘했어요! 🎉\n")
        return True
    else:
        print(f"❌ 오답입니다. 정답은 '{correct_answer}'예요.")
        print(f"💡 해설: {explanation}\n")
        return False

def main():
    print_intro()

    score = 0
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

    for i, quiz in enumerate(quiz_list, start=1):
        if ask_question(i, quiz["question"], quiz["answer"], quiz["explanation"]):
            score += 1

    print(f"📊 퀴즈 완료! 총 {len(quiz_list)}문제 중 {score}문제를 맞혔어요.")
    if score == len(quiz_list):
        print("🌟 완벽해요! 개인정보 보호 챔피언입니다!")
    elif score >= 2:
        print("👍 잘했어요! 조금 더 공부하면 완벽할 수 있어요.")
    else:
        print("📚 괜찮아요, 지금부터 배우면 늦지 않았어요!")

if __name__ == "__main__":
    main()
