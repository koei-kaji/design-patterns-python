class ClassNotFoundException(Exception):
    pass


class Class_:
    @staticmethod
    def get_class(class_name: str) -> object:
        """文字列からクラス（モジュール）をインポートし、クラスを取得する

        Args:
            class_name (str): クラス名

        Raises:
            ClassNotFoundException: 指定したクラスが存在しないときに発生

        Returns:
            object: オブジェクト（クラス）

        Examples:
            >>> from datetime import datetime
            >>> from typing import cast
            >>> D = cast(datetime, Class_.get_class("datetime.datetime"))
            >>> D.now()
                2022-04-04 15:57:18.539479
        """
        _DELIMITER = "."

        parts = class_name.split(_DELIMITER)
        module = _DELIMITER.join(parts[:-1])

        try:
            m = __import__(module)
            for comp in parts[1:]:
                m = getattr(m, comp)
        except (
            ModuleNotFoundError,  # モジュールがないとき
            ValueError,  # モジュールが空のとき
            AttributeError,  # モジュールに含まれていないとき
        ) as error:
            raise ClassNotFoundException from error

        return m
