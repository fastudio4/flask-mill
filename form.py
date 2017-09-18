from flask_wtf import FlaskForm
from wtforms import SelectField,  IntegerField, FloatField
from wtforms.validators import InputRequired

class MillInput(FlaskForm):
    materials = SelectField(label='Select materials',
                            validators=[InputRequired()],
                            choices=[('Plastic', 'Plastic'),
                                     ('Plexiglass', 'Plexiglass'),
                                     ('Wood', 'Wood'),
                                     ('Aluminum', 'Aluminum'),
                                     ('Brass/Bronze', 'Brass/Bronze'),
                                     ('Magnesium', 'Magnesium'),
                                     ('Steel', 'Steel'),
                                     ('Cast iron', 'Cast iron'),
                                     ('Titanium', 'Titanium')],
                            render_kw={'class': 'form-control'})
    diameter_mill = FloatField(label='Cutter diameter (mm)',
                               validators=[InputRequired()],
                               render_kw={'class': 'form-control',
                                          'placeholder': 3.175})
    tooth_mill = SelectField(label='Count tooth',
                            validators=[InputRequired()],
                            choices=[('1', 1),
                                     ('2', 2),
                                     ('3', 3),
                                     ('4', 4),
                                     ('5', 5),
                                     ('6', 6)],
                            render_kw={'class': 'form-control'})
    speed_spindel = IntegerField(label='Max speed spindle (rpm\min)',
                                 validators=[InputRequired()],
                                 render_kw={'class': 'form-control',
                                            'placeholder': 24000,
                                            'maxlength':5})
    frequency_spindle = IntegerField(label='Max frequency spindle (Hz)',
                                     validators=[InputRequired()],
                                     render_kw={'class': 'form-control',
                                                'placeholder': 400,
                                                'maxlength':3})
