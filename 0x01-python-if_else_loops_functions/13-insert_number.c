#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to first element
 * @number: input number
 * Return: address of new node, NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_ptr;
       
	new_ptr = *head;
	if (*new_ptr == NULL)
		return (:x
				NULL);

	
