import os
import threading
import shutil
import psutil
import time
from multiprocessing import Process

def create_kernel():
	os.system("unxz -v linux-5.19.3.tar.xz")
	os.system("tar xvf linux-5.19.3.tar")
	print(os.getcwd())
	opath=os.getcwd()+"/.config"
	npath=os.getcwd()+"/linux-5.19.3/.config"
	shutil.copyfile(opath,npath)
	os.chdir(os.getcwd()+"/linux-5.19.3")
	os.system("make -j 6")	
	os.system("make clean")
	os.system("make distclean")
		


def experiment_iter():

	t1=threading.Thread(target=create_kernel,name='krprocs')
	time1=time.time()
	t1.start()
	
	cputil=[]
	memusage=[]
	while(t1.is_alive()):
		
		cputil.append(psutil.cpu_percent(interval=1,percpu=False))
		memusage.append(psutil.Process(os.getpid()).memory_info().rss)
			
	time2=time.time()
	timeelapsed=time2-time1
	cpuutil=sum(cputil)/len(cputil)
	memusage=sum(memusage)/len(memusage)
	print("Time elapsed",timeelapsed)
	print("CPU util ",cpuutil)
	print("Mem usage ",memusage)
	return (timeelapsed,cpuutil,memusage)
	
def experiment(itr):	
	timelist=[]
	cpuutillist=[]
	memutilist=[]
	#store working directory in wd
	wd=os.getcwd()
	for i in range(itr):
		timee,cpu,mem=experiment_iter()
		os.chdir(wd)
		timelist.append(timee)
		cpuutillist.append(cpu)
		memutilist.append(mem)
	print("results")
	print("timelist")
	print(timelist)
	print("cpuutillist")
	print(cpuutillist)
	print("memutillist")
	print(memutilist)
experiment(5)
	
