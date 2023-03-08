#include "lists.h"

/**
 * check_cycle - function to check if singly linked list has a cycle
 * @list: input list
 * Return: 0 if no cycle and 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = second = list;

	if (!list)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
