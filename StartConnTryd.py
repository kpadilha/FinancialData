import socket
#import win32api
import TypeDataTryd as tdt
from TimesAndTrades.OutputTimesTrades import OutputTimesTrades
from configparser import ConfigParser

#---ESCOLHER O ATIVO EXEMPLO:-----------#
# PETR4  - Petrobras
# VALE3  - Vale
# ITUB4  - Itau
# INDQ19 - Indice Bovespa
# WINQ19 - Mini Indice Bovespa
#========================================#
ATIVO = 'WINM20'
#========================================#

#---INFORMACOES DO SERVIDOR--------------#
#========================================#
# Faz leitura do arquivo de configuração
config_object = ConfigParser()
config_object.read("config.ini")

serverdata = config_object["SERVERCONFIG"]
HOST = serverdata["host"]
PORT = int(serverdata["port"])

#HOST = '127.0.0.1'
#PORT = 12002
#========================================#

#---OPCAO DE COTACAO---------------------#
#========================================#

#========================================#

def ByteConvert(dataInfo):
    return str.encode(dataInfo + ATIVO + '#')

#Inicia a Execução
ott = OutputTimesTrades()
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
#        print("Id da thread principal %d" % (win32api.GetCurrentThreadId()))
        data = b''
        while True:
            try:
                s.sendall(ByteConvert(tdt.NEGOCIO_COMPLETO) )
                
                # Evita perdas de negócios quando a transmissão pelo socket ultrapassa 8192 caracteres 
                # ------------------------------------------------------------------------------------
                chunk = s.recv(8192)
                if len(chunk) >= 8192:
                    data = data + chunk
                else:
                    data = data + chunk
                    ott.OutputData(data.decode())
                    data = b''
               # --------------------------------------------------------------------------------------
            
            except Exception as ex:
                print(ex)
            
except Exception as ex:
    print('Não foi possivel conectar no servidor RTD. Erro: ', ex)
