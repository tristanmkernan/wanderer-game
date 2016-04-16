from components import *

PLAYER_MOVE_SPEED = 0.3

PLAYER_ATTACK_ANIMATION_DURATION = 500

STATE_MOVING = 'moving'
STATE_MOVING_WEST = STATE_MOVING + DirectionComponent.West
STATE_MOVING_EAST = STATE_MOVING + DirectionComponent.East
STATE_MOVING_SOUTH = STATE_MOVING + DirectionComponent.South
STATE_MOVING_NORTH = STATE_MOVING + DirectionComponent.North

STATE_STANDING_STILL = 'still'
STATE_STANDING_STILL_WEST = STATE_STANDING_STILL + DirectionComponent.West
STATE_STANDING_STILL_EAST= STATE_STANDING_STILL + DirectionComponent.East
STATE_STANDING_STILL_SOUTH = STATE_STANDING_STILL + DirectionComponent.South
STATE_STANDING_STILL_NORTH = STATE_STANDING_STILL + DirectionComponent.North

STATE_ATTACKING = 'attacking'

