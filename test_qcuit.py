# coding: utf-8

import math
import unittest

from qcuit import qcuit

from pyquil.gates import I, H, CNOT, X, Y, Z, SWAP


class testQcuit(unittest.TestCase):
  def setUp(self):
    self.q = qcuit()

  def test_input_and_output(self):
    self.q.set_initial_value(0, 1)
    results = self.q.run()
    self.assertListEqual([[0, 1]], results)

    self.q.set_initial_value(1, 0)
    results = self.q.run()
    self.assertListEqual([[1, 0]], results)

  def test_exptected_input_value(self):
    with self.assertRaises(Exception):
      self.q.set_initial_value(2)

  def test_pauli_x(self):
    self.q = qcuit()
    self.q.set_initial_value(0)
    self.q.inst(X(0))
    results = self.q.run()
    self.assertListEqual([[1]], results)

    self.q.set_initial_value(1)
    self.q.inst(X(0))
    results = self.q.run()
    self.assertListEqual([[0]], results)

  def test_pauli_y(self):
    self.q = qcuit()
    self.q.set_initial_value(0)
    self.q.inst(Y(0))
    results = self.q.run()
    self.assertListEqual([[1]], results)

    self.q.set_initial_value(1)
    self.q.inst(Y(0))
    results = self.q.run()
    self.assertListEqual([[0]], results)
    
  def test_pauli_z(self):
    self.q = qcuit()
    self.q.set_initial_value(0)
    self.q.inst(Z(0))
    results = self.q.run()
    self.assertListEqual([[0]], results)

    self.q.set_initial_value(1)
    self.q.inst(Z(0))
    results = self.q.run()
    self.assertListEqual([[1]], results)

  def test_hadamard(self):
    self.q = qcuit()
    self.q.set_initial_value(0)
    self.q.inst(H(0))
    alpha, beta = self.q.get_wavefunction()
    self.assertAlmostEqual(math.sqrt(1/2), alpha, 6)
    self.assertAlmostEqual(math.sqrt(1/2), beta, 6)

    self.q.set_initial_value(1)
    self.q.inst(H(0))
    alpha, beta = self.q.get_wavefunction()
    self.assertAlmostEqual(math.sqrt(1/2), alpha, 6)
    self.assertAlmostEqual(-math.sqrt(1/2), beta, 6)

  def test_cnot(self):
    self.q = qcuit()
    self.q.set_initial_value(0, 0)
    self.q.inst(CNOT(0, 1))
    results = self.q.run()
    self.assertListEqual([[0, 0]], results)

    self.q.set_initial_value(1, 0)
    self.q.inst(CNOT(0, 1))
    results = self.q.run()
    self.assertListEqual([[1, 1]], results)

    self.q.set_initial_value(0, 1)
    self.q.inst(CNOT(0, 1))
    results = self.q.run()
    self.assertListEqual([[0, 1]], results)

    self.q.set_initial_value(1, 1)
    self.q.inst(CNOT(0, 1))
    results = self.q.run()
    self.assertListEqual([[1, 0]], results)

  def test_swap(self):
    self.q = qcuit()
    self.q.set_initial_value(1, 0)
    self.q.inst(SWAP(0, 1))
    results = self.q.run()
    self.assertListEqual([[0, 1]], results)

    self.q.set_initial_value(0, 1)
    self.q.inst(SWAP(0, 1))
    results = self.q.run()
    self.assertListEqual([[1, 0]], results)

    self.q.set_initial_value(0, 0)
    self.q.inst(SWAP(0, 1))
    results = self.q.run()
    self.assertListEqual([[0, 0]], results)
    
    self.q.set_initial_value(1, 1)
    self.q.inst(SWAP(0, 1))
    results = self.q.run()
    self.assertListEqual([[1, 1]], results)

# CNOTで実装
    self.q.set_initial_value(1, 0)
    self.q.inst(CNOT(0, 1))
    self.q.inst(CNOT(1, 0))
    self.q.inst(CNOT(0, 1))
    results = self.q.run()
    self.assertListEqual([[0, 1]], results)
