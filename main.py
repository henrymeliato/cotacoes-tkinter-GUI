from tkinter import *
import requests

main = Tk()

class Application():
    def __init__(self):
        self.main = main
        self.tela()
        self.frames_tela()
        self.botoes()
        main.mainloop()
        self.cotacoes()
        self.main.mainloop()

    def cotacoes(self):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        requisicao_dic = requisicao.json()

        dolar = requisicao_dic['USDBRL']['bid']
        euro = requisicao_dic['EURBRL']['bid']
        btc = requisicao_dic['BTCBRL']['bid']

        texto=f'''
        DOLÁR: {dolar}
        EURO: {euro}
        BTC: {btc}
        '''

        self.lb_cotacao.config(text=texto)
    
    def tela(self):
        self.main.title("Cotações de Moedas")
        self.main.configure(background= 'darkblue')
        self.main.geometry("500x500")
        self.main.resizable(False, False)
    def frames_tela(self):
        self.frame_1 = Frame(self.main, bd=4, highlightbackground='black')
        self.frame_1.place(relx=0.1 , rely=0.1, relwidth=0.8, relheight=0.8)

    def botoes(self):
        self.bt_sair = Button(self.frame_1, text="Sair", command=self.main.quit)
        self.bt_sair.place(relx=0.85, rely=0.78, relwidth=0.1, relheight=0.12)

        self.lb_cotacao = Label(self.frame_1, text="Cotações de moedas")
        self.lb_cotacao.place(relx=0.35, rely=0.1)

        self.lb_moedas_opcao = Button(self.frame_1, text="BUSCAR COTAÇÕES", command=self.cotacoes)
        self.lb_moedas_opcao.place(relx=0.35, rely=0.3)

    
Application()
