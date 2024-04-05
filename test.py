from sys import exit

print("\n> fox\n> falco\n> sheik\n> marth\n> jiggs\n> peach\n> falcon\n> ics\n> pikachu\n> doc\n> samus\n> ganon\n> luigi\n> mario\n> ylink\n> link\n> dk\n> yoshi\n> zelda\n> roy\n> mewtwo\n> gameandwatch\n> ness\n> bowser\n> pichu\n> kirby\n")

def charselect():
    prompt = input("--Type quit to exit--\nType a character\n> ")
    # d_x, d_y, d_initialv, d_maxv, d_acceleration, traction_low, traction_high
    # maxwalk, jumpsquat, rollf, rollb, rollframes, d_trueinitialv, damulti, turnrun

    if prompt == "fox":
    
        stats = [11, 21, 2.02, 2.2, 0.12, 0.08, 0.16, 1.6, 3, 33.6, 33.6, 33, 1.9]

    elif prompt == "falco":
    
        stats = [11, 21, 1.82, 1.5, 0.12, 0.08, 0.16, 1.4, 5, 38.5, 38.5, 33, 1.9]
    
    elif prompt == "sheik":
    
        stats = [7, 21, 1.8, 1.8, 0.12, 0.08, 0.16, 1.2, 3, 40.04565, 37.71997, 33, 1.7]
        dattack = [4.58236, 4.79176, 3.38642]
    
    elif prompt == "marth":
    
        stats = [15, 27, 1.56, 1.8, 0.06, 0.06, 0.12, 1.6, 4, 40.23051, 40.19798, 37, 1.5]

    elif prompt == "jiggs":
    
        stats = [12, 23, 1.31, 1.1, 0.085, 0.09, 0.18, 0.7, 5, 32.90277, 32.89497, 36, 1.4]

    elif prompt == "peach" :
    
        stats = [15, 21, 1.3, 1.3, 0.12, 0.1, 0.2, 0.85, 5, 30.31844, 29.52969, 33, 1.2]
    
    elif prompt == "falcon":

        stats = [15, 28, 2.16, 2.30, 0.16, 0.08, 0.16, 0.85, 4, 33.95093, 33.86285, 33, 2, 0.001875, 23]
    
    elif prompt == "ics":
    
        stats = [13, 21, 1.4, 1.4, 0.07, 0.035, 0.07, 0.95, 3, 34.49494, 34.5, 33, 1.4]
    
    elif prompt == "pikachu":
    
        stats = [13, 22, 1.8, 1.8, 0.1, 0.09, 0.18, 1.24, 3, 36.67236, 33.3, 33, 1.8]
    
    elif prompt == "doc" or prompt == "mario":
    
        stats = [10, 21, 1.5, 1.5, 0.08, 0.06, 0.12, 1.1, 4, 33.00137, 33, 33, 1.5, 0.00075, 23]

    elif prompt == "samus":
    
        stats = [8, 22, 1.8, 1.4, 0.12, 0.06, 0.12, 1.0, 3, 39.60114, 39.59885, 46, 1.86]
    
    elif prompt == "ganon":
    
        stats = [15, 28, 1.35, 1.35, 0.09, 0.07, 0.14, 0.73, 6, 37.80104, 37.70296, 33, 1.3]

    elif prompt == "luigi":

        stats = [10, 21, 1.34, 1.34, 0.08, 0.025, 0.05, 1.1, 4, 37.50156, 37.5, 33, 1.3]

    elif prompt == "ylink" :
    
        stats = [12, 30, 1.72, 1.6, 0.12, 0.08, 0.16, 1.2, 4, 28.84717, 28.8, 39, 1.8]

    elif prompt == "link" :
    
        stats = [12, 30, 1.3, 1.3, 0.12, 0.1, 0.2, 1.2, 6, 36.65994, 36.6, 39, 1.3]

    elif prompt == "dk" :
    
        stats = [15, 30, 1.6, 1.6, 0.07, 0.08, 0.16, 1.2, 5, 38.4725, 34.99518, 33, 1.6]

    elif prompt == "yoshi" :
    
        stats = [13, 26, 1.43, 1.6, 0.1, 0.06, 0.12, 1.15, 5, 31.31754, 31.31937, 39, 1.33]

    elif prompt == "zelda" :
    
        stats = [15, 22, 1.1, 1.1, 0.12, 0.1, 0.2, 0.7, 6, 33.21847, 32.34975, 33, 1.1]

    elif prompt == "roy" :

        stats = [15, 27, 1.47, 1.61, 0.07, 0.06, 0.12, 1.2, 5, 37.7817, 37.75116, 37, 1.4]

    elif prompt == "mewtwo" :

        stats = [18, 29, 1.4, 1.4, 0.1, 0.04, 0.08, 1, 5, 51.96725, 51.98896, 39, 1.4]

    elif prompt == "gameandwatch" :

        stats = [8, 17, 1.5, 1.5, 0.08, 0.06, 0.12, 1.1, 4, 28.56, 28.56, 37, 1.5]

    elif prompt == "ness" :

        stats = [13, 25, 1.36, 1.4, 0.06, 0.06, 0.12, 0.84, 4, 30.00653, 35.02735, 33, 1.3]

    elif prompt == "bowser" :

        stats = [13, 29, 1.06, 1.5, 0.06, 0.06, 0.12, 0.65, 8, 28.98, 26.27791, 41, 1]

    elif prompt == "pichu" :

        stats = [13, 22, 1.72, 1.72, 0.1, 0.1, 0.2, 1.24, 3, 40, 38, 33, 1.8]

    elif prompt == "kirby" :
    
        stats = [12, 23, 1.4, 1.4, 0.1, 0.08, 0.16, 0.85, 3, 32.20272, 32.19508, 33, 1.4]

    elif prompt == "quit" :
        exit(0)

    else :
        print("Invalid character name.")
        charselect()

    return stats, prompt

def printwalkandmaxrun(d_maxv, maxwalk):
    print("\nMax Walk Speed: " , maxwalk)
    print("\nAverage Run velocity: " ,d_maxv)
