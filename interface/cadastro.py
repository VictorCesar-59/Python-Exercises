from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Reddit')
lt = [[sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
[sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
[sg.Checkbox('Salvar senha?')],
[sg.Button('Entrar')]]
#janelas
janela = sg.Window('Tela de login', lt)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos ==  'Entrar':
        if valores['usuario'] == 'Victor' and valores['senha'] == '943059':
            print('Bem vindo')

