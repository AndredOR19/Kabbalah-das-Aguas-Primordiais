import json
import datetime
import subprocess
import cv2
import mediapipe as mp
import os
import sys

# === CONFIGURAÇÃO ===
USE_WEBCAM = True  # False para ignorar análise facial
DEFAULT_COMMIT_MSG = "Atualização com dados psicossomáticos"

# === Função para entrada manual ===
def manual_input():
    print("\n=== Entrada manual de dados PSICO ===")
    try:
        hr = int(input("HR (bpm): "))
        hrv = int(input("HRV: "))
        resp = int(input("Respiração (rpm): "))
        focus = int(input("Foco (%): "))
        mood = input("Humor: ")
        note = input("Observações: ")
        return {
            "hr": hr,
            "hrv": hrv,
            "resp_rate": resp,
            "focus": focus,
            "mood": mood,
            "note": note
        }
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
        sys.exit(1)

# === Função para detecção via webcam ===
def webcam_emotion():
    try:
        mp_face = mp.solutions.face_mesh
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Erro: Câmera não disponível")
            return "neutro"
            
        print("\nAnalisando expressão... olhe para a câmera (5 seg).")
        emotions = {"feliz": 0, "neutro": 0, "triste": 0}

        with mp_face.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
            count = 0
            while count < 50:
                ret, frame = cap.read()
                if not ret:
                    break
                results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.multi_face_landmarks:
                    # Placeholder simples — em versão avançada analisaremos distâncias faciais
                    emotions["neutro"] += 1
                count += 1

        cap.release()
        cv2.destroyAllWindows()
        return max(emotions, key=emotions.get)
    except Exception as e:
        print(f"Erro na análise facial: {e}")
        return "neutro"

# === Função principal ===
def main():
    data = manual_input()
    if USE_WEBCAM:
        emo = webcam_emotion()
        data["mood_detected"] = emo

    data["timestamp"] = datetime.datetime.now().isoformat()

    # Salva JSON local para histórico
    os.makedirs(".gitpsychodata", exist_ok=True)
    with open(".gitpsychodata/current_psico.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Monta commit message automática
    psico_json_str = json.dumps(data, ensure_ascii=False)
    commit_msg = f"{DEFAULT_COMMIT_MSG}\nPSICO_JSON:\n{psico_json_str}"

    # Adiciona todos os arquivos modificados e comita
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("\n✅ Commit feito e enviado com dados PSICO_JSON.")
    except subprocess.CalledProcessError as e:
        print(f"Erro no processo de commit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