def wavedashing(traction_low, traction_high, maxwalk, jumpsquat, prompt, filename):
    data = open(filename, 'a')
    data.write("WAVEDASH\n")
    #------WAVEDASH--------
    airdodgev1 = 2.79000
    airdodgev2 = 2.67039
    airdodgev3 = 1.97283

    #z = (w - tv) / th , rounded up, max 9+j
    #i = w - zth
  
    zw1_1 = round((airdodgev1 - maxwalk) / traction_high + 0.5)
    if zw1_1 > 9 :
        zw1_1 = 9
    zw1_2 = airdodgev1 - (zw1_1*traction_high)

    zw2_1 = round((airdodgev2 - maxwalk)/traction_high + 0.5)
    if zw2_1 > 9 + jumpsquat :
        zw2_1 = 9 + jumpsquat
    zw2_2 = airdodgev2 - (zw2_1*traction_high)

    zw3_1 = round((airdodgev3 - maxwalk)/traction_high + 0.5)
    if zw3_1 > 9 + jumpsquat :
        zw3_1 = 9 + jumpsquat
    zw3_2 = airdodgev3 - (zw3_1*traction_high)

    if prompt == "sheik" or prompt == "marth" or prompt == "link" or prompt == "dk" or prompt == "roy" or prompt == "bowser" :
        a = True
    else:
        a = False

    data.write("Perfect waveland\n")

    if zw1_1 >= 9:
        n = 0
        wavedash1 = 0
    
        while n <= zw1_1 :
            wavedash1 = wavedash1 + airdodgev1 - traction_high * n
            data.write(str(wavedash1) + "\n")
            n = n + 1
        
        
        wavedash1 = wavedash1 / 10
        print("\nAverage Perfect Waveland velocity:",wavedash1)
    
    else:
        n = 0
        wavedash1_1 = 0
    
        while n <= zw1_1 :
            wavedash1_1 = wavedash1_1 + airdodgev1 - traction_high * n
            data.write(str(wavedash1_1) + "\n")
            n = n + 1

        m = 1
        wavedash1_2 = 0
    
        while m <= (9 - zw1_1) :  
            wavedash1_2 = wavedash1_2 + zw1_2 - traction_low * m
            data.write(str(wavedash1_1 + wavedash1_2) + "\n")
            m = m + 1
    
        wavedash1 = (wavedash1_1 + wavedash1_2)/ 10
        print("\nAverage Perfect Waveland velocity:" ,wavedash1)

    data.write("Max angle\n")

    if zw2_1 >= 9 + jumpsquat:
        n = 0
        if a == True:
            wavedash2 = -0.5*airdodgev2
        else:
            wavedash2 = 0
    
        while n <= zw2_1 :
            wavedash2 = wavedash2 + airdodgev2 - traction_high * n
            data.write(str(wavedash2) + "\n")
            n = n + 1
    else:

        n = 0
        if a == True:
            wavedash2_1 = -0.5*airdodgev2
        else:
            wavedash2_1 = 0
    
        while n <= zw2_1 :
            wavedash2_1 = wavedash2_1 + airdodgev2 - traction_high * n
            data.write(str(wavedash2_1) + "\n")
            n = n + 1

        m = 1
        wavedash2_2 = 0
    
        while m <= (9 + jumpsquat - zw2_1) :  
            wavedash2_2 = wavedash2_2 + zw2_2 - traction_low * m
            data.write(str(wavedash2_1 + wavedash2_2) + "\n")
            m = m + 1
    
        wavedash2 = (wavedash2_1 + wavedash2_2)

    data.write("Diagonal notch\n")

    if zw3_1 >= 9 + jumpsquat:

        n = 0
        if a == True:
            wavedash3 = -0.5*airdodgev3
        else:
            wavedash3 = 0
    
        while n <= zw3_1 :
            wavedash3 = wavedash3 + airdodgev3 - traction_high * n
            data.write(str(wavedash3) + "\n")
            n = n + 1



    else:

        n = 0
        if a == True:
            wavedash3_1 = -0.5*airdodgev3
        else:
            wavedash3_1 = 0
    
        while n <= zw3_1 :
            wavedash3_1 = wavedash3_1 + airdodgev3 - traction_high * n
            data.write(str(wavedash3_1) + "\n")
            n = n + 1

        m = 1
        wavedash3_2 = 0
    
        while m <= (9 + jumpsquat - zw3_1) :  
            wavedash3_2 = wavedash3_2 + zw3_2 - traction_low * m
            data.write(str(wavedash3_1 + wavedash3_2) + "\n")
            m = m + 1
    
        wavedash3 = (wavedash3_1 + wavedash3_2)
    


    wavedash2 = wavedash2 / (10 + jumpsquat)
    wavedash3 = wavedash3 / (10 + jumpsquat)
    print("\nAverage Max angle Wavedash velocity:" ,wavedash2)
    print("\nAverage Diagonal notch Wavedash velocity:" ,wavedash3)
    #when z = 9+j ;
    #Wavedash/land = Sum[w - thn, {n, 0, z}] / (10+j)
    #
    #when z < 9+j ;
    #Wavedash/land = ( Sum[w - thn, {n, 0, z}] + Sum[i - tn, {n, 1,(9+j-z)}] ) / (10+j)

    return wavedash1, wavedash2, wavedash3

def dashing(d_x, d_initialv, d_maxv, d_acceleration, traction_low, filename):
    # 
    data = open(filename, 'a')
    data.write("DASH\n0\n")

    #------------DASHING----------------


    if d_initialv == d_maxv:
        dash = d_maxv
        i = 1
        while i < d_x:
            data.write(str(n) + " == " + str(dash * i) + "\n")
            i += 1
        
        print("\nAverage Dash velocity: " ,dash)
    
    
    elif d_initialv > d_maxv:
        zd = round((d_initialv - d_maxv)/traction_low - 0.5) #rounded down
        if zd > (d_x - 2):
            zd = (d_x - 2)
    
        dash = 0
        n = 0
    
        while n <= zd:
            dash = dash + (d_initialv - traction_low*n)
            data.write(str(n) + " > " + str(dash) + "\n")
            n = n + 1
    
        #Dash = ( Sum[du - tn, {n, 0, z}] + dv(dx - z - 2) ) / (dx - 1)
        dash = (dash + d_maxv*(d_x - zd - 2))/(d_x - 1)
        print("\nAverage Dash velocity: " ,dash)
    
    else:
        zd = round((d_maxv - d_initialv)/d_acceleration - 0.5) #rounded down Marth:(1.8-1.79)/0.06 - 0.05 = 4 - 0.05 = 3.95 = 4
        if zd > (d_x - 2): #Marth 4 > 15-2
            zd = (d_x - 2)
    
        dash = 0
        n = 0
    
        data.write(str(zd) + " zd""\n")
        while n <= zd: # 0 <= 4
            dash = dash + (d_initialv + d_acceleration*n) # 0 + (1.56 + 0.06*0) = 1.56, 1.56 + (1.56 + 0.06*1) = 1.56
            data.write(str(n) + " <= " + str(dash) + "\n")
            n = n + 1
        
        #Dash = ( Sum[du + dan, {n, 0, z}] + dv(dx - z - 2) ) / (dx - 1)
        dash = (dash + d_maxv * (d_x - zd - 2))/(d_x - 1)
        # marth = (8.4 + 1.8 * (15 - 5 - 2))/(15 - 1)
        # 0, 1.56, 1.62, 1.68, 1.74, 1.8, 1.8, 1.8, 1.8, 1.8
        print("\nAverage Dash velocity: " ,dash)

    return dash

