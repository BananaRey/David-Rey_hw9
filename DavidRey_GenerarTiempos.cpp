#include <iostream>
#include <cstdlib>
#include <ctime>


using std::cout;
using std::endl;
//inicializo las funciones
int fibonacci(int N);
float get_time(int N);
// Construyo la funcion de fibonnaci
int fibonacci(int N){

//se hacen los casos base
if(N==0){
	return(0);
}
else if(N==1){
	return(1);
}
//llamo recursivamente la funcion
else{
	return (fibonacci(N-1)+fibonacci(N-2));
}
}
//construyo la funcion del tiempo

float get_time(int N){
clock_t t;
t = clock();
fibonacci(N);
t = clock() - t;
float time = ((float)t)/CLOCKS_PER_SEC;
	return(time);
}

// se hace el main 
int main(){
//declari variable de tiempo que se va a devolver
float t=0;
//se suma al t el tiempo que toma calcular fibonacci para cada i hasta 34
for(int i = 0; i < 35; ++i){
t=t+get_time(i);
}
cout <<t<< endl;
return 0;
}

