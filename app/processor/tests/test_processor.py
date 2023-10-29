from app.processor import processor

def test_process():
    assert processor.process() == "Starting process"

def test_admin():
    assert processor.process_admin() == "Starting admin process"