# Previsão do Tempo


## **Sobre** 
Consumo de api para previsão do tempo

## **Como usar:**
    Na variavel "cidade_buscada" digite a cidade que deseja consultar a previsão. A função "get_cidade" recebe a variavel e retorna seu woeid. 
    
<br>

    A função "get_clima" recebe o woeid da cidade e e retorna os dados do clima por dia. 

<br>

    A função "get_dia" recebe o index representante do dia e os dados retornados na função "get_clima".  E retorna a data, dia da semana, a máxima e minima e a descrição do tempo. 

    Entendendo o index:     
        O index recebido pela função funciona por inteiro e não datas
        Assim: 0 corresponde ao dia atual (hoje)
               1 corresponde ao dia seguinte (amanhã)

<br>

    Por fim a apresentação dos dados funciona por fatiamento de string. 
    
    

    