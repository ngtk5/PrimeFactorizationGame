from game import Game


def print_question():
    """ 問題文や例、注意事項を表示する関数 """

    print("次の数値を素因数分解せよ。\n"
          "なお、回答は1度ずつ行なわれる。\n"
          "以下に例を示す。")
    print("20の場合:\n"
          "[20]\n"
          "ユーザの回答：2\n"
          "[10] (2は20の素因数の１つであるため、計算後の10が表示される)\n"
          "ユーザの入力：2\n"
          "[5] (2は10の素因数の１つであるため、計算後の5が表示される)\n"
          "ユーザの入力：5\n"
          "正解！ (20の素因数が全て回答されたため、終了)")
    print("※素因数でない入力の場合、直前の問題の数値が表示されます。\n"
          "※入力する値は整数にしてください。")


if __name__ == '__main__':
    print_question()
    game: Game = Game()  # Gameクラスのインスタンスを生成
    # ここから無限ループ
    while True:
        # ユーザからの入力を受け付ける
        input_y_n: str = input("ゲームを始めますか?(y/n)：").lower()
        # 「y」の入力があればゲームを開始する
        if input_y_n == "y":
            game.start()
        # 「n」の入力があればループを抜ける
        elif input_y_n == "n":
            print("ゲームを終了します。")
            break
        # それ以外なら「y」または「n」の入力を促す
        else:
            print("[y]または[n]を入力してください。")
    # ここまで無限ループ
