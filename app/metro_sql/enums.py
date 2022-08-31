import enum

class MetroLine(enum.IntFlag):
    L_INVALID = 0x0000
    L_01 =  0x0002
    L_02 =  0x0004
    L_03 =  0x0008
    L_04 =  0x0010
    L_05 =  0x0020
    # ...
    L_15 =  0x8000

    
class MetroFleet(enum.Enum):
    FLEET_E = 1
    FLEET_G = 2
    FLEET_H = 3
    FLEET_I = 4
    FLEET_J = 5
    FLEET_K = 6
    FLEET_L = 7
    FLEET_M = 8


class MetroWay(enum.IntEnum):
    WAY_MINUS = -1
    WAY_PLUS  = +1
    WAY_ONE   = WAY_MINUS
    WAY_TWO   = WAY_PLUS
    
    
def metro_line_from_value(v):
    if v == 1:
        return MetroLine.L_01
    if v == 2:
        return MetroLine.L_02
    if v == 3:
        return MetroLine.L_03
    if v == 4:
        return MetroLine.L_04
    if v == 5:
        return MetroLine.L_05
    if v == 15:
        return MetroLine.L_15
    return MetroLine.L_INVALID
    