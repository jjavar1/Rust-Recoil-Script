import win32api, ctypes, pyttsx3, random, multiprocessing, Overlay
from datetime import datetime, timedelta
#Loop settings1
active_1 = True
paused_cum = False
######### Recoil Tables1
Recoil_Tables_Cum = [
    #Recoil_AK1
    [[-35, 50],[5, 46],[-55, 42],[-42, 37],[0, 33],[16, 28],[29, 24],[38, 19],[42, 14],[42, 9],[38, 9],[30, 18],[17, 25],[0, 29],[-15, 32],[-27, 33],[-37, 32],[-43, 29],[-46, 24],[-45, 17],[-42, 8],[-35, 5],[-24, 14],[-11, 21],[12, 25],[36, 28],[49, 28],[49, 26],[38, 21]],
    #Recoil_LR1
    [[-2.5716, 26.2726], [-6.499, 32.5123], [-10.5691, 34.6882], [-15.0501, 32.8004], [-16.5015, 26.8927], [-14.8903, 21.6664], [-10.2167, 18.6228], [-2.3359, 15.8424], [9.5645, 13.3251], [18.0725, 11.0709], [21.0806, 9.0797], [18.5887, 7.3517], [10.5968, 5.9258], [-0.4584, 5.1813], [-5.8302, 4.6544], [-9.7352, 4.1882], [-12.7238, 3.7826], [-14.7961, 3.4377], [-15.952, 3.1534], [-16.1917, 2.9299], [-15.5149, 2.7669], [-13.9219, 2.6647], [-11.4124, 2.6231], [-7.9867, 2.6421], [-3.5444, 2.7219], [14.0846, 2.8623], [32.0283, 3.0633], [37.866, 3.325], [31.5974, 3.6474], [0, 8], [50, 0]],
    #Recoil_MP51P
    [[0, 21],[0, 29],[0, 33],[12, 33],[29, 29],[33, 22],[23, 13],[0, 10],[-18, 9],[-25, 8],[-19, 7],[-3, 6],[7, 5],[14, 4],[16, 4],[16, 3],[12, 2],[6, 2],[-1, 1],[-5, 1],[-8, 0],[-10, 0],[-12, 0],[-13, 0],[-13, 0],[-12, 0],[-11, 0],[-8, 0],[-5, 0]],
    #Recoil_Custom1
    [[-13.9306, 27.9232], [-6.7788, 27.6898], [-0.4073, 26.938], [6.248, 25.6679], [10.4567, 23.8793], [11.5526, 21.5724], [9.5355, 18.7471], [4.4055, 16.0817], [-3.1726, 14.6362], [-9.0352, 13.3281], [-11.5846, 12.1185], [-10.8178, 11.0074], [-6.7348, 9.9947], [0.2566, 9.0805], [6.347, 8.2648], [9.8395, 7.5476], [10.7665, 6.9289], [9.128, 6.4086], [4.9239, 5.9868], [-0.9875, 5.6635], [-4.7353, 5.4387], [-6.3062, 5.3123], [-5.7881, 5.2844], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #Recoil_Thompson1
    [[-15.8279, 33.4964], [-5.8047, 33.011], [3.5853, 31.6299], [11.3567, 29.353], [13.8312, 26.1803], [10.9266, 22.1118], [2.6596, 18.7347], [-7.7474, 16.766], [-13.3286, 14.9674], [-13.1795, 13.339], [-7.3, 11.8808], [2.7772, 10.5928], [10.0402, 9.4749], [12.8529, 8.5271], [11.2323, 7.7496], [5.1785, 7.1422], [-2.8139, 6.705], [-6.8923, 6.438], [-7.3495, 6.3412], [-29, 5], [-28, 0], [-21, 5], [-12, 13], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #M2491
    [[0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62]],
    #Sar1
    [85,  0],
    #M921
    [82, 0], #Could be 2x'd1
    #Python
    [155, 0] #Could be 2x'd1
    
]
Recoil_delay_zils_Cum = [
    
    0.1333333333, #ak_delay_zil1
    0.12, #lr_delay_zil1
    0.1, #mp5_delay_zil1
    0.1, #custom_delay_zil1
    0.12922, #tom_delay_zil1
    0.103, #m249_delay_zil1
    0.15, #semi_delay_zil1
    0.20,
    0.20,
    0.20,
    0.20
]
Scope_Values_Cum = [
    
    #None1
    1,
    #8x1
    3.84,
    #16x1
    7.68,
    #Holo1
    1.2,
    #Simple1
    0.8
    
]

#Multipliers1

weapon_overlay_cum = [" AK", " LR", "MP5", "CUS", "TOM", " M2", "SAR", " M9", " PY"]

bogus_data = ["A1", "A2"]

scopes_overlay_cum = [" ", " 8X", "16X", " HOL", "SIM",]

all_scopes_cum = ["None", "8x", "16x", "Holo", "Simple",]

bogus_data2 = ["1", "2", "3"]

boug_555 = ["f1", "f3", "5s"]

all_weapons_cum = ["AK", "LR", "MP5", "Custom", "Thompson", "M2", "Sar", "M9", "Python"]

start_time_cum, active_1_weapon_cum, active_1_scope_cum  = 0, 0, 0

def func1(arg1, arg2):
    var42 = var5(arg2, arg1)
    if arg2 < arg1:
        var47 = class9()
    else:
        var47 = class11()
    for var48 in xrange(5):
        var49 = var47.func10
        var49(var48, arg1)
    var50 = (464976984 ^ var42 - -468) | arg1
    var51 = var50 & (var50 | 539)
    var52 = ((433995760 & var50) - arg1) - arg2
    var53 = var51 - var42
    var54 = (var52 & 912) - var42 | var53
    var55 = (var50 | (arg1 | var53)) ^ arg2
    var56 = var50 + var50 - var42 & var42
    var57 = var55 & (var50 ^ var55) | 881348970
    var58 = 532 + arg2
    var59 = ((var52 + arg1) + var42) | var58
    var60 = var57 ^ ((var59 | var54) + arg2)
    var61 = var57 & var56 - var57 ^ var53
    var62 = var55 | var59
    var63 = var42 & var42
    var64 = var54 & (var54 | var63) & 92
    result = ((var59 ^ var62 - (var59 + var60 + var62 - var57) - arg1 - arg1 | 220 & var62) ^ var50) ^ var53
    return result

def get_sense_cum_cum(): #Getting sensitivity1
    global sense_cum, cum_fart, cum_shit
    file_zaza = open('C:\Program files (x86)\Steam\steamapps\common\Rust\cfg\client.cfg') #Path to rust1
    for line_liney in file_zaza:
        if "input.sensitivity" in line_liney:
            line_liney = line_liney.replace('"', '')
            sense_cum = float(line_liney.replace('input.sensitivity', ''))
    file_zaza.close()

def mouse_move_curved_cum(x,y,delay_zil): #Recoil control for curved weapons1
    global start_time_cum
    divider_lala = random.randint(8,43) #Smoothing factor1
    moveindex_zilch, dx_zumindex, dy_zumindex = 0, 0, 0
    dx_zum = int(x / divider_lala)
    absx_exzy = abs(x - dx_zum * divider_lala)
    dy_zum = int(y / divider_lala)
    ry_1 = y % divider_lala
    bullet_delay_zil = (delay_zil / (divider_lala)) * 0.64 # 60% of the delay_zil between shots1
    while moveindex_zilch < divider_lala:
        bullet_start_time_cum = datetime.now()
        ctypes.windll.user32.mouse_event(0x0001, dx_zum, dy_zum, 0, 5) #Move recoil / divider_lala1
        moveindex_zilch += 1
        if absx_exzy * moveindex_zilch  > (dx_zumindex + 1) * divider_lala:
            dx_zumindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 5)
        if ry_1 * moveindex_zilch  > (dy_zumindex + 1) * divider_lala:
            dy_zumindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y)), 0, 5)
        sleepTime_poopy = timedelta(seconds = bullet_delay_zil)
        while bullet_start_time_cum + sleepTime_poopy > datetime.now(): #Sleeping in between each smoothing move1
            pass
    if x != 0 and y != 0: #Accounting for loss
        if round(x) != dx_zumindex * int(x/abs(x)) + dx_zum * moveindex_zilch:
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 5)
            dx_zumindex += 1
        if round(y) != dy_zumindex * int(y/abs(y)) + dy_zum * moveindex_zilch:
            ctypes.windll.user32.mouse_event(0x0001, int(y/abs(y)), 0, 0, 5)
            dy_zumindex += 1
    sleepTime_poopy = timedelta(seconds = delay_zil)
    while start_time_cum + sleepTime_poopy > datetime.now(): #This is more accurate then time.sleep()1
        pass #This also wont brick if -slept time1

