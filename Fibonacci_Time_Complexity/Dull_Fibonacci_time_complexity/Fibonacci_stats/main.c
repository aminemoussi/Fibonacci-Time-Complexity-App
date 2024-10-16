#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int fibonacci(int target){      //recursion is horrible for this kind of problem
    if (target == 1) {
        return 1;
    } else if (target == 0) {
        return 0;
    } else {
        return (fibonacci(target - 1) + fibonacci(target - 2));
    }

}


void file_maker(FILE *file_append, int i, double value, float time_spent){
    fprintf(file_append, "%d, %d, %f\n", i, value, time_spent);
}

int main(int argc, char *argv[]){
    clock_t begin, end, total_beg, total_end;
    double time_spent;
    const char *file_name = "Fibonacci_calc_results.txt";
    int value;

    if (argc != 2){
        printf("Error: %s the last element of the Fibonacci Sequence must be given.", argv[0]);
        return 1;
    }

    int target = atoi(argv[1]);

    if (target < 0){
        printf("Error: '%i' the last element of the Fibonacci Sequence must be Positive.", target);
        return 1;
    }

    //printf("Where to stop the calcuation: \n");
    //scanf("%i", &target);

    //printf("%i", target);

    total_beg = clock();

    FILE *file_write;

    FILE *file_append;

    file_write = fopen(file_name, "w");

    file_append = fopen(file_name, "a");

    //fprintf(file_write, "Hi there..");

    //fprintf(file_append, "Hi there..again");

    //fprintf(file_write, "Hi ");

    for (int i = 0; i <= target; i++){
        begin = clock();     //clock cycles
        value = fibonacci(i);
        printf("**Fibonacci of %i is: %i", i, value);
        end = clock();
        time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
        printf("...Execution time: %.6f", time_spent);
        printf("\n");
        file_maker(file_append, i, value, time_spent);
    }



    fclose(file_write);
    fclose(file_append);

    total_end = clock();

    double total = (double)(total_end - total_beg)/CLOCKS_PER_SEC ;
    printf("*****Total Execution time: %.6f", total);

}