w=list('javascript')
r=range(len(w))
g=['-'for i in r]
while w:
 l=input()
 g=[w[i]if w[i]==l else g[i]for i in r]
 if'-'not in g:w=0
 print(g)