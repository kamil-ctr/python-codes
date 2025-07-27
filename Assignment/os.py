#include <stdio.h>

// Function to calculate waiting time for FCFS (First Come First Serve)
void fcfs(int n, int bt[], int wt[]) {
    wt[0] = 0; // The first process has no waiting time
    // Calculate waiting time for each process (after the first)
    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1]; // Waiting time of the current process is the sum of the previous process's waiting time and its burst time
    }
}

// Function to calculate Round Robin (RR) scheduling
void roundRobin(int n, int bt[], int quantum) {
    int rem_bt[n], wt[n], tat[n];  // Arrays for remaining burst times, waiting times, and turnaround times
    int time = 0;  // Variable to track the total time elapsed

    // Initialize remaining burst times with the burst times of processes
    for (int i = 0; i < n; i++) rem_bt[i] = bt[i];

    // Process all the tasks until all remaining burst times are zero
    while (1) {
        int done = 1; // Flag to check if all processes are done
        for (int i = 0; i < n; i++) {
            if (rem_bt[i] > 0) {  // If a process still has remaining burst time
                done = 0;  // Not all processes are finished
                if (rem_bt[i] > quantum) {
                    time += quantum;  // Execute the process for a time quantum
                    rem_bt[i] -= quantum;  // Decrease the remaining burst time
                } else {
                    time += rem_bt[i];  // Execute the remaining burst time of the process
                    wt[i] = time - bt[i];  // Calculate waiting time for the process
                    rem_bt[i] = 0;  // Set remaining burst time to zero
                }
            }
        }
        if (done) break;  // Exit the loop if all processes are finished
    }

    // Calculate turnaround time and print results
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];  // Turnaround time is the sum of burst time and waiting time
        // Print the waiting time and turnaround time for each process
        printf("Process %d: Waiting Time = %d, Turnaround Time = %d\n", i + 1, wt[i], tat[i]);
    }
}

// Function to calculate Priority Scheduling
void priorityScheduling(int n, int bt[], int pri[]) {
    int wt[n], tat[n], p[n];  // Arrays for waiting times, turnaround times, and process indices

    // Initialize process indices
    for (int i = 0; i < n; i++) p[i] = i;

    // Sort the processes by priority (ascending order) using bubble sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (pri[j] > pri[j + 1]) {  // If the current process has a higher priority than the next
                // Swap the priorities
                int temp = pri[j];
                pri[j] = pri[j + 1];
                pri[j + 1] = temp;

                // Swap the burst times accordingly
                temp = bt[j];
                bt[j] = bt[j + 1];
                bt[j + 1] = temp;

                // Swap the process indices to maintain correct order
                temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }

    // Call FCFS to calculate waiting times after sorting by priority
    fcfs(n, bt, wt);

    // Calculate turnaround time and print results
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];  // Turnaround time is the sum of burst time and waiting time
        // Print the priority, waiting time, and turnaround time for each process
        printf("Process %d: Priority = %d, Waiting Time = %d, Turnaround Time = %d\n", p[i] + 1, pri[i], wt[i], tat[i]);
    }
}

int main() {
    int n, choice, quantum;

    // Ask the user to enter the number of processes
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    // Declare arrays for burst time and priority for each process
    int bt[n], pri[n];

    // Get the burst time for each process
    printf("Enter burst time for each process:\n");
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d", &bt[i]);  // Read burst time for each process
    }

    // Ask the user to choose a scheduling algorithm
    printf("Choose Scheduling Algorithm:\n");
    printf("1. First Come First Serve (FCFS)\n");
    printf("2. Round Robin (RR)\n");
    printf("3. Priority Scheduling\n");
    scanf("%d", &choice);  // Read the user's choice

    // Switch case to choose the appropriate scheduling algorithm
    switch (choice) {
        case 1: {
            // Calculate and print the waiting time and turnaround time for FCFS
            int wt[n], tat[n];
            fcfs(n, bt, wt);  // Call the FCFS function
            for (int i = 0; i < n; i++) {
                tat[i] = bt[i] + wt[i];  // Calculate turnaround time
                // Print waiting time and turnaround time
                printf("Process %d: Waiting Time = %d, Turnaround Time = %d\n", i + 1, wt[i], tat[i]);
            }
            break;
        }
        case 2:
            // Ask for the time quantum for Round Robin
            printf("Enter time quantum: ");
            scanf("%d", &quantum);  // Read the time quantum
            roundRobin(n, bt, quantum);  // Call the Round Robin function
            break;
        case 3:
            // Get the priority for each process
            printf("Enter priority for each process:\n");
            for (int i = 0; i < n; i++) {
                printf("Process %d: ", i + 1);
                scanf("%d", &pri[i]);  // Read the priority for each process
            }
            priorityScheduling(n, bt, pri);  // Call the Priority Scheduling function
            break;
        default:
            // Print an error message if the input is invalid
            printf("Invalid choice!\n");
    }

    return 0;  // Exit the program successfully
}