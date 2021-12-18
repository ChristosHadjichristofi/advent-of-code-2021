import math

def extractLiteralV(packet):
    literal = ""
    while packet[0] == '1':
        literal += packet[1:5]
        packet = packet[5:]
    
    literal += packet[1:5]
    return (int(literal, 2), packet[5:])

def executeOperation(typeID, literals):
    if typeID == 0:
        return sum(literals)
    elif typeID == 1:
        return math.prod(literals)
    elif typeID == 2:
        return min(literals)
    elif typeID == 3:
        return max(literals)
    elif typeID == 5:
        return 1 if literals[0] > literals[1] else 0
    elif typeID == 6:
        return 1 if literals[0] < literals[1] else 0
    elif typeID == 7:
        return 1 if literals[0] == literals[1] else 0

def day16_pt1(packet):

    version, typeID, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]
    
    literalV = None
    if typeID == 4:
        literalV, packet = extractLiteralV(packet)
    else:
        literals = []
        lengthID, packet = int(packet[0], 2), packet[1:]

        if lengthID == 0:
            length, packet = int(packet[:15], 2), packet[15:]
            subpacket, packet = packet[:length], packet[length:]
            while subpacket:
                subVersion, subLiteralV, subpacket = day16_pt1(subpacket)
                version += subVersion
                literals.append(subLiteralV)
        else:
            numOfPackets, packet = int(packet[:11], 2), packet[11:]
            for id in range(numOfPackets):
                subVersion, subLiteralV, packet = day16_pt1(packet)
                version += subVersion
                literals.append(subLiteralV)
        
        literalV = executeOperation(typeID, literals)
    
    return version, literalV, packet

def main():
    hex2bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', 
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111', 
    }
    
    with open('input.txt', 'r') as f:
        hexstr = f.read().strip()

    binsequence = ""
    for char in hexstr:
        binsequence += hex2bin[char]
    
    version, val, _ = day16_pt1(binsequence)
    print("Part 1:", version)
    print("Part 2:", val)
    

if __name__ == "__main__":
    main()