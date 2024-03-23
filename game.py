class DiceGame:
  __diceSize = 0
  __turnOwner = "Bob"
  __limitDiceValue = 99
  __probabilities = []
  __hasDiceSize = False

  def __init__(self, diceSize, turnOwner):
    self.__hasDiceSize = True if diceSize else False
    self.__diceSize = int(diceSize) if (diceSize) else 6
    self.__turnOwner = turnOwner if (turnOwner and self.typeChecking(turnOwner,[str])) else self.__turnOwner
    self.__probabilities = []

  def calcProbFirstTurn(self, diceSize):
    if diceSize <= 0:
      raise TypeError("diceSize cannot be negative")
    total_outcomes = diceSize
    favorable_outcomes = 1 
    return favorable_outcomes / total_outcomes

  def calcProbSecondTurn(self, diceSize):
    if type(diceSize) != int:
      raise TypeError("diceSize must be an integer")
    if diceSize <= 0:
      raise TypeError("diceSize cannot be negative")
    
    first_favorable_outcomes = diceSize - 1
    first_probability = first_favorable_outcomes / diceSize
    second_probability = 1 / diceSize
    return first_probability * second_probability 

  def calcProbability(self):
    limit = self.__limitDiceValue + 1
    posibleDiceValues = range(self.__diceSize, limit)
    
    if(self.__hasDiceSize):
      print(self.__diceSize)
      response = self.calcProbSecondTurn(self.__diceSize) if self.__turnOwner == "Alice" else self.calcProbFirstTurn(self.__diceSize)
      return response

    for actualDiceValue in posibleDiceValues:
        if self.__turnOwner == "Alice":
            self.__probabilities.append(self.calcProbSecondTurn(actualDiceValue))
            self.__turnOwner = "Bob"
        elif self.__turnOwner == "Bob":
            self.__probabilities.append(self.calcProbFirstTurn(actualDiceValue))
            self.__turnOwner = "Alice"

    return self.__probabilities

  def getProbabilitiesData(self):
      return [self.calcProbability(), self.__hasDiceSize]
  
  def typeChecking(self, variable, validTypes):
    return True if type(variable) in validTypes else False
    
