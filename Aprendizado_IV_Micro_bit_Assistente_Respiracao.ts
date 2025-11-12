// Assistente  de respiração.
// Função para pressionar o botão
input.onButtonPressed(Button.A, function () {


basic.showString("VAMOS RESPIRAR...")
 
 basic.clearScreen()
 basic.pause(1000)

 basic.showString("3")
 basic.pause(500)
 basic.showString("2")
 basic.pause(500)
 basic.showString("1")
 basic.clearScreen()
 basic.pause(1000)

// Pause  2  segundos
    basic.pause(2000)
// Função de repetição para respirar 6x
for (let index = 0; index < 6; index++) {
// Show  de  leds  crescente
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    //Pause  0.5  segundos
    basic.pause(500)

    basic.showIcon(IconNames.SmallDiamond)
     //Pause  0.5  segundos
    basic.pause(500)
    basic.showIcon(IconNames.Diamond)
    //Pause  0.5  segundos
    basic.pause(2000)
    basic.showIcon(IconNames.SmallDiamond)
    //Pause  0.5  segundos
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)

   }
    basic.clearScreen()
    basic.showString("FINALIZADO...")
    basic.pause(1000)
    basic.clearScreen()
})
