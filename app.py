import psutil

# Lista dos nomes dos processos que deseja finalizar
process_names = [
    "GEAgente.exe",
    # "LiberadorEstoque.exe",
    "IntegradorBimer_PDVAlterdata.exe"
]

# Função para finalizar os processos pelo nome
def finalizar_processos(names):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in names:
            try:
                proc.kill()  # Força o encerramento do processo
                print(f"Processo {proc.info['name']} com PID {proc.info['pid']} finalizado.")
            except psutil.NoSuchProcess:
                print(f"Processo {proc.info['name']} não encontrado.")
            except psutil.AccessDenied:
                print(f"Sem permissão para finalizar o processo {proc.info['name']}.")

# Finaliza os processos
finalizar_processos(process_names)
