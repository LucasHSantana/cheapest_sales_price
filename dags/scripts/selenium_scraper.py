from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
PLUGINS_DIR = os.path.join(BASE_DIR, 'plugins')
WEBDRIVERS_DIR = os.path.join(PLUGINS_DIR, 'webdrivers')

# Classe pai para webscraping usando selenium
class Scraper():
    def __init__(self, navegador, url=''):
        self._navegador = navegador
        self._url = url

        # Configura o webdriver correto para o navegador
        if self._navegador == 'edge':
            # options = webdriver.EdgeOptions()
            # options.add_argument("--headless")

            driver_exe = os.path.join(WEBDRIVERS_DIR, 'msedgedriver.exe')            
            # self._driver = webdriver.Edge(service=Service(executable_path=driver_exe), options=options)
            self._driver = webdriver.Edge(service=Service(executable_path=driver_exe))            
        else:
            print('navegador não implementado!')

    # Abre o navegador com a url informada
    def abrir_site(self, url=''):
        if url:
            self._url = url

        if not self._url:            
            raise ValueError('URL não informada!')        

        self._driver.maximize_window() # Maximiza a janela (Evita erros devido a mudança de layout no site)
        self._driver.get(self._url) # Abre o site

    # Fecha o navegador
    def close(self):
        self._driver.close()

    # Fecha o navegador e finaliza o serviço
    def quit(self):
        self._driver.quit()

if __name__ == '__main__':    
    scraper = Scraper('edge', 'https://www.google.com')
    scraper.abrir_site()