from string import Template

th = Template('${a}ab,${ab}')
str = th.substitute(a='as',ab='dd')
print(str)
