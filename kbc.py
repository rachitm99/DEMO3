import time
print('WELCOME IN THE WORLD OF QUESTIONS')
time.sleep(5)
print()
print()
print('RULE 1: There is 15+1 questions')
print('''                            !!!!!7 crore!!!!!!
                          -------1 crore--------
                         --------50 lakh----------
                        ---------25 lakh------------
                      ----------12,50,000-------------
                    -------------6,40,000----------------
                  **************3,20,000*******************
                ----------------1,60,000---------------------
              -------------------80,000-------------------------
            ---------------------40,000---------------------------
          -----------------------20,000-----------------------------
        *************************10,000*******************************
      ----------------------------5,000---------------------------------
    ------------------------------3,000-----------------------------------
  --------------------------------2,000-------------------------------------
----------------------------------1,000--------------------------------------- ''')
print()
print()
print()
print()
print()
print()
print()
print()
print()
time.sleep(1)
#print('* There will be 45s for first 5 question')
#print('* There will be 60s for next 5 question')
print('There will be no time limit.')
time.sleep(2)
print()
print()
print()
print()
print("If you need life line press 'L'")
print("press 'q 'for quit")
print()
print()
time.sleep(5)
print()
print()
print()
print()
print('so..... lets start the game')
time.sleep(7)
print()
q='1(audience poll)'
y='2(50:50)'
z='3(expert advice)'
w='4(replace the question)'
ll=[q,y,z,w]
print('FIRST QUESTION(1,000)')
time.sleep(2)
print()
print('Q1 Which of these sports is also the name of something that can be drunk')
print('(a) Polo')
print('(b) Squash')      
print('(c) Golf')
print('(d) Croquet')
a=input('enter the option(a,b,c,d)') 
if a.lower()=='l':
    print(str(ll))
    for i in range(4):
     opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
     if opt==1 :
        print('(a)5%,(b)93%,(c)0%,(d)2%')
        ll.remove(q)
     if opt==2:
        print("options 'a' and 'b' remains")
        ll.remove(y)
     if opt==4:
        print('Q1 Which is the only planet in our Solar System known to have life on it ')
        time.sleep(2)
        print('(a) Mars')
        print('(b) Earth')      
        print('(c) Venus')
        print('(d) Saturn')
        ll.remove(w)
     if opt==3:
        print('b is correct option')
        ll.remove(z)
     if opt==0:
        break
    a=input('enter the option(a,b,c,d)')
if a.lower()=='q':
   print('THANKS FOR PLAYING YOU WON 0 ruppes')
