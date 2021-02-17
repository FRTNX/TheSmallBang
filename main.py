import uuid

class Atom:
    """An atom, duh"""

    def __init__(self, atomic_properties):
        self.atomic_id = str(uuid.uuid4()) 
        self.name = atomic_properties['name']
        self.symbol = atomic_properties['symbol']
        self.atomic_number = atomic_properties['atomic_number']
        self.atomic_weight = atomic_properties['atomic_weight']
        self.density = atomic_properties['density']
        self.atomic_radius = atomic_properties['atomic_radius']
        self.melting_point = atomic_properties['melting_point']
        self.boiling_point = atomic_properties['boiling_point']
        self.phase = atomic_properties['phase']
        self.valence = atomic_properties['valence']
        self.period = atomic_properties['period']
        self.group = atomic_properties['group']
        self.atomic_radius = atomic_properties['atomic_radius']
        self.ionisation_potential = atomic_properties['ionisation_potential']
        self.electronic_configuration = atomic_properties['electronic_configuration']

    def __add__(self, atomic_additive):
        return Molecule({ 'atomic_members': [self, atomic_additive] })

    def __str__(self):
        return self.name

# Molecule + Atom = Molecule(Molecule.atoms, Atom)
# Consider how to create molecular intuition, e.g., avoiding rendering C02 as 02C

class Molecule:
    """An atomic cartel"""

    def __init__(self, molecular_properties):
        self.atomic_members = molecular_properties['atomic_members']
        self.empirical_formula = self._calculate_emperical_formula()
        self.atomic_bonds = [
            { 'bond_type': 'covelent', 'members': [] },
            { 'bond_type': 'hydrogen', 'members': [] }
        ]

    def __add__(self, atomic_additive):
        atomic_members = self.atomic_members + [atomic_additive]
        return Molecule({ 'atomic_members': atomic_members })

    def list_atomic_members(self):
        return [str(atom) for atom in self.atomic_members]

    def _calculate_emperical_formula(self):
        counted = []
        empirical_formula = ''
        for atom in self.atomic_members:
            if str(atom) not in counted:
                empirical_formula += f'{atom.symbol}{self.list_atomic_members().count(str(atom))}'
                counted.append(str(atom))
        return empirical_formula.replace('1', '')



Hydrogen = Atom({
    'name': 'Hydrogen',
    'symbol': 'H',
    'atomic_number': 1,
    'atomic_weight': { 'value': 1.0079, 'unit': 'g/mol' },
    'density': { 'value': 0.0000899, 'unit': 'g/cm3' },
    'atomic_radius': { 'value': 53, 'unit': 'pm' },
    'covalent_radius': { 'value': 38, 'unit': 'pm' },
    'van_der_waals_radius': { 'value': 120, 'unit': 'pm' },
    'melting_point': { 'temperature': -259.1, 'unit': 'celcius' },
    'boiling_point': { 'temperature': -252.9, 'unit': 'celcius' },
    'phase': 'gas',
    'valence': 1,
    'period': 1,
    'group': 'IA',
    'block': 's-block',
    'ionisation_potential': { 'score': 13.53, 'unit': 'eV' },
    'electronic_configuration': { 'K': 1 }
})

Oxygen = Atom({
    'name': 'Oxygen',
    'symbol': 'O',
    'atomic_number': 8,
    'atomic_weight': { 'weight': 15.9994, 'unit': 'g/mol' },
    'density': { 'density': 0.00142897, 'unit': 'g/cm3' },
    'atomic_radius': { 'value': 48, 'unit': 'pm' },
   'covalent_radius': { 'value': 66, 'unit': 'pm' },
    'van_der_waals_radius': { 'value': 152, 'unit': 'pm' },
    'melting_point': { 'temperature': -218.4, 'unit': 'celcius' },
    'boiling_point': { 'temperature': -182.9, 'unit': 'celcius' },
    'phase': 'gas',
    'valence': -2,
    'period': 2,
    'group': 'VIA',
    'block': 'p-block',
    'ionisation_potential': { 'score': 13.56, 'unit': 'eV' },
    'electronic_configuration': { 'K': 1 }
})

if __name__ == '__main__':
    # tests
