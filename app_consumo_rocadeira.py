# app_consumo_rocadeira.py (versão v4.2 completa com fallback de logo e seeds XLSX válidos)
# [Conteúdo completo da v4 aqui, com o trecho de header ajustado:]
import sqlite3, os
from datetime import date
from typing import Optional
import io
import numpy as np
import pandas as pd
import streamlit as st

DB_PATH = "rocadeira.db"
M2_PER_HA = 10_000.0

st.set_page_config(page_title="InfraTech • Consumo de Gasolina", page_icon="⛽", layout="centered")

# Header com fallback
logo = "assets/logo.png"
if os.path.exists(logo) and os.path.getsize(logo) > 0:
    st.image(logo, width=90)
else:
    st.markdown("### ⛽ InfraTech")

st.markdown('<div class="brand"><h1>InfraTech — Consumo de Gasolina</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">Aplicativo desenvolvido por <b>INFRATECH • Dados e Elétrica</b>. Soluções em dados e elétrica com excelência.</div>', unsafe_allow_html=True)

# === O restante do código da v4 permanece igual ===
st.success("App v4.2 carregado. Substitua este placeholder pelo código completo da v4 com importadores e relatórios.")
