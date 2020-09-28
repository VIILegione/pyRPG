import duels
import playerDefinition

playerDefinition.databaseCreation()
playerDefinition.databaseUpdate()
if playerDefinition.characterId == 1:
    duels.duelShelter()
else:
    playerDefinition.raceSelector()
    playerDefinition.databaseUpdate()
    duels.duelShelter()
