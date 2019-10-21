###################################################################
# Question 1
###################################################################

def zeta1(n):
  base = 0
  x = 1
  for i in range (n):
    base += 1/x
    x += 1
  return (base)

  ###################################################################
  # Question 2
  ###################################################################
a = [0,1,2,3,4,5,6]
def product(a):
  sum1 = 1
  for i in range(len(a)):
    sum1 = sum1 * a[i]

  return (sum1)

  ###################################################################
  # Question 3
  ###################################################################

a = [1,2,3,4,5,6,7,8,9,10]
def average(a):
  summ = 0
  for i in range(len(a)):
    summ = summ + a[i]
  avg = summ/len(a)
  return (avg)

  ###################################################################
  # Question 4
  ###################################################################

def to_str(a):
    s=''
    for i in range(len(a)):
        s=s+str(a[i])
    return s
a=[1,2,3,4,5,6,7,8,9,10]


  ###################################################################
  # Question 5
  ###################################################################
def threshold(a,x):
  array = []
  for num in a :
    if num >= x :
      array.append(num)
  return array
a = [1,2,3,4,5,6,7,8,9,10]

  ###################################################################
  # Question 6
  ###################################################################

def square(a):
    squareNumb=[]
    for val in a:
        squareNumb.append(val*val)
    return squareNumb
a=[1,2,3,4,5,6,7,8,9,10]

  ###################################################################
  # Question 7
  ###################################################################

def is_zero(x):
    if x == 0:
        return("zero")
    if x > 0:
        return("not zero")
    return (is_zero(x))


  ###################################################################
  # Question 8
  ###################################################################

def bmi_cat(bmi):
    if bmi < 18.5:
        return("underweight")
    if 18.5 <= bmi < 25:
        return("normal")
    if 25 <= bmi < 30:
        return("overweight")
    if bmi >= 30:
        return("obese")
    return (bmi_cat(bmi))

  ###################################################################
  # Question 9
  ###################################################################

def bmi_app():
    h = float(input('Enter your height(in inches) : '))
    w = float(input('Enter your weight(in pounds) : '))
    h_feet = int(h*0.0833333)
    h_inches = h - (h_feet*12)
    bmi = ( (w /(h * h)) * 703 )

    if bmi < 18.5:
        s = "underweight"
    if 18.5 <= bmi < 25:
        s = "normal"
    if 25 <= bmi < 30:
        s = "overweight"
    if bmi >= 30:
        s = "obese"
    return ("Your BMI is %f. You are %s" %(bmi, s))

  ###################################################################
  # Question 10
  ###################################################################

def weight_format(mg):
    MG=float(mg)
    G=float(1000)
    KG=float(G**2)
    T=float(G**3)
    if(MG<G):
        return '{0} {1}'.format(MG,"mg");
    elif(MG>=G and MG<KG):
        return '{0} {1}'.format(MG/G,"g");
    elif(MG>=KG and MG<T):
        return '{0} {1}'.format(MG/KG,"g");
    else:
        return '{0} {1}'.format(MG/T,"g");

    return(weight_format(mg))