def foxtrotting(d_x, d_y, d_initialv, d_maxv, d_acceleration, traction_low)    :
    #--------------FOXTROT--------------------
    data = open(filename, 'a')
    data.write("FOXTROT\n0\n")

    if d_initialv == d_maxv:
        i = 1
        while i < d_x:
            data.write(str(d_maxv * i) + "\n")
            i += 1
        n = 1
        foxtrot = 0
    
        while n <= (d_y - d_x) :
            foxtrot = foxtrot + d_maxv - traction_low * n
            data.write(str(foxtrot) + "\n")
            n = n + 1
    
        foxtrot = ( foxtrot + d_x * d_maxv - traction_low * (d_y - d_x) ) / d_y

        #Foxtrot = ( Sum[dv - tn, {n, 1, (dy-dx)}] + dxdv - t(dy - dx) ) / dy
        print("\nAverage Foxtrot velocity: " ,foxtrot)
    
    elif d_initialv > d_maxv:
        zf = round((d_initialv - d_maxv) / traction_low - 0.5) #rounded down
        #print "zf is ", zf
    
        if zf < ( d_x - 2 ) :
    
            n = 0
            foxtrot1 = 0
        
            while n <= zf :
                foxtrot1 = foxtrot1 + d_initialv - traction_low * n
                data.write(str(foxtrot1) + "\n")
                n = n + 1
        
            m = 1
            foxtrot2 = 0
        
            while m <= (d_y - d_x) :
                foxtrot2 = foxtrot2 + d_maxv - traction_low * m
                data.write(str(foxtrot1 + foxtrot2) + "\n")
                m = m + 1
        
            foxtrot = (foxtrot1 + foxtrot2 + d_maxv*(d_x - zf - 2) + d_maxv - traction_low*(d_y - d_x)) / d_y
    
        else :
        
            n = 0
            foxtrot = 0
        
            while n <= (d_y - 2):
                foxtrot = foxtrot + d_initialv - traction_low * n
                data.write(str(foxtrot) + "\n")
                n = n + 1
            foxtrot = ( foxtrot + d_initialv - traction_low * ( d_y - 2 ) ) / d_y
    
        print("\nAverage Foxtrot velocity: " ,foxtrot)
        #z = (du - dv) / t, rounded down
        #Foxtrot = ( Sum[du - tn, {n, 0, z}] + dv(dx - z - 2) + Sum[dv - tn, {n, 1, (dy-dx)}] + dv - t(dy - dx) ) / dy
    
    else:
        zf = round((d_maxv - d_initialv) / d_acceleration - 0.5) #rounded down
    
        n = 0
        foxtrot1 = 0
    
        while n <= zf :
            foxtrot1 = foxtrot1 + d_initialv + d_acceleration * n
            data.write(str(foxtrot1) + "\n")
            n = n + 1
    
        m = 1
        foxtrot2 = 0
    
        while m <= (d_y - d_x) :
            foxtrot2 = foxtrot2 + d_maxv - traction_low * m
            data.write(str(foxtrot1 + foxtrot2) + "\n")
            m = m + 1
    
        foxtrot = ( (foxtrot1 + foxtrot2 + d_maxv *(d_x - zf - 2) + d_maxv - traction_low * (d_y - d_x)) / d_y    )
    
        print("\nAverage Foxtrot velocity: " ,foxtrot)

    #Foxtrot = ( Sum[du + dan, {n, 0, z}] + dv(dx - z - 2) + Sum[dv - tn, {n, 1, (dy-dx)}] + dv - t(dy - dx) ) / dy
    return foxtrot

def rolling(rollf, rollb, rollframes):    
    # ------------ROLLING-------------

    rollforward = rollf / rollframes
    rollbackward = rollb / rollframes

    print("\nAverage Roll forward velocity: ", rollforward)
    print("\nAverage Roll backward velocity: ", rollbackward)
    print("\n")

    return rollforward, rollbackward
def velocityorder(d_maxv, maxwalk, wavedash1, wavedash2, wavedash3, dash, foxtrot, rollforward, rollbackward, wavesurf):
    #---------------Ordered list----------------

    velocityList = [maxwalk, rollforward, rollbackward, foxtrot, wavedash1, wavedash2, wavedash3, dash, d_maxv, wavesurf]
    velocityList.sort()
    for a in velocityList:
        if a == maxwalk :
            print("> Maxwalk....................... ", a)
        if rollforward == rollbackward :
            if a == rollforward :
                print("> Roll forward = Roll backward.. ", a)
        else :
            if a == rollbackward :
                print("> Roll backward................. ", a)
            if a == rollforward :
                print("> Roll forward.................. ", a)
        if a == foxtrot :
            print("> Foxtrot....................... ", a)
        if a == wavesurf :
            print("> Wavesurf...................... ", a)
        if a == wavedash1 :
            print("> Perfect waveland.............. ", a)
        if a == wavedash2 :
            print("> Max angle wavedash............ ", a)
        if a == wavedash3 :
            print("> Diagonal notch wavedash....... ", a)
        if dash == d_maxv :
            if a == dash :
                print("> Dash = Run.,,,................ ", a)
        else :
            if a == d_maxv :
                print("> Run........................... ", a)
            if a == dash :
                print("> Dash.......................... ", a)

