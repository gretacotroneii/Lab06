import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    #Gestisce l'evento del pulsante "Mostra": funzione per leggere tutti gli strumenti
    def mostra_strumenti(self,e):
        self._view.lista_strumenti.controls.clear()   #pulisce la lista precedente per evitare i duplicati
        strumenti=self._model.get_strumenti()   #ottengo la lista degli strumenti da model
        if strumenti is None:
            self._view.show_alert('Nessuno strumento trovato nel database')
            return
        # cosi prende l'oggetto strumento e lo converte in stringa di testo leggibile e popola la ListView con i risultati
        for s in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(str(s)))
        self._view.update()

    #Gestisce l'evento del pulsante "Cerca", ovvero cerca gli strumenti per tipo cercato
    def cerca_strumenti_per_tipo(self,e):
        #recupero il valore scritto dall'utente e rimuove gli spazi bianchi
        tipo_cercato=self._view.input_tipo_strumento.value.strip()
        if tipo_cercato is None:
            self._view.show_alert('Nessun tipo di strumento valido trovato')
            return

        #pulisco la lista grafica precedente per evitare i duplicati
        self._view.lista_strumenti_ricerca.controls.clear()

        strumenti=self._model.cerca_strumenti_per_tipo(tipo_cercato)
        if strumenti is None:
            self._view.show_alert('Nessun strumento trovato nel database')
            return

        for s in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))

        self._view.update()




