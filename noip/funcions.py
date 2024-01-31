from datetime import datetime, timedelta


def compare_date(data_label: str):
    """
    Check if the text en Label_date (example: "Jan 31, 2024" is equal to the actual date
    :param data_label:
    :return:
    """

    # Get the current date
    current_date = datetime.now()

    # Format the date in the desired format: "Jan 30, 2024"
    formatted_date = current_date.strftime("%b %d, %Y")

    # Print the formatted date
    print("date:", formatted_date)

    # Compare the formatted date with an example date
    # example: formatted_date = "Jan 30, 2024" and data_label = "Jan 30, 2024 09:34 PST" if only check the first
    # characters then compare two equals strings
    if formatted_date[:12] == data_label[:12]:
        print("Dates are equal.")
        return True
    else:
        print("Dates are different.")
        return False


def today_date():
    """

    :return: The actual date in format example: 30 Jun, 2024
    """

    # Get the current date
    current_date = datetime.now()

    # Format the date in the desired format: "Jan 30, 2024"
    formatted_date = current_date.strftime("%b %d, %Y")
    return formatted_date
