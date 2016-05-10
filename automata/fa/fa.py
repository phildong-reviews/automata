#!/usr/bin/env python3
"""Classes and methods for working with all finite automata."""

import abc

import automata.shared.exceptions as exceptions


class FA(metaclass=abc.ABCMeta):
    """An abstract base class for finite automata."""

    @abc.abstractmethod
    def __init__(self, **kwargs):
        """Initialize a complete finite FA."""
        pass

    def _validate_transition_start_states(self):
        """Raise an error if transition start states are missing."""
        missing_states = self.states - set(self.transitions.keys())
        if missing_states:
            raise exceptions.MissingStateError(
                'transition start states are missing ({})'.format(
                    ', '.join(missing_states)))

    def _validate_transition_end_states(self, path_states):
        """Raise an error if transition end states are invalid."""
        invalid_states = path_states - self.states
        if invalid_states:
            raise exceptions.InvalidStateError(
                'transition end states are not valid ({})'.format(
                    ', '.join(invalid_states)))

    def _validate_initial_state(self):
        """Raise an error if an initial state is invalid."""
        if self.initial_state not in self.states:
            raise exceptions.InvalidStateError(
                '{} is not a valid initial state'.format(self.initial_state))

    def _validate_final_states(self):
        """Raise an error if any final states are invalid."""
        invalid_states = self.final_states - self.states
        if invalid_states:
            raise exceptions.InvalidStateError(
                'final states are not valid ({})'.format(
                    ', '.join(invalid_states)))

    @abc.abstractmethod
    def validate_self(self):
        """Return True if this FA is internally consistent."""
        pass

    def _validate_input_symbol(self, symbol):
        """Raise an error if the given input symbol is invalid."""
        if symbol not in self.input_symbols:
            raise exceptions.InvalidSymbolError(
                '{} is not a valid input symbol'.format(symbol))

    @abc.abstractmethod
    def validate_input(self, input_str):
        """Check if the given string is accepted by this FA."""
        pass

    def copy(self):
        """Create an exact copy of the FA."""
        return self.__class__(self)

    def __eq__(self, other):
        """Check if two automata are equal."""
        return self.__dict__ == other.__dict__
