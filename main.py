EXAMPLE:1

price=678
text=("i went the market the one purches a remote={}")
print(text.format(price))
text=("i went the market the one purches a remote={:.1f}")
print(text.format(price))

EXAMPLE:2

quantity=3
itemno=10
price=89
text=("i went the {} pieces of the item naumber {} for={:.2f}")
print(text.format(quantity,itemno,price))

EXAMPLE:3

age=23
name="karthick"

text=("he,is {1}.his is age{0}")
print(text.format(age,name))

EXAMPLE:4
text=("he is a new bike purches {name} the model {model}")
print(text.format(name="yammaga",model="alpha"))
