from .models import Notification, NotificationFeedback


def create_notification(counselor, user, notification_type, extra_id, schedDay, schedStartTime, schedEndTime):
    Notification.objects.create(to_user=counselor, notification_type=notification_type, created_by=user, extra_id=extra_id,
                                schedDay=schedDay, schedStartTime=schedStartTime, schedEndTime=schedEndTime)


def create_feedback(employeeid,  notification_type, user, id, referral_id):
    NotificationFeedback.objects.create(to_user=employeeid, notification_type=notification_type,
                                        created_by=user, extra_id=id, referral_id=referral_id)
