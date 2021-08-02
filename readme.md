# Polumenta generator

[![Downloads](https://static.pepy.tech/personalized-badge/pylumenta?period=total&units=international_system&left_color=orange&right_color=blue&left_text=Downloads)](https://pepy.tech/project/pylumenta)
[![Downloads](https://pepy.tech/badge/pylumenta/month)](https://pepy.tech/project/pylumenta)
[![Downloads](https://pepy.tech/badge/pylumenta/week)](https://pepy.tech/project/pylumenta)

## Intro

This generator is inspired by http://polumenta.zardina.org/ and based on https://github.com/vl4dimir/polumenta.

## Getting started

### Requirements

- Python >= 3.7

### Installation

```python
pip install pylumenta
```

### Example

Generate one Polumenta:

```python
>>> from pylumenta.generator import jedanPolumenta
>>> pol = jedanPolumenta()
>>> print(pol)
Клађo
```

Generate array of unique Polumentas (max number is 100):

```python
>>> from pylumenta.generator import Polumente
>>> poliske = Polumente(5)
>>> print(poliske)
['Шаџo Полумента', 'Ховo Полумента', 'Фњалo Полумента', 'Тлацo Полумента', 'Млаџo Полумента']
```

Will certain Polumenta will be born in one million cycles and if so, in what cycle:

```python
>>> from pylumenta.generator import rodiPolumentu
>>> name, counter, status = rodiPolumentu('Фњалo')
Фњалo Полумента родио се у циклусу: 7273
>>> print(name, counter, status)
Фњалo 7273 True
```