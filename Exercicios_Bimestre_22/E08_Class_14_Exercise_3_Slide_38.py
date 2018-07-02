# 8 CRIAR EXEMPLO QUE ILUSTRE O PADRAO COMPOSITO
# Playlist Spotify

class Minhas_Musicas():
    def __init__(self, *lista_de_musicas):
        pass

    def escutar_musicas(self):
        pass

class Heavy_Metal(Minhas_Musicas):
    def __init__(self, *lista_de_musicas):
        self.lista_de_musicas = lista_de_musicas

    def escutar_musicas(self):
        print("Algumas musicas de METAL:")
        for arg in self.lista_de_musicas:
            print(arg)

class Hard_Rock(Minhas_Musicas):
    def __init__(self, *lista_de_musicas):
        self.lista_de_musicas = lista_de_musicas

    def escutar_musicas(self):
        print("Algumas musicas de HARD ROCK:")
        for arg in self.lista_de_musicas:
            print(arg)

class Minha_Playlist(Minhas_Musicas):
    def __init__(self):
        self.playlist = []

    def escutar_musicas(self):
        print("Playlist completa:")
        for algumas_musicas in self.playlist:
            for musicas in algumas_musicas:
                print(musicas)

    def adicionar_musicas(self, algumas_musicas):
        self.playlist.append(algumas_musicas.lista_de_musicas)

    def remover_musicas(self, algumas_musicas):
        self.playlist.remove(algumas_musicas.lista_de_musicas)

    def excluir_todas_as_musicas(self):
        print("Vamos fazer outra playlist?")
        self.playlist = []

def main():
    metal_songs_1 = ["War Pigs", "Seek and Destroy", "The Trooper"]
    metal_songs_2 = ["Raining Blood", "Peace Sells", "Walk"]
    hardrock_songs = ["Hot for Teacher", "Highway Star", "Loving you Sunday Morning"]

    print("Vamos escutar algumas musicas")

    metal_1 = Heavy_Metal(metal_songs_1)
    metal_1.escutar_musicas()

    metal_2 = Heavy_Metal(metal_songs_2)
    metal_2.escutar_musicas()

    hardrock = Hard_Rock(hardrock_songs)
    hardrock.escutar_musicas()

    print("Gostei, vou fazer uma playlist de rock com algumas delas")

    rock_playlist = Minha_Playlist()

    rock_playlist.adicionar_musicas(metal_1)
    rock_playlist.adicionar_musicas(hardrock)
    rock_playlist.escutar_musicas()

    rock_playlist.adicionar_musicas(metal_2)
    rock_playlist.escutar_musicas()

    rock_playlist.remover_musicas(metal_1)
    rock_playlist.escutar_musicas()

    rock_playlist.excluir_todas_as_musicas()

main()