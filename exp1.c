/*Write a C program that contains a string (char pointer) with a value “Hello world”. The 
program should XOR each character in this string with 0 and displays the result.*/

#include <stdio.h>
int main() {
 char str[] = "Hello world";
 for (int i = 0; str[i] != '\0'; i++) {
 str[i] = str[i] ^ 0;
 }
 printf("Result after XOR with 0: %s\n", str);
 return 0;
}