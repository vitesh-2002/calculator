def calc():
    import math
    
    for i in range(1,1000):        
    
        print('\n' +'CALCULATOR'.center(20,'='))
                       
        type=input('1. geometry, 2. arithmetic, 3. advanced -  ')
                   
        _geo_=['1', 'geometry', 'geo']
        _arth_=['2', 'arithmetic', 'arth']
        _adv_=['3', 'advanced', 'adv']
        _end=['end', 'clear', 'off']
        _pi=['pi', 'pie']

        if type in _pi:
            print(math.pi)
            continue

        elif type in _end:
            print('\nending program...\n')
            break
        
        elif type in _arth_:
            print('ADD,SUBTRACT,MULTIPLY,DIVIDE,EXPONENT,ROOT')
            
            try:
                firstval=float(input('enter first value: '))
            except ValueError:
                print('must be a numeric value!!')
                continue
            
            
            operator=input('+, -, *, /, ^, root:  ')
            try:
                secondval=float(input('enter second value: '))
            except ValueError:
                print('must be a numeric value!!')
            if str(operator)=='+':
                solution=firstval+secondval
            elif str(operator)=='-':
                solution=firstval-secondval
            elif str(operator)=='*':
                solution=firstval*secondval
            elif str(operator)=='/':
                try:                    
                    solution=firstval/secondval
                except ZeroDivisionError:
                    print('can not divide a number by 0...\n')
                    continue
            elif str(operator)=='^':
                solution=firstval**secondval
            elif str(operator)=='root':
                rooot=1/secondval
                solution=firstval**rooot
        
        elif type in _geo_:
            print('1. CIRCLE, 2. RECTANGLE, 3. TRIANGLE, 4. SQUARE, 5. TRAPEZOID')
            shape=input('circle, rectangle, triangle, square, trapezoid: ')
            _circ_=['1', 'circle', 'circ']
            _rect_=['2', 'rectangle', 'rect']
            _tri_=['3', 'triangle', 'tri']
            _square=['4', 'square','sq']
            _trapezoid=['5', 'trapezoid', 'trap']
            _geoend=['off', 'clear', 'end']

            if shape in _geoend:
                print('\nending program...\n')
                break

            elif shape in _trapezoid:
                print('to find area of a trapezoid...\n')
                try:
                    base1 = float(input('enter length of base 1: '))
                    base2 = float(input('enter length of base 2: '))
                    trapheight = float(input('enter height: '))
                except ValueError:
                    print('must only enter numeric values!!')
                    continue
                
                traparea = (0.5*(base1+base2))*trapheight
                solution = traparea

            elif shape in _circ_:
                measure=input('1. circumference, 2. area? ')
                _circumference_ = ['1', 'circumference', 'circ']
                _circlearea_ = ['2', 'area']
                if measure in _circumference_:
                    try:
                        l=float(input('radius: '))
                      
                    except ValueError:
                        print('must be a numeric value!!')
                        continue
                    solution=math.pi*l*2
                elif measure in _circlearea_:
                    try:
                        rad=float(input('radius: '))
                    except ValueError:
                        print('must be a numeric value!!')
                        continue
                    r=rad**2
                    solution=math.pi*r
            elif shape in _rect_:
                try:
                    print('To find area of rectangle...\n')
                    leng=float(input('length: '))
                    wid=float(input('width: '))
                except ValueError:
                    print('must be a numeric value!!')
                    continue
                solution=leng*wid
            elif shape in _tri_:
                print('To find area of triangle...\n')
                try:
                    base=float(input('base: '))
                    height=float(input('height: '))
                except ValueError:
                    print('must be a numeric value!!')
                    continue
                trarea=(base*height)
                solution=trarea/2
            elif shape in _square:
                print('To find the area of the square...\n')
                try:
                    sides=float(input('enter side length of square:  '))
                except ValueError:
                    print('must be a numeric value!!')
                    continue
                solution=sides**2
            else:
                print('try again, i didn\'t quite get that\n\n')
                continue
            
        elif type in _adv_:
            
            print('\n TRIGONOMETRY, PYTHAGOREAN \n')
            typadv=input('1. trig \n2. pythagorean \n\n')
            _trig_=['1', 'trigonometry', 'trig']
            _hypo_=['2', 'pythagorean', 'hypotenuse', 'hypot', 'hypo']
            _advend_=['end', 'clear', 'off']

            if typadv in _advend_:
                print('\nending program...\n')
                break
            
            elif typadv in _trig_:
                print('sine, cosine, tangent, cosecant, secant, cotangent \n')
                y=str(input('sin, cos, csc, sec, tan, cot:   '))
                try:
                    x=float(input('enter value of angle: '))
                    
                except ValueError:
                    print('must be a numeric value!! try again')
                    continue

                
                sin=['sin', 'sine']
                cos=['cos', 'cosine']
                tan=['tan', 'tangent']
                cot=['cot', 'cotangent']
                csc=['csc', 'cosecant']
                sec=['sec', 'secant']
                try:
                    
                    if y in sin:
                        solution=math.sin(x)
                    elif y in cos:
                        solution=math.cos(x)
                    elif y in tan:
                        solution=math.tan(x)
                    elif y in csc:
                        s=math.sin(x)
                        solution=1/s
                    elif y in sec:
                        c=math.cos(x)
                        solution=1/c
                    elif y in cot:
                        t=math.tan(x)
                        solution=1/t
                    else:
                        raise ValueError
                except ValueError:
                    print('try again...')
                    continue
            elif typadv in _hypo_:
                print('a^2 + b^2 = c^2')
                print('find hypotenuse or use it to find a side length \n')
                q=input('1. hypotenuse, 2. side length? ')
                hypot=['1','hypotenuse', 'hyp', 'hypo', 'hypot']
                sidelen=['2','side', 'side length', 'sidelength']
                if q in sidelen:
                    try:
                        hyp=float(input('enter value of hypotenuse: '))
                        side=float(input('enter value of known side length: '))
                    except ValueError:
                        print('must be a numeric value!!')
                        continue
                    hypt=hyp**2
                    sidel=side**2
                    missing=hypt-sidel
                    missingval=math.sqrt(missing)
                    solution=missingval
                elif q in hypot:
                    try:
                        first=float(input('enter value of first sidelength: '))
                        second=float(input('enter value of second sidelength: '))
                    except ValueError:
                        print('must be a numeric value!!')
                        continue
                    f=float(first)
                    s=float(second)
                    hypo=(f**2)+(s**2)
                    answer=math.sqrt(hypo)
                    solution=answer
                else:
                    print('sorry didn\'t quite get that...')
                    continue
            else:
                print('sorry didn\'t quite get that...')
                continue
        else:
            print('\n sorry didn\'t quite get that...\n')
            continue
        


        print('\nAnswer: ', solution)
                
                
            
            
    
        
