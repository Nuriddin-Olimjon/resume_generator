from celery import shared_task
from celery.utils.log import get_task_logger

from apps.profile import views

logger = get_task_logger(__name__)


@shared_task(name="send_activation_link")
def send_activation(domain, user_id, template):
    logger.info("Sent link")
    return views.send_activation_link(domain, user_id, template)
