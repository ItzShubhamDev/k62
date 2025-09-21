import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner

from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP16, board.GP17, board.GP26, board.GP22, board.GP27)
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP14, board.GP15, board.GP13, board.GP12, board.GP11, board.GP10,
    board.GP9, board.GP8
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

keyboard.keymap = [
  [
    KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO, KC.RSFT,
    KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL
  ]
]

if __name__ == '__main__':
    keyboard.go()