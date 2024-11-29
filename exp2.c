/*Write a C program that contains a string (char pointer) with a value “Hello world”. The 
program should AND or and XOR each character in this string with 127 and display the 
result.*/

#include <stdio.h>
int main() {
 char *str = "Hello world";
 int i;
 printf("Original string: %s\n", str);
 printf("AND with 127: ");
 for (i = 0; str[i] != '\0'; i++) {
 printf("%c", str[i] & 127);
 }
 printf("\n");
 printf("OR with 127: ");
 for (i = 0; str[i] != '\0'; i++) {
 printf("%c", str[i] | 127);
 }
 printf("\n");
 printf("XOR with 127: ");
 for (i = 0; str[i] != '\0'; i++) {
 printf("%c", str[i] ^ 127);
 }
 printf("\n");
 return 0;
}