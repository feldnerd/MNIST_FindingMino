import numpy as np

# To do: this should be turned into a function rather tha hard-coded

zero  =  np.array([1,1,1,1,1,1,1,1,1,1])
one   =  np.array([0,1,1,1,1,1,1,1,1,1])
two   =  np.array([0,0,1,1,1,1,1,1,1,1])
three =  np.array([0,0,0,1,1,1,1,1,1,1])
four  =  np.array([0,0,0,0,1,1,1,1,1,1])
five  =  np.array([0,0,0,0,0,1,1,1,1,1])
six   =  np.array([0,0,0,0,0,0,1,1,1,1])
seven =  np.array([0,0,0,0,0,0,0,1,1,1])
eight =  np.array([0,0,0,0,0,0,0,0,1,1])
nine  =  np.array([0,0,0,0,0,0,0,0,0,1])

#----------------------------------------------------------------------------------------

zero_one = abs(zero-one)
zero_two = abs(zero-two)
zero_three = abs(zero-three)
zero_four = abs(zero-four)
zero_five = abs(zero-five)
zero_six = abs(zero-six)
zero_seven = abs(zero-seven)
zero_eight = abs(zero-eight)
zero_nine = abs(zero-nine)

one_two = abs(one-two)
one_three = abs(one-three)
one_four = abs(one-four)
one_five = abs(one-five)
one_six = abs(one-six)
one_seven = abs(one-seven)
one_eight = abs(one-eight)
one_nine = abs(one-nine)

two_three = abs(two-three)
two_four = abs(two-four)
two_five = abs(two-five)
two_six = abs(two-six)
two_seven = abs(two-seven)
two_eight = abs(two-eight)
two_nine = abs(two-nine)

three_four = abs(three-four)
three_five = abs(three-five)
three_six = abs(three-six)
three_seven = abs(three-seven)
three_eight = abs(three-eight)
three_nine = abs(three-nine)

four_five = abs(four-five)
four_six = abs(four-six)
four_seven = abs(four-seven)
four_eight = abs(four-eight)
four_nine = abs(four-nine)

five_six = abs(five-six)
five_seven = abs(five-seven)
five_eight = abs(five-eight)
five_nine = abs(five-nine)

six_seven =abs(six-seven)
six_eight = abs(six-eight)
six_nine = abs(six-nine)

seven_eight = abs(seven-eight)
seven_nine = abs(seven-nine)

eight_nine = abs(eight-nine)

#----------------------------------------------------------------------------------------

data = np.array([zero_one,
        zero_two,
        zero_three,
        zero_four,
        zero_five,
        zero_six,
        zero_seven,
        zero_eight,
        zero_nine,
        one_two,
        one_three,
        one_four,
        one_five,
        one_six,
        one_seven,
        one_eight,
        one_nine,
        two_three,
        two_four,
        two_five,
        two_six,
        two_seven,
        two_eight,
        two_nine,
        three_four,
        three_five,
        three_six,
        three_seven,
        three_eight,
        three_nine,
        four_five,
        four_six,
        four_seven,
        four_eight,
        four_nine,
        five_six,
        five_seven,
        five_eight,
        five_nine,
        six_seven,
        six_eight,
        six_nine,
        seven_eight,
        seven_nine,
        eight_nine])

#----------------------------------------------------------------------------------------


multi_hot_dict = {"0_1":zero_one,
                "0_2":zero_two,
                "0_3":zero_three,
                "0_4":zero_four,
                "0_5":zero_five,
                "0_6":zero_six,
                "0_7":zero_seven,
                "0_8":zero_eight,
                "0_9":zero_nine,
                "1_2":one_two,
                "1_3":one_three,
                "1_4":one_four,
                "1_5":one_five,
                "1_6":one_six,
                "1_7":one_seven,
                "1_8":one_eight,
                "1_9":one_nine,
                "2_3":two_three,
                "2_4":two_four,
                "2_5":two_five,
                "2_6":two_six,
                "2_7":two_seven,
                "2_8":two_eight,
                "2_9":two_nine,
                "3_4":three_four,
                "3_5":three_five,
                "3_6":three_six,
                "3_7":three_seven,
                "3_8":three_eight,
                "3_9":three_nine,
                "4_5":four_five,
                "4_6":four_six,
                "4_7":four_seven,
                "4_8":four_eight,
                "4_9":four_nine,
                "5_6":five_six,
                "5_7":five_seven,
                "5_8":five_eight,
                "5_9":five_nine,
                "6_7":six_seven,
                "6_8":six_eight,
                "6_9":six_nine,
                "7_8":seven_eight,
                "7_9":seven_nine,
                "8_9":eight_nine}

labels = np.array([0,0,0,0,0,0,0,0,0,
                   1,1,1,1,1,1,1,1,
                   2,2,2,2,2,2,2,
                   3,3,3,3,3,3,
                   4,4,4,4,4,
                   5,5,5,5,
                   6,6,6,
                   7,7,
                   8])


def multi_hot_encode(list_numA_numB):
    
    encoded_list = []
    
    for pair in list_numA_numB:
    
        key = str(min(pair[0],pair[1])) + '_' + str(max(pair[0],pair[1]))
        value = multi_hot_dict[key]
        
        encoded_list.append(value)
    
    return encoded_list

def reverse_multi_hot_encode(value):
    
    i = 0
    for code in data:
        if (value == code).all():
            index = i
        
        i = i + 1
    
    return labels[index]