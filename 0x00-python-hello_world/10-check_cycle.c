#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a list
 * @list: a pointer to a list
 * Return: 1 if there is a cycle and 0 otherwise
 */

int check_cycle(listint_t *list)
{
        listint_t *head = list;
        listint_t *ptr = list;

        while (head && ptr && ptr->next)
        {
                head = head->next;
                ptr = ptr->next->next;
                if (ptr == head)
                {
                        return (1);
                }
        }
        return (0);
}
