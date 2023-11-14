//I confirm that this assignment is my own work. Where I have referred to sources, I have provided citations as comments in the code.

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
//#include <bits/stdc++.h>

using namespace std;


class articles
{
public:
  string title;
  string abstract;
  string keywords;
  string author;
  string date;
  string subsection;
  string end;
};

  //creating an array to save articles
  articles a[100];
  int nums;
  string lines;

  void load(void)
  {  //string to copy file into
      string line;  
    //open file
    fstream file("Sample.txt");

    //if file doesn't open display error message
    if (!file) 
    { 
      cout << "Error opening file" << endl;
      exit(0);
      
    }
    //searching strings in file
    for (int i = 0; !file.eof(); i++) 
    {
      getline(file, line);
      if (line == "") 
      { //if true, save line into class
        getline(file, line); // get the next line 
        //get title from file
        a[nums].title = line; // save first line into class
        a[nums].title = a[nums].title + lines;
        //get abstract and save to class
        getline(file, line); //ignore empty line
        getline(file, line);
        a[nums].abstract = line; // saves abstract in class
        a[nums].abstract = a[nums].abstract + lines;
        //get keywords
        getline(file, line); 
        getline(file, line);
        a[nums].keywords = line; // save in class
        a[nums].keywords = a[nums].keywords + lines;
  
        //get authore
        getline(file, line); 
        getline(file, line);
        a[nums].author = line; //save in class
        a[nums].author = a[nums].author + lines;
  
        //get date
        getline(file, line);
        a[nums].date = line; // save in class
        a[nums].date = a[nums].date + lines;

        //get sections
        getline(file, line); 
        getline(file, line);
        a[nums].subsection = line; // save in class
        a[nums].subsection = a[nums].subsection + lines;
  
       a[nums].end = "------------------------------------\n";
  
        nums++; // counts        
      }
    }

  file.close();//close file
  }

//display all artciles
void display(void)
{
  for (int j = 0; j < nums; j++) 
  {
    //using the articles saved into the class through the array
    cout << a[j].title;
    cout << a[j].abstract;
    cout << a[j].keywords;
    cout << a[j].author;
    cout << a[j].date;
    cout << a[j].subsection;
    cout << a[j].end;
    
  }
}

//first article tiltle
void article1(void)
{
  for (int j = 0; j < 1; j++) 
  {
    cout << a[j].title<<endl; //display title
  }
}

//second article
void article2(void)
{
  for (int j = 1; j < 2; j++)
  {
    cout << a[j].title<<endl;//display title
   
  }
}

//third article
void article3(void)
{
  for (int j = 2; j < 3; j++) 
  {
    cout << a[j].title<<endl;//display title
  }
}

//add article to file
void add(void)
{
  
  cout<<"Enter Title of article:  ";
  cin>>a[nums].title;
  a[nums].title = a[nums].title + lines;
  //title of article saved to class
  
  cout<<"Enter Abstract of article:  ";
  cin>>a[nums].abstract;
  a[nums].abstract = a[nums].abstract + lines;
  //abstract save to class
  
  cout<<"Enter Keywords of article:  ";
  cin>>a[nums].keywords;
  a[nums].keywords = a[nums].keywords + lines;
  //keywords saved to class
  
  cout<<"Enter Author of article:  ";
  cin>> a[nums].author;
  a[nums].author = a[nums].author + lines;
  //author saved to file
  
  cout <<"Enter Last edited date of article:  ";
  cin>> a[nums].date;
  a[nums].date = a[nums].date + lines;
  //date last edited saved to class
  
  cout<<"Enter subsection titles of article:";
  cin>>a[nums].subsection;
  a[nums].subsection = a[nums].subsection + lines;
  //subsection saved to file
  
  a[nums].end= "------------------------------------\n";
  
}

//functions to delete file
void deletearticle(void)
{
  fstream inputFile("Sample.txt");
  string option;
  cout<<"Once you delete this file, you can't use it again"<<endl;
  cout<<"Are you sure you want to delete this file:"<<endl;
  
  cin>>option;
  if(option == "Yes" || option == "yes")
  {
    remove("Sample.txt");//deletes file
  }
  else
  {
    cout<<"Better option"<<endl;
  }
}

