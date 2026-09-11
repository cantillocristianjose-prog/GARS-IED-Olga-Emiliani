Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\activate
cd pagina_web
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
mkdir public
Expand-Archive -Path "frontend.zip" -DestinationPath "public" -Force
rm -f frontend.zip
deactivate