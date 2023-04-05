from dataclasses import dataclass


@dataclass
class PrimeFactorization:
    """
    与えられた整数を素因数分解するクラス

    Attributes:
        num (int): 素因数分解する整数

    """

    num: int

    def factorize(self) -> list:
        """
        与えられた整数を素因数分解し、その結果をリストとして返すメソッド

        Returns:
            list: 素因数のリスト
        """
        factors: list = []  # 素因数のリストを格納する変数
        for i in range(2, self.num+1):
            # 2から順に割り切れるかどうかを確認する
            while self.num % i == 0:
                # 割り切れる場合はその数で割り、割り切れなくなるまで繰り返す
                factors.append(i)
                self.num //= i
            if self.num == 1:
                break
        return factors


if __name__ == '__main__':
    pass
