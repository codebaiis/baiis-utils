





def log_performance_time(service_name=''):
    import logging
    from time import perf_counter

    log_level='INFO'
    logging.basicConfig(level=log_level)

    def decorator(original_func):

        def wrapper(*args, **kwargs):
            original_func_name = original_func.__name__
            logging.info(f'  - {service_name} - {log_level}: running {original_func_name}().')

            time1 = perf_counter()

            result = original_func(*args, **kwargs)

            time2 = perf_counter()
            perf_time = round(time2 - time1, 2)
            logging.info(f'  - {service_name} - {log_level}: ran {original_func_name}() in {perf_time}s.')

            return result

        return wrapper

    return decorator



def log_performance_time_and_args(service_name=''):
    import logging
    from time import perf_counter

    log_level='INFO'
    logging.basicConfig(level=log_level)

    def decorator(original_func):

        def wrapper(*args, **kwargs):
            original_func_name = original_func.__name__
            logging.info(f'  - {service_name} - {log_level}: running {original_func_name}(). | args: {args}, kwargs: {kwargs}.')

            time1 = perf_counter()

            result = original_func(*args, **kwargs)

            time2 = perf_counter()
            perf_time = round(time2 - time1, 2)
            logging.info(f'  - {service_name} - {log_level}: ran {original_func_name}() in {perf_time}s.')

            return result

        return wrapper

    return decorator
