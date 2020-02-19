characters=input("enter the sequence")
characters=characters.upper()

if characters.count("A") + characters.count("U") + characters.count("G") + characters.count("C") == len(characters):   
    print("this sequence is RNA")
elif characters.count("A") + characters.count("T") + characters.count("G") + characters.count("C") == len(characters):   
    print("this sequence is DNA") 
elif characters.count("A") + characters.count("T") + characters.count("G") + characters.count("C") != len(characters):
    print ("this is a protein sequence")

