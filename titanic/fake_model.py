def fake_predict(userAge):
    if userAge > 18:
        prediction = "survived (over 18)"
    else:
        prediction = "Super survived (under 18)"

    return prediction