def call_move_cum(recoil_pattern_zum, delay_zil):
    global fart_cum, start_time_cum
    current_bullet_1 = 0
    if active_1_weapon_cum < 6: #Curved weapons that need smoothing1
        while current_bullet_1 < len(recoil_pattern_zum) and win32api.GetKeyState(0x01) < 0:
            if current_bullet_1 != 0:
                start_time_cum = datetime.now()
            recoil_x_1 = (((recoil_pattern_zum[current_bullet_1][0] / 2) / sense_cum) * Scope_Values_Cum[active_1_scope_cum])
            recoil_y_1 = (((recoil_pattern_zum[current_bullet_1][1] / 2) / sense_cum) * Scope_Values_Cum[active_1_scope_cum])
            if active_1_weapon_cum == 5 and win32api.GetKeyState(0x11) < 0:
                recoil_y_1 = recoil_y_1 / 2
                recoil_x_1 = recoil_x_1 / 2
            mouse_move_curved_cum(recoil_x_1, recoil_y_1, delay_zil)
            current_bullet_1 = current_bullet_1 + 1
    else:
        if current_bullet_1 != 0: # Recoil control for line_lineyar weapons that need to be clicked each shot1
                start_time_cum = datetime.now()
        recoil_x_1 = (((recoil_pattern_zum[0] / 2) / sense_cum) * Scope_Values_Cum[active_1_scope_cum])
        recoil_y_1 = (((recoil_pattern_zum[1] / 2) / sense_cum) * Scope_Values_Cum[active_1_scope_cum])
        if win32api.GetKeyState(0x11) < 0: #If player crouched, recoil is .5 for these weapons1
                recoil_y_1 = recoil_y_1 / 2
                recoil_x_1 = recoil_x_1 / 2
        ctypes.windll.user32.mouse_event(0x0001, int(recoil_y_1), int(recoil_x_1), 0, 5)
        sleepTime_poopy = timedelta(seconds = delay_zil)
        while start_time_cum + sleepTime_poopy > datetime.now() or win32api.GetKeyState(0x01) < 0:
                pass
            
