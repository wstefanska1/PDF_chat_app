const chat = document.getElementById("chat");

let selectedFile = null;

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = "msg " + type;
    div.innerText = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

function typingIndicator() {
    const div = document.createElement("div");
    div.className = "msg bot typing";
    div.innerText = "Thinking...";
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    return div;
}

async function send() {
    const input = document.getElementById("input");
    const text = input.value.trim();

    if (!text) return;

    if (!selectedFile) {
        alert("Choose PDF document");
        return;
    }

    addMessage(text, "user");
    input.value = "";

    const typing = typingIndicator();

    try {
        const res = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ topic: text, file: selectedFile })
        });

        const data = await res.json();

        if (!res.ok) {
            typing.remove();
            addMessage("Server error: " + (data.error || res.status), "bot");
            return;
        }

        typing.remove();
        addMessage(data.response, "bot");

    } catch (err) {
        typing.remove();
        addMessage("Error connecting to backend", "bot");
        console.error(err);
    }
}

async function uploadPDF() {
    const input = document.getElementById("pdfInput");

    if (!input.files.length) return;

    const formData = new FormData();
    formData.append("file", input.files[0]);

    try {
        const res = await fetch("/add_pdf", { method: "POST", body: formData });
        const data = await res.json();

        if (!res.ok) {
            addMessage("Error: " + (data.error || res.status), "bot");
            return;
        }

        input.value = "";
        loadDocuments();

    } catch (err) {
        console.error(err);
        addMessage("PDF upload failed", "bot");
    }
}

async function loadDocuments() {
    try {
        const res = await fetch("/documents");
        const data = await res.json();

        const container = document.getElementById("docList");
        container.innerHTML = "";

        data.documents.forEach(doc => {
            const btn = document.createElement("button");
            btn.innerText = doc.name;

            btn.onclick = () => {
                selectedFile = doc.name;
                highlightSelected(btn);
                document.getElementById("chatHeader").innerText = doc.name;
            };

            container.appendChild(btn);
        });

    } catch (err) {
        console.error("Failed to load documents", err);
    }
}

function highlightSelected(activeBtn) {
    document.querySelectorAll("#docList button")
        .forEach(b => b.classList.remove("active"));

    if (activeBtn) {
        activeBtn.classList.add("active");
    }
}

function resetHeader() {
    selectedFile = null;
    document.getElementById("chatHeader").innerText = "PDF Chat";
    document.querySelectorAll("#docList button")
        .forEach(b => b.classList.remove("active"));
}

resetHeader();
loadDocuments();