import functions

def test_add():
    assert functions.add(0,0) == 0
    assert functions.add(1234098765678765674326,1234098765678765674326) == 2468197531357531348652
    assert functions.add(-3, 4) == 1 
    assert functions.add(-10, -10) == -20
    assert functions.add(12, 4) == 16 
    assert functions.add(12.4, 4.2) == 16.6

    


def test_sub():
    assert functions.sub(0,0) == 0
    assert functions.sub(1234098765678765674326,1234098765678765674325) == 1    
    assert functions.sub(-3, 4) == -7 
    assert functions.sub(-10, -10) == -0
    assert functions.sub(12, 4) == 8
    assert functions.sub(12.4, 4.2) == 8.2


def test_mul():
    assert functions.mult(0,0) == 0
    assert functions.mult(1234098,123409876) == 152299881151848
    assert functions.mult(-3, 4) == -12 
    assert functions.mult(-10, -10) == -100
    assert functions.mult(12, 4) == 48 
    assert functions.mult(12.4, 4.2) == 48.8
    

def test_div():
    assert functions.div(0,0) == "Undefined"
    assert functions.div(1234098765678765674326,345432345432) == 3572620751.93
    assert functions.div(-3, 4) == -0.75
    assert functions.div(-10, -10) == 1
    assert functions.div(12.4, 4.3) == 2.88372093023 