import sys
import math
import matplotlib.pyplot as plt


for file_name in sys.argv[1:]:
	print file_name
	fichier = open(file_name)
	curves = [[[]]]
	test_cases = []
	new_curve = True
	for line in fichier.read().split('\n'):
		if(len(line) == 0):
			break
		if(line[0] == "E"):
			curves.append([[]])
			test_cases.append(int(line.split(" ")[1]))
			new_curve = True
		elif(line[0] == "#"):
			if(not new_curve):
				curves[-1].append([])
			new_curve = False
		else:
			points = line.split(',')
			curves[-1][-1].append((int(points[0]),int(points[1])))

	curves = curves[:-1] #The last curve is in fact between END and EOF.

	dist_n1,dist_n2 = [],[]
	max_n1,max_n2 = [],[]
	sum_n1,sum_n2 = [],[]
	coeff_repli = []
	nb_noise = []
	nb_real_curve = []
	mean_dist = []
	nb_curves = []
	nb_points = []
	evaluation = []

	for file_curves in curves:
		coeff_repli_temp = []
		nb_curves.append(0)
		nb_points.append(0)
		dist_n1.append([])
		dist_n2.append([])

		for curve in file_curves:
			nb_curves[-1] = nb_curves[-1] + 1
			dist_n1[-1].append(0)
			dist_n2[-1].append(0)
			cur_point = curve[0]
			nb_points[-1] = nb_points[-1] + 1

			for points in curve[1:]:
				nb_points[-1] = nb_points[-1] + 1
				dist_n1[-1][-1] = dist_n1[-1][-1] + abs(points[0] - cur_point[0]) + abs(points[1] - cur_point[1])
				dist_n2[-1][-1] = dist_n2[-1][-1] + math.sqrt((points[0] - cur_point[0])**2 + (points[1] - cur_point[1])**2)
				cur_point = points

			coeff_repli_temp.append(dist_n2[-1][-1] / len(curve))

		maxi = max(coeff_repli_temp)
		coeff_repli.append([float(i)/maxi] for i in coeff_repli_temp)

		max_n1.append(max(dist_n1[-1]))
		max_n2.append(max(dist_n2[-1]))
		sum_n1.append(sum(dist_n1[-1]))
		sum_n2.append(sum(dist_n2[-1]))
		mean_dist.append(sum(dist_n2[-1])/nb_points[-1])
		nb_noise.append(sum(i < 0.1 for i in coeff_repli[-1]))
		nb_real_curve.append(sum(i > 0.3 for i in coeff_repli[-1]))

		evaluation.append(3*nb_real_curve[-1]-nb_noise[-1])
	def print_norm_plot(tab_y, tab_x,legend):
		mini = min(tab_y)
		maxi = max(tab_y)
		new_tab_y = [float(i - mini)/max(1,maxi-mini)  for i in tab_y]

		plt.plot(tab_x,new_tab_y, label = legend)

	def print_norm_plot2(tab_y, tab_x,legend):
		maxi = max(tab_y)
		new_tab_y = [float(i)/max(1,maxi)  for i in tab_y]

		plt.plot(tab_x,new_tab_y, label = legend)

	print_norm_plot(nb_curves,test_cases,"nb_curves")
	#print_norm_plot(max_n1,test_cases,"max_n1")
	#print_norm_plot(max_n2,test_cases,"max_n2")
	print_norm_plot(nb_points,test_cases,"nb_points")
	#print_norm_plot(sum_n1,test_cases,"sum_n1")
	#print_norm_plot(sum_n2,test_cases,"sum_n2")
		
	#print_norm_plot2(mean_dist,test_cases,"mean_dist")
	#print_norm_plot2(nb_real_curve,test_cases,"nb_real_curve")
	#print_norm_plot2(nb_noise,test_cases,"nb_noise")
	#print_norm_plot2(evaluation,test_cases,"evaluation")
	#print nb_points,nb_curves
	plt.legend()
	plt.axis([-1,101,-0.1,1.1])
	plt.show()
	fichier.close()

#fichier = open("contour")