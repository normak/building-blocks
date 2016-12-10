def substrings(phrase, dictionary):
	counts = {}
	for word in dictionary:
		if word.lower() in phrase.lower():
			counts[word.lower()] = phrase.lower().count(word.lower())
	return counts

dictionary = ["below","down","go","going","horn","how","howdy","it","i",
"low","own","part","partner","sit"]

print substrings("below", dictionary)
print substrings("Howdy partner, sit down! How's it going?", dictionary)