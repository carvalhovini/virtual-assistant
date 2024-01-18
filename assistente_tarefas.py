# assistente_tarefas.py

import spacy
from datetime import datetime, timedelta
from plyer import notification

nlp = spacy.load("pt_core_news_sm")

def extrair_informacoes_tarefa(comando):
    doc = nlp(comando)
    data_vencimento = extrair_data_vencimento(doc)
    return {"descricao": doc.text, "data_vencimento": data_vencimento}

def extrair_data_vencimento(doc):
    for ent in doc.ents:
        if ent.label_ == "DATE":
            data_texto = ent.text
            data = extrair_data(data_texto)
            if data:
                return data.strftime("%Y-%m-%d")
    return None

def extrair_data(data_texto):
    try:
        return datetime.strptime(data_texto, "%Y-%m-%d")
    except ValueError:
        return None

def enviar_notificacao(tarefa):
    notification.notify(
        title="Lembrete de Tarefa",
        message=f"Lembre-se de: {tarefa['descricao']}",
        app_name="Assistente de Tarefas",
        timeout=10
    )

# Função para aprender com o usuário
def aprender_com_usuario():
    print("Vamos aprender! Digite uma pergunta ou comando personalizado:")
    pergunta = input("Você: ")
    resposta = input("Resposta: ")
    # Adicionar lógica para armazenar a pergunta e resposta em um arquivo ou banco de dados
    print("Ótimo! Eu vou lembrar disso.")

# Função para interação com o usuário
def interagir_com_usuario():
    while True:
        comando = input("Você: ")

        if comando.lower() == "sair":
            break
        elif comando.lower() == "aprender":
            aprender_com_usuario()
        else:
            print("Digite a descrição da tarefa:")
            descricao = input("Descrição: ")

            if descricao.lower() == "sair":
                break

            print("Digite a data de vencimento (opcional, formato YYYY-MM-DD):")
            data_input = input("Data de Vencimento: ")
            data_vencimento = None

            if data_input.strip():  # Verificar se foi fornecida uma data
                data_vencimento = extrair_data(data_input)

                if not data_vencimento:
                    print("Data inválida. Ignorando a data de vencimento.")
                    data_vencimento = None

            informacoes_tarefa = {"descricao": descricao, "data_vencimento": data_vencimento}

            # Lógica de armazenamento e notificação aqui
            print("Tarefa adicionada:")
            print("Descrição:", informacoes_tarefa["descricao"])
            if informacoes_tarefa["data_vencimento"]:
                print("Data de Vencimento:", informacoes_tarefa["data_vencimento"])
            enviar_notificacao(informacoes_tarefa)

if __name__ == "__main__":
    aprender_com_usuario()  # Chamada para aprendizado inicial
    interagir_com_usuario()  # Chamada para interação contínua
