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

def compare_lists(name):
	my_file = open(name)
	name_list = my_file.readlines()
	print name_list
	my_file.close()

compare_lists("liz_fav_foods.txt")
compare_lists("laura_fav_foods.txt")


