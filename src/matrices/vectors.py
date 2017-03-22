def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
      >>> a = [1, 2, 3]
      >>> b = [1, 1, 1]
      >>> add_vectors(a, b)
      [2, 3, 4]
      >>> a
      [1, 2, 3]
      >>> b
      [1, 1, 1]
    """
    return [u[i] + v[i] for i in range(len(u))]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
