import moduleSum
from moduleSub import sub
from moduleDiv import div as divi
import moduleDiv

if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))
    print("Tổng :", moduleSum.sum(a, b))
    print("Hiệu :", sub(a, b))
    print("Tích :", divi.multi(a, b))
    print("Thương :", moduleDiv.div(a, b))