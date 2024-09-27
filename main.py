from pydub import AudioSegment
import math
import os

def split_audio(file_path, prefixo, output_dir, chunk_duration_ms=180000):
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_mp3(file_path)
    
    # Calcular o número de partes
    total_duration = len(audio)
    num_chunks = math.ceil(total_duration / chunk_duration_ms)

    # Criar diretório para salvar os arquivos
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_chunks):
        start_time = i * chunk_duration_ms
        end_time = start_time + chunk_duration_ms

        # Extrair pedaço do áudio
        chunk = audio[start_time:end_time]
        
        # Definir o nome do arquivo
        chunk_name = f"{prefixo}{i + 1}.mp3"
        chunk_path = os.path.join(output_dir, chunk_name)
        
        # Exportar o pedaço como MP3
        chunk.export(chunk_path, format="mp3")
        print(f"Exportado: {chunk_name}")

if __name__ == "__main__":
    # Caminho do arquivo MP3 de entrada
    input_file = input("Nome do arquivo: ")

    output_dir = input("Informe a pasta: ")
    prefixo = input("Informe o início dos arquivos: ")
    
    # Dividir o áudio em pedaços de até 3 minutos (180000 ms)
    split_audio(input_file, prefixo, output_dir)
