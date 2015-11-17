#liz = open("liz_fav_foods.txt")
#liz_list = liz.readlines()
#print liz_list


#liz.close()

#laura = open ("laura_fav_foods.txt")
#laura_list = laura.readlines()
#print laura_list

#laura.close()


#compare_ = open("laura_fav_foods.txt" and "liz_fav_foods.txt")

#compare_list = compare_favs.readlines()
#print compare_list

#compare_favs.close()

#ef compare_lists(name):
#my_file = open(name)
#name_list = my_file.readlines()
#print name_list
#my_file.close()

#compare_lists("liz_fav_foods.txt")
#compare_lists("laura_fav_foods.txt")


def compare_favs(person1, person2):
	person_file1 = open(person1)
	person_file2 = open(person2)
	if (person_file1.readline(1) == person_file2.readline(1)):
		print "Our faves are the same"
	else:
		print "Our faves are not the same"
	person_file1.close()
	person_file2.close()

compare_favs ("liz_fav_foods.txt", "laura_fav_foods.txt")

