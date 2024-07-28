def goto(browser, url):
    return browser.get(url)


def click_burron(browser, element):
    return browser.click(element)


action_dict = {}

action_dict["goto"] = goto
