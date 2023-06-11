#include "lists.h"

/**
 * is_palindrome - checks if palindrome
 * @head: listint_t
 * Return: int
*/

int is_palindrome(listint_t **head)
{
	int *tab;
	int i = 0, n = 0;
	listint_t *current = *head;

	while(current)
	{
		current = current->next;
		n++;
	}
	if(n == 0)
		return (1);
	tab = malloc(sizeof(int) * n);
	current = *head;
	while(current)
	{
		tab[i] = current->n;
		current = current->next;
		i++;
	}
	for(i = 0; i < n; i++)
		if(tab[i] != tab[n - i - 1])
			return (0);
	return (1);
}
