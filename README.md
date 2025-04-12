# Atividade de Redes Neurais Artificiais (MLP) – Resolução do Problema XOR

## Descrição (Português)

Este repositório contém a implementação investigativa e analítica de uma Rede Neural Multicamadas (MLP) aplicada ao problema lógico XOR, utilizando o código fornecido (mlp_simples.py) da disciplina. A atividade consistiu em variar três parâmetros críticos durante o treinamento:

- **Número de Neurônios nas Camadas Ocultas:** (exemplo: 2, 4, 6)
- **Taxa de Aprendizagem:** (exemplo: 0.01, 0.1, 0.5)
- **Quantidade de Épocas:** (exemplo: 1000, 5000, 10000)

Foram realizadas diversas combinações desses parâmetros, com cada configuração repetida três vezes. Foram registrados resultados como o erro médio final e gráficos de convergência, que ilustram como essas variações influenciam a capacidade da rede em aprender o comportamento esperado para o problema XOR.

## Estrutura do Projeto

- **mlp_simples.py:**  
  Implementa a MLP com métodos para feedforward, backpropagation, treinamento e previsão.

- **plot_convergence.py:**  
  (Opcional) Script para geração de gráficos de convergência (erro médio versus número de épocas) a partir dos experimentos.

- **README.md:**  
  Este arquivo de documentação.

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Marceloalvesll/AI-Lab-MLP-XOR.git

    Entre na pasta do projeto:

cd AI-Lab-MLP-XOR

Execute a rede neural:

python mlp_simples.py

(Opcional) Gere os gráficos de convergência:

    python plot_convergence.py

Parâmetros Testados

Foram exploradas as seguintes configurações, dentre outras:

    Experimento Padrão:
    hidden_sizes = [2], learning_rate = 0.1, epochs = 1000

    Outras Variações:

        hidden_sizes = [4], learning_rate = 0.01, epochs = 5000

        hidden_sizes = [4], learning_rate = 0.5, epochs = 10000

        hidden_sizes = [4], learning_rate = 0.5, epochs = 5000

        hidden_sizes = [2], learning_rate = 0.05, epochs = 5000

        hidden_sizes = [6], learning_rate = 0.1, epochs = 5000

Cada configuração foi avaliada com base no erro médio final e na convergência, evidenciada por meio dos gráficos gerados.
Impacto e Relevância

    Impacto Econômico:
    A melhoria na convergência e a redução do erro indicam um melhor aproveitamento dos recursos computacionais. Em aplicações industriais, isso pode se traduzir em menor tempo de máquina, economia de energia e melhor aproveitamento da matéria-prima.

    Tempo de Processamento:
    Os experimentos também possibilitam avaliar a viabilidade do tempo de processamento, garantindo que a solução seja prática tanto para ambientes industriais quanto acadêmicos.

Links

    GitHub: https://github.com/Marceloalvesll/AI-Lab-MLP-XOR

Autor

Marcelo Alves Leite
Estudante de Sistemas de Informação
Universidade Estadual do Tocantins



---

### Versão em Inglês

```markdown
# Artificial Neural Networks (MLP) Investigation – XOR Problem

## Description

This repository contains an investigative and analytical implementation of a Multilayer Perceptron (MLP) applied to the XOR logical problem, using the provided code (mlp_simples.py) from the course. The activity involved varying three critical training parameters:

- **Number of Neurons in Hidden Layers:** (e.g., 2, 4, 6)
- **Learning Rate:** (e.g., 0.01, 0.1, 0.5)
- **Number of Epochs:** (e.g., 1000, 5000, 10000)

Several combinations of these parameters were tested, with each experiment repeated three times. The results—such as the final average error and convergence graphs—illustrate how these variations affect the network's ability to learn the expected behavior for the XOR problem.

## Project Structure

- **mlp_simples.py:**  
  Implements the MLP with methods for feedforward, backpropagation, training, and prediction.

- **plot_convergence.py:**  
  (Optional) A script to generate convergence graphs (average error vs. number of epochs) based on the experiments.

- **README.md:**  
  This documentation file.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Marceloalvesll/AI-Lab-MLP-XOR.git

    Navigate to the project folder:

cd AI-Lab-MLP-XOR

Run the neural network:

python mlp_simples.py

(Optional) Generate the convergence plots:

    python plot_convergence.py

Tested Parameters

The following configurations were tested, among others:

    Standard Experiment:
    hidden_sizes = [2], learning_rate = 0.1, epochs = 1000

    Other Variations:

        hidden_sizes = [4], learning_rate = 0.01, epochs = 5000

        hidden_sizes = [4], learning_rate = 0.5, epochs = 10000

        hidden_sizes = [4], learning_rate = 0.5, epochs = 5000

        hidden_sizes = [2], learning_rate = 0.05, epochs = 5000

        hidden_sizes = [6], learning_rate = 0.1, epochs = 5000

Each configuration was evaluated based on the final average error and convergence behavior, as illustrated by the generated graphs.
Impact and Relevance

    Economic Impact:
    Improved convergence and reduced error indicate better computational efficiency. In industrial applications, this can translate to reduced machine time, energy savings, and more efficient use of raw materials.

    Processing Time:
    The experiments also allow for an evaluation of processing time, ensuring that the solution is practical for both industrial and academic settings.

Links

    GitHub: https://github.com/Marceloalvesll/AI-Lab-MLP-XOR

Author

Marcelo Alves Leite
Information Systems Student
Universidade Estadual do Tocantins