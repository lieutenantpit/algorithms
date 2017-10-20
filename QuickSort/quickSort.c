#include <stdio.h>
#include <stdlib.h>

#define RECURSION_LIMIT 200000

int count = 0;
int recursion_call = 0;
void quickSort(int *array, int l, int r);
void quickSort2(int *array, int l, int r);
void print_array(int *array, int l, int r);

int main(int argc, char *argv[])
{
   FILE *fd = fopen("QuickSort.txt","r");
   int lines = 0;
   int *array = NULL;
   char ch;
   char el[10] = {0};
   int i = 0;

   if( fd == NULL )
   {
      perror("fopen");
      exit(1);
   }

   while ((ch = fgetc(fd)) != EOF)
   {
      if (ch == '\n')
         lines++;
   }

   array = calloc(lines,sizeof(int));

   if( array == NULL )
   {
      perror("calloc");
      exit(2);
   }
   fseek(fd, 0, SEEK_SET);
   while (fgets(el, 10, fd) != NULL)
   {
      //printf("el is [%s]\n", el);
      array[i] = atoi(el);
      i++;
   }

   print_array(array,0, lines-1);
   printf("total: %d\n", lines);

   quickSort2(array, 0, lines-1);
   print_array(array,0, lines-1);
   printf("swap count: %d\n", count);
   fclose(fd);
   return 0;
}

void quickSort(int *s_arr, int first, int last)
{
    if (first < last)
    {
        int left = first, right = last;
        int pivot = s_arr[first];

        do
        {
            while (s_arr[left] < pivot) left++;
            while (s_arr[right] > pivot) right--;
            if (left <= right)
            {
                int tmp = s_arr[left];
                s_arr[left] = s_arr[right];
                s_arr[right] = tmp;
                left++;
                right--;
            }
        } while (left <= right);
        quickSort(s_arr, first, right);
        quickSort(s_arr, left, last);
    }
    count += last-first-1;
}

void quickSort2(int *s_arr, int first, int last)
{
  recursion_call++;
  if(recursion_call >= RECURSION_LIMIT)
  {
    printf("FAIL. Too many recursion calls:%d\n", recursion_call );
    exit(2);
  }

   if(first < last)
   {
      int i,j;
      int tmp;
      int pivot = s_arr[first];
      
      i = first + 1;
      for(j = first+1; j <= last; j++)
      {
         if(s_arr[j] < pivot)
         {
            tmp = s_arr[i];
            s_arr[i] = s_arr[j];
            s_arr[j] = tmp;
            i++;         
         }
      }
      tmp = s_arr[first];
      s_arr[first] = s_arr[i-1];
      s_arr[i-1] = tmp;

      quickSort2(s_arr, first, i-1);
      quickSort2(s_arr, i, last);

   }
   count += last-first-1;
}

void print_array(int *array, int l, int r)
{
   puts("0 1 2 3 4 5 6 7 8 9");
   for(int i = l; i <= r; i++)
   {
      if(i == r )
         printf("%d\n",array[i]);
      else
         printf("%d ",array[i]);
   }
}