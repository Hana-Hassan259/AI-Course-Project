async function summarize() {
    const text = document.getElementById('summaryInput').value;
    const res = await fetch('/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await res.json();
    document.getElementById('summaryOutput').innerText = data[0]?.summary_text || "Error generating summary.";
}

async function generate() {
    const prompt = document.getElementById('generatePrompt').value;
    const res = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    document.getElementById('generateOutput').innerText = data[0]?.generated_text || "Error generating content.";
}

async function classify() {
    const text = document.getElementById('classifyInput').value;
    const res = await fetch('/classify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await res.json();
    document.getElementById('classifyOutput').innerText = JSON.stringify(data, null, 2);
}

async function extractKeywords() {
    const text = document.getElementById('keywordInput').value;
    const res = await fetch('/keywords', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await res.json();
    const keywords = data.map(([word, score]) => `${word}: ${score.toFixed(4)}`);
    document.getElementById('keywordOutput').innerText = keywords.join('\n');
}


async function textToSpeech() {
    const text = document.getElementById('ttsInput').value;
    const res = await fetch('/speak', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await res.json();
    const audio = document.getElementById('audioPlayer');
    audio.src = data.audio_file;
    audio.load();
}

async function transcribeAudio() {
    const file = document.getElementById('sttFile').files[0];
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('/transcribe', {
        method: 'POST',
        body: formData
    });

    const data = await res.json();
    document.getElementById('sttOutput').innerText = data.transcription || data.error;
}
