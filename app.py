import streamlit as st
import random

def main():
    st.title("ワーキングメモリトレーニングApp (試作版)")

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
        # 回答入力欄
        st.text_input("回答を入力してください", key="answer_input")
        
        # 記憶の状態を選択
        st.write("記憶の状態:")
        st.checkbox("はっきり覚えている", key="state_clear")
        st.checkbox("曖昧さがある", key="state_vague")
        st.checkbox("まったく思い出せない", key="state_none")
    else:
        st.info("ボタンを押すと、質問がランダムに表示されます。")

    st.divider()

    # 編集セクション
    st.subheader("質問文の編集")
    
    # セッション状態から現在のリストを取得して表示
    current_questions_text = "\n".join(st.session_state.questions)
    
    # フォームを使用して入力内容を管理
    with st.form("edit_form"):
        new_questions_text = st.text_area(
            "質問文を1行に1つずつ入力してください",
            value=current_questions_text,
            height=300
        )
        submit_button = st.form_submit_button("保存する")
        
        if submit_button:
            # 入力されたテキストをリストに変換してセッション状態に保存
            st.session_state.questions = [
                line.strip() for line in new_questions_text.split("\n") if line.strip()
            ]
            st.success("質問リストを保存しました！")
            st.rerun()

if __name__ == "__main__":
    main()
