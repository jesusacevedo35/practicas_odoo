from odoo import models, fields

class PracticaDashboard(models.Model):
    # _name es el identificador técnico en Odoo y el nombre de la tabla en PostgreSQL
    _name = 'einsa.practica.dashboard'
    _description = 'Dashboard de Prácticas EINSA'

    # Campos básicos
    name = fields.Char(string='Nombre del Tablero', required=True)
    description = fields.Text(string='Descripción')
    active = fields.Boolean(string='Activo', default=True)
    date = fields.Date(string='Fecha', default=fields.Date.context_today)
    
    # Campo relacional: Conecta este registro con los usuarios del sistema Odoo
    responsible_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    
    # Campos de selección: Crean un menú desplegable con opciones predefinidas
    area = fields.Selection([
        ('ventas', 'Ventas'),
        ('ti', 'Tecnologías de Información'),
        ('rh', 'Recursos Humanos')
    ], string='Área', default='ti')
    
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('approved', 'Aprobado'),
        ('done', 'Finalizado')
    ], string='Estado', default='draft')
    
    # Campo de texto enriquecido (permite negritas, listas, etc.)
    notes = fields.Html(string='Notas adicionales')

    # El puente de regreso (One2many): 1 (un) Dashboard tiene Muchos KPIs
    # Apunta al modelo 'einsa.practica.kpi' a través del campo 'dashboard_id'
    kpi_ids = fields.One2many(
        'einsa.practica.kpi', 
        'dashboard_id', 
        string='Indicadores (KPIs)'
    )