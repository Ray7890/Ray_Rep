x = ['asam', 'LISA', 'barT']
def fuc(a):
 return a.capitalize()
y = map(fuc, x)
print y

def fuc2(a):
  b = a[0].upper() + a[1:].lower()
  return b
  
z = map(fuc2, x)
print z

