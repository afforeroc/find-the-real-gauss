#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find The Real Gauss!"""

def iterative_sum(num_list):
    """Calculate the sum using a for loop."""
    total = 0
    for num in num_list:
        total += num
    return total


def python_sum(num_list):
    """Calculate the sum using standart 'sum' function of python."""
    return sum(num_list)


def fake_gauss_1(num_list):
    """Fake Gauss v1"""
    a = num_list[0]
    b = num_list[-1]
    n = b - a + 1
    return int(n * (n + 1)/2)


def fake_gauss_2(num_list):
    """Fake Gauss v3"""
    a = num_list[0]
    b = num_list[-1]
    return int(b * (a + b)/2)

   
def fake_gauss_3(num_list):
    """Fake Gauss v3"""
    a = num_list[0]
    b = num_list[-1]
    n = b - a + 1
    return int(n * (b + 1)/2)

   
def the_real_gauss(num_list):
    """Real Gauss"""
    return '?'
  
  
def compare_algorithms(a, b):
    print('//////////////////////////////')
    list_of_numbers = list(range(a, b + 1))
    n = len(list_of_numbers)
    print('List: [{}, {}, ..., {}, {}]'.format(a, a + 1, b - 1, b))
    print('Size of list: {}\n'.format(n))
    total1 = iterative_sum(list_of_numbers)
    total2 = python_sum(list_of_numbers)
    total3 = fake_gauss_1(list_of_numbers)
    total4 = fake_gauss_2(list_of_numbers)
    total5 = fake_gauss_3(list_of_numbers)
    total6 = the_real_gauss(list_of_numbers)
    print('Algorithm\tSum')
    print('---------------------')
    print('Iterative\t{}'.format(total1))
    print('Standart\t{}'.format(total2))
    print('Fake Gauss 1\t{}'.format(total3))
    print('Fake Gauss 2\t{}'.format(total4))
    print('Fake Gauss 3\t{}'.format(total5))
    print('The Real Gauss\t{}'.format(total6))


def main():
    """Compare different algorithms that sum all integers of an interval."""
    print("==== Find The Real Gauss! ====")
    compare_algorithms(1, 100)
    compare_algorithms(101, 200)


if __name__ == '__main__':
    main()
