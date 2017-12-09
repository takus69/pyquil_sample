# coding: utf-8

'''
pyquilで量子コンピュータの実装を行うためのモジュール
'''

from pyquil.quil import Program
import pyquil.api as api
from pyquil.gates import I, X


class qcuit:
  '''
  量子コンピュータの回路を作成するためのクラス
  '''
  def __init__(self):
    self.qvm = api.QVMConnection()
  
  def set_initial_value(self, *args):
    '''
    入力する量子ビットの初期値|0> or |1>を設定する
    入力値は0 or 1
    '''
    for arg in args:
      if arg not in [0, 1]:
        raise(Exception('Unexpected value. Included value except 0 and 1.'))
    self.p = Program()
    self.classical_regs = []

    for i in range(len(args)):
      if args[i] == 0:
        self.p.inst(I(i))
      else:
        self.p.inst(X(i))
      self.classical_regs.append(i)

  def run(self):
    '''
    入力の量子ビットに設定した量子論理ゲートを作用させて、出力結果を得る
    '''
    for reg in self.classical_regs:
      self.p.measure(reg, reg)
    return self.qvm.run(self.p, self.classical_regs)

  def inst(self, gate):
    '''
    量子論理ゲートを設定する
    pyquil.quil.Program.inst()
    と使い方は同じ
    '''
    self.p.inst(gate)

  def get_wavefunction(self):
    return self.qvm.wavefunction(self.p)
