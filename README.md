# ExperimentalComputer
Working on this during break at school. Has a few issues, but no bugs yet. Any help would be awesome!

SOME ISSUES:

DON'T KNOW WHAT TO CLASSIFY THIS AS

GATES ARE NOT OPTIMIZED - WAY TOO MANY IF STATEMENTS AND NOT SCALABALE

SOME GATES ARE KINDA USELESS

Some documentation:

3 bits, which change randomly with each calculation

calculationamount - amount of calculations

Bit1 is just the bit being operated on

Gates:

setsTo - Sets bit1 to selected position (ex: setsTo(q1,0))

invert - Inverts bit1 (ex: invert(q1))

both - sets remaining bit to e if bit1 and bit2 are equal (ex: both(q1,q2,0))

all - sets bit1 to e if all bits are equal (ex: all(q1, 0))

unequal - sets remaining bit to e if bit1 and bit2 are unequal (ex: unequal(q1,q2,0))