def dashdancing(d_x, d_initialv, d_maxv, d_acceleration, traction_low, d_trueinitialv):
    #------------DASHDANCING-----------------------
            
    if d_initialv == d_maxv :
        vz = d_maxv
        #print "1: vz is " ,vz
    elif d_initialv > d_maxv :
        vz = d_initialv - traction_low * (d_x - 2)
        vz = d_maxv
        #if vz > d_maxv :
        #    vz = d_maxv
        #    print "2-2: vz is " ,vz
        # i think even when vz is above d_max, vx will just use d_maxv and cannot go higher.
        #print "2:vz is " ,vz
    
    else :
        vz = d_initialv + d_acceleration * (d_x - 2)
        if vz > d_maxv :
            vz = d_maxv
        #print "3: vz is " ,vz

    vx = - 1 *(( vz / 4 ) - traction_low)
    if vx > 0:
        vx = 0
    #print "vx is " , vx

    if (vx + d_trueinitialv) > d_maxv :
        z = round(((vx + d_trueinitialv - d_maxv) / traction_low) - 0.5)
        if z > d_x - 1:
            z = d_x - 1
        #print "1: z is " , z
        vy = vx + d_trueinitialv - traction_low * (d_x - 1)
        vy = d_maxv
        #if vy < d_maxv:
        #    print "1-1: vy is ", vy
        #    vy = d_maxv
        #print "1: vy is " , vy
        dashdance = 0
        n = 1
    
        while n <= z :
            dashdance = dashdance + vx + d_trueinitialv - traction_low * n
            n = n + 1
    
        dashdance = dashdance + d_maxv * (d_x - z - 1) + 2 * ((vy / 4) - traction_low)
    
        print("\nDash dance distance: " ,dashdance)

    elif (vx + d_trueinitialv) < d_maxv :
        #print "\ntest 1"
        z = round(((d_maxv - vx - d_trueinitialv) / d_acceleration) - 0.5)
        if z > d_x - 1:
            z = d_x - 1
        #print "2: z is " , z
        vy = vx + d_trueinitialv + d_acceleration * (d_x - 1)
        if vy > d_maxv:
            vy = d_maxv
        #print "2: vy is " , vy
        dashdance = 0
        n = 1
    
        while n <= z :
            dashdance = dashdance + vx + d_trueinitialv + d_acceleration * n
            n = n + 1
    
        dashdance = dashdance + d_maxv * (d_x - z - 1) + 2 * ((vy / 4) - traction_low)
    
        print("\nDash dance distance: " ,dashdance)

    elif (vx + d_trueinitialv) == d_maxv :

        dashdance = d_maxv * (d_x - 1) + 2 * ((d_maxv / 4) - traction_low)
    
        print("\nDash dance distance: " ,dashdance)

    dashdancevelocity = dashdance / (d_x + 1)

    print("\nAverage Dash dance velocity: " , dashdancevelocity)

def extendeddashdancing(d_x, d_initialv, d_maxv, d_acceleration, traction_low, d_trueinitialv):
    #--------EXTENEDED DASHDANCE--------------

    if d_initialv == d_maxv :
        vframedx = d_maxv
        #print "1: vframedx is " ,vframedx
    elif d_initialv > d_maxv :
        vframedx = d_initialv - traction_low * (d_x - 2)
        if vframedx < d_maxv:
            vframedx = d_maxv
        #print "2: vframedx is" ,vframedx
    
    else :
        vframedx = d_initialv + d_acceleration * (d_x - 2)
        if vframedx > d_maxv :
            vframedx = d_maxv
        #print "3: vframedx is " ,vframedx

    vframe20 = vframedx - traction_low * (20 - d_x)
    #print "vframe20 is " , vframe20

    vframe21 = - 1 *(( vframe20 / 4 ) - traction_low)
    if vframe21 > 0:
        vframe21 = 0
    #print "vframe21 is " , vframe21

    if (vframe21 + d_trueinitialv) > d_maxv :
        #print "\nTesting>>>>>>>>>>>>>>"
        # z is how many frames of traction it takes to get from frame23 to dmaxv
        z = round(((vframe21 + d_trueinitialv - d_maxv) / traction_low) - 0.5)
        if z > d_x - 1:
            z = d_x - 1
        #print "1: z is " , z

        exdashdance = 0
        n = 1
    
        while n <= z :
            exdashdance = exdashdance + vframe21 + d_trueinitialv - traction_low * n
            n = n + 1
        if ( vframe21 + d_trueinitialv - traction_low*(z+1) ) > d_maxv :
            m = 1
    
            while m <= (20 - z) :
                exdashdance = exdashdance + vframe21 + d_trueinitialv - traction_low * (z + m)
                m = m + 1
        
            vframe41 = exdashdance + vframe21 + d_trueinitialv - traction_low * (z - m)
            #print "1-1:vframe41 is THIS NEEDS ATTENTION", vframe41
            exdashdance = exdashdance + 2 * ((vframe41/4) - traction_low)
        
        else :
            m = 1
            while m <= (20 - d_x) :
                exdashdance = exdashdance + d_maxv - traction_low * m
                m = m + 1
            #print "1: m is ",m
            vframe41 = d_maxv - traction_low * (m - 1)
            #print "1-2:vy is ", vframe41
            exdashdance = exdashdance + 2 * ((vframe41/4) - traction_low)
    
        exdashdance = exdashdance + d_maxv * ( d_x - z - 1)
        print("\n20 frame Extended Dash dance distance: " ,exdashdance)

    elif (vframe21 + d_trueinitialv) < d_maxv :
        #print "\ntest 1"
        # z is how many frames of acceleration it takes to get from frame23 to dmaxv
        z = round(((d_maxv - vframe21 - d_trueinitialv) / d_acceleration) - 0.5)
        if z > d_x - 1:
            z = d_x - 1
        #print "z is " , z

        exdashdance = 0
        n = 1
    
        while n <= z :
            exdashdance = exdashdance + vframe21 + d_trueinitialv + d_acceleration * n
            n = n + 1
            #print "exdashdance1 : " , exdashdance
        if ( vframe21 + d_trueinitialv + d_acceleration*(z+1) ) > d_maxv :
            m = 1
    
            if z == d_x - 1 :
                vframe21plusdx = vframe21 + d_trueinitialv + d_acceleration * z
                while m <= (20 - d_x) :
                    exdashdance = exdashdance + vframe21plusdx - traction_low * m
                    m = m + 1
                vy = vframe21 + d_trueinitialv + d_acceleration * z - traction_low * (20 - d_x)
                exdashdance = exdashdance + 2 * ((vy/4) - traction_low)
                #print "1:vy is ", vy
            
            else :
                exdashdance = exdashdance  + d_maxv * (d_x - z - 1)
                while m <= (20 - d_x) :
                    exdashdance = exdashdance + d_maxv - traction_low * m
                    m = m + 1
                vy = d_maxv - traction_low * (20 - d_x)
                frame42 = ((vy/4) - traction_low)
                #print "frame 42 is ", frame42
                exdashdance = exdashdance + 2 * ((vy/4) - traction_low)
                #print "2:vy is ", vy
    
        else :
            m = 1
            while m <= (20 - d_x) :
                exdashdance = exdashdance + vframe21 + d_trueinitialv  + d_acceleration * z - traction_low * m
                m = m + 1
        
            vy = vframe21 + d_trueinitialv + d_acceleration * z - traction_low * m
            #print "3:vy is ", vy
            exdashdance = exdashdance + 2 * ((vy/4) - traction_low)
        
            
        #exdashdance = exdashdance + d_maxv * (d_x - z - 1) + 2 * ((vy / 4) - traction_low)
    
        print("\n20 frame Extended Dash dance distance: " ,exdashdance)
    

    elif (vframe21 + d_trueinitialv) == d_maxv :
    
        exdashdance = 0
        m = 1
        while m <= (20 - d_x):
            exdashdance = exdashdance + traction_low * m
            m = m + 1
        vy = d_maxv - (20 - d_x) * traction_low
    
        exdashdance = exdashdance + d_maxv * (d_x - 1) + 2 * ((vy / 4) - traction_low)
    
        print("\20 frame Extended Dash dance distance: " ,exdashdance)

    exdashdancevelocity = exdashdance / 21

    print("\nAverage Extended Dash dance velocity: " , exdashdancevelocity)

