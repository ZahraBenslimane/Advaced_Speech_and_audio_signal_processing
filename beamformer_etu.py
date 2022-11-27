import numpy as np #line:1
N =8 #line:4
d =0.06 #line:5
def beam_filter (OOO0000000O00O0O0 ,OO00000OO0O0OOO00 ,O00O0OO00O0000OOO ,OOOO00OOO0O000OO0 =0 ,OO00O0OO0O0O00O0O :int =0 ):#line:7
    ""#line:19
    OO0OOOO00OOO0O0OO =(OO00O0OO0O0O00O0O -OO00000OO0O0OOO00 -1 )/2 *O00O0OO00O0000OOO #line:22
    return np .exp (-1j *2 *np .pi *OOO0000000O00O0O0 /340 *OO0OOOO00OOO0O0OO *np .cos (OOOO00OOO0O000OO0 *np .pi /180 ))#line:24
def beamformer (OOO0OO0000O00O000 ,O0O000OOOO0000OOO ,OO0O000OOOOOO0OO0 ,O0O0OOO0OO0O00OOO ):#line:27
    ""#line:35
    O000O00OOO00OO000 ,OOO00O0OOO0O0OOO0 =np .shape (OOO0OO0000O00O000 )#line:38
    OOO00O00O0O0O00O0 =np .arange (0 ,O0O0OOO0OO0O00OOO ,O0O0OOO0OO0O00OOO /OOO00O0OOO0O0OOO0 )#line:41
    O00OO00O00OOOOO0O =np .zeros ((O000O00OOO00OO000 ,1 ),dtype =np .complex_ )#line:49
    OO000O0O0O0O0000O =np .zeros ((len (O0O000OOOO0000OOO ),1 ),dtype =np .complex_ )#line:50
    OO0000OO000OO0OOO =np .fft .fft (OOO0OO0000O00O000 )#line:53
    OO00OO0OOOOOO00O0 =np .abs (OOO00O00O0O0O00O0 -OO0O000OOOOOO0OO0 ).argmin ()#line:57
    O0000OO0O0O0O0OOO =OOO00O00O0O0O00O0 [OO00OO0OOOOOO00O0 ]#line:60
    OO0O0OO0O00OOOO00 =OO0000OO000OO0OOO [:,OO00OO0OOOOOO00O0 ]#line:61
    for O00OOO0O0000000OO ,OOO00OOOOOO0OO000 in enumerate (O0O000OOOO0000OOO ):#line:64
        for OO0O0O00OOO00OOOO in np .arange (0 ,O000O00OOO00OO000 ):#line:66
            OO00OOO00OOO000O0 =beam_filter (O0000OO0O0O0O0OOO ,O000O00OOO00OO000 ,d ,theta =OOO00OOOOOO0OO000 ,mic_id =OO0O0O00OOO00OOOO )#line:68
            O00OO00O00OOOOO0O [OO0O0O00OOO00OOOO ,:]=OO0O0OO0O00OOOO00 [OO0O0O00OOO00OOOO ]*OO00OOO00OOO000O0 #line:70
        OO000O0O0O0O0000O [O00OOO0O0000000OO ,:]=sum (O00OO00O00OOOOO0O ,1 )#line:72
    O0O0O0OOO0O0OO000 =np .sum (np .square (np .abs (OO000O0O0O0O0000O )),1 )#line:75
    return O0O0O0OOO0O0OO000 #line:77
if __name__ =="__main__":#line:79
    print ("Simulation")#line:80
    beamformer (1 )