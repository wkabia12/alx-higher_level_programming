#include "lists.h"
/**
 *is_palindrome - checks palindrome in singly linked list
 *@head: list arguement
 *Return: 1 if True else 0
 */
int is_palindrome(listint_t **head)
{
	int n;
	listint_t *slw, *fst;
	listint_t *rev_2nd_half;
	listint_t *p1, *p2;

	n = count(*head);

	if (n <= 1)
		return (1);

	slw = *head;
	fst = *head;

	while (fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
	}
	if (n % 2 == 1)
		slw = slw->next;


	rev_2nd_half = rev_list(slw);
	p1 = *head;
	p2 = rev_2nd_half;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}
/**
 *count - checks number of nodes in singly linked list
 *@head: list arguement
 *Return: count of nodes
 */
int count(listint_t *head)
{
	int c;

	c = 0;

	while (head != NULL)
	{
		c++;
		head = head->next;
	}
	return (c);
}
/**
 *rev_list - reverse singly linked list
 *@head: list arguement
 *Return: pointer to rev list
 */
/* count the number of nodes in the linked list */
listint_t *rev_list(listint_t *head)
{
	listint_t *p, *c, *n;

	p = NULL;
	c = head;
	n = NULL;

	while (c != NULL)
	{
		n = c->next;
		c->next = p;
		p = c;
		c = n;
	}
	return (p);
}
