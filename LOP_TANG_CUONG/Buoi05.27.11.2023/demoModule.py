import moduleSum
import moduleSub
import moduleMulti
import moduleDiv

if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))
    print("Tổng :", moduleSum.sum(a, b))
    print("Hiệu :", moduleSub.sub(a, b))
    print("Tích :", moduleMulti.multi(a, b))
    print("Thương :", moduleDiv.div(a, b))