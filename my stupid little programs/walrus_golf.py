f=lambda(e:=str(s)):abs(eval("".join(['+'if e[i-1]>e[i+1]else'-'][0]if e[i]=='8'else e[i]for i in range(len(e)))))

print(f(789))