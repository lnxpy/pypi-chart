from pyaction import PyAction


workflow = PyAction()


@workflow.action()
def my_action(
    package_name: str,
    chart_width: int,
    chart_height: int,
    chart_title: str,
    days_limit: int,
    output_path: str,
) -> None:
    pass
