import subprocess

# Função para iniciar os processos com parâmetros
def iniciar_processos(comandos):
    for comando in comandos:
        try:
            processo = subprocess.Popen(comando, shell=True)
            print(f"Processo '{comando}' iniciado com PID {processo.pid}.")
        except Exception as e:
            print(f"Erro ao iniciar o processo {comando}: {e}")

# Lista de comandos para iniciar os programas com parâmetros
comandos = [
    r'"C:\Program Files\Alterdata\ERP\GEAgente.exe" -Ugeliberador -SFrgHy654j8q -C"ALTERDATA (ODBC)"',
    # r'"C:\Program Files\Alterdata\ERP\LiberadorEstoque.exe" -Ugeliberador -SFrgHy654j8q -C"ALTERDATA (ODBC)',
    r'"C:\Program Files\Alterdata\ERP\IntegradorBimer_PDVAlterdata.exe" -Ugeliberador -SFrgHy654j8q -C"ALTERDATA (ODBC)'
]

# Inicia os processos
iniciar_processos(comandos)