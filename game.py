from random_number_generator import RandomNumberGenerator
from answer_check import AnswerChecker
from prime_factorization import PrimeFactorization


class AnswerCounter:
    """
    正答数と誤答数をカウントするためのクラス

    Attributes:
        _correct_count (int): 正答数のカウンター(初期値0)
        _incorrect_count (int): 誤答数のカウンター(初期値0)
        _result_incorrect_count (int): 累計誤答数のカウンター(初期値0)

    """
    _correct_count: int = 0
    _incorrect_count: int = 0
    _result_incorrect_count: int = 0

    @property
    def correct_count(self) -> int:
        """
        正答数を返す

        Returns:
            int: 正答数
        """
        return self._correct_count

    @property
    def incorrect_count(self) -> int:
        """
        誤答数を返す

        Returns:
            int: 誤答数
        """
        return self._incorrect_count

    @property
    def result_incorrect_count(self) -> int:
        """
        累計誤答数を返す

        Returns:
            int: 累計誤答数
        """
        return self._result_incorrect_count

    def add_correct_count(self, value: int = 1) -> None:
        """
        正答数を増やす

        Args:
            value (int, optional): 増やす数(初期値1)
        """
        self._correct_count += value

    def add_incorrect_count(self, value: int = 1) -> None:
        """
        誤答数を増やす

        Args:
            value (int, optional): 増やす数(初期値1)
        """
        self._incorrect_count += value
        self._result_incorrect_count += value

    def reset_incorrect_count(self) -> None:
        """
        累計誤答数を0にリセットする
        """
        self._incorrect_count = 0


class Game:
    """
    素因数分解ゲームを実行するためのクラス

    Attributes:
        rng (RandomNumberGenerator): ランダムな整数値を生成するためのオブジェクト
        answer_counter (AnswerCounter): 正答数・誤答数をカウントするためのオブジェクト
        _user_input (int): ユーザから入力された数値を保持するための変数(初期値は0)

    """
    rng: RandomNumberGenerator = RandomNumberGenerator()  # ランダムな整数値を生成するためのオブジェクト
    answer_counter: AnswerCounter = AnswerCounter()  # 正答数・誤答数をカウントするためのオブジェクト
    _user_input: int = 0  # ユーザから入力された数値を保持するための変数

    def start(self) -> None:
        """
        素因数分解ゲームを開始する
        """
        random_num: int = self.rng.generate_num()  # ランダムな整数値を生成する
        prime_factors: list = PrimeFactorization(random_num).factorize()  # 生成された整数値を素因数分解する
        answer_checker: AnswerChecker = AnswerChecker(random_num, prime_factors)  # 正誤判定するためのオブジェクトを生成する
        self.answer_counter.reset_incorrect_count()  # 誤答回数を0にする
        print(f"開始値：[{random_num}]")
        while True:
            self.check_input()  # ユーザから入力された数値を取得する
            # 誤答の場合
            if not answer_checker.check(self._user_input):
                self.answer_counter.add_incorrect_count()  # 誤答数+1
            # 正答の場合
            else:
                # リストが空になった場合
                if not answer_checker.prime_factors:
                    self.answer_counter.add_correct_count()  # 正答数+1
                    print("クリア!\n"
                          f"今回の誤答数：{self.answer_counter.incorrect_count}回\n"
                          f"累計誤答数：{self.answer_counter.result_incorrect_count}回\n"
                          f"累計正答数：{self.answer_counter.correct_count}回")
                    break
                # リストが空ではない場合
                else:
                    print(f"[{answer_checker.target_num}]")

    def check_input(self) -> None:
        """
       ユーザから入力された数値を取得し、_user_inputにint型で格納する

       Raises:
           ValueError
               入力された値が整数に変換できなかった場合。

       """
        while True:
            try:
                self._user_input = int(input("ユーザの入力: "))
                break
            except ValueError:
                print("入力された値は整数ではありません。")


if __name__ == '__main__':
    pass
