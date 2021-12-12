def day8_part1(outputValues):
    counter = 0
    for outputValueList in outputValues:
        for outputValue in outputValueList.split(' '):
            length = len(outputValue)
            if length == 2 or length == 4 or length == 3 or length == 7:
                counter = counter + 1

    return counter

def day8_part2(inputSignals, outputValues):
    sum = 0
    for i in range(len(inputSignals)):
        # for each line create a new dictionary
        signalsOfNums = {}
        # get all input signals that exist in that line
        for inputSignal in inputSignals[i].split(' '):
            # find length of inputSignal
            length = len(inputSignal)
            # define a set with the chars of the signal so as they're at the same positions
            signal = set(inputSignal)
            # known signals are for num 1 (len 2), num 4 (len 4), num 7 (len 3), num 8 (len 8)
            if length == 2:
                signalsOfNums[1] = signal
            elif length == 4:
                signalsOfNums[4] = signal
            elif length == 3:
                signalsOfNums[7] = signal
            elif length == 7:
                signalsOfNums[8] = signal
        
        # for every other number try to find its signal
        for inputSignal in inputSignals[i].split(' '):
            length = len(inputSignal)
            signal = set(inputSignal)
            # numbers 2, 3, 5
            if length == 5:
                # number 3 is a superset of number 1
                if signalsOfNums[1].issubset(signal):
                    signalsOfNums[3] = signal
                # number 2 is a superset of the difference between set of number 8 and set of number 4
                elif (signalsOfNums[8] - signalsOfNums[4]).issubset(signal):
                    signalsOfNums[2] = signal
                # in every other case with len 5 is number 5
                else:
                    signalsOfNums[5] = signal 
            # numbers 0, 6, 9
            elif length == 6:
                # number 9 is superset of number 4
                if signalsOfNums[4].issubset(signal):
                    signalsOfNums[9] = signal
                # number 0 is superset of number 1
                elif signalsOfNums[1].issubset(signal):
                    signalsOfNums[0] = signal
                # in every other case with len 6 is number 6
                else:
                    signalsOfNums[6] = signal

        # each time create a list with the numbers that came up from the signals
        outputNumbers = [list(signalsOfNums.keys())[list(signalsOfNums.values()).index(set(x))] for x in outputValues[i].split(' ')]
        # create the integer from the list and add to prev sum
        sum += int("".join(str(n) for n in outputNumbers))

    return sum

def main():
    inputSignals = [f.split(' | ')[0].rstrip("\n") for f in open('input.txt', 'r').readlines()]
    outputValues = [f.split(' | ')[1].rstrip("\n") for f in open('input.txt', 'r').readlines()]

    print("Part 1:", day8_part1(outputValues))
    print("Part 2:", day8_part2(inputSignals, outputValues))

if __name__ == "__main__":
    main()