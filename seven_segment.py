def seven_segment_display():

    number = int(input("Enter the number : "))

    if  10 > number > 0:
        hex_dict = {1:0x7E, 2:0x6D, 3:0x79, 4:0x33,5:0x5B, 6:0x5F, 7:0x70, 8:0x7F, 9:0x7B}

        binary_display =  bin(hex_dict[number])[2:].zfill(7)

        a,b,c,d,e,f,g = map(int,list(binary_display))

        print(("*" if a else " ")*8)
        print("*" if f else " ", " "*4,"*" if b else " " )
        print("*" if f else " ", " "*4,"*" if b else " " )
        print(("*" if f else " ")*8)
        print("*" if e else " ", " "*4,"*" if c else " " )
        print(("*" if d else " ")*8)
    else:
        raise  Exception("This number cannot show in seven segments. Number must be between 0-10(Not included) ")

  



seven_segment_display()



