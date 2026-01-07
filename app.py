import streamlit as st
import random

def main():
    st.title("ワーキングメモリ トレーニング（試作版）")

    # セッション状態の初期化
    if "questions" not in st.session_state:
        st.session_state.questions = [
            "【トイレ】トイレの換気扇は回っていたか？",
            "【トイレ】トイレロールの残りはどのくらいだったか？",
            "【トイレ】水を流すノブはどちらの手で引いたか？",
            "【トイレ】トイレの電気は消したか？",
            "【歯磨き】歯磨きはどこからスタートして、どこを最後に磨き終えたか？",
            "【歯磨き】歯磨き中の姿勢はどうだったか？",
            "【歯磨き】歯磨き中に浮かんだ思考は？",
            "【歯磨き】歯磨き中に聞こえた環境音は？"
        ]
    
    if "current_q" not in st.session_state:
        st.session_state.current_q = None

    # トレーニングセクション
    st.subheader("トレーニング")
    if st.button("出題する", type="primary"):
        if st.session_state.questions:
            st.session_state.current_q = random.choice(st.session_state.questions)
        else:
            st.warning("質問リストが空です。下の編集エリアから追加してください。")
            st.session_state.current_q = None

    if st.session_state.current_q:
        st.markdown(f"### Q. {st.session_state.current_q}")
        # 回答入力欄 (HTMLのテキストボックス形式に近い Streamlit の text_input)
        st.text_input("回答を入力してください", key="answer_input")
    else:
        st.info("ボタンを押すと、質問がランダムに表示されます。")

    st.divider()

    # 編集セクション
    st.subheader("質問文の編集")
    
    current_questions_text = "\n".join(st.session_state.questions)
    new_questions_text = st.text_area(
        "質問文を1行に1つずつ入力してください",
        value=current_questions_text,
        height=300
    )

    if st.button("保存する"):
        st.session_state.questions = [
            line.strip() for line in new_questions_text.split("\n") if line.strip()
        ]
        st.success("質問リストを保存しました！")
        st.rerun()

if __name__ == "__main__":
    main()
