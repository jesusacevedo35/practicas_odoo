from odoo import models, fields

class PracticaKpi(models.Model):
    _name = 'einsa.practica.kpi'
    _description = 'Indicador Clave de Rendimiento (KPI)'

    # Campos básicos solicitados
    name = fields.Char(string='Nombre del KPI', required=True)
    description = fields.Text(string='Descripción')
    unit = fields.Char(string='Unidad (ej. %, MXN, Hrs)')
    target_value = fields.Float(string='Valor Objetivo')
    
    # El puente de ida (Many2one): Muchos KPIs pertenecen a 1 (un) Dashboard
    # ondelete='cascade' significa que si borras el tablero, se borran sus KPIs
    dashboard_id = fields.Many2one(
        'einsa.practica.dashboard', 
        string='Tablero Padre', 
        ondelete='cascade'
    )