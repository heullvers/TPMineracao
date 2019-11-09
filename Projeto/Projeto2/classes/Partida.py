class Partida(object):
    def __init__(self, posicao_time_dentro, posicao_time_fora,  media_gols_marcados_por_jogo_time_casa_em_casa, 
    media_gols_sofridos_por_jogo_time_casa_em_casa, media_gols_sofridos_por_jogo_time_visitante_fora, gols_marcados_time_casa_segundo_sexto, 
    gols_marcados_time_visitante_segundo_sexto, gols_sofridos_time_visitante_quinto_sexto, quantidade_de_gols_no_momento_expulsao_um_time_a, 
    minuto_expulsao_um, minuto_expulsao_dois, diferenca_gols_expulsao_um, diferenca_gols_expulsao_dois, expulsao_dois_m_v_Visitante, 
    quarto_ultimo_jogo_visitante_V, momento_expulsao_um_v_d_e_V, expulsao_um_m_v_Mandante, momento_expulsao_dois_v_d_e_D, 
    momento_expulsao_dois_v_d_e_E, momento_expulsao_dois_v_d_e_V, resultado_final_v_d_e):

        ###
        self.posicao_time_dentro = posicao_time_dentro
        self.posicao_time_fora= posicao_time_fora
        ###

        ###Casa
        self.media_gols_marcados_por_jogo_time_casa_em_casa = media_gols_marcados_por_jogo_time_casa_em_casa
        self.media_gols_sofridos_por_jogo_time_casa_em_casa = media_gols_sofridos_por_jogo_time_casa_em_casa
        self.gols_marcados_time_casa_segundo_sexto = gols_marcados_time_casa_segundo_sexto

        #Visitante
        self.media_gols_sofridos_por_jogo_time_visitante_fora = media_gols_sofridos_por_jogo_time_visitante_fora
        self.gols_marcados_time_visitante_segundo_sexto = gols_marcados_time_visitante_segundo_sexto
        self.gols_sofridos_time_visitante_quinto_sexto = gols_sofridos_time_visitante_quinto_sexto

        self.quarto_ultimo_jogo_visitante_V = quarto_ultimo_jogo_visitante_V 
        ###

        self.minuto_expulsao_um = minuto_expulsao_um
        self.minuto_expulsao_dois = minuto_expulsao_dois

        self.diferenca_gols_expulsao_um = diferenca_gols_expulsao_um
        self.diferenca_gols_expulsao_dois = diferenca_gols_expulsao_dois

        self.momento_expulsao_um_v_d_e_V = momento_expulsao_um_v_d_e_V
        self.expulsao_um_m_v_Mandante = expulsao_um_m_v_Mandante
        self.expulsao_dois_m_v_Visitante = expulsao_dois_m_v_Visitante

        self.momento_expulsao_dois_v_d_e_D = momento_expulsao_dois_v_d_e_D
        self.momento_expulsao_dois_v_d_e_E = momento_expulsao_dois_v_d_e_E
        self.momento_expulsao_dois_v_d_e_V = momento_expulsao_dois_v_d_e_V

        self.quantidade_de_gols_no_momento_expulsao_um_time_a = quantidade_de_gols_no_momento_expulsao_um_time_a

        self.resultado_final_v_d_e = resultado_final_v_d_e
        