
prime(int number)
for i=0;i=1000;i++{
    if number%i == 0:
        sout("not prime")
        break

sout("prime")
}

// int i = 0;
// while (i < 5) {
//   cout << i << "\n";
//   i++;
// }

// The Main Method
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	printf( "\nHello World\n\n" );
// }

// Command Line Arguments
// Try running this program with some command line parameters.
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	// Prints each argument on the command line.
// 	for( int i = 0; i < argc; i++ )
// 	{
// 		printf( "arg %d: %s\n", i, argv[i] );
// 	}
// }

// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	int x;
// 	int y;
	
// 	// ensure the correct number of parameters are used.
// 	if ( argc == 3 ) 
// 	{
// 		x = atoi( argv[1] );
// 		y = atoi( argv[2] );
		
// 		printf( "%d + %d = %d\n", x, y, x + y );
		
// 		// Will print something like: 3 + 2 = 5
// 	}

// }

// The For Loop
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	int i;
	
// 	for( i = 0; i < 10; i++ ) 
// 	{
// 		printf( "Iteration %d\n", i );
// 	}
// }
// The While Loop
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	int i = 0;

// 	while ( i < 10 )
// 	{
// 		i++;
// 		printf( "Iteration %d\n", i );
// 	}

// }
// The If Statement
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	for ( i = 0; i < 10; i++ )
// 	{
// 		if ( i == 1 ) {
			
// 			printf( "i = 1\n" );
			
// 		} else if ( ( i == 2 ) || ( i == 3 ) ) {
			
// 			printf( "i = 2 or 3\n" );
			
// 		} else {
			
// 			printf( "i = %d\n", i );
			
// 		}
// 	}
// }
// Arrays
// #include <stdio.h>
// int main( int argc, const char* argv[] )
// {
// 	int numbers[10];
// 	int i;
	
// 	for ( i = 0; i < 10; i ++ )
// 	{
// 		numbers[i] = i * i;
// 		// Note that arrays are zero based
// 	}
	
// 	for ( i = 0; i < 10; i ++ )
// 	{
// 		printf( "numbers[%d] = %d", i, numbers[i] );
// 	}

// }