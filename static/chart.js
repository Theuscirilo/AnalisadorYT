function showError(msg) {
  alert(msg);
}


function analyzeVideo() {
  const url = document.getElementById('urlInput').value.trim();
  if (!url) {
    showError('Por favor, cole uma URL do YouTube');
    return;
  }

  document.getElementById('emptyState').classList.add('hidden');
  document.getElementById('loading').classList.remove('hidden');
  document.getElementById('results').classList.add('hidden');

  fetch('/analisar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url })
  })
  .then(response => response.json())
  .then(data => displayResults(data))
  .catch(error => {
    showError('Erro ao analisar o vídeo. Tente novamente.');
    console.error(error);
  });
}


document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('analyzeBtn').addEventListener('click', analyzeVideo);
});
