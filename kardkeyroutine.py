from routines import Routine

@Routine(60)
def my_routine_task(b):
        print(b)



my_routine_task('Hello!')
my_routine_task('Yay!')