if a=='b':
    print('correct option.you have won 1000 ruppes')
    x=input('Continue????')
    print()
    print('SECOND QUESTION(2,000)')
    print()
    print('Q2 The Sanchi Stupa is place of pilgrimage for which religious')
    time.sleep(2)
    print('(a) Sikhs')
    print('(b) Buddhists')
    print("(c) Christians ")
    print('(d) Muslims')
    print()
    b=input('enter the option(a,b,c,d)')
    
    
    if b.lower()=='l':   
     print(str(ll))
     for i in range(4):
      opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
      if opt==1 :
        print('(a)26%,(b)57%,(c)7%,(d)10%')
        ll.remove(q)
      if opt==2:
        print("options 'a' and 'b' remains")
        ll.remove(y)
      if opt==4:
         print('Q2 what is the weight of any body at centre of earth')
         time.sleep(2)
         print('(a) Equal to radius of Earth')
         print('(b) 0')      
         print('(c) Equal to mass of Earth')
         print('(d) infinity')
         ll.remove(w)
      if opt==3:
        print('b is correct option')
        ll.remove(z)
      if opt==0:
         break
     b=input('enter the option(a,b,c,d)')
    if a.lower()=='q':
     print('THANKS FOR PLAYING YOU WON 1000 ruppes')     
    if b=='b':
        print('correct option.you have won 2000 ruppes')
        x=input('Continue????')
    
        print()    
        print('THIRD QUESTION(3,000)')    
        print()
        print('Q3 Who discover electron,proton and neutron resp ')
        time.sleep(2)
        print('(a) rutherford,chadwick, thomson')
        print('(b) goldsten,chadwick,thomson')      
        print('(c) thomson,goldsten,chadwick')
        print('(d) bohr,chadwick,thomson')
        print()
        c=input('enter the option(a,b,c,d)')
        if c.lower()=='l':
         print(str(ll))
         for i in range(4):        
          opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
          if opt==1 :
           print('(a)16%,(b)27%,(c)51%,(d)6%')
           ll.remove(q)       
          if opt==2:
           print("options 'c' and 'b' remains")
           ll.remove(y)       
          if opt==4:
            print('Q3 which team has won the title maximum and how many')
            time.sleep(2)
            print('(a) MI-3')
            print('(b) CSK-4')      
            print('(c) MI-4')
            print('(d) CSK-3')
            ll.remove(w)
          if opt==3:
            print('c is correct option')
            ll.remove(z)
          if opt==0:
           break
         c=input('enter the option(a,b,c,d)')
        if a.lower()=='q':
                  print('THANKS FOR PLAYING YOU WON 2000 ruppes')   
        if c=='c':
            print('correct option.you have won 3000 ruppes')
            x=input('Continue????') 
            print()
            print('FOURTH QUESTION(5,000)')
            print()
            print("Q4 Which animal is often referred to as 'man's best friend'?")
            time.sleep(2)
            print('(a) Cat ')
            print('(b) Dog')      
            print('(c) Monkey')
            print('(d) Donkey')
            print()
            d=input('enter the option(a,b,c,d)')
            if d.lower()=='l':
             print(str(ll))
             for i in range(4):   
               opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
               if opt==1 :
                print('(a)10%,(b)60%,(c)15%,(d)15%')
                ll.remove(q)  
               if opt==2:
                  print("options 'c' and 'b' remains")
                  ll.remove(y)
               if opt==4:
                    print('Q4 Who among these is allowed to carry a walkie-talkie during a cricket match ')
                    time.sleep(2)
                    print('(a) Captain')
                    print('(b) Umpire')      
                    print('(c) Third Man')
                    print('(d) Wicket-keeper')
                    ll.remove(w)
               if opt==3:
                print('b is correct option')
                ll.remove(z)
               if opt==0:
                break
             d=input('enter the option(a,b,c,d)')
            if a.lower()=='q':
                            print('THANKS FOR PLAYING YOU WON 3000 ruppes')    
            if d=='b':
               print('correct option.you have won 5000 ruppes')
               x=input('Continue????')
               print()
               print('FIFTH QUESTION(10,000)')
               print()
               print('Q5 Which of these is not an ape')
               time.sleep(2)
               print('(a) Gorilla')
               print('(b) Chimpanzee')      
               print('(c) Orangutan')
               print('(d) Monkey')
               print()
               e=input('enter the option(a,b,c,d)')
               if e.lower()=='l':
                 print(str(ll))
                 for i in range(4):
                  opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
                  if opt==1 :
                   print('(a)6%,(b)7%,(c)27%,(d)60%')
                   ll.remove(q)
                  if opt==2:
                      print("options 'c' and 'd' remains")
                      ll.remove(y)
                  if opt==4:
                      print('Q5 Which of these ingredients in a curry would give it a yellow colour ')
                      time.sleep(2)
                      print('(a) Elaichi')
                      print('(b) Ajwain')      
                      print('(c) Dhaniya')
                      print('(d) Haldi')
                      ll.remove(w)
                  if opt==3:
                        print('d is correct option')
                        ll.remove(z)
                  if opt==0:
                     break
                 e=input('enter the option')
               if a.lower()=='q':
                                  print('THANKS FOR PLAYING YOU WON 5000 ruppes')      
               if e=='d':
                  print('correct option.you have won 10,000 ruppes')
                  x=input('Continue????')
                  print()
                  print('SIXTH QUESTION(20,000)')
                  time.sleep(2)
                  print()
                  print('Q6 In which of these water bodies are the Lakshadweep Islands located')
                  time.sleep(2)
                  print('(a) Indian Ocean')
                  print('(b) Arabian Sea')      
                  print('(c) Bay of bengal')
                  print('(d) Gulf of Kutch')
                  print()
                  f=input('enter the option(a,b,c,d)')
                  if f.lower()=='l':
                   print(str(ll))
                   for i in range(4):
                    opt=int(input('Enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
                    if opt==1 :
                      print('(a)29%,(b)30%,(c)28%,(d)13%')
                      ll.remove(q)
                    if opt==2:
                       print("options 'a' and 'b' remains")
                       ll.remove(y)
                    if opt==4:
                     print("Q6 what are 'bell-bottom' a type of ? ")
                     time.sleep(2)
                     print('(a) Trouser')
                     print('(b) Shirt')      
                     print('(c) Shoe')
                     print('(d) Hats')
                     ll.remove(w)
                    if opt==3:
                       print('b is correct option')
                       ll.remove(z)
                    if opt==0:
                     break
                   f=input('enter the option(a,b,c,d)')
                  if a.lower()=='q':
                                      print('THANKS FOR PLAYING YOU WON 10,000 ruppes')   
                  if f=='b':
                    print('correct option.you have won 20,000 ruppes')
                    x=input('Continue????')
                    print()
                    print('SEVENTH QUESTION(40,000)')
                    time.sleep(2)
                    print() 
                    print('Q7 In which country is the Wimbledon tennis tournament held? ')
                    time.sleep(2)
                    print('(a) USA')
                    print('(b) Endland')      
                    print('(c) France')
                    print('(d) Australia')
                    print()
                    g=input('enter the option(a,b,c,d)')
                    if g.lower()=='l':
                        print(str(ll))
                        for i in  range(4):
                           opt=int(input('Enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
                           if opt==1 :
                             print('(a)23%,(b)27%,(c)17%,(d)33%')
                             ll.remove(q)
                           if opt==2:
                              print("options 'a' and 'b' remains")
                              ll.remove(y)
                           if opt==4:
                             print('Q7 With which Hindu deity is the ISKCON movement associated')
                             time.sleep(2)
                             print('(a) Ganesha')
                             print('(b) Krishna ')      
                             print('(c) Shiva')
                             print('(d) Brahma')
                             ll.remove(w)
                           if opt==3:
                              print('b is correct option')
                              ll.remove(z)
                           if opt==0:
                            break
                        g=input('enter the option')
                    if a.lower()=='q':
                                print('THANKS FOR PLAYING YOU WON 20,000 ruppes')        
                    if g=='b':
                          print('correct option.you have won 40,000 ruppes')
                          x=input('Continue????')
                          print()    
                          print('EIGHTH QUESTION(80,000)')
                          time.sleep(2)
                          print()
                          print("Q8 In the Mahabharata,who was born with 'kawach' and 'kundala'?")
                          time.sleep(2)
                          print('(a) Arjuna')
                          print('(b) Yudhishthira')      
                          print('(c) Karna')
                          print('(d) Bheeshma')
                          print()
                          H=input('enter the option(a,b,c,d)')
                          if H.lower()=='l':
                             print(str(ll))
                             for i in range(4):
                               opt=int(input('Enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
                               if opt==1 :
                                print('(a)25%,(b)27%,(c)27%,(d)21%')
                                ll.remove(q)
                               if opt==2:
                                        print("options 'c' and 'b' remains")
                                        ll.remove(y)
                               if opt==4:
                                     
                                     print('Q8 WHICH COUNTRY FLAG IS NOT RECTANGLE IN SHAPE ')
                                     time.sleep(2)
                                     print('(a) ENGLAND')
                                     print('(b) BERMUDA TRIANGLE')      
                                     print('(c) NEPAL')
                                     print('(d) ZIMBAWBE')
                                     print()
                                     print()
                                     print()
                                     print()
                                     print()
                                     print()
                                     ll.remove(w)
                                     time.sleep(2)
                               if opt==3:
                                   print('c is correct option')
                                   ll.remove(z)
                               if opt==0:
                                 break
                             H=input('enter the option(a,b,c,d)')
                          if a.lower()=='q':
                                           print('THANKS FOR PLAYING YOU WON 40,000 ruppes')       
                          if H=='c':
                              print('correct option.you have won 80,000 ruppes')
                              x=input('Continue????')
                              print()
                              print('NINTH QUESTION(1,60,000)')
                              time.sleep(2)
                              print()
                              print('Q9 Which title is usally held by the eldest son of the British monarch ')
                              time.sleep(2)
                              print('(a) Duke of Edinburgh')
                              print('(b) Prince of Wales')      
                              print('(c) Grand Prince')
                              print('(d) Duke of York')
                              print()
                              I=input('enter the option(a,b,c,d)')
                              if I.lower()=='l':
                                print(str(ll))
                                for  i in range(4): 
                                 opt=int(input('enter lifeline no.'))
                                 if opt==1 :
                                  print('(a)27%,(b)66%,(c)7%,(d)0%')
                                  ll.remove(q)
                                 if opt==2:
                                   print("options 'a' and 'b' remains")
                                   ll.remove(y)
                                 if opt==4:
                                      print('Q9 Which of these metals is found in both bronze and brass?')
                                      time.sleep(2)
                                      print('(a) Silver')
                                      print('(b) Copper')      
                                      print('(c) Tin')
                                      print('(d) Iron')
                                      ll.remove(w)
                                 if opt==3:
                                     print('b is correct option')
                                     ll.remove(z)
                                 if opt==0:
                                      break
                                I=input('enter the option(a,b,c,d)')
                              if a.lower()=='q':
                                            print('THANKS FOR PLAYING YOU WON 80,000 ruppes')        
                              if I=='b':
                                 print('correct option.you have won 1,60,000 ruppes')
                                 x=input('Continue????')
                                 print()
                                 print('TENTH QUESTION(3,20,000)')
                                 time.sleep(2)
                                 print()
                                 print("Q10 Who is the author of the book 'India Wins Freedom'")
                                 time.sleep(2)
                                 print('(a) Abul Kalam Azad')
                                 print('(b) Mahatma Gandhi')      
                                 print('(c) Rajendra Prasad')
                                 print('(d) S Radhakrishnan')
                                 print()
                                 J=input('enter the option(a,b,c,d)') 
                                 if J.lower()=='l':
                                     print(str(ll))
                                     for i in range(4):
                                      opt=int(input('enter lifeline  no.'))
                                      if opt==1 :
                                          print('(a)66%,(b)27%,(c)7%,(d)0%')
                                          ll.remove(q)
                                      if opt==2:
                                            print("options 'a' and 'b' remains")
                                            ll.remove(y)
                                      if opt==4:
                                           print('Q10 Which chemical compound in tea is responsible for its stimulating effect')
                                           time.sleep(2)
                                           print('(a) Caffine')
                                           print('(b) Carmine')      
                                           print('(c) Nicotine')
                                           print('(d) Tannin')
                                           ll.remove(w)
                                      if opt==3:
                                          print('a is correct option')
                                          ll.remove(z)
                                      if opt==0:
                                           break
                                     J=input('enter the option(a,b,c,d)')
                                 if a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 1,60,000 ruppes')            
                                 if J=='a':
                                      print('correct option.you have won 3,20,000 ruppes')
                                      print()
                                      x=input('Continue????')
                                      print()
                                      print('Now you have unlock KOTI KA CHHOTI KA PRASHAN')
                                      print('Which is our JACKPOT QUESTION')
                                      print()
                                      print()
                                      x=input('Continue????')
                                      print()
                                      print('ELEVENTH QUESTION (6,40,000)')
                                      time.sleep(2)
                                      print()
                                      print("Q11 Which of these countries has never participated in the ICC Cricket World Cup ")
                                      time.sleep(2)
                                      print('(a) Canada ')
                                      print('(b) UAE ')      
                                      print('(c) Holland')
                                      print('(d) Malaysia')
                                      print()
                                      J=input('enter the option(a,b,c,d)') 
                                      if J.lower()=='l':
                                        print(str(ll))
                                        for i in range(4):
                                         opt=int(input('enter lifeline  no.'))
                                         if opt==1 :
                                          print('(a)22%,(b)24%,(c)21%,(d)33%')
                                          ll.remove(q)
                                         if opt==2:
                                            print("options 'd' and 'c' remains")
                                            ll.remove(y)
                                         if opt==4:
                                           print('Q11 Which of these is not a stock market index')
                                           time.sleep(2)
                                           print('(a) Nikkei ')
                                           print('(b) Sensex')      
                                           print('(c) Dow Jones')
                                           print('(d) GATT')
                                           ll.remove(w)
                                         if opt==3:
                                          print('d is correct option')
                                          ll.remove(z)
                                         if opt==0:
                                           break
                                      if a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 3,20,000 ruppes')            
                                      if J=='d':
                                       print('correct option.you have won 6,40,000 ruppes')
                                       print()
                                       x=input('Continue????')
                                       print()
                                       print('TWELVTH QUESTION (12,50,000)')
                                       time.sleep(2)
                                       print()
                                       print("Q12 Which of these actors has not played nine different roles in one film ? ")
                                       time.sleep(2)
                                       print('(a) Sivaji Ganesan ')
                                       print('(b) Sanjeev Kumar ')      
                                       print('(c) Chiranjeevi')
                                       print('(d) A Nageshwar Rao')
                                       print()
                                       J=input('enter the option(a,b,c,d)') 
                                       if J.lower()=='l':
                                        print(str(ll))
                                        for i in range(4):
                                         opt=int(input('enter lifeline  no.'))
                                         if opt==1 :
                                          print('(a)26%,(b)23%,(c)27%,(d)24%')
                                          ll.remove(q)
                                         if opt==2:
                                            print("options 'c' and 'd' remains")
                                            ll.remove(y)
                                         if opt==4:
                                           print('Q12 In hindu tradition,which of these is one of the eight forms of marriage? ')
                                           time.sleep(2)
                                           print('(a) Kalyana')
                                           print('(b) Magha')      
                                           print('(c) Gandharva')
                                           print('(d) Saranga')
                                           ll.remove(w)
                                         if opt==3:
                                          print('c is correct option')
                                          ll.remove(z)
                                         if opt==0:
                                           break
                                        J=input('enter the option(a,b,c,d)')
                                       if a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 6,40,000 ruppes')            
                                       if J=='c':
                                        print('correct option.you have won 12,50,000 ruppes')
                                        print()
                                        x=input('Continue????')
                                        print()
                                        print('THIRTEENTH QUESTION (25,00,000)')
                                        time.sleep(2)
                                        print()
                                        print("Q13 Which Indian president has also been the speaker of the Lok Sabha ")
                                        time.sleep(2)
                                        print('(a) Zail Singh')
                                        print('(b) N Sanjiva Reddy')      
                                        print('(c) S Radhakrishnan')
                                        print('(d) R Venkataraman')
                                        print()
                                        J=input('enter the option(a,b,c,d)') 
                                        if J.lower()=='l':
                                         print(str(ll))
                                         for i in range(4):
                                          opt=int(input('enter lifeline  no.'))
                                          if opt==1 :
                                           print('(a)28%,(b)26%,(c)24%,(d)22%')
                                           ll.remove(q)
                                          if opt==2:
                                            print("options 'c' and 'b' remains")
                                            ll.remove(y)
                                          if opt==4:
                                           print('Q13 Ustad Isa is credited with being the architect of which monument? ')
                                           time.sleep(2)
                                           print('(a) Red Fort')
                                           print('(b) Taj Mahal')      
                                           print('(c) Jama Masjid')
                                           print('(d) Fatehpur Sikri')
                                           ll.remove(w)
                                          if opt==3:
                                           print('Not sure b lag raha hai')
                                           ll.remove(z)
                                          if opt==0:
                                           break
                                         J=input('enter the option(a,b,c,d)')
                                        if a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 12,50,000 ruppes')            
                                        if J=='b':
                                         print('correct option.you have won 25,00,000 ruppes')
                                         print()
                                         x=input('Continue????')
                                         print()
                                         print('FOURTEENTH QUESTION (50,00,000)')
                                         print()
                                         time.sleep(2)
                                         print("Q14 Who was the first unoppposed candidate to be elected VP of india")
                                         print('(a) Zakir Hussain')
                                         print('(b) B D Jatti')      
                                         print('(c) V V Giri')
                                         print('(d) S Radhakrishnan')
                                         print()
                                         if J.lower()=='l':
                                          print(str(ll))
                                          for i in range(4):
                                           opt=int(input('enter lifeline  no.'))
                                           if opt==1 :
                                            print('(a)25%,(b)25%,(c)24%,(d)26%')
                                            ll.remove(q)
                                           if opt==2:
                                            print("options 'c' and 'd' remains")
                                            ll.remove(y)
                                           if opt==4:
                                            print('Q14 In hindi mythology whose son is Bali ')
                                            time.sleep(2)
                                            print('(a) Jambavan')
                                            print('(b) Pavan')      
                                            print('(c) Indra')
                                            print('(d) Shiva')
                                            ll.remove(w)
                                           if opt==3:
                                            print('c is correct option')
                                            ll.remove(z)
                                           if opt==0:
                                            break
                                          J=input('enter the option(a,b,c,d)')
                    
                                         if a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 25,00,000 ruppes')            
                                         if J=='c':
                                          print('correct option.you have won 50,00,000 ruppes')
                                          print()
                                          x=input('Continue????')
                                          print()
                                          print('FIFTEENTH QUESTION (1,00,00,000)')
                                          time.sleep(2)
                                          print()
                                          print("Q15 Which branch of Ayurveda deals with mental disorders")
                                          time.sleep(2)
                                          print('(a) Kaayachikitsa')
                                          print('(b) Bhutavidya')      
                                          print('(c) Vaajikarna')
                                          print('(d) Rasaayana')
                                          print()
                                          J=input('enter the option(a,b,c,d)') 
                                          if J.lower()=='l':
                                           print(str(ll))
                                           for i in range(4):
                                            opt=int(input('enter lifeline  no.'))
                                            if opt==1 :
                                             print('(a)26%,(b)27%,(c)24%,(d)23%')
                                             ll.remove(q)
                                            if opt==2:
                                             print("options 'a' and 'b' remains")
                                             ll.remove(y)
                                            if opt==4:
                                             print('Q15 How many obstacles are there in the 3000m steeplechase athletic event')
                                             time.sleep(2)
                                             print('(a) 16')
                                             print('(b) 35')      
                                             print('(c) 24')
                                             print('(d) 32')
                                             ll.remove(w)
                                            if opt==3:
                                             print('b is correct option')
                                             ll.remove(z)
                                            if opt==0:
                                             break
                                           J=input('enter the option(a,b,c,d)')
                                          if a.lower()=='q':
                                                    print('THANKS FOR PLAYING YOU WON 50,00,000 ruppes')            
                                          if J=='b':
                                           print('correct option.you have won 1,00,00,000 ruppes')
                                           print()
                                           print()
                                           time.sleep(5)
                                           print('Now its time to play our Jackpot question')
                                           print()
                                           print()
                                           print('You can not use any lifeline')
                                           print()
                                           print()
                                           x=input('READY????????')
                                           print()
                                           print()
                                           print('The question is .................')
                                           print()
                                           print()
                                           print('Last question(7,00,00,000)')
                                           time.sleep(2)
                                           print()
                                           print('Q16 Who was the first women to produce a Hindi film, in which she also acted?')
                                           time.sleep(2)
                                           print('(a) Fatima Begum')
                                           print('(b) Kamla Bai')
                                           print('(c) Nasreen')
                                           print('(d) Zubeida')
                                           w=input('enter the option')
                                           if w=='':
                                               print('7 crore!!!!!!!!!!!!!!!!!!!')
                                               print()
                                               print('CONGRATULATION!!!!!!! YOU HAVE WON THE MONEY 7 crore PAISE')
                                               print('THANK YOU FOR PLAYING MY KBC')
                                           else:
                                               print('INCORRECT ANSWER!!!!!!!!!')
                                               print('you are disqualified,3,20,000 ruppes')
                                               
                                          if J=='a' or J=='c' or J=='d':
                                           print('INCORRECT ANSWER!!!!!!!!!!!')
                                           print('you are disqualified,3,20,000 ruppes')    
      
                                         if J=='b' or J=='a' or J=='d':
                                          print('INCORRECT ANSWER!!!!!!!!!!!')
                                          print('you are disqualified,3,20,000 ruppes')    
     
                                        if J=='a' or J=='c' or J=='d':
                                         print('INCORRECT ANSWER!!!!!!!!!!!')
                                         print('you are disqualified,3,20,000 ruppes')    
    
                                       if J=='b' or J=='a' or J=='d':
                                        print('INCORRECT ANSWER!!!!!!!!!!!')
                                        print('you are disqualified,3,20,000 ruppes')    
   
                                      if J=='b' or J=='c' or J=='a':
                                       print('INCORRECT ANSWER!!!!!!!!!!!')
                                       print('you are disqualified,3,20,000 ruppes')    
 
                                 if J=='b' or J=='c' or J=='d':
                                       print('INCORRECT ANSWER!!!!!!!!!!!')
                                       print('you are disqualified,10,000 ruppes')    

                              if I=='a' or I=='c' or I=='d':
                                 print('INCORRECT ANSWER!!!!!!!!!!!')
                                 print('you are disqualified,10,000 ruppes')    

                          if H=='a' or H=='b' or H=='d':
                            print('INCORRECT ANSWER!!!!!!!!!!!')
                            print('you are disqualified,10,000 ruppes')    

                    if g=='a' or g=='c' or g=='d':
                      print('INCORRECT ANSWER!!!!!!!!!!!')
                      print('you are disqualified,10,000 ruppes')    

                  if f=='a' or f=='c' or f=='d':
                     print('INCORRECT ANSWER!!!!!!!!!!!')
                     print('you are disqualified,10,000 ruppes')    

               if e=='a' or e=='c' or e=='b':
                   print('INCORRECT ANSWER!!!!!!!!!!!')
                   print('you are disqualified,0 ruppes')    

            if d=='a' or d=='c' or d=='d':
                print('INCORRECT ANSWER!!!!!!!!!!!')
                print('you are disqualified,0 ruppes')    

        if c=='a' or c=='b' or c=='d':
            print('INCORRECT ANSWER!!!!!!!!!!!')
            print('you are disqualified,0 ruppes')    
    if b=='a' or b=='c' or b=='d':
        print('INCORRECT ANSWER!!!!!!!!!!!')
        print('you are disqualified, 0 ruppes')    
if a=='a' or a=='c' or a=='d':
    print('INCORRECT ANSWER!!!!!!!!!!!')
    print('you are disqualified, 0 ruppes')
    
      
      

