import ex25

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5 - 1
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

sentence = "All good\tthings come to those who wait."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

ex25.print_first_word(words)
ex25.print_last_word(words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words

ex25.print_first_and_last(sentence)

ex25.print_first_and_last_sorted(sentence)
