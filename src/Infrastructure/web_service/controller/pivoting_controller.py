from Application.services.pivoting_service import PivotingService

class PivotingController:

  def __init__(self):
    self.pivoting_service = PivotingService()
 
  def parcial(self, data):
    return self.pivoting_service.parcial(data)

  def staggered(self, data):
    return self.pivoting_service.staggered(data)

  def total(self, data): 
    return self.pivoting_service.total(data)
