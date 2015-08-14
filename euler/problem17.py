#coding: UTF-8
# 1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.
# では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.
# 注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字, 115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習.
NUMBER_DEF = {
	1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
	11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
	30: 'thirty',40: 'forty',50: 'fifty',60: 'sixty',70: 'seventy',80: 'eighty',90: 'ninety',
}
THREE_DIGIT = 'hundred'
FOUR_DIGIT = 'thousand'

def make_two_digit_str(target):
	if NUMBER_DEF.has_key(target):
		return NUMBER_DEF[target]
	else:
		_target = str(target)
		return "%s%s" % (NUMBER_DEF[int(_target[0] + '0')],NUMBER_DEF[int(_target[1])])
		
def make_three_digit_str(target):
	_target = str(target)
	one_digit = NUMBER_DEF[int(_target[0])] + THREE_DIGIT
	second_digit = int(_target[1:3])
	if second_digit == 0:
		return one_digit
	else:
		return "%sand%s" % (one_digit ,make_two_digit_str(second_digit))

total = 0
for i in range(1,1001):
	if NUMBER_DEF.has_key(i):
		total += len(NUMBER_DEF[i])
		continue
	if i < 100:
		total += len(make_two_digit_str(i))
	elif i < 1000:
		total += len(make_three_digit_str(i))
	else:
		total += len('one' + FOUR_DIGIT)		
print total
