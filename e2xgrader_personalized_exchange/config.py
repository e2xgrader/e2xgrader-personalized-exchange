from traitlets.config import Config


def activate_exchange(config: Config) -> None:
    """Activate the personalized exchange in the given config.
    This will set all exchange classes to use the personalized exchange.
    """
    config.ExchangeFactory.exchange = "e2xgrader_personalized_exchange.exchange.exchange.Exchange"
    config.ExchangeFactory.submit = "e2xgrader_personalized_exchange.exchange.submit.ExchangeSubmit"
    config.ExchangeFactory.collect = (
        "e2xgrader_personalized_exchange.exchange.collect.ExchangeCollect"
    )
    config.ExchangeFactory.fetch_assignment = (
        "e2xgrader_personalized_exchange.exchange.fetch_assignment.ExchangeFetchAssignment"
    )
    config.ExchangeFactory.release_assignment = (
        "e2xgrader_personalized_exchange.exchange.release_assignment.ExchangeReleaseAssignment"
    )
    config.ExchangeFactory.fetch_feedback = (
        "e2xgrader_personalized_exchange.exchange.fetch_feedback.ExchangeFetchFeedback"
    )
    config.ExchangeFactory.release_feedback = (
        "e2xgrader_personalized_exchange.exchange.release_feedback.ExchangeReleaseFeedback"
    )
    config.ExchangeFactory.list = "e2xgrader_personalized_exchange.exchange.list.ExchangeList"


def activate_exam_exchange(config: Config) -> None:
    """Activate the personalized exam exchange in the given config.
    This will activate the personalized exchange and also enable the
    display of the hashcode cell in the exported notebook.
    """
    activate_exchange(config)
    config.ExchangeSubmit.exam_mode = True
    config.SubmissionExporter.show_hashcode_cell = True