def wavesurfing(d_initialv, d_maxv, d_acceleration, traction_low, traction_high, maxwalk, jumpsquat, prompt, wdtype, query):
    #------------------WAVESURFING--------------------------
    if wdtype == "pw":
        airdodgev2 = 2.79000
    elif wdtype == "ma":
        airdodgev2 = 2.67039
    elif wdtype == "dn":
        airdodgev2 = 1.97283
    i = round((airdodgev2 - maxwalk)/traction_high + 0.5)
    if i > 9 :
        i = 9
    j = airdodgev2 - (i*traction_high)

    if i >= 9:
        n = 0
        wavedash2noj = 0
    
        while n <= i :
            wavedash2noj = wavedash2noj + airdodgev2 - traction_high * n
            n = n + 1
        wavedashframe10 = airdodgev2 - traction_high * (n - 1)
        if query == True:
            return wavedashframe10
        #print "wavedash frame 10 is " ,wavedashframe10
        if prompt == "sheik" or prompt == "marth" or prompt == "link" or prompt == "dk" or prompt == "roy" or prompt == "bowser" :
            wavedash2noj = wavedash2noj - 0.5*airdodgev2
        #print "\nAverage Max angle Wavedash velocity: no jumpsquat" ,wavedash2noj

    else:

        n = 0
        wavedash2_1 = 0
    
        while n <= i :
            wavedash2_1 = wavedash2_1 + airdodgev2 - traction_high * n
            n = n + 1

        m = 1
        wavedash2_2 = 0
    
        while m <= (9 - i) :  
            wavedash2_2 = wavedash2_2 + j - traction_low * m
            m = m + 1
    
        wavedashframe10 = j - traction_low * (m - 1)
        if query == True:
            return wavedashframe10
        
        #print "wavedashframe10 is " ,wavedashframe10
        wavedash2noj = (wavedash2_1 + wavedash2_2)
        if prompt == "sheik" or prompt == "marth" or prompt == "link" or prompt == "dk" or prompt == "roy" or prompt == "bowser" :
            wavedash2noj = wavedash2noj - 0.5*airdodgev2
        #print "\nAverage Max angle Wavedash no jumpsquat:" ,wavedash2noj

    cactuarframes = 5
    print("Wavesurf dash frames: " , cactuarframes)
    
    if d_initialv == d_maxv :
        n = 1
        cactuarjumpsquat = 0
        cactuarjumpsquatv = d_maxv
        while n <= jumpsquat:
            if cactuarjumpsquatv <= maxwalk :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_low
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "1: jumpsquat velocity ", cactuarjumpsquatv
                #print "1: jumpsquat distancw " ,cactuarjumpsquat
            else :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_high
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "2: jumpsquat velocity ", cactuarjumpsquatv
                #print "2: jumpsquat distancw " ,cactuarjumpsquat
        #print "jumpsquat distance is " ,cactuarjumpsquat
        cactuardashvelocity = ( wavedash2noj + wavedashframe10 + (cactuarframes - 1) * d_maxv + cactuarjumpsquat)  / (10 + cactuarframes + jumpsquat)
        
        print("Cactuardash velocity: " ,cactuardashvelocity)
        
    elif d_initialv > d_maxv :
    
        zd = round((d_initialv - d_maxv)/traction_low - 0.5) #rounded down
        #print " zd is " ,zd
        if zd > (cactuarframes - 2):
            zd = (cactuarframes - 2)
        #print " zd is ", zd
        dash = 0
        n = 0
    
        while n <= zd:
            dash = dash + (d_initialv - traction_low*n)
            n = n + 1
        if zd == cactuarframes - 2 :
            dashv = d_initialv - traction_low*zd
        else :
            dashv = d_maxv
        #print "dashv is ",dashv
        #print "dash is ",dash
        dash = (dash + d_maxv*(cactuarframes - 2 - zd))
        #print "dash is " ,dash
        n = 1
        cactuarjumpsquat = 0
        cactuarjumpsquatv = d_maxv
        while n <= jumpsquat:
            if cactuarjumpsquatv <= maxwalk :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_low
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "1: jumpsquat velocity ", cactuarjumpsquatv
                #print "1: jumpsquat distancw " ,cactuarjumpsquat
            else :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_high
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "2: jumpsquat velocity ", cactuarjumpsquatv
                #print "2: jumpsquat distancw " ,cactuarjumpsquat
        #print "jumpsquat distance is " ,cactuarjumpsquat    
        cactuardash = ( wavedash2noj + wavedashframe10 + dash + cactuarjumpsquat)
        cactuardashvelocity =  cactuardash / (10 + cactuarframes + jumpsquat)
        
        #print "Cactuardash distance: " ,cactuardash
        print("cactuardash velocity: " ,cactuardashvelocity)

    elif d_maxv > d_initialv :
    
        zd = round((d_maxv - d_initialv)/d_acceleration - 0.5) #rounded down
        if zd > (cactuarframes - 2):
            zd = (cactuarframes - 2)
    
        dash = 0
        n = 0
    
        while n <= zd:
            dash = dash + (d_initialv + d_acceleration*n)
            n = n + 1
    
        if zd == cactuarframes - 2 :
            dashv = d_initialv + d_acceleration*zd
        else :
            dashv = d_maxv
    
        dash = (dash + d_maxv*(cactuarframes - 2 - zd))
        #print "dash is " , dash
        n = 1
        cactuarjumpsquat = 0
        cactuarjumpsquatv = dashv
        while n <= jumpsquat:
            if cactuarjumpsquatv <= maxwalk :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_low
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "1: jumpsquat velocity ", cactuarjumpsquatv
                #print "1: jumpsquat distancw " ,cactuarjumpsquat
            else :
                n = n + 1
                cactuarjumpsquatv = cactuarjumpsquatv - traction_high
                cactuarjumpsquat = cactuarjumpsquat + cactuarjumpsquatv
                #print "2: jumpsquat velocity ", cactuarjumpsquatv
                #print "2: jumpsquat distancw " ,cactuarjumpsquat
        #print "jumpsquat distance is " ,cactuarjumpsquat
        cactuardash = ( wavedash2noj + wavedashframe10 + dash + cactuarjumpsquat)
        cactuardashvelocity =  cactuardash / (10 + cactuarframes + jumpsquat)
        
        #print "Cactuardash distance: " ,cactuardash
        print("cactuardash velocity: " ,cactuardashvelocity)
    return cactuardashvelocity

#--------------------------------------------

