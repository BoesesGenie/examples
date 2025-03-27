/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
  let mem = 0;
  const sum = l1.val + l2.val;
  let next1 = l1.next;
  let next2 = l2.next;
  const result = new ListNode(sum % 10, undefined);
  let current = result;

  mem = sum >= 10 ? 1 : 0;

  while(next1 || next2) {
    const num1 = next1 ? next1.val : 0;
    const num2 = next2 ? next2.val : 0;
    const sum = num1 + num2 + mem;

    current.next = new ListNode(sum % 10, undefined);
    current = current.next;

    mem = sum >= 10 ? 1 : 0;

    next1 && (next1 = next1.next);
    next2 && (next2 = next2.next);
  }

  if (mem) {
    current.next = new ListNode(mem, undefined);
  }

  return result;
};
