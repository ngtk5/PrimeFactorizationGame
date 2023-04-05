from dataclasses import dataclass


@dataclass
class AnswerChecker:
    """
    素因数分解対象の値と素因数リストを保持し、ユーザが入力した値が素因数リスト内に存在するかチェックするクラス

    Attributes:
        _target_num (int): 素因数分解対象の値
        _prime_factors (list): _target_numの素因数が格納されたリスト

    """

    _target_num: int
    _prime_factors: list

    def check(self, answer: int) -> bool:
        """
        ユーザの回答がリスト内にある場合、_target_numをユーザの回答で割り、
        リスト内の該当する値を削除する。ユーザの回答がリスト内になかった場合、Falseを返す。

        Args:
            answer (int): ユーザが入力した値

        Returns:
            bool: ユーザの回答がリスト内に存在する場合はTrue、それ以外はFalseを返す。
        """
        if answer in self._prime_factors:
            self._target_num //= answer
            self._prime_factors.remove(answer)
            return True
        else:
            return False

    @property
    def target_num(self) -> int:
        """
        _target_numの値を返すgetterメソッド。

        Returns:
            int: 素因数分解対象の値
        """
        return self._target_num

    @property
    def prime_factors(self) -> list:
        """
        _prime_factorsの値を返すgetterメソッド。

        Returns:
            list: 素因数リスト
        """
        return self._prime_factors


if __name__ == '__main__':
    pass
