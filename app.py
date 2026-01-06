import streamlit as st
import random

def main():
    st.title("ワーキングメモリ トレーニング（試作版）")

    # 質問文リスト
    # あとで編集しやすいようにリストで定義
    questions = [
        "今、自分は何をしようとしていた？",
        "次にやる行動は何？",
        "今の感情を一言で言うと？",
        "身体のどこかに力は入っていない？",
        "直前の1分間、何を考えていた？",
        "今の姿勢はどうなっている？"
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
