import pyaudio
import numpy as np

# Configurações de áudio
sample_rate = 44100
buffer_size = 1024

# Inicializa o objeto PyAudio
p = pyaudio.PyAudio()

# Abre o stream de entrada do microfone
input_stream = p.open(format=pyaudio.paFloat32,
                      channels=1,
                      rate=sample_rate,
                      input=True,
                      frames_per_buffer=buffer_size)

# Abre o stream de saída do microfone
output_stream = p.open(format=pyaudio.paFloat32,
                       channels=1,
                       rate=sample_rate,
                       output=True,
                       frames_per_buffer=buffer_size)

# Loop principal de processamento em tempo real
while True:
    # Lê os dados do microfone
    input_data = input_stream.read(buffer_size)
    
    # Converte os dados para um array numpy
    audio_data = np.frombuffer(input_data, dtype=np.float32)
    
    # Processa os dados do áudio
    processed_data = process_audio(audio_data)
    
    # Converte os dados processados para bytes
    output_data = processed_data.astype(np.float32).tobytes()
    
    # Envio do áudio processado como saída do microfone
    output_stream.write(output_data)

# Encerra os streams e termina a execução
input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
p.terminate()
