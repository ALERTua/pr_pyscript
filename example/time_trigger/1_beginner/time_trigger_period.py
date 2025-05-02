@time_trigger('period(now, 24h)')  # Trigger every 24 hours starting from the time of the HA startup
def daily_trigger():
    persistent_notification.create(
        notification_id='feed_the_cats',
        title='Feed the cats',
        message='Please feed the cats',
    )
