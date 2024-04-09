import tkinter
from tkinter import messagebox
def constructArray(n, k):
    ans = [j for j in range(1, n-k+1)]
    while k > 0:
        if ans[-1] + k in ans or ans[-1] + k > n:
            ans.append(ans[-1] - k)
        else:
            ans.append(ans[-1] + k)
        k -= 1

    return ans

print(constructArray(5,3))
print(constructArray(10,3))


messagebox.showinfo("", "設定完了!")

