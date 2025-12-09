import { useEffect, useState } from "react";
import { getKeywords, addKeyword, deleteKeyword } from "../services/api";

export default function KeywordManager() {
    const [keywords, setKeywords] = useState([]);
    const [input, setInput] = useState("");

    const load = async () => {
    const res = await getKeywords();
    setKeywords(res.data);
    };

    const handleAdd = async () => {
    await addKeyword(input);
    setInput("");
    load();
    };

    const handleDelete = async (id) => {
    await deleteKeyword(id);
    load();
    };

    useEffect(() => { load(); }, []);

    return (
    <div>
        <h2>🔍 Keywords</h2>
        <input value={input} onChange={(e) => setInput(e.target.value)} />
        <button onClick={handleAdd}>Add</button>

        <ul>
        {keywords.map(k => (
            <li key={k.id}>
            {k.name} <button onClick={() => handleDelete(k.id)}>❌</button>
            </li>
        ))}
        </ul>
    </div>
    );
}