def wavedashdistance(traction_low, traction_high, maxwalk, prompt):
    #------WAVEDASH Distance--------
    airdodgev1 = 2.79000
    airdodgev2 = 2.67039
    airdodgev3 = 1.97283

    #z = (w - tv) / th , rounded up, max 9+j
    #i = w - zth
  
    zw1_1 = round((airdodgev1 - maxwalk) / traction_high + 0.5)

    zw1_2 = airdodgev1 - (zw1_1*traction_high)

    zw2_1 = round((airdodgev2 - maxwalk)/traction_high + 0.5)

    zw2_2 = airdodgev2 - (zw2_1*traction_high)

    zw3_1 = round((airdodgev3 - maxwalk)/traction_high + 0.5)

    zw3_2 = airdodgev3 - (zw3_1*traction_high)


    n = 0
    wavedash1_1 = 0
    
    while n <= zw1_1 :
        wavedash1_1 = wavedash1_1 + airdodgev1 - traction_high * n
        n = n + 1

    m = 1
    wavedash1_2 = 0
    
    while (zw1_2 - traction_low * m) > 0 :  
        wavedash1_2 = wavedash1_2 + zw1_2 - traction_low * m
        m = m + 1
    
    wavedash1 = (wavedash1_1 + wavedash1_2)
    print("\nPerfect Waveland distance:" ,wavedash1)


    n = 0
    wavedash2_1 = 0

    while n <= zw2_1 :
        wavedash2_1 = wavedash2_1 + airdodgev2 - traction_high * n
        n = n + 1

    m = 1
    wavedash2_2 = 0
    
    while (zw2_2 - traction_low * m) > 0 :  
        wavedash2_2 = wavedash2_2 + zw2_2 - traction_low * m
        m = m + 1
    
    wavedash2 = (wavedash2_1 + wavedash2_2)
    print("\nMax Angle wavedash distance: ",wavedash2)

    n = 0
    wavedash3_1 = 0

    while n <= zw3_1 :
        wavedash3_1 = wavedash3_1 + airdodgev3 - traction_high * n
        n = n + 1

    m = 1
    wavedash3_2 = 0
    
    while (zw3_2 - traction_low * m) > 0 :  
        wavedash3_2 = wavedash3_2 + zw3_2 - traction_low * m
        m = m + 1
    
    wavedash3 = (wavedash3_1 + wavedash3_2)
    print("\nDiagonal notch wavedash distance: " ,wavedash3)
    

    
    if prompt == "sheik" or prompt == "marth" or prompt == "link" or prompt == "dk" or prompt == "roy" or prompt == "bowser" :

        wavedash2 = (wavedash2 - 0.5*airdodgev2)
        wavedash3 = (wavedash3 - 0.5*airdodgev3)
        print("\Corrected Max angle Wavedash distance: *" ,wavedash2)
        print("\Corrected Diagonal notch Wavedash distance: *" ,wavedash3)


def start():
    sts, prompt = charselect()

    print("Stats: ", sts)
    print("Character: ", prompt)
    print("Tasks:\n> maxwalkandrun\n> wavedash\n> dash\n> foxtrot\n> rolling\n> dashdance\n> wavesurf\n> stats\n> all (can make ordered list with all)\n> smashturn")
    task = input("Type a task:\n> ")
    if task == "maxwalkandrun":
        printwalkandmaxrun(sts[3], sts[7])
    elif task == "wavedash":
        wavedash1, wavedash2, wavedash3 = wavedashing(sts[5], sts[6], sts[7], sts[8], prompt, "test.txt")
        wavedashdistance(sts[5], sts[6], sts[7], prompt)
    elif task == "dash":
        dash = dashing(sts[0], sts[2], sts[3], sts[4], sts[5], "test.txt")
    elif task == "foxtrot":
        foxtrot = foxtrotting(sts[0], sts[1], sts[2], sts[3], sts[4], sts[5])
    elif task == "rolling":
        rollforward, rollbackward = rolling(sts[9], sts[10], sts[11])
    elif task == "dashdance":
        dashdancing(sts[0], sts[2], sts[3], sts[4], sts[5], sts[12])
        extendeddashdancing(sts[0], sts[2], sts[3], sts[4], sts[5], sts[12])
    elif task == "wavesurf":
        prompt2 = input("Type of wavedash?\n> Perfect waveland (pw)\n> Max Angle wavedash (ma)\n> Diagonal notch wavedash (dn)\n\n> ")
        if prompt2 == "pw":
            wavesurf = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "pw", False)
        elif prompt2 == "ma":
            wavesurf = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "ma", False)
        elif prompt2 == "dn":
            wavesurf = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "dn", False)
    elif task == "stats":
        print("\nDash frames: ", sts[0])
        print("\nInitial Dash velocity: ", sts[2])
        print("\nDash acceleration: ", sts[4])
        print("\nMaximum dash velocity: ", sts[3])
        print("\nVelocity when high traction is in affect: >", sts[7])
        print("\nHigh traction: ", sts[6])
        print("\nLow traction: ", sts[5])
    elif task == "all":
        printwalkandmaxrun(sts[3], sts[7])
        wavedash1, wavedash2, wavedash3 = wavedashing(sts[5], sts[6], sts[7], sts[8], prompt)
        wavedashdistance(sts[5], sts[6], sts[7], prompt)
        dash = dashing(sts[0], sts[2], sts[3], sts[4], sts[5])
        foxtrot = foxtrotting(sts[0], sts[1], sts[2], sts[3], sts[4], sts[5])
        rollforward, rollbackward = rolling(sts[9], sts[10], sts[11])
        dashdancing(sts[0], sts[2], sts[3], sts[4], sts[5], sts[12])
        extendeddashdancing(sts[0], sts[2], sts[3], sts[4], sts[5], sts[12])
        wavesurf = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "ma", False)
        print("\nDash frames: ", sts[0])
        print("\nInitial Dash velocity: ", sts[2])
        print("\nDash acceleration: ", sts[4])
        print("\nMaximum dash velocity: ", sts[3])
        print("\nVelocity when high traction is in affect: >", sts[7])
        print("\nHigh traction: ", sts[6])
        print("\nLow traction: ", sts[5])
        prompt2 = input("\nWould you like an ordered list of velocities? (Y/N)\n> ")
        if prompt2 == "Y" or prompt2 == "y":
            velocityorder(sts[3], sts[7], wavedash1, wavedash2, wavedash3, dash, foxtrot, rollforward, rollbackward, wavesurf)
        else:
            print("I'll take that as a no.\n")
    elif task == "smashturn":
        filename = "turns.txt"
        prompt2 = input("From what state?\n> walk\n> wavedash\n> dash\n> all\n\n> ")
        if prompt2 == "walk":
            walksmashturn(sts[5], sts[7], filename)
        elif prompt2 == "wavedash":
            prompt3 = input("What kind of wavedash?\n> perfect waveland (pw)\n> max angle (ma)\n> diagonal notch (dn)\n\n")
            if prompt3 == "pw":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "pw", True)
                wdsmashturn(sts[5], sts[6], sts[7], "pw", wdf10, filename)
            elif prompt3 == "ma":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "ma", True)
                wdsmashturn(sts[5], sts[6], sts[7], "ma", wdf10, filename)
            elif prompt3 == "dn":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "dn", True)
                wdsmashturn(sts[5], sts[6], sts[7], "dn", wdf10, filename)
        elif prompt2 == "dash":
            dashsmashturnempty(sts[0], sts[2], sts[3], sts[4], sts[5], filename)
            dashsmashturnfull(sts[0], sts[2], sts[3], sts[4], sts[5], filename)
        elif prompt2 == "all":
            walksmashturn(sts[5], sts[7], prompt, filename)
            wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "pw", True)
            wdsmashturn(sts[5], sts[6], sts[7], "pw", wdf10, filename)
            wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "ma", True)
            wdsmashturn(sts[5], sts[6], sts[7], "ma", wdf10, filename)
            wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "dn", True)
            wdsmashturn(sts[5], sts[6], sts[7], "dn", wdf10, filename)
            dashsmashturnempty(sts[0], sts[2], sts[3], sts[4], sts[5], filename)
            dashsmashturnfull(sts[0], sts[2], sts[3], sts[4], sts[5], filename)
        
    elif task == "moonwalk":
        prompt2 = input("\nWhat kind of moonwalk?\n> stationary\n> wavedash\n> walk\n\n> ")
        if prompt2 == "stationary":
            moonwalk(sts[1], sts[3], sts[4], sts[5], sts[6], sts[7], sts[12], sts[13], sts[14], 0)
        elif prompt2 == "wavedash":
            prompt3 = input("\nWhat kind of wavedash?\n> perfect waveland (pw)\n> max angle wavedash (ma)\n> diagonal notch wavedash (dn)\n\n> ")
            if prompt3 == "pw" or prompt3 == "perfect waveland":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "pw", True)
                moonwalk(sts[1], sts[3], sts[4], sts[5], sts[6], sts[7], sts[12], sts[13], sts[14], wdf10)
            elif prompt3 == "ma" or prompt3 == "max angle":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "ma", True)
                moonwalk(sts[1], sts[3], sts[4], sts[5], sts[6], sts[7], sts[12], sts[13], sts[14], wdf10)
            elif prompt3 == "dn" or prompt3 == "diagonal notch":
                wdf10 = wavesurfing(sts[2], sts[3], sts[4], sts[5], sts[6], sts[7], sts[8], prompt, "dn", True)
                moonwalk(sts[1], sts[3], sts[4], sts[5], sts[6], sts[7], sts[12], sts[13], sts[14], wdf10)
        elif prompt2 == "walk":
            moonwalk(sts[1], sts[3], sts[4], sts[5], sts[6], sts[7], sts[12], sts[13], sts[14], sts[7])
    #elif task == "boostgrab":
        #boostgrab(da)
    else:
        print("Invalid task.")
        start()


    start()
