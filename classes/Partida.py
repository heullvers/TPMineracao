class Partida(object):
    def __init__(self, nome_campeonato, temporada, pais, rodada,
    time_dentro, time_fora, resultado_final, gols_mandante, gols_visitante, horario, turno, dia_semana,
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
    qtd_expulsoes_time_a, qtd_expulsoes_time_b):

        self.nome_campeonato = nome_campeonato
        self.temporada = temporada
        self.pais = pais
        self.rodada = rodada

        ###
        self.time_mandante = time_dentro
        self.time_visitante = time_fora
        self.resultado_final = resultado_final
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
        
        self.media_gols_marcados_sofridos_por_jogo_time_mandante_em_casa = media_gols_marcados_sofridos_por_jogo_time_casa_em_casa
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
        
        self.media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa = media_gols_marcados_sofridos_por_jogo_time_visitante_em_casa
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
        self.qtd_expulsoes_time_mandante = qtd_expulsoes_time_a
        self.qtd_expulsoes_time_visitante = qtd_expulsoes_time_b
        
        