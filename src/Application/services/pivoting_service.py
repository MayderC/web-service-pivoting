from ..helper_maths.parcial import parcial as helper_parcial
from ..helper_maths.staggered import staggered as helper_staggered
from ..helper_maths.total import total as helper_total

class PivotingService: 
  def __init__(self):
    pass

  def parcial(sefl, data):
    return helper_parcial(data.matrix, data.vector, data.unknowns)

  def staggered(self, data):
    return helper_staggered(data.matrix, data.vector, data.unknowns)

  def total(self, data):
    return helper_total(data.matrix, data.vector, data.unknowns)