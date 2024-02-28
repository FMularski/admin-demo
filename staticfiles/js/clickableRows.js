function enableClickableRowsModules() {
    const modules = document.querySelectorAll("div.module tbody");

    if (!modules) return;

    modules.forEach(module_ => {
        const rows = [...module_.children];

        rows.forEach(row => {
            const url = row.querySelector("a").getAttribute("href");
            
            row.addEventListener("click", function(e) {
                if (e.target.tagName === "TH") window.location = url;
            });
        });
    });
}

function enableClickableRowsResultList() {
    const resultList = document.querySelector("table#result_list tbody");
    
    if (!resultList) return;

    const rows = [...resultList.children];

    rows.forEach(row => {
        const url = row.querySelector("th.field-pk a").getAttribute("href");

        row.addEventListener("click", function(e) {
            if (e.target.tagName === "TD" || e.target.tagName === "TH") window.location = url;
        });
    })
}

enableClickableRowsModules();
enableClickableRowsResultList();