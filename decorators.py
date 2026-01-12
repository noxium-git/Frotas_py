from datetime import datetime

def log_operacao(func):
    def wrapper(*args, **kwargs):
        agora = datetime.now()
        print(f"[{agora.strftime('%Y-%m-%d %H:%M:%S')}] A executar: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
