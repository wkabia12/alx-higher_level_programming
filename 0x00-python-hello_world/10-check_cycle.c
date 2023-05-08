#include "lists.h"
/**
 *check_cycle - checks if there is loop in singly linked list
 *@list: list arguement
 *Return: 1 if loop else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *sp, *fp;

	sp = list;
	fp = list;

	while (sp && fp && fp->next)
	{
		sp = sp->next;
		fp = fp->next->next;
		if (sp == fp)
			return (1);
	}
	return (0);
}
