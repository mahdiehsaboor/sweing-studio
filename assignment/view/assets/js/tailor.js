function edit(id) {
    alert("Edit : " + id);
}


async function remove(id) {
    await fetch("/tailor?id="+id , {
        method: "DELETE"
    })
        .then(response => document.location.replace("/tailor"));
}