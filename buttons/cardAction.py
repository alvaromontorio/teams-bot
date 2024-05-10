from botbuilder.schema import ChannelAccount, SuggestedActions, ActionTypes, CardAction

def generate_action_card(value: str) -> CardAction:
    ac_template = CardAction(
                #title="Red",
                type=ActionTypes.im_back,
                value=value,
                #image="https://via.placeholder.com/20/FF0000?text=R",
                #image_alt_text="R",
            )
    return ac_template

def get_action_cards(values: list) -> list:
    result = []

    for value in values:
        ac = generate_action_card(value)
        result.append(ac)
        
    return result