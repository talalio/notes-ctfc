const delete_endpoint = "/notes/del"
   
const deleteNote = (note_element) => {
    let note_id = note_element.attributes['nid'].value
    const delete_req = async (note_id) => {
        await fetch(delete_endpoint, {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            redirect: "follow",
            body: `id=${note_id}`,
        })
    }
    delete_req(note_id)
    window.location.replace("/")
}