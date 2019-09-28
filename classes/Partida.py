class Partida(object):
    def __init__(self, nome_campeonato, temporada, pais, rodada,
    time_dentro, time_fora, resultado_final, resultado_final_v_d_e,gols_mandante, gols_visitante, horario, turno, dia_semana,
    posicao_time_dentro, posicao_time_fora,
    ultimo_jogo_casa, segundo_ultimo_jogo_casa, terceiro_ultimo_jogo_casa, quarto_ultimo_jogo_casa, quinto_ultimo_jogo_casa, ultimo_jogo_visitante, segundo_ultimo_jogo_visitante, terceiro_ultimo_jogo_visitante, quarto_ultimo_jogo_visitante, quinto_ultimo_jogo_visitante,
    media_gols_marcados_por_jogo_time_casa_em_casa, media_gols_marcados_por_jogo_time_casa_fora, media_gols_marcados_por_jogo_time_casa_global, media_gols_sofridos_por_jogo_time_casa_em_casa, media_gols_sofridos_por_jogo_time_casa_fora, media_gols_sofridos_por_jogo_time_casa_global, media_gols_marcados_sofridos_por_jogo_time_casa_em_casa, media_gols_marcados_sofridos_por_jogo_time_casa_fora, media_gols_marcados_sofridos_por_jogo_time_casa_global, jogos_sem_sofrer_gols_time_casa_em_casa, jogos_sem_sofrer_gols_time_casa_fora, jogos_sem_sofrer_gols_time_casa_global, jogos_sem_marcar_gols_time_casa_em_casa, jogos_sem_marcar_gols_time_casa_fora, jogos_sem_marcar_gols_time_casa_global, jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa, jogos_com_mais_de_dois_gols_e_meio_time_casa_fora, jogos_com_mais_de_dois_gols_e_meio_time_casa_global, jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa, jogos_com_menos_de_dois_gols_e_meio_time_casa_fora, jogos_com_menos_de_dois_gols_e_meio_time_casa_global,
    media_gols_marcados_por_jogo_time_visitante_em_casa, media_gols_marcados_por_jogo_time_visitante_fora, media_gols_marcados_por_jogo_time_visitante_global, media_gols_sofridos_por_jogo_time_visitante_em_casa, media_gols_sofridos_por_jogo_time_visitante_fora, media_gols_sofridos_por_jogo_time_visitante_global, media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa, media_gols_marcados_sofridos_por_jogo_time_visitante_fora, media_gols_marcados_sofridos_por_jogo_time_visitante_global, jogos_sem_sofrer_gols_time_visitante_em_casa, jogos_sem_sofrer_gols_time_visitante_fora,jogos_sem_sofrer_gols_time_visitante_global, jogos_sem_marcar_gols_time_visitante_em_casa, jogos_sem_marcar_gols_time_visitante_fora, jogos_sem_marcar_gols_time_visitante_global,jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa, jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora, jogos_com_mais_de_dois_gols_e_meio_time_visitante_global, jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa, jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora, jogos_com_menos_de_dois_gols_e_meio_time_visitante_global,
    gols_marcados_time_casa_primeiro_sexto, gols_sofridos_time_casa_primeiro_sexto, gols_marcados_time_casa_segundo_sexto, gols_sofridos_time_casa_segundo_sexto, gols_marcados_time_casa_terceiro_sexto, gols_sofridos_time_casa_terceiro_sexto, gols_marcados_time_casa_quarto_sexto, gols_sofridos_time_casa_quarto_sexto, gols_marcados_time_casa_quinto_sexto, gols_sofridos_time_casa_quinto_sexto, gols_marcados_time_casa_ultimo_sexto, gols_sofridos_time_casa_ultimo_sexto,
    gols_marcados_time_visitante_primeiro_sexto, gols_sofridos_time_visitante_primeiro_sexto, gols_marcados_time_visitante_segundo_sexto, gols_sofridos_time_visitante_segundo_sexto, gols_marcados_time_visitante_terceiro_sexto, gols_sofridos_time_visitante_terceiro_sexto, gols_marcados_time_visitante_quarto_sexto, gols_sofridos_time_visitante_quarto_sexto, gols_marcados_time_visitante_quinto_sexto, gols_sofridos_time_visitante_quinto_sexto, gols_marcados_time_visitante_ultimo_sexto, gols_sofridos_time_visitante_ultimo_sexto,
    minuto_primeira_expulsao_time_a, minuto_segunda_expulsao_time_a, minuto_terceira_expulsao_time_a,minuto_quarta_expulsao_time_a, minuto_primeira_expulsao_time_b, minuto_segunda_expulsao_time_b, minuto_terceira_expulsao_time_b, minuto_quarta_expulsao_time_b,
    placar_momento_expulsao_um, placar_momento_expulsao_dois, placar_momento_expulsao_tres, placar_momento_expulsao_quatro, placar_momento_expulsao_cinco, placar_momento_expulsao_seis, placar_momento_expulsao_sete, placar_momento_expulsao_oito,
    expulsao_um_cartao, expulsao_dois_cartao, expulsao_tres_cartao, expulsao_quatro_cartao, expulsao_cinco_cartao, expulsao_seis_cartao, expulsao_sete_cartao, expulsao_oito_cartao,
    quantidade_de_gols_apos_expulsao_um_time_a, quantidade_de_gols_apos_expulsao_um_time_b, quantidade_de_gols_apos_expulsao_dois_time_a, quantidade_de_gols_apos_expulsao_dois_time_b, quantidade_de_gols_apos_expulsao_tres_time_a, quantidade_de_gols_apos_expulsao_tres_time_b, quantidade_de_gols_apos_expulsao_quatro_time_a, quantidade_de_gols_apos_expulsao_quatro_time_b, quantidade_de_gols_apos_expulsao_cinco_time_a, quantidade_de_gols_apos_expulsao_cinco_time_b, quantidade_de_gols_apos_expulsao_seis_time_a, quantidade_de_gols_apos_expulsao_seis_time_b, quantidade_de_gols_apos_expulsao_sete_time_a, quantidade_de_gols_apos_expulsao_sete_time_b, quantidade_de_gols_apos_expulsao_oito_time_a, quantidade_de_gols_apos_expulsao_oito_time_b,
    quantidade_de_gols_no_momento_expulsao_um_time_a, quantidade_de_gols_no_momento_expulsao_um_time_b, quantidade_de_gols_no_momento_expulsao_dois_time_a, quantidade_de_gols_no_momento_expulsao_dois_time_b, quantidade_de_gols_no_momento_expulsao_tres_time_a, quantidade_de_gols_no_momento_expulsao_tres_time_b, quantidade_de_gols_no_momento_expulsao_quatro_time_a, quantidade_de_gols_no_momento_expulsao_quatro_time_b, quantidade_de_gols_no_momento_expulsao_cinco_time_a, quantidade_de_gols_no_momento_expulsao_cinco_time_b, quantidade_de_gols_no_momento_expulsao_seis_time_a, quantidade_de_gols_no_momento_expulsao_seis_time_b, quantidade_de_gols_no_momento_expulsao_sete_time_a, quantidade_de_gols_no_momento_expulsao_sete_time_b, quantidade_de_gols_no_momento_expulsao_oito_time_a, quantidade_de_gols_no_momento_expulsao_oito_time_b,
    momento_expulsao_um_v_d_e, momento_expulsao_dois_v_d_e, momento_expulsao_tres_v_d_e, momento_expulsao_quatro_v_d_e, momento_expulsao_cinco_v_d_e, momento_expulsao_seis_v_d_e, momento_expulsao_sete_v_d_e, momento_expulsao_oito_v_d_e,
    intervalo_expulsao_um_v_d_e, intervalo_expulsao_dois_v_d_e, intervalo_expulsao_tres_v_d_e, intervalo_expulsao_quatro_v_d_e, intervalo_expulsao_cinco_v_d_e, intervalo_expulsao_seis_v_d_e, intervalo_expulsao_sete_v_d_e, intervalo_expulsao_oito_v_d_e,
    expulsao_um_m_v, expulsao_dois_m_v, expulsao_tres_m_v, expulsao_quatro_m_v, expulsao_cinco_m_v, expulsao_seis_m_v, expulsao_sete_m_v, expulsao_oito_m_v,
    qtd_expulsoes_time_a, qtd_expulsoes_time_b,
    posse_time_a, posse_time_b, chutes_a_gol_time_a, chutes_a_gol_time_b, chutes_fora_time_a, chutes_fora_time_b, ataques_time_a, ataques_time_b, ataques_perigosos_time_a, ataques_perigosos_time_b, impedimentos_time_a, impedimentos_time_b, faltas_time_a, faltas_time_b, escanteios_time_a, escanteios_time_b):

        self.nome_campeonato = nome_campeonato
        self.temporada = temporada
        self.pais = pais
        self.rodada = rodada

        ###
        self.time_mandante = time_dentro
        self.time_visitante = time_fora
        self.resultado_final = resultado_final
        self.resultado_final_v_d_e = resultado_final_v_d_e
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante
        self.horario = horario
        self.turno = turno
        self.dia_da_semana = dia_semana

        ###
        self.posicao_atual_na_tabela_time_mandante = posicao_time_dentro
        self.posicao_atual_na_tabela_time_visitante = posicao_time_fora

        ###
        self.ultimo_jogo_time_mandante = ultimo_jogo_casa
        self.segundo_ultimo_jogo_time_mandante = segundo_ultimo_jogo_casa
        self.terceiro_ultimo_jogo_time_mandante = terceiro_ultimo_jogo_casa
        self.quarto_ultimo_jogo_time_mandante = quarto_ultimo_jogo_casa
        self.quinto_ultimo_jogo_time_mandante = quinto_ultimo_jogo_casa
        
        self.ultimo_jogo_time_visitante = ultimo_jogo_visitante
        self.segundo_ultimo_jogo_time_visitante = segundo_ultimo_jogo_visitante
        self.terceiro_ultimo_jogo_time_visitante = terceiro_ultimo_jogo_visitante
        self.quarto_ultimo_jogo_time_visitante = quarto_ultimo_jogo_visitante
        self.quinto_ultimo_jogo_time_visitante = quinto_ultimo_jogo_visitante

        ###Casa
        self.media_gols_marcados_por_jogo_time_mandante_em_casa = media_gols_marcados_por_jogo_time_casa_em_casa
        self.media_gols_marcados_por_jogo_time_mandante_fora = media_gols_marcados_por_jogo_time_casa_fora
        self.media_gols_marcados_por_jogo_time_mandante_global = media_gols_marcados_por_jogo_time_casa_global
        
        self.media_gols_sofridos_por_jogo_time_mandante_em_casa = media_gols_sofridos_por_jogo_time_casa_em_casa
        self.media_gols_sofridos_por_jogo_time_mandante_fora = media_gols_sofridos_por_jogo_time_casa_fora 
        self.media_gols_sofridos_por_jogo_time_mandante_global = media_gols_sofridos_por_jogo_time_casa_global
        
        self.media_gols_marcados_e_sofridos_por_jogo_time_mandante_em_casa = media_gols_marcados_sofridos_por_jogo_time_casa_em_casa
        self.media_gols_marcados_e_sofridos_por_jogo_time_mandante_fora= media_gols_marcados_sofridos_por_jogo_time_casa_fora
        self.media_gols_marcados_e_sofridos_por_jogo_time_mandante_global = media_gols_marcados_sofridos_por_jogo_time_casa_global
        
        self.jogos_sem_sofrer_gols_time_mandante_em_casa = jogos_sem_sofrer_gols_time_casa_em_casa
        self.jogos_sem_sofrer_gols_time_mandante_fora = jogos_sem_sofrer_gols_time_casa_fora
        self.jogos_sem_sofrer_gols_time_mandante_global = jogos_sem_sofrer_gols_time_casa_global
        
        self.jogos_sem_marcar_gols_time_mandante_em_casa = jogos_sem_marcar_gols_time_casa_em_casa
        self.jogos_sem_marcar_gols_time_mandante_fora = jogos_sem_marcar_gols_time_casa_fora
        self.jogos_sem_marcar_gols_time_mandante_global = jogos_sem_marcar_gols_time_casa_global
        
        self.jogos_com_mais_de_dois_gols_e_meio_time_mandante_em_casa = jogos_com_mais_de_dois_gols_e_meio_time_casa_em_casa
        self.jogos_com_mais_de_dois_gols_e_meio_time_mandante_fora = jogos_com_mais_de_dois_gols_e_meio_time_casa_fora
        self.jogos_com_mais_de_dois_gols_e_meio_time_mandante_global = jogos_com_mais_de_dois_gols_e_meio_time_casa_global
        
        self.jogos_com_menos_de_dois_gols_e_meio_time_mandante_em_casa = jogos_com_menos_de_dois_gols_e_meio_time_casa_em_casa
        self.jogos_com_menos_de_dois_gols_e_meio_time_mandante_fora = jogos_com_menos_de_dois_gols_e_meio_time_casa_fora
        self.jogos_com_menos_de_dois_gols_e_meio_time_mandante_global = jogos_com_menos_de_dois_gols_e_meio_time_casa_global

        #Visitante
        self.media_gols_marcados_por_jogo_time_visitante_em_casa = media_gols_marcados_por_jogo_time_visitante_em_casa
        self.media_gols_marcados_por_jogo_time_visitante_fora = media_gols_marcados_por_jogo_time_visitante_fora
        self.media_gols_marcados_por_jogo_time_visitante_global = media_gols_marcados_por_jogo_time_visitante_global
        
        self.media_gols_sofridos_por_jogo_time_visitante_em_casa = media_gols_sofridos_por_jogo_time_visitante_em_casa
        self.media_gols_sofridos_por_jogo_time_visitante_fora = media_gols_sofridos_por_jogo_time_visitante_fora 
        self.media_gols_sofridos_por_jogo_time_visitante_global = media_gols_sofridos_por_jogo_time_visitante_global
        
        self.media_gols_marcados_e_sofridos_por_jogo_time_visitante_em_casa = media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa
        self.media_gols_marcados_e_sofridos_por_jogo_time_visitante_fora= media_gols_marcados_sofridos_por_jogo_time_visitante_fora
        self.media_gols_marcados_e_sofridos_por_jogo_time_visitante_global = media_gols_marcados_sofridos_por_jogo_time_visitante_global
        
        self.jogos_sem_sofrer_gols_time_visitante_em_casa = jogos_sem_sofrer_gols_time_visitante_em_casa
        self.jogos_sem_sofrer_gols_time_visitante_fora = jogos_sem_sofrer_gols_time_visitante_fora
        self.jogos_sem_sofrer_gols_time_visitante_global = jogos_sem_sofrer_gols_time_visitante_global
        
        self.jogos_sem_marcar_gols_time_visitante_em_casa = jogos_sem_marcar_gols_time_visitante_em_casa
        self.jogos_sem_marcar_gols_time_visitante_fora = jogos_sem_marcar_gols_time_visitante_fora
        self.jogos_sem_marcar_gols_time_visitante_global = jogos_sem_marcar_gols_time_visitante_global
        
        self.jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa = jogos_com_mais_de_dois_gols_e_meio_time_visitante_em_casa
        self.jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora = jogos_com_mais_de_dois_gols_e_meio_time_visitante_fora
        self.jogos_com_mais_de_dois_gols_e_meio_time_visitante_global = jogos_com_mais_de_dois_gols_e_meio_time_visitante_global
        
        self.jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa = jogos_com_menos_de_dois_gols_e_meio_time_visitante_em_casa
        self.jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora = jogos_com_menos_de_dois_gols_e_meio_time_visitante_fora
        self.jogos_com_menos_de_dois_gols_e_meio_time_visitante_global = jogos_com_menos_de_dois_gols_e_meio_time_visitante_global

        ###
        self.gols_marcados_time_mandante_primeiro_sexto = gols_marcados_time_casa_primeiro_sexto
        self.gols_sofridos_time_mandante_primeiro_sexto  = gols_sofridos_time_casa_primeiro_sexto 
        self.gols_marcados_time_mandante_segundo_sexto = gols_marcados_time_casa_segundo_sexto
        self.gols_sofridos_time_mandante_segundo_sexto = gols_sofridos_time_casa_segundo_sexto
        self.gols_marcados_time_mandante_terceiro_sexto = gols_marcados_time_casa_terceiro_sexto
        self.gols_sofridos_time_mandante_terceiro_sexto = gols_sofridos_time_casa_terceiro_sexto
        self.gols_marcados_time_mandante_quarto_sexto = gols_marcados_time_casa_quarto_sexto
        self.gols_sofridos_time_mandante_quarto_sexto = gols_sofridos_time_casa_quarto_sexto
        self.gols_marcados_time_mandante_quinto_sexto = gols_marcados_time_casa_quinto_sexto
        self.gols_sofridos_time_mandante_quinto_sexto = gols_sofridos_time_casa_quinto_sexto
        self.gols_marcados_time_mandante_ultimo_sexto = gols_marcados_time_casa_ultimo_sexto
        self.gols_sofridos_time_mandante_ultimo_sexto = gols_sofridos_time_casa_ultimo_sexto

        self.gols_marcados_time_visitante_primeiro_sexto = gols_marcados_time_visitante_primeiro_sexto
        self.gols_sofridos_time_visitante_primeiro_sexto = gols_sofridos_time_visitante_primeiro_sexto
        self.gols_marcados_time_visitante_segundo_sexto = gols_marcados_time_visitante_segundo_sexto
        self.gols_sofridos_time_visitante_segundo_sexto = gols_sofridos_time_visitante_segundo_sexto
        self.gols_marcados_time_visitante_terceiro_sexto = gols_marcados_time_visitante_terceiro_sexto
        self.gols_sofridos_time_visitante_terceiro_sexto = gols_sofridos_time_visitante_terceiro_sexto
        self.gols_marcados_time_visitante_quarto_sexto = gols_marcados_time_visitante_quarto_sexto
        self.gols_sofridos_time_visitante_quarto_sexto = gols_sofridos_time_visitante_quarto_sexto
        self.gols_marcados_time_visitante_quinto_sexto = gols_marcados_time_visitante_quinto_sexto
        self.gols_sofridos_time_visitante_quinto_sexto = gols_sofridos_time_visitante_quinto_sexto
        self.gols_marcados_time_visitante_ultimo_sexto = gols_marcados_time_visitante_ultimo_sexto
        self.gols_sofridos_time_visitante_ultimo_sexto = gols_sofridos_time_visitante_ultimo_sexto
        ###
        
        self.minuto_primeira_expulsao_time_mandante = minuto_primeira_expulsao_time_a
        self.minuto_segunda_expulsao_time_mandante = minuto_segunda_expulsao_time_a
        self.minuto_terceira_expulsao_time_mandante = minuto_terceira_expulsao_time_a
        self.minuto_quarta_expulsao_time_mandante = minuto_quarta_expulsao_time_a
        self.minuto_primeira_expulsao_time_visitante = minuto_primeira_expulsao_time_b
        self.minuto_segunda_expulsao_time_visitante = minuto_segunda_expulsao_time_b
        self.minuto_terceira_expulsao_time_visitante = minuto_terceira_expulsao_time_b
        self.minuto_quarta_expulsao_time_visitante = minuto_quarta_expulsao_time_b

        ###
        self.placar_momento_expulsao_um = placar_momento_expulsao_um
        self.placar_momento_expulsao_dois = placar_momento_expulsao_dois
        self.placar_momento_expulsao_tres = placar_momento_expulsao_tres
        self.placar_momento_expulsao_quatro = placar_momento_expulsao_quatro
        self.placar_momento_expulsao_cinco = placar_momento_expulsao_cinco
        self.placar_momento_expulsao_seis = placar_momento_expulsao_seis
        self.placar_momento_expulsao_sete = placar_momento_expulsao_sete
        self.placar_momento_expulsao_oito = placar_momento_expulsao_oito

        ###
        #vermelho direto ou segundo amarelo
        self.expulsao_um_cartao_vd_ou_sa = expulsao_um_cartao
        self.expulsao_dois_cartao_vd_ou_sa = expulsao_dois_cartao
        self.expulsao_tres_cartao_vd_ou_sa = expulsao_tres_cartao
        self.expulsao_quatro_cartao_vd_ou_sa = expulsao_quatro_cartao
        self.expulsao_cinco_cartao_vd_ou_sa = expulsao_cinco_cartao
        self.expulsao_seis_cartao_vd_ou_sa = expulsao_seis_cartao
        self.expulsao_sete_cartao_vd_ou_sa = expulsao_sete_cartao
        self.expulsao_oito_cartao_vd_ou_sa = expulsao_oito_cartao

        ###
        self.quantidade_de_gols_apos_expulsao_um_time_mandante = quantidade_de_gols_apos_expulsao_um_time_a
        self.quantidade_de_gols_apos_expulsao_um_time_visitante = quantidade_de_gols_apos_expulsao_um_time_b
        self.quantidade_de_gols_apos_expulsao_dois_time_mandante = quantidade_de_gols_apos_expulsao_dois_time_a
        self.quantidade_de_gols_apos_expulsao_dois_time_visitante = quantidade_de_gols_apos_expulsao_dois_time_b
        self.quantidade_de_gols_apos_expulsao_tres_time_mandante = quantidade_de_gols_apos_expulsao_tres_time_a
        self.quantidade_de_gols_apos_expulsao_tres_time_visitante = quantidade_de_gols_apos_expulsao_tres_time_b
        self.quantidade_de_gols_apos_expulsao_quatro_time_mandante = quantidade_de_gols_apos_expulsao_quatro_time_a
        self.quantidade_de_gols_apos_expulsao_quatro_time_visitante = quantidade_de_gols_apos_expulsao_quatro_time_b
        self.quantidade_de_gols_apos_expulsao_cinco_time_mandante = quantidade_de_gols_apos_expulsao_cinco_time_a
        self.quantidade_de_gols_apos_expulsao_cinco_time_visitante = quantidade_de_gols_apos_expulsao_cinco_time_b
        self.quantidade_de_gols_apos_expulsao_seis_time_mandante = quantidade_de_gols_apos_expulsao_seis_time_a
        self.quantidade_de_gols_apos_expulsao_seis_time_visitante = quantidade_de_gols_apos_expulsao_seis_time_b
        self.quantidade_de_gols_apos_expulsao_sete_time_mandante = quantidade_de_gols_apos_expulsao_sete_time_a
        self.quantidade_de_gols_apos_expulsao_sete_time_visitante = quantidade_de_gols_apos_expulsao_sete_time_b
        self.quantidade_de_gols_apos_expulsao_oito_time_mandante = quantidade_de_gols_apos_expulsao_oito_time_a
        self.quantidade_de_gols_apos_expulsao_oito_time_visitante = quantidade_de_gols_apos_expulsao_oito_time_b
        ###

        self.quantidade_de_gols_no_momento_expulsao_um_time_mandante = quantidade_de_gols_no_momento_expulsao_um_time_a
        self.quantidade_de_gols_no_momento_expulsao_um_time_visitante = quantidade_de_gols_no_momento_expulsao_um_time_b
        self.quantidade_de_gols_no_momento_expulsao_dois_time_mandante = quantidade_de_gols_no_momento_expulsao_dois_time_a
        self.quantidade_de_gols_no_momento_expulsao_dois_time_visitante = quantidade_de_gols_no_momento_expulsao_dois_time_b
        self.quantidade_de_gols_no_momento_expulsao_tres_time_mandante = quantidade_de_gols_no_momento_expulsao_tres_time_a
        self.quantidade_de_gols_no_momento_expulsao_tres_time_visitante = quantidade_de_gols_no_momento_expulsao_tres_time_b
        self.quantidade_de_gols_no_momento_expulsao_quatro_time_mandante = quantidade_de_gols_no_momento_expulsao_quatro_time_a
        self.quantidade_de_gols_no_momento_expulsao_quatro_time_visitante = quantidade_de_gols_no_momento_expulsao_quatro_time_b
        self.quantidade_de_gols_no_momento_expulsao_cinco_time_mandante = quantidade_de_gols_no_momento_expulsao_cinco_time_a
        self.quantidade_de_gols_no_momento_expulsao_cinco_time_visitante = quantidade_de_gols_no_momento_expulsao_cinco_time_b
        self.quantidade_de_gols_no_momento_expulsao_seis_time_mandante = quantidade_de_gols_no_momento_expulsao_seis_time_a
        self.quantidade_de_gols_no_momento_expulsao_seis_time_visitante = quantidade_de_gols_no_momento_expulsao_seis_time_b
        self.quantidade_de_gols_no_momento_expulsao_sete_time_mandante = quantidade_de_gols_no_momento_expulsao_sete_time_a
        self.quantidade_de_gols_no_momento_expulsao_sete_time_visitante = quantidade_de_gols_no_momento_expulsao_sete_time_b
        self.quantidade_de_gols_no_momento_expulsao_oito_time_mandante = quantidade_de_gols_no_momento_expulsao_oito_time_a
        self.quantidade_de_gols_no_momento_expulsao_oito_time_visitante = quantidade_de_gols_no_momento_expulsao_oito_time_b

        ###
        self.momento_expulsao_um_v_d_e = momento_expulsao_um_v_d_e
        self.momento_expulsao_dois_v_d_e = momento_expulsao_dois_v_d_e
        self.momento_expulsao_tres_v_d_e = momento_expulsao_tres_v_d_e
        self.momento_expulsao_quatro_v_d_e = momento_expulsao_quatro_v_d_e
        self.momento_expulsao_cinco_v_d_e = momento_expulsao_cinco_v_d_e
        self.momento_expulsao_seis_v_d_e = momento_expulsao_seis_v_d_e
        self.momento_expulsao_sete_v_d_e = momento_expulsao_sete_v_d_e
        self.momento_expulsao_oito_v_d_e = momento_expulsao_oito_v_d_e

        ###
        self.intervalo_expulsao_um_v_d_e = intervalo_expulsao_um_v_d_e
        self.intervalo_expulsao_dois_v_d_e = intervalo_expulsao_dois_v_d_e
        self.intervalo_expulsao_tres_v_d_e = intervalo_expulsao_tres_v_d_e
        self.intervalo_expulsao_quatro_v_d_e = intervalo_expulsao_quatro_v_d_e
        self.intervalo_expulsao_cinco_v_d_e = intervalo_expulsao_cinco_v_d_e
        self.intervalo_expulsao_seis_v_d_e  = intervalo_expulsao_seis_v_d_e 
        self.intervalo_expulsao_sete_v_d_e  = intervalo_expulsao_sete_v_d_e 
        self.intervalo_expulsao_oito_v_d_e  = intervalo_expulsao_oito_v_d_e 
        ###

        self.momento_expulsao_um_v_d_e  = momento_expulsao_um_v_d_e 
        self.momento_expulsao_dois_v_d_e  = momento_expulsao_dois_v_d_e 
        self.momento_expulsao_tres_v_d_e  = momento_expulsao_tres_v_d_e 
        self.momento_expulsao_quatro_v_d_e = momento_expulsao_quatro_v_d_e
        self.momento_expulsao_cinco_v_d_e = momento_expulsao_cinco_v_d_e
        self.momento_expulsao_seis_v_d_e  = momento_expulsao_seis_v_d_e 
        self.momento_expulsao_sete_v_d_e  = momento_expulsao_sete_v_d_e 
        self.momento_expulsao_oito_v_d_e  = momento_expulsao_oito_v_d_e 
        ###

        self.expulsao_um_m_v = expulsao_um_m_v
        self.expulsao_dois_m_v = expulsao_dois_m_v
        self.expulsao_tres_m_v = expulsao_tres_m_v
        self.expulsao_quatro_m_v = expulsao_quatro_m_v
        self.expulsao_cinco_m_v = expulsao_cinco_m_v
        self.expulsao_seis_m_v = expulsao_seis_m_v
        self.expulsao_sete_m_v = expulsao_sete_m_v
        self.expulsao_oito_m_v = expulsao_oito_m_v

        ###
        self.qtd_expulsoes_time_mandante = qtd_expulsoes_time_a
        self.qtd_expulsoes_time_visitante = qtd_expulsoes_time_b

        ##estatisticas ao fim do jogo, talvez não seja necessário
        self.posse_time_mandante = posse_time_a
        self.posse_time_visitante = posse_time_b
        self.chutes_a_gol_time_mandante = chutes_a_gol_time_a
        self.chutes_a_gol_time_visitante = chutes_a_gol_time_b
        self.chutes_fora_time_mandante = chutes_fora_time_a
        self.chutes_fora_time_visitante = chutes_fora_time_b
        self.ataques_time_mandante = ataques_time_a
        self.ataques_time_visitante = ataques_time_b
        self.ataques_perigosos_time_mandante = ataques_perigosos_time_a
        self.ataques_perigosos_time_visitante = ataques_perigosos_time_b
        self.impedimentos_time_mandante = impedimentos_time_a
        self.impedimentos_time_visitante = impedimentos_time_b
        self.faltas_time_mandante = faltas_time_a
        self.faltas_time_visitante = faltas_time_b
        self.escanteios_time_mandante = escanteios_time_a
        self.escanteios_time_visitante = escanteios_time_b
        
        