#bai 1
print("bai 1")
def kiem_tra_chan(n):
    return n % 2 == 0

# Nhập dữ liệu từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Xuất kết quả
if kiem_tra_chan(n):
    print("True")
else:
    print("False")
 #bai 2
print("bai 2")
ds = [1,2,3,4,5,66,77,88]
so_chan = list(filter(lambda x: x%2==0, ds))
tong_so_chan = sum(so_chan)
print(tong_so_chan)
#bai 3
print("bai 3")
for x in range(1,30):
    x=x**2 
    if x%3==0:
        print(x)
ds = [x**2 for x in range(1, 31) if (x**2) % 3 == 0]
print(ds)

#bai 4
def thong_ke_chuoi(lst):
    lst ={}
    if