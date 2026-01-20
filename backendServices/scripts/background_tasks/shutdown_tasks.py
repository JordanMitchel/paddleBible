async def shutdown_consumer(app, logger):
    logger.info("🔄 Shutting down Kombu consumer...")
    bff_consumer_service = getattr(app.state, "bff_consumer_service", None)

    if bff_consumer_service:
        bff_consumer_service.should_stop = True
        bff_consumer_service.connection.close()
        logger.info("✅ Kombu consumer stopped cleanly.")
