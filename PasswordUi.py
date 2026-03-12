import customtkinter as ctk
import random
import string
import json 
import os 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCIEZKA_PLIKU = os.path.join(BASE_DIR, "passwords.json")

#Ustawiam Styl generatora
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Konfiguracja okna
        self.title("Password Generator")
        self.geometry("400x400")

        #Zakldaki
        self.tabview = ctk.CTkTabview(self, width=400, height=400)
        self.tabview.pack(pady=10)
        self.tabview.add("Generator")
        self.tabview.add("Wygenerowane")


        #---- Zakładka: Generator -----

        self.polehasla = ctk.CTkLabel(self.tabview.tab("Generator"), text="Podaj długość hasła:")
        self.polehasla.pack(pady=10)

        self.entry = ctk.CTkEntry(self.tabview.tab("Generator"), placeholder_text="Podaj długość hasła", width=200)
        self.entry.pack(pady=10)

        self.button_add = ctk.CTkButton(self.tabview.tab("Generator"), text="GENERUJ HASŁO", command=self.generuj_haslo, cursor="hand2")
        self.button_add.pack(pady=10)
    #----Hasła do wyboru ------

        self.wybierz = ctk.CTkTextbox(self.tabview.tab("Generator"), width=200, height=200, state ="disabled")
        self.wybierz.pack(pady=10)

        #Kolor tagów
        self.wybierz.tag_config("active_line", background="red", foreground="white")
        self.wybierz.bind("<Button-1>", self.podswielt_wybor)
        

        self.button_add2 = ctk.CTkButton(self.tabview.tab("Generator"), text = "ZAPISZ WYBRANE HASŁA", command=self.zapisz_hasla, cursor="hand2")
        self.button_add2.pack(pady=10)
        #---- Zakładka: Wygenerowane -----
        self.wygenerowane = ctk.CTkLabel(self.tabview.tab("Wygenerowane"), text="Wygenerowane hasło:")
        self.wygenerowane.pack(pady=10)
        self.textbox = ctk.CTkTextbox(self.tabview.tab("Wygenerowane"), width=300, height=400, font=("Arial", 16), state ="disabled")
        self.textbox.pack(pady=10)

        

        self.button_delete = ctk.CTkButton(self.tabview.tab("Wygenerowane"), text="USUŃ HASŁO", command=self.usun_haslo, cursor="hand2")
        self.button_delete.pack(pady=10)
        #-----Pzycissk Zapisu na dole -----

        self.button_save = ctk.CTkButton(self, text="ZAPISZ I WYJDŹ ", command=self.save_quit, cursor="hand2")
        self.button_save.pack(pady=10)
        
              
        try:
            with open(SCIEZKA_PLIKU, "r", encoding="utf-8") as plik:

                data = json.load(plik)

                for tekst in data:
                    self.textbox.configure(state="normal")
                    self.textbox.insert("end", tekst + "\n")
                    self.textbox.configure(state="disabled")

        except FileNotFoundError:
            pass

        self.protocol("WM_DELETE_WINDOW", self.save_quit)

    def generuj_haslo(self):
        try:
            dlugosc = int(self.entry.get())
            znaki = string.ascii_letters + string.digits + string.punctuation  

            
            #Petla While
            for i in range(5):
                
                haslo = ""
                for i in range(dlugosc):
                    haslo += random.choice(znaki)

                    

                self.wybierz.configure (state="normal")
                self.wybierz.insert("end", f"{haslo}\n")
                self.wybierz.configure(state="disabled")
                self.wygenerowane.configure(text=f" Wygenerowane hasło: {haslo}")
                self.entry.delete(0, "end")


        except ValueError:
            self.wygenerowane.configure(text="Podaj liczbę całkowitą")

    def zapisz_hasla(self):
        #Wybieram haslo lub hasla do zapisania
        wybrane = self.wybierz.get("insert linestart", "insert lineend").strip()


        if wybrane: #Sprawdzam pustą linie
            self.textbox.configure(state="normal")


            if wybrane not in self.textbox.get("1.0", "end"):
                self.textbox.insert("end", f"{wybrane}\n")


                #Usuwam jedno haslo z listy wyboru

                self.wybierz.configure(state='normal')
                self.wybierz.delete("insert linestart", "insert lineend + 1c" )
                

                self.wygenerowane.configure(text=f" Wybrane hasło: {wybrane}")

        self.wybierz.configure(state='disabled')
        self.textbox.configure(state="disabled")

    def podswielt_wybor(self, even=None):
        
        self.after(10, self._wykonaj_malowanie)


    def usun_haslo(self):
        try:
            self.textbox.configure(state="normal")
            wybrane = self.textbox.get("insert linestart", "insert lineend").strip()

            if not wybrane:
                print("Nic nie zaznaczono")
                return
            
            
            tresc = self.textbox.get("1.0", "end")
            #Usuwamy zaznaczenie
            nowa_tresc = tresc.replace(wybrane, "")

            self.textbox.delete("1.0", "end")
            self.textbox.insert("1.0", nowa_tresc.strip())
            
            print(f"Usunieto : {wybrane}")  
            self.textbox.configure(state="disabled")
        
        except :
            print("Nic nie zaznaczono")
        

    def _wykonaj_malowanie(self):
       #Czyscimy stare podswietlenie okna
        self.wybierz.configure(state="normal")
        self.wybierz.tag_remove("active_line", "1.0", "end")
        self.wybierz.tag_add("active_line", "insert linestart", "insert lineend +1c")
        self.wybierz.configure(state="disabled")

    def save_quit(self):
        linie = self.textbox.get("1.0", "end-1c").splitlines()

        

        

        with open(SCIEZKA_PLIKU, "w", encoding="utf-8") as plik:
            json.dump(linie, plik, indent=4, ensure_ascii=False)

        self.destroy()

    


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()