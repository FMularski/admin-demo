function initAdminCommander() {
    const commander = document.querySelector("#admin-commander");
    const darkPanel = document.querySelector("#dark-panel");
    const openBtn = document.querySelector("#open-commander-btn");
    const closeBtn = document.querySelector("#close-commander-btn");
    const executeBtn = document.querySelector("#execute-commander-btn");
    const copyBtn = document.querySelector("#copy-commander-btn");
    const output = document.querySelector("#output");
    const outputPreview = document.querySelector("#output-preview");
    const commandInput = document.querySelector("#commander-input input");
    const url = "/commander/admin-commander/";
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    openBtn.addEventListener("click", () => {
        darkPanel.classList.remove("hidden");
        commander.classList.remove("hidden");
        openBtn.classList.add("hidden");
        commandInput.focus();
    });

    closeBtn.addEventListener("click", () => {
        darkPanel.classList.add("hidden");
        commander.classList.add("hidden");
        output.classList.add("hidden");
        openBtn.classList.remove("hidden");
        executeBtn.classList.add("disabled");
        copyBtn.classList.add("hidden");
        commandInput.value = "";
    });

    executeBtn.addEventListener("click", async () => {
        if (!commandInput.value) return;

        output.classList.remove("hidden");
        outputPreview.innerHTML = `<div class="loader"></div>`;
        executeBtn.classList.add("disabled");
        copyBtn.classList.add("hidden");
        
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({"command": commandInput.value}),
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            }
        });

        executeBtn.classList.remove("disabled");
        if (response.status == 500) {
            outputPreview.innerHTML = `<code>Server error.</code>`;
            return;
        }
        
        const responseJson = await response.json();
        copyBtn.classList.remove("hidden");
        outputPreview.innerHTML = `<code>${responseJson.output}</code>`;
    });

    copyBtn.addEventListener("click", () => {
        copyBtn.classList.add("copied");
        copyBtn.innerText = "Copied!";

        navigator.clipboard.writeText(
            outputPreview.innerHTML.replace("<code>", "").replace("</code>", "")
        );

        setTimeout(() => {
            copyBtn.classList.remove("copied");
            copyBtn.innerText = "Copy";
        }, 3000);
    });

    commandInput.addEventListener("keyup", event => {
        if (!commandInput.value) executeBtn.classList.add("disabled");
        else executeBtn.classList.remove("disabled");

        if (event.keyCode == 13 && !executeBtn.classList.contains("disabled")) // Enter
            executeBtn.click();
    });

    document.addEventListener("keyup", event => {
        if (event.keyCode == 27) // Esc
            closeBtn.click();
    });

    document.addEventListener("keyup", event => {
        if (event.keyCode == 67 && event.altKey) // alt+c
            openBtn.click();
    });
}

initAdminCommander();