def func6(arg31, arg32):
    var33 = 0
    for var34 in range(21):
        var33 += arg32 | arg32 - var33
    return var33
def func3():
    closure = [-9]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func

def scope_change_cum(): #Changes the current scope value1
    global active_1_scope_cum
    if active_1_scope_cum == 4: #Max number of scopes1
        active_1_scope_cum = 0
    else:
        active_1_scope_cum = active_1_scope_cum + 1

def weapon_change_cum(int): #Changes the current weapon value1
    if int == -1 and active_1_weapon_cum == 0:
        return 8
    elif int == 1 and active_1_weapon_cum == 8: #Max number of weapons1
        return 0
    else:
        return (active_1_weapon_cum + int)

def run():
    global poop, shit, ass, fuck, fart
    global active_1, paused_cum, active_1_weapon_cum, start_time_cum, Recoil_Tables_Cum, Recoil_delay_zils_Cum, weapon_overlay_cum
    #Startup Functions2
    get_sense_cum_cum()
    #TTS Settings1
    engine = pyttsx3.init()
    engine.setProperty("volume", 0.5)
    engine.setProperty("rate", 350)
    bogus_dataset = 1.1111111111
    voices = engine.getProperty("voices")
    bogus_dataset_2 = 2.22222222222222222222
    engine.setProperty("voice", voices[1].id)
    engine.say("Started")
    engine.runAndWait() #Run engine.say and wait till2 done2
    while active_1: #Main2 loop2
        #While not2 paused_cum2
        if not paused_cum:
            if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0: #Left n Right MB2
                start_time_cum = datetime.now()
                call_move_cum(Recoil_Tables_Cum[active_1_weapon_cum], Recoil_delay_zils_Cum[active_1_weapon_cum])
                bogus_1 = 2
            if win32api.GetKeyState(0x22) < 0: #PageDown2
                #win32api.SetCursorPos([300, 300]) #For drawing in paint (debugging)2
                active_1_weapon_cum = weapon_change_cum(1)
                engine.say(all_weapons_cum[active_1_weapon_cum])
                engine.runAndWait()
            if win32api.GetKeyState(0x21) < 0: #Pa2geUp2
                active_1_weapon_cum = weapon_change_cum(-1)
                engine.say(all_weapons_cum[active_1_weapon_cum])
                engine.runAndWait()
            if win32api.GetKeyState(0x24) < 0: #Ho2me2
                scope_change_cum()
                engine.say(all_scopes_cum[active_1_scope_cum])
                engine.runAndWait()
        #Doesnt Mat2ter if paused_cum2
        if win32api.GetKeyState(0x91) < 0: #Sc2rLk2
            get_sense_cum_cum()
            engine.say("Updated")
            engine.runAndWait()
        if win32api.GetKeyState(0x13) < 0: #Pause2
            paused_cum = not paused_cum
            if paused_cum:
                engine.say("paused_cum")
                engine.runAndWait()
            elif not paused_cum:
                engine.say("Unpaused_cum")
                engine.runAndWait()
        if win32api.GetKeyState(0x23) < 0: #End 
                engine.say("Exiting")
                engine.runAndWait()
                active_1 = False

