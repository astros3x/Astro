import os
import ctypes
import webbrowser
import tkinter as tk
from pystyle import *



#settings
def cls():
      os.system('cls' if os.name=='nt' else 'clear')

def settings():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW('Astro - vBETA | Coded by 2Loop#6969')

def light():
      os.system('color f0')
      astro()

def dark():
      os.system('color 4')
      astro()

def quitastro():
      cls()
      raise SystemExit



#ascii menu
asciibyme = (Colorate.Vertical(Colors.red_to_purple,'''                                                                                                                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                                                  
                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                                                            ▄▄█:~?Y555JJ?!~^.█▄                                                
                  █.:^~~!!7???JJ?!^.██                                                                      ▄▄▄▄!JYJ7~^:.  ..:::::..                                               
                  █.:::..░░   ..^~7JYJ~▄                                                                    █:~!^.░░  .^7??7!~^:...█░                          ▄▄▄        ██████ ▄▄▄█████▓ ██▀███   ▒█████                       
                █..:^^~!7??!^░      ^77:█▄                                                               ▄▄.  ░░░.!5PY!:.█▄▄▄  ░                              ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒                       
                █.▄^7YG57:░     :.        ▄▄▄                                                            █:.:7^..:!5&@@#BG5?~:█▄▄▄^!7!:█                      ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒                       
                    █.^7YPBB&@@&BJ^   .!: :█                                                            ▄?. !5P#@@#Y?P&5^.  .~YB&P555Y7.█                     ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░                     
              █~?YJ~: .~!~^!P&#?~!?P#BGP5!  ?▄                                                          █!Y   ~B@5~.:?5J?JJ5G&@@@#:   .!?!.█                ░   ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ | vBETA                     
            █!GBG5P@&GY7^:...^!77!~^~7G#?.  7J█                                                        ▄█^#~.7B&5^^?B&P7!!~~!77JY5GG5?~:  :~:█                  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░                                          
          █.JY~.  !@@@@@@#BGGPGGGB###B5YPG5~.P?█                                                     ▄ ^##Y#&J..7PGGBG5J7~~^^^:::::^!!777!^^.█▄                  ▒   ▒▒ ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░                     
        █:?^ ░.!P&BPJ7~^:....    .~~7B@#PP#BP@J█                                    ^^.            █7&@@#577J55YJJ?7!7?JY5PGBBBPJ7~^. ▒.:^^~^:..▄             ░     ░  ░      ░              ░         ░ ░                    
        █:░.!J5Y!^:.::^^~~~~~!!777?JY5PPPY!P@@@G~█                        :^^::~7^  .GJ         ▄▄▄^P@@@#GPP5?~.░░.^?PGPB@@@@BJ^:.█  ▒▒░░░  ▒░...`^¬.               ░░              ░      ░░░          ░░   
        █.^!7!░ ░░░.:^~!7YGBBGP5Y?!~!?Y55YJ?7G@@@@G7.█▄▄▄▄▄▄▄▄..       :^JJ!Y@@G:^#Y:7@^  ▄▄▄▄▄▄:7G@@@#P5PGYJYBP: 7G&@?. !@&7 ▒▒▒      ░    ░░    ▒ ▒         ░     ░[Best of github░| Coded by░2Loop#6969]░                     
    █.^~^:░░    ░ ░ ░▒ ░ :7B@@@BB&BJ: ^JPGBGGB&@@@@&GY?7!!!!~^.  .^!?55JP@@&#GY^?@@&&G. .^~!7?YP#&#GJ!!YB&#7^.P@~.BPYJ?!^J@?█▒░ ░    ░    ░      ░ ░                ░             ░         ░░           ░
    █.:.░ ░▒  ░  ░   ░  ░   .#@! ^BGY^Y#J!!J&#BP?!!?JJYJ?7~^.█  .^~!7J&@@@@?~7JG@@@@#5J5:  .:^^~7J5PPPPGGGPPPPGP~ P@GJJJY5B@7█    ░                  ░                                       ░ 
    ░░░░ ░      ░          █.#@PYYY5Y P&!.~?PPPP55PGPB&&&#BGGY: :^~!!75&@@@J:░░:!G@@@@B#~ :.   YG5YP&@BJJY5PB##PJ!~!?Y5Y7::G#!▄          ░                                              
    ▒  ░                  █:B&?:!?Y#@J 7G#BBBG5Y?~~:?&@P!^::J@█     :5@@#J?YPP^ :J&@@@&&&B5.?..GJ...:J&P.:░░.~:~Y@&G5J?7?YY5&@P~█                       ░            ░                                        ░
        ░    ░           █7#G!7YPP5YY55PG&@P~.:! :^7@#~  .^!7~█    .5B@@?^!..B7 !~#@GP#Y5@&B7   ^~:.  !@G^7 ░~?!7&5:~?5GPJ!~7P&@G!.▄          ░               [00] Quit░                    
                      █~G@@GPY??JP##57~.?&Y7?J:.Y~&@~█            :^5@@&J:.^^   ^@@Y ?@^55~          █P@~P^ ░.~~^:  .^75&@#Y!^!P&#?:▄                ░        [01] Info ░░░           ░       
      ░              █!B@&P?7JP#&#GPY7~.  :77^  57Y@#█              !PYB&BPJ7.   .YB@P░5G~            █5@~5Y░░!:^?^:!~^!7?JYG##Y~:7G#5~█                      [02] Light░theme                     
                  █7B@P7~?G#GJ7!7YP░..:..:.!~ .#~P@#.█   .^.    .  7@G?!?G!.?~  :~!J^  ~YJ          ▄.B@^BP 5GJ&7▒░~P&BY7^:.:7G@B7.^Y#G!▄                     [03] Dark theme                    
                █7B#J^~P@@&5?░░░░!5@&G?. !P~5Y:@J7@@J█ :77:   :!.  :#@GGP7~ Y@G~         !          █Y@P~@#G@@&BP5J!^75GPPGGGPP#@@&Y:.?#G!▄▄           ░      [04] AstriV2 - Best Multitool░                    
              █^G#?:7B@#PJ?7777??JJJ!:.~?P@&B@G@B.P@@JJ5!    ^P:  ..^J  7@7 ^J&@J                  █Y@#:J@@@P~.░░░.^~~^.:^^:....^!JG#P~.7BG~█▄▄               [05] Discord                ░░ 
              █J#J:7GP?:░░░░░    ░ ░  .~!~^^^~JG@@@7~&@@B:   ░:&?^5BBG5!.~7@Y .Y?#@! :^^:        ..▄:P@G~.7@@G░ ░ ▒  ░░▒.: ░  ░░▒░▒ ░░.!YY^.?B5.█            ░[06] MassReport TikTok                     
            █.PP:^Y?:░▒░░   ░   ░   .:.░▒░   ░ ~#@@#5J&@#?.░░5@G@&7.░.!~~P##J?#YP@#G57^.▄▄▄▄▄▄^!:.?#@5!#&!G@P  ░   ░▒  ░     ░  ░  ░ ░▒ .!!..YB~█▄▄▄         ░[07] MassReport Insta                        
░           █^G? :~.░░░  ░            ░░        ░░░~@&^~?!J#@&Y!&@@@~ ~7!. ▒▒ ^?Y55G@@&!:!J?7~:  YJ^?B@@Y:#5G&!#@~          ░  ░     ░░░░░░ ░:. ~GY█         ░[08] TokenGrabber + RAT                     
          █^G~░░▒░ ░           ░     ░          ░░B@^#@#?.7G@@@@@@?B&55G:░░▒:5@@@@@7?@#!:..:.5@B#PG@Y :? ~@~:B&!█                     ░    ░ ▒▒.YP.█          [09] DiscordNuker                     
        █:P^░  ░    ░      ░                   ▄##.5:7@:  :?G&@@@@[Ascii by 2Loop#6969]7 Y@#J?JY5G@@Y.^^#~^!B@5^█▄▄▄                         ░ !5:█▄          [10] Remote Access AdvancedTool░                  
        █Y~▒   ░                              ▄7@7 ^!B&?77!~~~?5B&@P~.:G..7J7~^.@@.5@@#PJ!~G@5 Y@~:?P@@#GPPPPGB#P?:█          ░░              ░▒ :J:          [11] Batch Obfscator                    
        █~^▒                      ░          ▄▄!@&YPBBPYYJJJY5PP5555PGBB@G5?~:▒▒░.?B&G5YYY55PB#P&@B&BY!^.░░░░░░░.~?YJ!.                        ░ ░ :!.░       [12] Rubber Ducky Repo                      
      █.^░                               ▄▄▄^Y&BY?~:░    .~: ░..^?##B&P7^ ▒▒░▒.?G@@#5?~:. ^ ▒:!5P?^  ▒░░  ▒░░   ▒░░:!7~.               ░      ░   ░.^▒░   ░   [13] FlipperZero Base                    
      ░█.~░  ▒            ░              ▄.^7J7:░░░ ░  ::. :P7░ ^JB&G7.▒▒▒░░:!~.Y@#?^:~^!: ▒░░░░░  ░ ░   ░  ░       ░░:~^.                        `^¬..▒      [14] Best░discord RAT                     
                                      ▄.^^^.░ ░   ░░ 5BPB!░J@JP@#J: ^:.:::..::   ~BG5JJ?!.▒░    ░░       ░░         ░ ░ ..                        ░    ░░     [15] BuildYourTokenGrabber(BETA)░                  
                                      ░░░░░  ░      ^#: PG B@@#!.:!7JPPJJ?!^..░  ▒.^^^:  ░     ░ ░        ░          ░          ░                      ░ ░    [16] Best discord Token Grabber         ░
                                      ░  ░          .5:^#~?@@5~JP5YYP55#^             ░▒░        ▒                    ░                              ░   ░                         
                                    ░               :~BP^&@#G&Y75&&! .&7              ░░                  ░                                                                       
                                                  : ░~@~Y@@@&~7&BG&GPB5.  ░      ░                                                                                                
          ░        ░                              ^J~~@~5@@@?^@B.░:~77:                              ░                                                                            
                                  ░                :YB@G~#@@!!@P░░.Y#J:                                       ░░                                                                  
                                                      ~5@B7P&#~Y@5:?@#G&Y                                                                                                          
                                                        :?PYJ5P77G&#@P ^#?                                                                                                         
                                                          ▒:~!77!^!#@@P..P~                       ░                                                                                
                                                          ▒░   .::░J@7G&~.7^░                                                                                                      
                                                              .~ ░:GJ .##: ..:^.                                                                                          ░       
                          ░                                ▒░J.▒.7^ ▒ J@!░ ~@&5?:                                                                                                 
                                                            ^G.▒   ░░:B#:.~^?#?^!:.                                                                                               
                                                            :@B7^^~75@B^ ░:G5~Y?                                                                                                  
                                                              Y@@@@@@@Y.░7PG#@&7?7▒                               ░                                                                
                                                              7#@@@@5 ▒^@G::?&@J!.                                                     ░                                          
                                                                .7P&@&!▒░JB?: ^&@!▒▒     ░                                                                   ░                    
                                                                  :~?5J!:^^^. Y@P                                                                                                 
                                                                      ░▒:~~^:~B@P                                                                                                 
                                                          ^YG#BBP?^ ░░.Y#GGB@@@@?                                                ░                                                
                                                          ^@@57~~7P#P~ .&&: .B@@#:                                                                                                 
                                                          :##. ^!!:.J#5^:5BJ!&@P:                                                                                                  
                  ░                                       .??YG75&J :YBPJG@@&P:                                                                                                   
                                                            .PJ.  Y@~░ .^!!~^:~7!^.                                                                                                
                                                            ~&P?JYP@Y            .:.                                                                                               
                                                            :~~^::!Y                                                                                                              
                                                        `^¬...:                        [astro@input] > ''', 2))



