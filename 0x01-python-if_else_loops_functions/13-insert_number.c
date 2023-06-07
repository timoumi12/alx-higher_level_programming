#include "lists.h"

/**
 * insert_node - insert n into sorted list
 * @head: node
 * @number: int
 * Return: listint_t
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (current == NULL || current->n >= new->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next && current->next->n < new->n)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
