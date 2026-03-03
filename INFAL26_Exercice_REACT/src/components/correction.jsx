import React, { useState } from "react";

function TodoList() {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState("");

    const handleAddTask = () => {
        setTasks((currentTasks) => [...currentTasks, newTask]);
        setNewTask(""); // Réinitialiser le champ après l'ajout
    };

    return (
        <div>
            <input
                type="text"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
                placeholder="Entrez une nouvelle tâche"
            />
            <button onClick={handleAddTask}>Ajouter</button>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ul>
        </div>
    );
}

export default TodoList;
