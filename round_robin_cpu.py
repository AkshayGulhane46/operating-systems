#funcion for finding waiting time for all the processes
def findWatingTime(processes, n, bt, wt, quantam):
    rem_bt=[0]*n
    #copy the burst time into remaining time in rt[]
    for i in range(n):
        rem_bt[i]=bt[i]
    t=0 #currenttime

    #keep all traversing processes in round robin nmanner
    #untill all of them are not done

    while(1):
        done=True
        #traverse all processes one by one repetedly
        for i in range(n):
            #if burst time of a process is greater than 0
            #then only need to process further

            if(rem_bt[i]>0):
                done=False  #there is pending process

                if(rem_bt[i]>quantam):
                    #increase the value of t i.e. shows
                    #how much time a process has been processed
                    t += quantam
                    #decrease the burst_time of a current process by quantam
                    rem_bt[i] -= quantam
                #If burst time is smaller than or equal to quantam
                #last cycle for this process
                else:
                    #increase value of t i.e. show how much time a process
                    #has been processed
                    t=t+rem_bt[i]
                    #waiting time is current time minus time used by this process
                    wt[i]=t-bt[i]
                    #as the process gets fully executed make its remaining burst time 0
                    rem_bt[i]=0
        #if all processes are done
        if(done==True):
          break

#function to calculate turn around time
def findTurnaroundTime(processes, n, bt, wt, tat):
    #calculate turnaround time
    for i in range(n):
        tat[i]=bt[i]+wt[i]

#function to calculate average waiting and turnaround time
def findAvgTime(processes, n, bt, quantam):
    wt=[0]*n
    tat=[0]*n

    #function to find waiting time
    findWatingTime(processes,n,bt,wt,quantam)

    #function to find turnaround time
    findTurnaroundTime(processes,n,bt,wt,tat)

    #Display processes along with all details
    print("processes burst time ","turn-around time","waiting time")
    total_wt=0
    total_tat=0
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print(" ", i+1, "\t\t", bt[i], "\t", wt[i], "\t\t\t", tat[i])
    print("\nAverage waiting time=%.5f" %(total_wt/n))
    print("Average turnaround time=%.5f"%(total_tat/n))



if __name__ == "__main__":
    proc=[1,2,3,4,5,6]
    n=6
    burst_time=[10,5,8,13,13,2]
    quantam=2;
    findAvgTime(proc,n,burst_time,quantam)

