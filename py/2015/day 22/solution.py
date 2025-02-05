from math import inf
from typing import TypedDict

BOSS_HP = 13
BOSS_ATK = 8
PLAYER_HP = 10
PLAYER_MANA = 250


class GameState(TypedDict):
    is_over: bool
    boss_hp: int
    player_hp: int
    player_mana: int
    player_armor: int
    shield_left: int
    poison_left: int
    recharge_left: int


# Actions: MDRSP
# Magic missile, Drain, Recharge, Shield, Poison
def simulate(
    action: str, game_state: GameState, hard_mode: bool = False
) -> GameState:
    def _simulate_effects() -> None:
        if game_state["recharge_left"]:
            game_state["recharge_left"] -= 1
            game_state["player_mana"] += 101
        game_state["shield_left"] -= 1
        if game_state["shield_left"] <= 0:
            game_state["player_armor"] = 0
        if game_state["poison_left"]:
            game_state["poison_left"] -= 1
            game_state["boss_hp"] -= 3

    # player turn
    if hard_mode:
        game_state["player_hp"] -= 1
        if game_state["player_hp"] <= 0:
            game_state["is_over"] = True
            return game_state
    _simulate_effects()
    if game_state["boss_hp"] <= 0:
        game_state["is_over"] = True
        return game_state
    match action:
        case "M":
            game_state["boss_hp"] -= 4
            game_state["player_mana"] -= 53
        case "D":
            game_state["boss_hp"] -= 2
            game_state["player_hp"] += 2
            game_state["player_mana"] -= 73
        case "R":
            if game_state["recharge_left"] > 0:
                game_state["is_over"] = True
                return game_state
            game_state["recharge_left"] = 5
            game_state["player_mana"] -= 229
        case "S":
            if game_state["shield_left"] > 0:
                game_state["is_over"] = True
                return game_state
            game_state["shield_left"] = 6
            game_state["player_armor"] = 7
            game_state["player_mana"] -= 113
        case "P":
            if game_state["poison_left"] > 0:
                game_state["is_over"] = True
                return game_state
            game_state["poison_left"] = 6
            game_state["player_mana"] -= 173

    # Not enough mana to cast selected spell or boss is defeated
    if game_state["player_mana"] < 0 or game_state["boss_hp"] <= 0:
        game_state["is_over"] = True
        return game_state

    # boss turn
    _simulate_effects()
    if game_state["boss_hp"] <= 0:
        game_state["is_over"] = True
        return game_state
    game_state["player_hp"] -= BOSS_ATK - game_state["player_armor"]
    if game_state["player_hp"] <= 0:
        game_state["is_over"] = True
    return game_state


def run_simulation(hard_mode: bool) -> int:
    last_game_states: dict[list[str], GameState] = {}
    winning_states: dict[list[str], GameState] = {}
    actions = "MDPRS"

    # init game states
    for action in actions:
        last_game_states[action] = simulate(
            action,
            {
                "boss_hp": BOSS_HP,
                "is_over": False,
                "player_armor": 0,
                "player_hp": PLAYER_HP,
                "player_mana": PLAYER_MANA,
                "poison_left": 0,
                "recharge_left": 0,
                "shield_left": 0,
            },
            hard_mode,
        )

    # do BFS
    while True:
        new_game_states: dict[list[str], GameState] = {}
        for past_actions, game_state in last_game_states.items():
            for action in actions:
                action_result = simulate(action, game_state.copy(), hard_mode)
                if action_result["is_over"]:
                    if (
                        action_result["boss_hp"] <= 0
                        and action_result["player_mana"] >= 0
                    ):
                        winning_states[past_actions + action] = action_result
                elif len(past_actions + action) <= 10:
                    new_game_states[past_actions + action] = action_result
        # no continuable game states
        if len(new_game_states) == 0:
            break
        last_game_states = new_game_states

    minimum_mana_spent = inf
    minimum_actions = ""
    for actions in winning_states.keys():
        mana_spent = 0
        for action in actions:
            match action:
                case "M":
                    mana_spent += 53
                case "P":
                    mana_spent += 173
                case "S":
                    mana_spent += 113
                case "R":
                    mana_spent += 229
                case "D":
                    mana_spent += 73
        if mana_spent < minimum_mana_spent:
            minimum_mana_spent = mana_spent
            minimum_actions = actions
    print(f"Winning actions are {minimum_actions}")
    print(winning_states[minimum_actions])
    return minimum_mana_spent


if __name__ == "__main__":
    print(f'Part one answer is {run_simulation(False)}')
    print(f'Part two answer is {run_simulation(True)}')
