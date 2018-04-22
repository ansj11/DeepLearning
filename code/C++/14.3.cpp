#include <pthread.h>
#include <iostream>

void* PrintAs(void* unused)
{
	while(true) std::cerr<<'a';
	return NULL;
}

void* PrintZs(void* unused)
{
	while(true) std::cerr<<'z';
	return NULL;
}

int main()
{
	pthread_t thread_id;
	pthread_create(&thread_id,NULL,&PrintAs,NULL);
	PrintZs(NULL);
	return 0;
}

/*int pthread_create(pthread_t*thread,const pthread_attr_t* attr,void*(*start_routine)(void*),void* arg);*/