#info window
def info(infoastro):
    class App(tk.Frame):
        def __init__(fin, hit=None):
            super().__init__(hit)
            fin.pack()
            fin.copyframe(infoastro)
        def copyframe(fin, creditss):
            frame = tk.Frame(fin)
            frame.pack(padx=10, pady=10)
            text = tk.Text(frame, height=5, width=45)
            text.insert(tk.END, creditss)
            text.config(state=tk.DISABLED)
            text.pack(side=tk.LEFT)
    window = tk.Tk()
    window.geometry('350x100')
    window.title('Astro - vBETA | Info')
    estra = App(hit=window)
    astro()
    estra.mainloop()
    return estra



#menu input
def astro():
    settings()
    while True:
        iinput = input(asciibyme)
        try:
            iinput = int(iinput)
            break
        except (ValueError, TypeError, NameError):
            astro()
    if iinput == 0:
          quitastro()
    elif iinput == 1:
          #info content
          info('This program was written by 2Loop#6969.\n I created it inspired by some previous old programs.\n  Contains many repositories (all credits go to their creators).\n  I hope it can be useful.')
    elif iinput == 2:
          light()
    elif iinput == 3:
          dark()
    elif iinput == 4:
          webbrowser.open('https://discord.gg/XnRjFmgPYz')
          astro()
    elif iinput == 5:
          webbrowser.open('https://discord.gg/XnRjFmgPYz')
          astro()
    elif iinput == 6:
          webbrowser.open('https://github.com/Lorenzik/TMRB')
          astro()
    elif iinput == 7:
           webbrowser.open('https://github.com/Khanejo/Instagram-mass-reporter')
           astro()
    elif iinput == 8:
          webbrowser.open('https://github.com/ilylunar/Oracle-Rat-Grabber')
          astro()
    elif iinput == 9:
          webbrowser.open('https://github.com/KDot227/hazard-nuker-mirror')
          astro()
    elif iinput == 10:
          webbrowser.open('https://github.com/quasar/Quasar')
          astro()
    elif iinput == 11:
          webbrowser.open('https://github.com/KDot227/Somalifuscator')
          astro()
    elif iinput == 12:
          webbrowser.open('https://github.com/hak5/usbrubberducky-payloads')
          astro()
    elif iinput == 13:
          webbrowser.open('https://github.com/UberGuidoZ/Flipper')
          astro()
    elif iinput == 14:
          webbrowser.open('https://github.com/3ct0s/disctopia-c2')
          astro()
    elif iinput == 15:
          webbrowser.open('https://github.com/CaptainBeluga/BYTG')
          astro()
    elif iinput == 16:
          webbrowser.open('https://github.com/addi00000/empyrean')
          astro()
    else:
        astro()


#69
if __name__ == '__main__':
     astro()