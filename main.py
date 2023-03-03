"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):

    def __init__(self):
        self.items = []
        self.class_total = 0

    def addItem(self, item):
        if item == "tophat":
            class_num = 2
        elif item == "bowtie":
            class_num = 4
        elif item == "monocle":
            class_num = 5
        else:
            class_num = 0
        self.items.append(class_num)
        return self.items

    def getClassiness(self):
        for i in self.items:
            self.class_total += i
        print(self.class_total)


# Test cases
me = Classy()

me.addItem("tophat")
me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
me.getClassiness()

# # Should be 2
# print me.getClassiness()
#
# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# # Should be 11
# print me.getClassiness()
#
# me.addItem("bowtie")
# # Should be 15
# print me.getClassiness()
