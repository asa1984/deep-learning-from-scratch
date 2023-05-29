# coding: utf-8
import sys, os

sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
from dataset.mnist import load_mnist
from typing import List


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(
    dict(
        list(
            map(
                lambda label: (
                    label,
                    len(list(filter(lambda element: element == label, t_train[0:999]))),
                ),
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            )
        )
    )
)
