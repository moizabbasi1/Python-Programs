###################################################################
# Question 1
###################################################################
def f2c(t):
  t = (t - 32) * 5.0/9.0
  return (t)


###################################################################
# Question 2
###################################################################
def lboz2kg(p,o):
  p = p / 2.20462
  o = o / 35.274
  total_w = p + o
  return (total_w)


###################################################################
# Question 3
###################################################################
def bibformat_mla(author,title,city,publisher,year):
  str = author +". "+  title + ". " + city + ": " + publisher +", "+ year
  print (str)

###################################################################
# Question 4
###################################################################
def bibformat_apa(author,title,city,publisher,year):
  str = author + " " + year + ". " + title + ". " + city + ": " + publisher +"."
  print (str)


###################################################################
# Question 5
###################################################################
def joker():
  joker = input("What is your name? ")
    return ("Hey %s, I heard you burned 2,000 calories. That’s why you shouldn’t leave brownies in the oven while you nap."%(joker))


###################################################################
# Question 6
###################################################################
def bmi(w,h):
  w = w * 703
  h = h ** 2
  total_bmi = w / h
  return (total_bmi)


###################################################################
# Question 7
###################################################################
def lbs2lboz(p):
    # converting p to int and making it a whole number
    l = int(p)
    # taking the remaining value and multihying by 16 to get the ounces
    o = (p - l) * 16
    # returning a pair containing value in pounds and ounces
    return (l, o)


###################################################################
# Question 8
###################################################################
def oz2lboz(oz):
    # dividing by 16 and getting integer part to get pounds
    l = int(oz / 16)
    # subtracting the value above from oz to get remaining ounces
    o = oz - (l * 16)
    return (l, o)


###################################################################
# Question 9
###################################################################
def bmi_calculator():
  appelation = input(' Appelation : ')
  fname = input(' First name : ')
  lname = input(' Last name : ')
  h = float(input(' Height(in inches) : '))
  w = float(input(' Weight(in pounds) : '))
  h_feet = int(h*0.0833333)
  h_inches = h - (h_feet*12)
  bmi = ( (w /(h * h)) * 703 )
  return(" BMI Record for %s %s %s \n Subject is %d feet %f inches tall and weighs %f pounds \n The subject's BMI is %f" %(appelation,fname,lname,h_feet,h_inches,w,bmi))


###################################################################
# Question 10
###################################################################
def hashes(n):
 b = ('#') * n
 return ("%s" %(b) )
