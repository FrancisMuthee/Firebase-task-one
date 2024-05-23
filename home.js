//Initialize firebase
firebase.initializeApp({
    apiKey: "AIzaSyCc6J5Kb5RevV8SilYBsg_f9EMWTk3NZ1A",
    authDomain: "plp-apps-8b276.firebaseapp.com",
    projectId: "plp-apps-8b276",
    storageBucket: "plp-apps-8b276.appspot.com",
    messagingSenderId: "355415471570",
    appId: "1:355415471570:web:0724934c9d11ef27dd840b",
})

const db = firebase.firestore();

//Function to add a task
function addTask() {
    const taskInput = document.getElementById("task-input");
    const task = taskInput.value.trim(); // remove whitespaces
    if (task !== "") { // Task not empty
        db.collection("tasks").add({ //name collection tasks
            task: task, // Record plus task.
            timestamp: firebase.firestore.FieldValue.serverTimestamp(),
        });
        taskInput.value = ""; // Reset the input to empty, Enable to add a task to database
        console.log("Task added");
    }
}

function renderTasks(doc){
    const taskList = document.getElementById("task-list");
    const taskItem = document.createElement("li");
    taskItem.className = "task-item";
    taskItem.innerHTML = `
        <span>${doc.data().task}</span>
        <button onclick = "deleteTask('${doc.id}')">Delete</button>
    `;
    taskList.appendChild(taskItem)
}

//Real-time listener for tasks

db.collection("tasks")
    .orderBy("timestamp", "desc")
    .onSnapshot(snapshot => { //Set realtime listener
        const changes = snapshot.docChanges();
        changes.forEach(change => {
            if (change.type === "added"){
                renderTasks(change.doc);
            }
        });
    });



//Function to delete a task
function deleteTask(id) {
    db.collection("tasks").doc(id).delete();
}
