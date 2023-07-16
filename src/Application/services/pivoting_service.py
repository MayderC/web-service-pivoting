from ..helper_maths.parcial import parcial as helper_parcial

class PivotingService: 
  def __init__(self):
    pass

  def parcial(sefl, data):
    return helper_parcial(data.matrix, data.vector, data.unknowns)

  def staggered(self, data):
    return data

  def total(self, data):
    return data