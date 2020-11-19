# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class BinaryString:
    def __init__(self, binary):
        self.value = binary

    @property
    def value(self):
        return self._value

    @property
    def msb(self):
        return self._value[0]

    @property
    def lsb(self):
        return self._value[-1]

    @value.setter
    def value(self, value):
        if type(value) != str:
            raise ValueError("Binary string given must be a string")
        for digit in value:
            if digit not in ["1", "0"]:
                raise ValueError("Binary string given contains values that are not 1 or 0")
        self._value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        return BinaryString(str(self) + str(other))

    def __len__(self):
        return len(self.value)

    def __invert__(self):
        inverted = ""
        for bit in self.value:
            if bit == "1":
                inverted += "0"
            else:
                inverted += "1"
        return BinaryString(inverted)

    def __int__(self):
        column_value = 2 ** (len(self))
        i=0
        total=0
        while column_value > 1:
            column_value //= 2
            if self.value[i] == "1":
                total += column_value
            i+=1
        return total


class FixPointNumber(BinaryString):
    def __init__(self, binary, point):
        if type(point) != int:
            raise ValueError("The argument <point> must be a whole number")
        self._binary_point = point
        super(FixPointNumber, self).__init__(binary)

    def __float__(self):
        column_value = 2 ** (len(self)-1)
        total = 0
        for bit in self.value:
            total += int(bit) * column_value
            column_value /= 2
        total = total * (2**(self._binary_point-len(self)))
        return total

    def __int__(self):
        return int(float(self))

    def __str__(self):
        if self._binary_point < len(self):
            return self.value[:self._binary_point] + "." + self.value[self._binary_point:]
        else:
            return self.value


class TwosComplementNumber(BinaryString):
    def __abs__(self):
        """ Returns whole number part of twos complement number as BinaryString"""
        if self.is_negative():
            self = self._convert()
        return self

    def _convert(self):
        leading_one = len(self)-1
        while self.value[leading_one] != "1" and leading_one >= 0:
            leading_one -= 1

        flipped_bits = ~BinaryString(self.value[:leading_one])
        unflipped_bits = BinaryString(self.value[leading_one:])

        return flipped_bits + unflipped_bits

    @property
    def sign_bit(self):
        return self.msb

    def to_positive(self):
        return self._convert()

    def __neg__(self):
        return self._convert()

    def is_positive(self):
        if self.sign_bit == "1":
            return False
        else:
            return True

    def is_negative(self):
        if self.sign_bit == "0":
            return False
        else:
            return True

    def __int__(self):
        if self.is_negative():
            # return super(TwosComplementNumber, self).int(self.to_positive())
            return -BinaryString.__int__(self.to_positive())
        else:
            return BinaryString.__int__(self)


class Mantissa(TwosComplementNumber, FixPointNumber):
    def __init__(self, value):
        super(Mantissa, self).__init__(value, 1)


class FloatingPointNumber():
    def __init__(self, mantissa, exponent):
        self.mantissa = Mantissa(mantissa)
        self.exponent = BinaryString(exponent)

    @classmethod
    def as_single_string(cls, binary, mantissa_size):
        return cls(binary[:mantissa_size], binary[mantissa_size:])

    @property
    def mantissa(self):
        return self._mantissa

    @mantissa.setter
    def mantissa(self, mantissa):
        self._mantissa = mantissa

    @property
    def exponent(self):
        return self._exponent

    @exponent.setter
    def exponent(self, exponent):
        self._exponent = exponent

    def __str__(self):
        return str(self.mantissa + self.exponent)

    def __int__(self):

class Input:
    def __init__(self):
        pass
    def GetInputFromUser(self):
        while True:
            binary = input(
                'please enter an 8 bit binary number in twos complement(this will have an implied binary point between the 1st and 2nd bit')
            try:
                binary = binary.replace(' ', '')
                decimal = int(binary, 2)
                break
            except:
                print("What you entered is not Binary. Please type a binary number")
                continue
        self.binary = binary
    def MantissaInput(self):
        while True:
            mantissa = input('please enter a 4 bit mantissa')
            try:
                mantissa = mantissa.replace(' ', '')
                decimal = int(mantissa, 2)
                break
            except:
                print("What you entered is not Binary. Please type a binary number")
                continue
        self.mantissa = mantissa
    #def MantissaInput(self, tent):
        #print('this is overloaded function')
        #self.mantissa = 1010
        #print(tent)
    def convertmantissaToInteger(self):
        mantissa = int(self.mantissa,2)
        return mantissa
    def convertBinaryToList(self):
        result = []
        result[:] = self.binary
        char1 = [result[0]]
        if char1 == ['1']:
            finalconvert = []
            for string in result:
                newstring = string.replace('1', '0')
                finalconvert.append(newstring)
                secondstring = string.replace('0', '1')
                finalconvert.append(secondstring)
                del finalconvert[8:]
        else:
            finalconvert= []
            finalconvert = result
        n = 0
        x = 0
        for i in finalconvert:
            y = int(i) * (2**n)
            n+=-1
            x = x+y
        finalValue= x*(2**(self.convertmantissaToInteger()))
        if char1 == ['1']:
            finalValue = finalValue*(-1)
        print(finalValue)
        
        return 4


abc = Input()
abc.GetInputFromUser()
abc.MantissaInput()
abc.convertmantissaToInteger()
abc.convertBinaryToList()



class Hexidecimal():

    def hexidecimalConverter(self):
        while True:
            binary = input('please enter a binary string with a length that is a multiple of 4 to convert into hexadecimal')
            try:
                bstr = binary.replace(' ', '')
                decimal = int(bstr, 2)
                break
            except:
                print("What you entered is not Binary. Please type a binary number")
                continue

        hstr = '%0*X' % ((len(bstr) + 3) // 4, int(bstr, 2))
        print('The hexidecimal value of {} is {}'.format(binary, hstr))

abc = Hexidecimal()
abc.hexidecimalConverter()

class SignBit():
    my_list = []

    for i in range(0, 9):
        my_list.append(int(input("please enter a binary digit for your number, first digit is sign bit: ")))
        print(my_list)

    bit = 128
    total = 0

    for i in range(1, 8):
        if (my_list[i] == 1):
            total += bit
        else:
            total += 0
        bit /= 2

    if (my_list[0] == 1):
        print(total * -1)
    else:
        print(total)

SignBit()
   


if __name__ == '__main__':
    x = FloatingPointNumber("10000100", "1100")
    print(int(x))


