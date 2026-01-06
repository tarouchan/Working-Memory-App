import streamlit as st
import random

def main():
    st.title("ワーキングメモリ トレーニング（試作版）")

    # 質問文リスト
    # カテゴリ別に定義
    questions = [
        "【トイレ】トイレの換気扇は回っていたか？",
        "【トイレ】トイレロールの残りはどのくらいだったか？",
        "【トイレ】水を流すノブはどちらの手で引いたか？",
        "【トイレ】トイレの電気は消したか？",
        "【歯磨き】歯磨きはどこからスタートして、どこを最後に磨き終えたか？",
        "【歯磨き】歯磨き中の姿勢はどうだったか？",
        "【歯磨き】歯磨き中に浮かんだ思考は？",
        "【歯磨き】歯磨き中に聞こえた環境音は？"
    ]

    # 「出題する」ボタン
    if st.button("出題する", type="primary"):
        # ランダムに1つ選んで表示
        selected_question = random.choice(questions)
        st.markdown(f"### Q. {selected_question}")
    else:
        st.info("ボタンを押すと、質問がランダムに表示されます。")

if __name__ == "__main__":
    main()