def wdsmashturn(traction_low, traction_high, maxwalk, wdtype, wdf10, filename):
    data = open(filename, 'a')
    data.write("-----WAVEDASH TURN-----\n")
    if wdtype == "pw":
        data.write("~~~~~PERFECT WAVELAND~~~~~\n\n")
    elif wdtype == "ma":
        data.write("~~~~~MAX ANGLE~~~~~\n\n")
    elif wdtype == "dn":
        data.write("~~~~~DIAGONAL NOTCH~~~~~\n\n")

    wdnextf = wdf10
    newv = wdf10
    i = 0
    while i < 5:
        smashturn = 0
        print("\nStarting velocity: ", newv)
        data.write("Starting velocity: " + str(newv) + "\n")
        if newv > maxwalk:
            newv -= traction_high
        else:
            newv -= traction_low
        turn1 = newv
        print("From actionable frame %s\nFull distance: %s" % (i + 1, newv*2))
        data.write("From actionable frame " + str(i + 1) + "\nFull turn distance: " + str(newv*2) + " | From Turn 1 : " + str(newv) + "\n")
    
    
        while newv > 0:
            if newv > maxwalk:
                newv -= traction_high
            else:
                newv -= traction_low
                if newv < 0:
                    newv = 0
            smashturn += newv
        print("Empty distance:", (smashturn + turn1))
        data.write("Empty turn distance: " + str(smashturn + turn1) + " | From Turn 1: " + str(smashturn) + "\n\n")
    
        if wdnextf > maxwalk:
            wdnextf -= traction_high
        else:
            wdnextf -= traction_low
        newv = wdnextf
        i += 1
    data.write("\n")

def walksmashturn(traction_low, maxwalk, prompt, filename):
    data = open(filename, 'a')
    data.write("----------[[[[[[[[[" + prompt + "]]]]]]]]]---------\n")
    data.write("-----WALK TURN-----\n")

    print("\nMaxwalk Speed:", maxwalk)
    data.write("Maxwalk Speed: " + str(maxwalk) + "\n")
    newv = maxwalk - traction_low
    print("Full distance: ", newv*2)
    data.write("Full turn distance: " + str(newv * 2) + " | From Turn 1: " + str(newv) + "\n")
    smashturn = newv
    turn1 = newv
    while newv > 0:
        newv -= traction_low
        if newv < 0:
            newv = 0
        smashturn += newv
    print("Empty distance: ", smashturn)
    data.write("Empty turn distance: " + str(smashturn) + " | From Turn 1: " + str(smashturn - turn1) + "\n")
    data.write("\n")
    
    
def dashsmashturnfull(d_x, d_initialv, d_maxv, d_acceleration, traction_low, filename):
    data = open(filename, 'a')
    data.write("-----DASH SMASH TURN (Full)-----\n")
    #previousvelocity*0.25 - traction = newvelocity :min 0
    if d_initialv == d_maxv:
        smashturn = (d_maxv * 0.25 - traction_low) * 2
        if smashturn < 0:
            smashturn = 0
        print("\nFrom any frame, smash turn (full) distance: " ,smashturn)
        data.write("From any frame, smash turn (full) distance: " + str(smashturn) + " | From Turn 1: " + str(smashturn / 2) + "\n")
    
    elif d_initialv > d_maxv:
        print("\nSmash Turn Full from dash (Dash back):\nFrom Dash Frame | Distance\n---------------------------")
        data.write("Smash Turn Full from dash (Dash back):\nFrom Dash Frame | Distance | From Turn 1\n---------------------------\n")
        i = 0
        while i <= d_x:
            previousvelocity = d_initialv - (i * traction_low)
            if previousvelocity < d_maxv :
                previousvelocity = d_maxv
            smashturn = (previousvelocity * 0.25 - traction_low) * 2
            print("> %s | %s" % ((i + 1) , smashturn))
            data.write("> " + str(i + 1) + " | " + str(smashturn) + " | " + str(smashturn / 2) + "\n")
            i += 1
    
    else:
        print("\nSmash Turn Full from dash (Dash back):\nFrom Dash Frame | Distance\n---------------------------")
        data.write("Smash Turn Full from dash (Dash back):\nFrom Dash Frame | Distance | From Turn 1\n---------------------------\n")
        i = 0
        while i <= d_x:
            previousvelocity = d_initialv + (i * d_acceleration)
            if previousvelocity > d_maxv :
                previousvelocity = d_maxv
            smashturn = (previousvelocity * 0.25 - traction_low) * 2
            print("> %s | %s" % ((i + 1), smashturn))
            data.write("> " + str(i + 1) + " | " + str(smashturn) + " | " + str(smashturn / 2) + "\n")
            i += 1
    data.write("\n")

