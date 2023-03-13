
def ucln(a,b):
    if b == 0:
        return a
    else:
        return ucln(b,a%b)
def main():
    a=int(input("nhập a:"))
    b=int(input("nhập b:"))
    print(ucln(a,b))
if __name__=="__main__":
    main()
