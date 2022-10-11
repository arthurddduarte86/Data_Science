#!/usr/bin/env python
# coding: utf-8

# # F-strings em Python

# Variáveis em texto

# In[5]:


faturamento = 1000

print("O faturamento foi de {}".format(faturamento)) #jeito convencional não usando o F-string
print(f"O faturamento foi: {faturamento}")


# In[6]:


nome_arquivo = "vendas.txt"


# In[14]:


caminho = r'link do caminho para o arquivo'   # r  antes da string, é uma raw string, uma string pura
arquivo = open(f"{caminho}/{nome_arquivo}", "r")
print(arquivo.read())
arquivo.close()


# Formatando com casa decimal

# In[17]:


print(f"Faturamento: {faturamento:.2f}")


# In[ ]:





# Formato moeda

# In[21]:


print(f"Faturamento: R${faturamento:,.2f}")


# In[ ]:





# Número fixo de digitos

# In[22]:


#cpf = 01206406299 # Python não aceita o numero começar com 0
cpf = 1206406299
print(f"CPF: {cpf:011}") # formata o cpf para ter 11 digitos e preencher o digito ausente com 0


# Percentual

# In[25]:


margem_lucro = 0.27
print(f"Margem: {margem_lucro:.2%}")


# Datas

# In[28]:


from datetime import datetime
hoje = datetime.now()
print(f"Data de hoje: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")


# Só cuidado com textos com chaves {}

# In[33]:


produto = 'iphone'
print(f"{{Produto: {produto}}}") # resulta em um dicionário


# Corpo do E-mail

# In[37]:


texto = f"""
Bom dia, diretoria
Faturamento: {faturamento}
Margem de Lucro: {margem_lucro}
Data: {hoje}"""
print(texto)