def dashsmashturnempty(d_x, d_initialv, d_maxv, d_acceleration, traction_low, filename):
    data = open(filename, 'a')
    data.write("-----DASH SMASH TURN (Empty)-----\n")
    if d_initialv == d_maxv:
        velocity = d_maxv * 0.25 - traction_low
        turn1 = velocity
        if velocity < 0:
            velocity = 0
        smashturn = 0
        while velocity > 0:
            smashturn = smashturn + velocity
            velocity = velocity - traction_low
        print("\nFrom any frame, smash turn (empty) distance: " ,smashturn)
        data.write("From any frame, smash turn (empty) distance: " + str(smashturn) + " | " + str(smashturn - turn1) + "\n")
    
    elif d_initialv > d_maxv:
        print("\nSmash Turn Empty from dash (Empty pivot):\nFrom Dash Frame | Distance\n---------------------------")
        data.write("Smash Turn Empty from dash (Empty pivot):\nFrom Dash Frame | Distance | From Turn 1\n---------------------------\n")
        i = 0
        while i <= d_x:
            previousvelocity = d_initialv - (i * traction_low)
            if previousvelocity < d_maxv :
                previousvelocity = d_maxv
            velocity = previousvelocity * 0.25 - traction_low
            turn1 = velocity
            if velocity < 0:
                velocity = 0
            smashturn = 0
            while velocity > 0:
                smashturn = smashturn + velocity
                velocity = velocity - traction_low
            print("> %s | %s" % ((i + 1), smashturn))
            data.write("> " + str(i + 1) + " | " + str(smashturn) + " | " + str(smashturn - turn1) + "\n")
            i += 1
    
    else:
        print("\nSmash Turn Empty from dash (Empty pivot):\nFrom Dash Frame | Distance\n---------------------------")
        data.write("Smash Turn Empty from dash (Empty pivot):\nFrom Dash Frame | Distance | From Turn 1\n---------------------------\n")
        i = 0
        while i <= d_x:
            previousvelocity = d_initialv + (i * d_acceleration)
            if previousvelocity > d_maxv :
                previousvelocity = d_maxv
            velocity = previousvelocity * 0.25 - traction_low
            turn1 = velocity
            if velocity < 0:
                velocity = 0
            smashturn = 0
            while velocity > 0:
                smashturn = smashturn + velocity
                velocity = velocity - traction_low
            print("> %s | %s" % ((i + 1), smashturn))
            data.write("> " + str(i + 1) + " | " + str(smashturn) + " | " + str(smashturn - turn1) + "\n")
            i += 1
    data.write("\n")    

def moonwalk(d_y, d_maxv, d_acceleration, traction_low, traction_high, maxwalk, d_trueinitialv, damulti, turnrun, originalv):
    ang = 0.7
    angle = (1 - ang) / 0.0125
    danew = d_acceleration - (angle * damulti)
    newv = originalv
    newvtest = 0
    a = False
    b = 0
    j = 1
    while b != 2 and j != 11:
        moonwalk = 0
        newv2 = newv - d_trueinitialv
        if newv2 > 0:
            newv2 = newv2 - traction_low
            if newv2 < 0:
                newv2 = 0
        
        else:
            newv2 = newv2 + traction_low
            if newv2 > 0:
                newv2 = 0

        moonwalk = newv
        moonwalk += newv2    

        if j == 1:
            newv = - d_trueinitialv
            moonwalk = newv + traction_low

        moonwalk += (newv2*2 + danew*3)
        newv = newv2 + (danew * 2)

        i = 5
        while i <= d_y:
            newv = newv + d_acceleration
            if newv > d_maxv:
                newv = d_maxv
                a = True
            moonwalk = moonwalk + newv
            if i == d_y - 1:
                boostrunv = newv
            i += 1
        print("\nNo.%s moonwalk distance: %s" % (j, moonwalk))
        print("No.%s moonwalk avg velocity: %s" % (j, (moonwalk / d_y)))
        boostrun = boostrunv
        # plus run1
    
        k = 0
        l = False
        while k <= turnrun:
            if boostrunv + d_acceleration < d_maxv:
                boostrunv += d_acceleration
            else :
                if l == False:
                    boostrunv = d_maxv
                    l = True
                else :
                    boostrunv += (d_acceleration - traction_low)
            boostrun += boostrunv
            k += 1
        print("~ Boostrun distance: %s" % boostrun)
        print("~ Boostrun velocity: %s" % (boostrun / turnrun))
        print("~ Boostrun peak velocity: %s" % boostrunv)
        print("~ Boostrun with moonwalk distance: %s" % (boostrun + moonwalk - newv))
        print("~ Boostrun with moonwalk velocity: %s" % ((boostrun + moonwalk - newv) / (d_y + turnrun)))
    
        newv2 = newv
        i = 0
        while newv2 > 0:
            if newv2 > maxwalk:
                newv2 = newv2 - traction_high
            else:
                newv2 = newv2 - traction_low
            moonwalk = moonwalk + newv2
            i += 1
        moonwalk = moonwalk - newv2
        print("\nNo.%s moonwalk distance with drift: %s" % (j, moonwalk))
        print("No.%s moonwalk avg velocity with drift: %s" % (j, (moonwalk / (d_y + i))))
        print("No.%s moonwalk with drift, total frames: %s" % (j, (i + d_y)))
        print("\n", "-" * 8, "+", "-" * 8)
        if a == True:
            b += 1
            a = False
        j += 1
        if newvtest == newv:
            break
        newvtest = newv
    
    if j < 11:
        print("Chained moonwalk No.%s is the maximum, and all following moonwalks will have equal stats." % (j - 1))
    else :
        print("Chained moonwalks will gain less distance each time, or increase very slowly.")

#def boostgrab():
    # dash 4 frames
    #

start()