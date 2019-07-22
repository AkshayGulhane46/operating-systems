# function to find waiting time for all the processes
def findWaitingTime(processes, n, bt, wt):
    # waiting time for first process is 0
    wt[0] = 0
    # calculate waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


# function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
    # calculate turnaround time by adding bt[i]+wt[i]

    for i in range(n):
        tat[i] = bt[i] + wt[i]


# function to calculate average time
def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    # function to find waiting time of all processes
    findWaitingTime(processes, n, bt, wt)

    # function to find turnaround time
    findTurnAroundTime(processes, n, bt, wt, tat)

    # display processes along with all details
    print("processes Burst Time " + " waiting time " + "turn around time")

    # calculate total waiting time and total turn around time
    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t\t" + str(tat[i]))

    print("average waiting time is " + str(total_wt / n))
    print("average turnaround time is " + str(total_tat / n))


# source code
if __name__ == "__main__":   #while writing main write carefully
    processes = [1, 2, 3, 4, 5, 6, 7]
    n = len(processes)

    burst_time = [10, 5, 8, 8, 7, 4, 3]

    findavgTime(processes, n, burst_time)
