# Assistente  de respiração.
# Função para pressionar o botão

def on_button_pressed_a():
    basic.show_string("VAMOS RESPIRAR...")
    basic.clear_screen()
    basic.pause(1000)
    basic.show_string("3")
    basic.pause(500)
    basic.show_string("2")
    basic.pause(500)
    basic.show_string("1")
    basic.clear_screen()
    basic.pause(1000)
    # Pause  2  segundos
    basic.pause(2000)
    # Função de repetição para respirar 6x
    for index in range(6):
        # Show  de  leds  crescente
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        # Pause  0.5  segundos
        basic.pause(500)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        # Pause  0.5  segundos
        basic.pause(500)
        basic.show_icon(IconNames.DIAMOND)
        # Pause  0.5  segundos
        basic.pause(2000)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        # Pause  0.5  segundos
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    basic.clear_screen()
    basic.show_string("FINALIZADO...")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
