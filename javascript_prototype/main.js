function scoreTask(task) {

    const taskTypeScores = {
      PrescriptionRequest: 3,
      ReviewResults: 3,
      PatientCommunication: 1,
      SickNotes: 1,
      ReferralLetters: 1,
      MedicalReports: 1,
    };

    const baseScore = taskTypeScores[task.task_type] || 0;
    const timeDays = Number(task.time_in_pipeline) || 0;
    const timingPenalty = 0.1 * (timeDays * timeDays);

    return baseScore + timingPenalty;
  }

  const taskForm = document.querySelector("#taskForm");
  const taskContainer = document.querySelector("#tasks");
  const modalBackdrop = document.querySelector(".modal-backdrop");
  const editForm = document.querySelector("#editForm");

  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

  // 1) RENDER TASKS
  function renderTasks() {
    // Clear the container
    taskContainer.innerHTML = "";

    // Sort tasks by severity descending
    // We recalculate severity each time because
    // it might have changed if user edits
    tasks.forEach((task) => {
      task.severity = scoreTask(task);
    });
    tasks.sort((a, b) => b.severity - a.severity);

    tasks.forEach((task, i) => {
      const card = document.createElement("div");
      card.classList.add("card");
      const heading = document.createElement("h4");
      heading.textContent = `${task.task_type} (score: ${task.severity.toFixed(2)})`;

      // Example: show time in pipeline
      const pTime = document.createElement("p");
      pTime.textContent = `Time in pipeline: ${task.time_in_pipeline} days`;

      // “Delete” button
      const delBut = document.createElement("button");
      delBut.innerText = "Delete";
      delBut.addEventListener("click", function () {
        tasks.splice(i, 1);
        saveTasks();
        renderTasks();
      });

      // “Edit” button
      const editBut = document.createElement("button");
      editBut.innerText = "Edit";
      editBut.addEventListener("click", function () {
        openEditForm(task, i);
      });

      card.appendChild(heading);
      card.appendChild(pTime);
      card.appendChild(delBut);
      card.appendChild(editBut);
      taskContainer.appendChild(card);
    });
  }

  // 2) ADD A NEW TASK
  taskForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const newTask = {
      task_type: taskForm.task_type.value,
      time_in_pipeline: taskForm.time_in_pipeline.value,
      // If you had more fields, you'd gather them here
    };
    tasks.push(newTask);
    saveTasks();
    renderTasks();
  });

  // 3) EDIT TASK
  function openEditForm(task, index) {
    modalBackdrop.classList.remove("hidden");

    // Fill in form with existing values
    editForm.task_type.value = task.task_type;
    editForm.time_in_pipeline.value = task.time_in_pipeline;

    // Swap out the old “saveButton” event so it doesn’t stack
    const saveButton = document.querySelector("#saveButton");
    // In case a prior open edit used the same button
    saveButton.onclick = function (e) {
      e.preventDefault();
      // Update the existing task
      tasks[index].task_type = editForm.task_type.value;
      tasks[index].time_in_pipeline = editForm.time_in_pipeline.value;

      saveTasks();
      renderTasks();
      closeModal();
    };
  }

  // 4) CANCEL EDIT
  document.querySelector("#cancelButton").addEventListener("click", closeModal);
  function closeModal() {
    modalBackdrop.classList.add("hidden");
  }

  // 5) SAVE to localStorage
  function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  // 6) INITIAL RENDER
  renderTasks();
