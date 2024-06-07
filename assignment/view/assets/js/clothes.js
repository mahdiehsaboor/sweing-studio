function edit(id) {
    alert("Edit : " + id);
}


async function remove(id) {
    await fetch("/clothes?id="+id , {
        method: "DELETE"
    })
        .then(response => document.location.replace("/clothes"));
}