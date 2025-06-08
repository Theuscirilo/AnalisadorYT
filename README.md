
## 🎥 Analisador de Vídeo YouTube com IA  
Este é um projeto web moderno que permite ao usuário colar uma URL de vídeo do YouTube e obter estatísticas visuais e um resumo automático usando a API da OpenAI.

## 🚀 Funcionalidades  
🔍 Análise de vídeos do YouTube via URL

🧠 Resumo gerado por inteligência artificial (OpenAI GPT)

🖼️ Exibição da thumbnail do vídeo

📱 Interface responsiva e moderna com Tailwind CSS

🌐 Backend com Flask (Python)

## 🛠️ Tecnologias Usadas  
**Frontend:**  
- HTML5  
- Tailwind CSS  
- JavaScript Vanilla  

**Backend:**  
- Python 3.10+  
- Flask  
- OpenAI API  

🖥️ Como Rodar Localmente  
1. Clone o repositório:  
```
git clone https://github.com/seu-usuario/analisador-youtube.git
cd analisador-youtube
```

2. Crie e ative o ambiente virtual:  
**Linux/macOS:**  
```
python -m venv venv
source venv/bin/activate
```

**Windows:**  
```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:  
```
pip install -r requirements.txt
```

4. Configure a chave da OpenAI:  
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:  
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Ou defina diretamente no terminal antes de rodar a aplicação:  
**Linux/macOS:**  
```
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Windows (CMD):**  
```
set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5. Rode o servidor local:  
```
python app.py
```

Acesse no navegador:  
📍 http://127.0.0.1:5000

🧪 Exemplo de Uso  
- Cole a URL de um vídeo do YouTube no campo de entrada  
- Clique em "Analisar"  
- Veja a thumbnail do vídeo e um resumo gerado automaticamente pela IA

⚠️ Aviso de Limite  
A API da OpenAI possui limites de uso. Verifique seu painel de uso para evitar exceder a cota gratuita ou contratada.

📄 Licença  
MIT © [Matheus Cirilo de Almeida]

---
