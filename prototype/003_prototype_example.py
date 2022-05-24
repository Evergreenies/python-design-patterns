# Filename      :       003_prototype_example.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22
import copy


class SelfReferencingEntity(object):
    """Self referencing"""

    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        """Reinitializing parent"""
        self.parent = parent


class SomeComponent(object):
    """
    Python provides its own interface of prototype via `copy.copy` and
    `copy.deepcopy` functions. And any class that wants to implement
    custom implementations have to override `__copy__` and `__deepcopy__`
    member functions.
    """

    def __init__(self, some_init, some_list_of_objects, some_circular_ref):
        self.some_init = some_init
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Create a shallow copy. This method will be called whenever someone
        calls `copy.copy` with this object and the returned value is returned
        as the new shallow copy.
        :return:
        :rtype:
        """

        # First, let's create copies of nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of
        # the nested objects.
        new = self.__class__(
            self.some_init, some_list_of_objects, some_circular_ref
        )
        return new

    def __deepcopy__(self, memo: dict):
        """
        Create a deep copt. This method will be called whenever someone calls
        `copy.deepcopy`  with this object and returned value is required as
        the new deep copy.

        What is the use of argument `memo`? This is the dictionary that is
        used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all `deepcopy` calls you
        make in the `__deepcopy__` implementations to prevent infinite
        recursion.

        :param memo:
        :type memo:
        :return:
        :rtype:
        """

        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone object itself, using the prepared clones of
        # the nested objects.
        new = self.__class__(
            self.some_init, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == '__main__':
    _list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    _circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, _list_of_objects, _circular_ref)
    _circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)
    shallow_copied_component.some_list_of_objects.append('another object')
    if component.some_list_of_objects[-1] == 'another object':
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ This shows that deep-copied objects contain same reference, they "
        "are not cloned repeatedly."
    )
