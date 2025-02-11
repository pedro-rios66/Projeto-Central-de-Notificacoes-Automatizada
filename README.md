# 📅 Central de Notificações de Governança 🔔  

A **Central de Notificações de Governança** é um sistema de automação que verifica eventos agendados dentro das próximas **24 horas** e emite notificações diretamente no terminal. O projeto foi desenvolvido para demonstrar **automação de processos** e **manipulação de arquivos CSV** com **Python e Pandas**.  

---

## 🚀 **Recursos e Funcionalidades**  

✅ **Automação de Notificações** – Verifica eventos programados e emite alertas.  
✅ **Manipulação de Arquivos CSV** – Lê, processa e atualiza eventos dinamicamente.  
✅ **Execução Agendada** – Usa `schedule` para verificar eventos automaticamente.  
✅ **Código Modularizado** – Separação lógica em diferentes arquivos para facilitar manutenção.  
✅ **Estruturação Profissional** – Pronto para ser utilizado em portfólios e repositórios públicos.  

---

## 📚 **Estrutura do Projeto**  

```
central-governanca/
│── data/  
│   ├── eventos.csv  # Base de dados com os eventos  
│── src/  
│   ├── main.py  # Arquivo principal que executa o programa  
│   ├── eventos.py  # Módulo para carregamento e verificação de eventos  
│   ├── notificacoes.py  # Módulo de notificações e atualização do CSV  
│── README.md  # Documentação do projeto  
│── requirements.txt  # Dependências do projeto  
│── .gitignore  # Arquivos a serem ignorados pelo Git  
```

---

## 🛠 **Tecnologias Utilizadas**  

- **Python** – Linguagem principal.  
- **Pandas** – Manipulação eficiente de arquivos CSV.  
- **Schedule** – Automação de execução em intervalos programados.  

---

## 📦 **Instalação e Execução**  

### **1️⃣ Clonar o Repositório**  
```sh
git clone https://github.com/pedro-rios66/Projeto-Central-de-Notificacoes-Automatizada
cd Projeto-Central-de-Notificacoes-Automatizada
```

### **2️⃣ Criar Ambiente Virtual (Opcional, Recomendado)**  
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Instalar Dependências**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Executar o Programa**  
```sh
python src/main.py
```

---

## 📊 **Formato do Arquivo CSV**  

O arquivo **`eventos.csv`** deve seguir o seguinte formato:  

| id | nome_evento             | data        | hora  | notificado |
|----|------------------------|------------|------|------------|
| 1  | Reunião da Diretoria   | 2025-02-01 | 15:30 | Não        |
| 2  | Apresentação de Resultados | 2025-01-27 | 10:00 | Não |

- **`data`** no formato `YYYY-MM-DD`.  
- **`hora`** no formato `HH:MM`.  
- **`notificado`** pode ser `Sim` ou `Não`.  

---

## 📌 **Como Funciona?**  

1️⃣ O sistema **lê o arquivo CSV** e carrega os eventos.  
2️⃣ Ele **filtra eventos das próximas 24 horas**.  
3️⃣ Se houver eventos próximos, ele **exibe notificações no terminal**.  
4️⃣ Após notificar, ele **atualiza o status no CSV**.  
5️⃣ O programa **verifica automaticamente** a cada **30 minutos**.  

---

## ✅ **Exemplo de Notificação no Terminal**  

```
🔍 Iniciando verificação de eventos...
📅 Eventos próximos encontrados:
  id  | nome_evento          | data        | hora
-------------------------------------------------
  4   | Teste de Projeto     | 2025-01-27  | 18:00

🔔 Notificação: O evento 'Teste de Projeto' ocorrerá em 2025-01-27 às 18:00.
✅ Eventos atualizados no arquivo 'eventos.csv'.
```

---

## 🚀 **Melhorias Futuras**  

🔹 **Integração com API de E-mail ou Telegram** para notificações automatizadas.  
🔹 **Interface Web para visualização e gerenciamento dos eventos.**  
🔹 **Banco de Dados SQL em vez de CSV para maior escalabilidade.**  



🔗 **GitHub:** [github.com/pedro-rios66/Projeto-Central-de-Notificacoes-Automatizada](https://github.com/pedro-rios66/Projeto-Central-de-Notificacoes-Automatizada)

