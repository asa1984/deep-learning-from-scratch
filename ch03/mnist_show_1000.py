# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
from typing import List


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

def count_by_label(num:int) -> int:
    target = filter(lambda label: label==num, t_train)
    return list(target).count()

result = list(map(lambda label: {label, count_by_label(label)},[0,1,2,3,4,5,6,7,8,9]))

print(result)