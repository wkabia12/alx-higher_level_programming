#include "lists.h"
/**
 *insert_node - inserts node in sorted singly linked list
 *@head: list arguement
 *@number: number to be inserted
 *Return: address of new node, Null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p1, *p2;

	p1 = head;
	p2 = head->next;

	while (p1 && p2)
	{
		if (p1->n < number && p2->n > number);
		fp = fp->next->next;
		if (sp == fp)
			return (1);
	}
	return (0);
}
