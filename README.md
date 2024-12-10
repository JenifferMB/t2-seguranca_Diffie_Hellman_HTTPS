# Trabalho Prático 2 – Simulador de HTTPS

## Descrição do Projeto
Este trabalho tem como objetivo explorar os conceitos de segurança de sistemas, através do desenvolvimento de uma solução que simula parte do protocolo HTTPS. O projeto consiste em duas etapas principais: a geração de chaves utilizando o método de Diffie-Hellman e a troca de mensagens de forma segura usando criptografia AES no modo CBC.

## Atividades a Serem Desenvolvidas

### Etapa 1 – Geração da Chave
1. **Cálculo de Chave (Diffie-Hellman)**:
   - Gerar um valor `a` menor que o número primo `p`, com no mínimo 30 dígitos.
   - Calcular `A = g^a mod p` e enviar o valor de `A` (em hexadecimal) ao professor.
   - Usar o valor `B` fornecido pelo professor para calcular `V = B^a mod p`.
   - Obter a chave da sessão `S` aplicando SHA256 sobre `V` e utilizando os 128 bits menos significativos.

### Etapa 2 – Troca de Mensagens Seguras
1. **Decodificação da Mensagem**:
   - Receber uma mensagem cifrada no formato `[128 bits com IV][mensagem]`.
   - Decifrar a mensagem usando AES em modo CBC com a chave de sessão `S`.

2. **Envio de Resposta**:
   - Inverter os caracteres da mensagem decifrada.
   - Reenviar a mensagem cifrada no formato `[128 bits com IV aleatório][mensagem invertida]`.

## Entrega do Trabalho
- O trabalho deve ser postado no Moodle no prazo estipulado.
- Entregar um arquivo ZIP contendo:
  - Código fonte do projeto.
  - Relatório com detalhes da solução, implementação e processo de compilação.
  - Link para o vídeo explicativo no YouTube (5-10 minutos).

## Critérios de Avaliação
- **Soluções Desenvolvidas** (6,0 pontos):
  - Solução para a Etapa 1.
  - Solução para a Etapa 2.

- **Recursos Adicionais** (4,0 pontos):
  - Relatório:
    - Formatação (capa, capítulos, alinhamento justificado).
    - Organização (frases curtas, encadeamento de ideias, coerência).
    - Conteúdo (detalhamento da solução e implementação).
  - Vídeo explicativo:
    - Tempo máximo de 10 minutos.
    - Explicação clara e objetiva.

## Considerações Finais
- Todos os membros do grupo devem participar ativamente do desenvolvimento e da apresentação.
- Trabalhos plagiados ou soluções não funcionais receberão nota zero.
- Utilize o fórum do Moodle para comunicação durante as etapas do trabalho.
