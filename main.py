import pyautogui
import pyperclip
import time

print('========== MERN STACK PROJECT STARTER ==========\n')
print('by Rian Oliveira\n')

# Pega os dados necessários do usuário.
USERNAME = input('Nome de usuário do GitHub: ')
PROJECT_NAME = input('Nome do projeto: ')
DB_NAME = input('Nome do banco de dados: ')
PROJECT_LOCATION = input('Local onde ficará o projeto na sua máquina: ')

print('\nIniciando projeto, aguarde...')
print('Por favor, não mexa no teclado e mouse enquanto o programa estiver rodando.')

# Abre o navegador.
time.sleep(5)
pyautogui.hotkey('win', 'd')
time.sleep(0.5)
pyautogui.hotkey('win')
time.sleep(0.5)
pyautogui.write('Microsoft Edge')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('win', 'up')

# Vai até o perfil do GitHub do usuário.
time.sleep(0.5)
pyautogui.write('https://github.com/new')
time.sleep(0.5)
pyautogui.press('enter')

# Cria um novo repositório.
time.sleep(2)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.write(PROJECT_NAME)
time.sleep(0.5)
for i in range(9):
    pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('win', 'd')

# Abre o terminal.
time.sleep(0.5)
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('Git Bash')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')

# Inicia o banco de dados MongoDB.
time.sleep(0.5)
pyautogui.write('mongod')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('win', 'd')

# Abre o terminal.
time.sleep(0.5)
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('Git Bash')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')

# Entra no MongoDB.
time.sleep(0.5)
pyautogui.write('mongo')
time.sleep(0.5)
pyautogui.press('enter')

# Cria um novo banco de dados e uma collection de exemplo.
time.sleep(0.5)
pyautogui.write('use ' + DB_NAME)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('db.example.insertOne({ "name" : "example" })')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('show dbs')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('db.example.find().pretty()')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')

# Cria o diretório do projeto.
time.sleep(0.5)
pyperclip.copy('cd ' + PROJECT_LOCATION)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('mkdir ' + PROJECT_NAME)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('cd ' + PROJECT_NAME)
time.sleep(0.5)
pyautogui.press('enter')

# Abre o VSCode.
time.sleep(0.5)
pyautogui.write('code .')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('win', 'up')

# Clona o repositório do GitHub que contém o template a ser utilizado.
time.sleep(2)
pyautogui.hotkey('ctrl', '"')
time.sleep(2)
pyautogui.write('git clone https://github.com/riandeoliveira/mern-stack-template .')
time.sleep(0.5)
pyautogui.press('enter')

# Remove o repositório git do template.
time.sleep(10)
pyautogui.write('bash')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('rm -rf .git')
time.sleep(0.5)
pyautogui.press('enter')

# Inicia um novo repositório git.
time.sleep(0.5)
pyautogui.write('git init')
time.sleep(0.5)
pyautogui.press('enter')

# Configura a branch de master para main.
time.sleep(5)
pyautogui.write('git branch -M main')
time.sleep(0.5)
pyautogui.press('enter')

# Adiciona o repositório do GitHub pertencente ao projeto.
time.sleep(1)
pyautogui.write("git remote add origin 'https://github.com/" + USERNAME + "/" + PROJECT_NAME + "'")
time.sleep(0.5)
pyautogui.press('enter')

# Adiciona todo o template ao repositório local.
time.sleep(3)
pyautogui.write('git add .')
time.sleep(0.5)
pyautogui.press('enter')

# Faz commit de todo o projeto.
time.sleep(5)
pyautogui.write("git commit -m 'Initial commit'")
time.sleep(0.5)
pyautogui.press('enter')

# Faz um push, mandando o projeto para o GitHub.
time.sleep(5)
pyautogui.write('git push origin main')
time.sleep(0.5)
pyautogui.press('enter')

# Instala as dependências do back-end.
time.sleep(5)
pyautogui.write('cd server')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('npm install')
time.sleep(0.5)
pyautogui.press('enter')

# Instala as dependências do front-end.
time.sleep(30)
pyautogui.write('cd ..')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('cd client')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('npm install')
time.sleep(0.5)
pyautogui.press('enter')

print('\n================================================')