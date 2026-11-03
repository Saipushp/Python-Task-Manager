
import tasks


# Test 1: Add a new task
def test_add_task(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(tasks, "FILE_NAME", str(test_file))

    tasks.add_task("Learn Python")

    result = tasks.load_tasks()

    assert len(result) == 1
    assert result[0]["task"] == "Learn Python"
    assert result[0]["completed"] is False


# Test 2: Complete a task
def test_complete_task(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(tasks, "FILE_NAME", str(test_file))

    tasks.add_task("Learn Git")
    tasks.complete_task(1)

    result = tasks.load_tasks()

    assert result[0]["completed"] is True


# Test 3: Delete a task
def test_delete_task(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(tasks, "FILE_NAME", str(test_file))

    tasks.add_task("Learn SQL")
    tasks.delete_task(1)

    result = tasks.load_tasks()

    assert len(result) == 0


# Test 4: Invalid task number
def test_invalid_task_number(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(tasks, "FILE_NAME", str(test_file))

    tasks.add_task("Learn Python")
    tasks.complete_task(10)

    result = tasks.load_tasks()

    assert len(result) == 1
    assert result[0]["completed"] is False
