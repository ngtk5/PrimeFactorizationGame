import random


class RandomNumberGenerator:
    """
    最小値と最大値の範囲内でランダムな整数値を生成するクラス

    Attributes:
        min_value (int): 生成されるランダムな整数値の最小値を表す整数値(初期値は10)
        max_value (int): 生成されるランダムな整数値の最大値を表す整数値(初期値は300)

    """

    min_value: int = 10
    max_value: int = 300

    def generate_num(self) -> int:
        """
        min_valueとmax_valueの範囲内でランダムな整数値を取得する

        Returns:
            int: min_valueとmax_valueの範囲内でランダムに生成された整数値
        """
        return random.randint(self.min_value, self.max_value)


if __name__ == "__main__":
    pass
