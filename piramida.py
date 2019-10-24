while True:
    a= float(input ("Скільки років будують піраміду '1-6'? :"))

    from colorama import init
    from colorama import Fore, Back, Style
    init()

    if a ==6 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % ('#', '#'))
        print ('%10s %1s' % ('##', '##'))
        print ('%10s %1s' % ('###', '###'))
        print ('%10s %1s' % ('####', '####'))
        print ('%10s %1s' % ('#####', '#####'))
        print ('%10s %1s' % ('######', '######'))
    

    if a ==5 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % (' ', ' '))
        print ('%10s %1s' % ('##', '##'))
        print ('%10s %1s' % ('###', '###'))
        print ('%10s %1s' % ('####', '####'))
        print ('%10s %1s' % ('#####', '#####'))
        print ('%10s %1s' % ('######', '######'))

    if a ==4 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % (' ', ' '))
        print ('%10s %1s' % ('  ', '  '))    
        print ('%10s %1s' % ('###', '###'))
        print ('%10s %1s' % ('####', '####'))
        print ('%10s %1s' % ('#####', '#####'))
        print ('%10s %1s' % ('######', '######'))

    if a ==3 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % (' ', ' '))
        print ('%10s %1s' % ('  ', '  '))    
        print ('%10s %1s' % ('   ', '   '))    
        print ('%10s %1s' % ('####', '####'))
        print ('%10s %1s' % ('#####', '#####'))
        print ('%10s %1s' % ('######', '######'))

    if a ==2 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % (' ', ' '))
        print ('%10s %1s' % ('  ', '  '))    
        print ('%10s %1s' % ('   ', '   '))    
        print ('%10s %1s' % ('    ', '    '))
        print ('%10s %1s' % ('#####', '#####'))
        print ('%10s %1s' % ('######', '######'))

    if a ==1 :
        print ( Fore.YELLOW )
        print ('%10s %1s' % (' ', ' '))
        print ('%10s %1s' % ('  ', '  '))    
        print ('%10s %1s' % ('   ', '   '))    
        print ('%10s %1s' % ('    ', '    '))
        print ('%10s %1s' % ('     ', '    '))    
        print ('%10s %1s' % ('######', '######'))
        


