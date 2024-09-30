def chart_title_decoder(title: str) -> str:
    """decodes the input chart title

    Args:
        title (str): the chart title

    Returns:
        str: the human-readable version of title
    """

    return title.replace("_", " ")