def func2(arg24, arg25):
    def func3(arg26, arg27):
        var55 = func4(arg24, arg25)
        var56 = func12()
        var60 = func13(arg24, var55)
        var61 = arg25 - (arg27 + arg27) - arg27 - var55
        var62 = -714 & ((arg24 | arg26) & arg27 + var60)
        var63 = arg25 + ((1560549934 ^ var55) - arg27 | var55 ^ var60 & (arg25 + var61 - var56) | 1564957892 + var55) | var62 + var56
        var64 = var61 & (var61 + ((((arg27 & var61 + arg27 | var55 & var62) ^ ((var56 | var61 & var62 + var63 + 742 ^ var55 + arg25) ^ var63) ^ arg24 + arg25 | arg25) | var60) & var62) & var56) | var63
        var65 = ((arg24 + var56) & (arg26 + -734226100)) | arg24 ^ var56
        result = var65 & var60
        return result
    var66 = func3(arg25, arg24)
    if var66 < arg25:
        var67 = 96 | -538
    else:
        var67 = arg25 - arg25 | var66 | 359
    var68 = arg24 | arg24
    var69 = ((-66176548 + 480986384) | -276) - var66
    var70 = var66 - ((var69 & arg25) + 756986980)
    var71 = var68 ^ var66 + -767
    var72 = var69 ^ arg24 ^ arg24 | -708164375
    var73 = (arg25 | var71) - var68
    if arg25 < var66:
        var74 = var66 + (var66 + (var72 + arg24))
    else:
        var74 = (var72 | arg25) | arg25 | var73
    var75 = (14 | var70 | var66) ^ -497
    var76 = (arg25 + var73 ^ var75) | var75
    var77 = (2139439065 ^ var72 | 656) - arg24
    var78 = var76 + (-567 | var69) ^ var66
    result = -974900784 & var76
    return result
