code = '''
use "console";
var int x 5;
var bool cond True;
console.output(1+x*3);
use "math";
while (cond & x) {
    console.output x;
    set x (x - 2);
};
console.warn(math.PI);'''

objs = {"console":["output","warn","error"], "math":["PI","E"]}

tokens = []

alphabet = "abcdefghijklmnopqrstuvwxyz" 
alphabet += alphabet.upper()
alphabet += '1234567890'

current_token = ""

pushing_string = False

for char in code.strip():
    if not pushing_string:
        if char in alphabet:
            current_token += char
        else:
            tokens.append(current_token)
            current_token = ''
            if char == '"':
                pushing_string = True
                tokens.append('"')
            elif char in '{}().+-*/%;&^!=':
                tokens.append(char)
                current_token = ''
                
    else:
        if char == '"':
            pushing_string = False
            tokens.append(current_token)
            tokens.append('"')
            current_token = ''
        else:
            current_token += char
            
final = []
for i in tokens:
    if i != '':
        final.append(i)

print(final)

print("".join(final))

