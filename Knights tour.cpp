#include<iostream>
#include <iomanip>

using namespace std;

//defining the size of the chessboard
//the defines the board size, change it for a different size
#define K 8 

//function prototypes
//int moves();
//bool checks();
//void displaysoln();
int solve();




//checks if the movement is in range, and if that position has been marked
bool checks(int x, int y, int solns[K][K]) 
{     
   return ( x >= 0 && x < K && y >= 0 && y < K && solns[x][y] == -1);
}

//function to display the matrix of the solution, displays the matrix
void displaysoln(int solns[K][K]) 
{
  for (int x = 0; x < K; x++) 
  {
    for (int y = 0; y < K; y++)
      cout << setw(4) << solns[x][y] << " ";
    cout << endl;
   }
}
   
// function to solve knight's tour problem 
int moves(int x, int y, int movei, int solns[K][K], int xmove[], int ymove[])
{
  int k, next_x, next_y;
  if (movei == K * K)
    return 1;
  //Trying all the moves from the current coordinates (x, y) 
  for (k = 0; k < 8; k++) 
  {
    next_x = x + xmove[k];// next move is the current position plus the next coordinate move of x
    next_y = y + ymove[k];// next move is the current position plus the next coordinate move of y
    if (checks(next_x, next_y, solns)) 
    {
      solns[next_x][next_y] = movei;
      if (moves(next_x, next_y, movei + 1, solns,xmove, ymove) == 1)
        return 1;
      else
      {
     // backtracking
        solns[next_x][next_y] = -1;
      }
    }
  }
    return 0;
}

// This function uses the moves function to carry out the knight's tour, prints out theres no solution for this a solution cannot be found
int solve()
{
  int solns[K][K];
  // Initializing a solution matrix 
  for (int x = 0; x < K; x++)
    for (int y = 0; y < K; y++)
      solns[x][y] = -1;
  
  //defining the x,y coordinate moves for the knight
  int ymove[8] = { 1, 2, 2, 1, -1, -2, -2, -1 };
  int xmove[8] = { 2, 1, -1, -2, -2, -1, 1, 2 };
  
  // Knight starts at the coordiante (0,0)
  solns[0][0] = 0;
  
  // Start from (0,0) aned explores all possible movements
  if (moves(0, 0, 1, solns, xmove, ymove) == 0) 
  {
    //if no solution can be found 
    cout << "No solution for this";
    return 0;
  }
  else
  {
    //if solution canm be found
    displaysoln(solns);
    return 1;
  }
}

// main function, calling the solve() function
int main()
{
  // calling the function
  solve();
}

  