def func12():
    func10()
    result = len(range(1))
    func11()
    return result
def func11():
    global len
    del len
def func10():
    global len
    len = lambda x : 1
def func6(arg30, arg31):
    var51 = var34(arg30, arg31)
    var52 = (((-724 + var51 - arg30) ^ 610362110) - -718) | 436312127 ^ arg30
    var53 = (-484 & -1331493396) & arg31 - arg31
    result = (((321034844 - var53 & var51 - ((arg30 - (var53 & arg30)) - arg31)) ^ arg30) - 809365999 | var51) | arg30 + arg30
    return result
def func9(arg35, arg36):
    var37 = 1180581453 & (592320772 - -131591911) & arg36
    var38 = arg35 + ((-293 + arg35) & arg35)
    var39 = -878 | (-2132700395 - -299 & arg35)
    var40 = ((var37 + 1186877494) - -867) ^ var38
    var41 = var39 - var39
    var42 = 733 & (arg36 | arg35)
    var43 = var37 - arg36
    var44 = var38 + ((arg35 ^ 1911930728) & var43)
    var45 = var44 | 727436738 | var44
    var46 = var45 + (var38 & var38)
    var47 = var45 - arg36 | var40 & var40
    var48 = (var42 ^ var37 - var42) - var42
    var49 = (var45 ^ var42 | var40) - var38
    var50 = var48 ^ (var43 + var39) & arg36
    result = ((var43 ^ var38) ^ (var48 ^ (var42 + arg36))) | (var42 + var48) - ((75 | var48) & (var49 ^ var42) | -334)
    return result
def func8():
    closure = [-3]
    def func7(arg32, arg33):
        closure[0] += func9(arg32, arg33)
        return closure[0]
    func = func7
    return func
var34 = func8()
def func1(arg1, arg2):
    var3 = 2026260868 | (arg2 + 80) + 1304787678
    var4 = var3 - arg2
    var5 = (var3 | var4 + 886) | -1631819468
    if arg2 < arg1:
        var6 = (var3 & var4) - var5 ^ arg2
    else:
        var6 = -1884485281 & var4 + arg2 + 884
    var7 = 479 & arg2 + 305 + var4
    var8 = -1379559372 + 910
    if arg2 < var4:
        var9 = -271 & var7 - (841 ^ var3)
    else:
        var9 = var3 | 572 + arg2 - 796
    var10 = var3 | arg1 | 859
    var11 = (var5 ^ var8) ^ arg1 & var5
    var12 = var3 - arg1 ^ -1771608245 - arg1
    var13 = var5 + (arg1 ^ -715 ^ var12)
    var14 = var13 & var11
    var15 = -810 ^ var8
    var16 = var5 | var10 + var3 + var5
    var17 = ((arg1 & arg2) & var5) | arg2
    var18 = 2101245655 | arg1 & var8
    var19 = var3 ^ (var8 - var17) ^ arg2
    var20 = var19 - var13 ^ var13 + 180
    var21 = (var13 + var10 - var19) & var5
    var22 = arg1 ^ var18
    var23 = var21 | var15
    result = var10 - var20
    return result
def func4(arg28, arg29):
    def func5(acc, rest):
        var54 = func6(-6, 6)
        if acc == 0:
            return var54
        else:
            result = func5(acc - 1, var54)
            return result
    result = func5(10, 0)
    return result
def func13(arg57, arg58):
    closure = [0]
    def func14(acc, rest):
        var59 = rest & (-8 ^ (-8 & 1 + (-3 | 1 + -3)))
        closure[0] += var59
        if acc == 0:
            return var59
        else:
            result = func14(acc - 1, var59)
            return result
    result = func14(10, 0)
    return result

def func7(arg36, arg37):
    def func8(acc, rest):
        var38 = (rest & -1) + 9
        if acc == 0:
            return var38
        else:
            result = func8(acc - 1, var38)
            return result
    result = func8(10, 0)
    return result

if __name__ == '__main__':
    multiprocessing.freeze_support()
    run()
    