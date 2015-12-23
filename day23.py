a = ['jio a, +19','inc a','tpl a','inc a','tpl a','inc a','tpl a','tpl a','inc a','inc a','tpl a','tpl a','inc a','inc a','tpl a','inc a','inc a','tpl a','jmp +23','tpl a','tpl a','inc a','inc a','tpl a','inc a','inc a','tpl a','inc a','tpl a','inc a','tpl a','inc a','tpl a','inc a','inc a','tpl a','inc a','inc a','tpl a','tpl a','inc a','jio a, +8','inc b','jie a, +4','tpl a','inc a','jmp +2','hlf a','jmp -7']

pos = 0
d = {'a':1, 'b':0}
while pos < len(a):
    cmd = a[pos]
    
    #print (cmd, d)
    
    if cmd[2] == 'f':
        #hlf
        d[cmd[4]] = d[cmd[4]] // 2
        pos += 1
        
    if cmd[2] == 'l':
        d[cmd[4]] = d[cmd[4]] * 3
        pos += 1
        
    if cmd[2] == 'c':
        d[cmd[4]] = d[cmd[4]] + 1
        pos += 1
        
    if cmd[2] == 'p':
        blocks = cmd.split()
        pos += int(blocks[1])
        
    if cmd[2] == 'e':
        blocks = cmd.split(', ')
        step = int(blocks[1])
        if d[cmd[4]] % 2 == 0:
            pos += step
        else:
            pos += 1
            
    if cmd[2] == 'o':
        blocks = cmd.split(', ')
        step = int(blocks[1])
        if d[cmd[4]] == 1:
            pos += step
        else:
            pos += 1

print(d)