//search for a word in file
void search(void)
{
  fstream inputFile("Sample.txt");

    if (!inputFile) //checking for error when opeing file
    {
        cerr << "Error opening file." << endl;
    }

    string SearchWord;
    cout << "Enter the word to search: ";
    cin >> SearchWord;

    string word;

    
    bool found = false; //declaring a bool function

 // reads the file word by word and stores each word.
    while (inputFile >> word) 
    {
        if (word == SearchWord) 
        {
            found = true;//if word is founf, found becomes true
            break;
        }
        
    }
    if (found) 
    {
        cout << "Word found "  << endl;
    } 
    else
    {
        cout << "Word not found." << endl;
    }

    inputFile.close();//close file
  
}

//counting letters in the article
void count(void)
{
  fstream inputFile("Sample.txt");

    if (!inputFile) 
    {
        cerr << "Error opening file." << endl;
        
    }
  int index = 0; //initializing count
  int index2 =0;  //initializing count
  int index3 = 0;  //initializing count
  string word;
  int numoflines;
  int numoflines2;
  int numoflines3;
  while (getline (inputFile, word)) 
  {
    while(inputFile >> word) 
    {
     if(numoflines>=1 && numoflines <=11)//lines where article is found
      {
        numoflines++;
      }
    index++;
      
    }
  
  }
  while (getline (inputFile, word)) 
  {
    while(inputFile >> word) 
    {
     if(numoflines2>=14 && numoflines2 <=24)//lines where article is found
      {
        numoflines2++;
      }
    index2++;
      
    }
  }
  while (getline (inputFile, word)) 
  {
    while(inputFile >> word) 
    {
     if(numoflines3>=27 && numoflines3<=37)//lines where article is found
      {
        numoflines3++;
      }
    index3++;
      
    }
  }
    if(index < index2 && index < index3)//if article 1 is less
    {
      cout<<"Article 1 (Computational Neuroscience) had the least letters"<<endl;
    }
    else if (index2 < index && index2 < index3)//if article 2 is less
    {
      cout<<"Article 2 (The renaissance) has the least letters";
    }
    else //if article 3 is less
    {
      cout<<"Article 3 (The American civil war) has the least letters";
    }
 inputFile.close();
     
}
//save edited sile`
void save(void)
{
  fstream rewrite("Sample.txt");

  if(!rewrite)
  {//error checking
    cout<<"Error opening file for output<<endl";
    exit(0);
    
  } 
  for (int j = 0; j < nums; j++) 
  {
    rewrite << a[j].title;
    rewrite<<" ";
    rewrite << a[j].abstract;
    rewrite << a[j].keywords;
    rewrite << a[j].author;
    rewrite << a[j].date;
    rewrite << a[j].subsection;
    rewrite << a[j].end;
  }
  rewrite.close();//close file
  cout<<"File updated!";
  
}

int main()
{
   load();
  int choice;
 
  while(true)
  {
    cout<<"What would you like to do with the file (Select a number):"<<endl;
    cout<<"1.Display File"<<endl;
    cout<<"2.Display titles"<<endl;
    cout<<"3.Add to file"<<endl;
    cout<<"4.Search file"<<endl;
    cout<<"5.Update file"<<endl;
    cout<<"6. Article with the least letters"<<endl;
    cout<<"7.Display edited file"<<endl;
    cout<<"8.Delete file"<<endl;
    cin>>choice; 
    if(choice==1)
    {
      display();
      cout<<endl;
    }
    else if (choice ==2)
    {
      article1();
      cout<<endl;
      article2();
      cout<<endl;
      article3();
      cout<<endl;
    }
    else if (choice ==3)
    {
      add();
      cout<<endl;
    }
    else if(choice==4)
    {
      search();
      cout<<endl;
    }
    else if(choice ==5)
    {
      save();
      cout<<endl;
    }
    else if(choice ==6)
    {
      count();
      cout<<endl;
    }
    else if(choice ==7)
    {
      display();
      cout<<endl;
    }
    else if(choice ==8)
    {
      deletearticle();
      cout<<endl;
    }
    else
    {
      break;
    }
  }
  
}
//references:https://techindetail.com/search-word-in-text-cpp/
//https://www.programiz.com/cpp-programming/library-function/cstdio/remove#:~:text=The%20remove()%20function%20in,in%20the%20cstdio%20header%20file.
//https://replit.com/@ReemaTariq/structFile01#main.cpp


