
training_data = [("the wall street journal reported today that apple corporation made money".split(),
				    "B I I I O O O B I O O".split()),
				    ( "georgia tech is a university in georgia".split(),
				    "B I O O O O B".split()
    )]


print(training_data)





[(['the', 'wall', 'street', 'journal', 'reported', 'today', 'that', 'apple', 'corporation', 'made', 'money'],
  ['B', 'I', 'I', 'I', 'O', 'O', 'O', 'B', 'I', 'O', 'O']), 
(['georgia', 'tech', 'is', 'a', 'university', 'in', 'georgia'], ['B', 'I', 'O', 'O', 'O', 'O', 'B'])]
