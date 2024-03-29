import time

from pylibTMSU.CarregarXMLConexao import CarregarXMLConexao, banco_dados
from pylibTMSU.CarregaXMLCadJustBloqueio import CarregarXMLCadJustBloqueio
from pylibTMSU.InicializarAmbiente import driver, wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# Constantes criadas
DRIVER = driver
WAIT = wait


class GerarJusBloqSubContratada:

    def __init__(self):

        # variaveis de chamada de classe
        conec = CarregarXMLConexao()
        just = CarregarXMLCadJustBloqueio()
        self.link = banco_dados()
        self.url = conec.url_ambiente()
        self.descricao = just.descricao
        self.complemento = just.complemento
        self.excluido = just.excluido

    def carrega_tela_justi_bloq_sub(self):

        try:
            # Acessa a tela Justificativa de bloqueio subcontratada
            # Acesso para tela de Justificativa de bloqueio subcontratada atraves do link
            url = f'{self.url}/Femsa.Zeus/JustificativaBloqueioSubcontratada?cod=705{self.link} '
            DRIVER.get(url)
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao tentar Acesso para tela de Justificativa de bloqueio subcontratada atraves do link'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Justificativa'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'Justificativa'))).send_keys(self.descricao)
        except Exception as e:
            print(f'Erro ao tentar inserir justificativa'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            if self.complemento == '' or self.complemento != 'N':
                pass
            else:
                complemento_obr = DRIVER.find_element(By.XPATH, '//*[@id="frm"]/div/div[2]/label/span')
                DRIVER.execute_script("arguments[0].click();", complemento_obr)
                time.sleep(0.3)
        except Exception as e:
            print(f'Erro ao selecionar "Complemento Obrigatorio"'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            if self.excluido == '' or self.excluido != 'N':
                pass
            else:
                excluido = DRIVER.find_element(By.XPATH, '//*[@id="frm"]/div/div[3]/label/span')
                DRIVER.execute_script("arguments[0].click();", excluido)
                time.sleep(0.3)
        except Exception as e:
            print(f'Erro ao selecionar "Excluido"'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')

        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnSalvar'))).click()
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao clicar no botão Salvar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnConfirmarAcao'))).click()
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao clicar no botão de confirmação'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')


    def consultar(self):
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'btnConsultar'))).click()
            time.sleep(0.5)
        except Exception as e:
            print(f'Erro ao clicar no botão Consultar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')
        try:
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaValue_1'))).click()
            time.sleep(0.5)
            WAIT.until(ec.element_to_be_clickable(
                (By.ID, 'ContainerConsultaValue_1'))).send_keys(self.descricao)
            time.sleep(0.2)
            WAIT.until(ec.element_to_be_clickable((By.ID, 'ContainerConsultaSearch_1'))).click()
        except Exception as e:
            print(f'Erro ao Consultar'
                  f'\nOcorreu algo inesperdado -----> {str(e.__doc__)}')


justificativa = GerarJusBloqSubContratada()
