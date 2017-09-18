from calc import Milling
from flask import Flask, render_template
from form import MillInput

mill = Flask(__name__)
mill.secret_key = 'mill-calculation-python-flask'

@mill.route('/', methods=['GET', 'POST'])
def index():
    form = MillInput()
    if form.validate_on_submit():
        materials = str(form.materials.data)
        diametr = float(form.diameter_mill.data)
        tooth = int(form.tooth_mill.data)
        speed_spindel = int(form.speed_spindel.data)
        frequency_spindle = int(form.frequency_spindle.data)
        value = Milling(materials, diametr, tooth, speed_spindel, frequency_spindle)
        input = {
            'materials': value.material,
            'diametr': value.d_cut,
            'tooth': value.t_cut
        }
        return render_template('output.html', output=value.setting, input=input)
    return render_template('input.html', form=form)

mill.run(debug=False)