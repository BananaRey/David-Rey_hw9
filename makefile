#el compilador 
gen_times.x: DavidRey_GenerarTiempos.cpp
	c++ DavidRey_GenerarTiempos.cpp -o gen_times.x
#se compila y manda al archivo
times_cpp.csv: gen_times.x
	./gen_times.x>times_cpp.csv
#se hace el texto con pyhton
times_python.csv: DavidRey_GenerarTiempos.py
	python DavidRey_GenerarTiempos.py>times_python.csv
#
cpp_vs_python.png: times_cpp.csv times_python.csv
