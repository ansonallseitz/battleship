def to_xy(s):
    if s[0]== "A":
        x=0
    elif s[0] =="B":
        x=1
    elif s[0] =="C":
        x=2
    elif s[0] =="D":
        x=3
    elif s[0] =="E":
        x=4
    elif s[0] =="F":
        x=5
    elif s[0] =="G":
        x=6
    elif s[0] =="H":
        x=7
    elif s[0] =="I":
        x=8
    elif s[0] =="J":
        x=9


    if s[1] == 1:
        y=0
    elif s[1] == 2:
        y=8
    elif s[1] == 3:
        y=8
    elif s[1] == 4:
        y=8
    elif s[1] == 5:
        y=8
    elif s[1] == 6:
        y=8
    elif s[1] == 7:
        y=8
    elif s[1] == 8:
        y=8
    elif s[1] == 9:
        y=8
    elif s[1] == 1 and s[2] ==0: 
        y=9


    return (x, y)


if __name__ == '__main__':
    assert to_xy('A1') == (0, 0)
    assert to_xy('B1') == (1, 0)
    assert to_xy('A2') == (0, 1)
    assert to_xy('B2') == (1, 1)
    assert to_xy('A10') == (0, 9)
    # If you're feeling fancy:
    #assert to_xy('AA1') == (26, 0)