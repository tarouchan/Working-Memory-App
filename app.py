import streamlit as st
import random

def main():
    st.title("ワーキングメモリ トレーニング（試作版）")

    # 質問文リスト
    # あとで編集しやすいようにリストで定義
    questions = [
        "サプリは飲んだ後、残りは何セットだったか？",
        "体重計の電源をOFFにしたか？",
        "水道は「浄水」「シャワー」「原水」のどれから、どれに切り替えたか？",
        "ケトルのキャップの閉め方はどんな状態にしたか？",
        "「はちみつ」「にがり」の残りはどのくらいだったか？",
        "水筒のキャップを確実に閉めたか？",
        "整髪料の残りはどのくらいだったか？"
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
