# i:0~9
# j:0~8
def getWays(a, b, step):
    process(0,0,a, b, step)

def process(i,j, a, b, step):
    if i< 0 or i>9 or j<0 or j>8:
        return 0
    if step == 0:
        return 1 if i==a and j == b else 0
    return process(i-2,j+1,a,b,step-1)+ \
        process(i-1,j+2,a,b,step-1)+ \
        process(i+1,j+2,a,b,step-1)+ \
        process(i+2,j+1,a,b,step-1)+ \
        process(i+2,j-1,a,b,step-1)+ \
        process(i+1,j-2,a,b,step-1)+ \
        process(i-1,j-2,a,b,step-1)+ \
        process(i-2,j-1,a,b,step-1),
    