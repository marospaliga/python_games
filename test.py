import algoplay as play

#vytvorenie postavičky vo forme kruhu
player = play.new_text(
    words= "Maj sa dobre",
    color = "lightblue", #farba postavičky
    x = 0, #x-ová súradnica postavičky
    y = -100 ) #y-ová súradnica postavičky

player2 = play.new_text(
    words= "AHOJ",
    color = "red",
    x = 0,
    y = 100 )

@play.when_key_pressed('p', 'r')
def zmenafarby(key):
    if key == "p":
        player2.color = "pink"
    if key == "r":    
        player2.color = "red"



play.start_program()